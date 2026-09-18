#!/usr/bin/env python3
"""Send a bounded task to an already-resident local Ollama model."""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


def endpoint(value: str) -> str:
    if "://" not in value:
        value = "http://" + value
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("OLLAMA_HOST must use http or https")
    if parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise ValueError("remote Ollama endpoints are refused by this helper")
    return value.rstrip("/")


def request_json(url: str, payload=None, timeout: int = 600):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data)
    if data is not None:
        request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def model_names(status):
    return [
        item.get("name") or item.get("model")
        for item in status.get("models", [])
        if item.get("name") or item.get("model")
    ]


def select_model(loaded, requested):
    if requested:
        return requested
    preferred = os.environ.get("OLLAMA_DELEGATE_MODEL")
    if preferred:
        return preferred
    return next((name for name in loaded if "qwen" in name.lower()), loaded[0] if loaded else None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", help="task prompt; stdin is used when omitted")
    parser.add_argument("--host", default=os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434"))
    parser.add_argument("--model", help="resident model to use")
    parser.add_argument("--allow-load", action="store_true", help="allow a non-resident model (may evict another model)")
    parser.add_argument("--list", action="store_true", help="list resident models and exit")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--max-tokens", type=int, default=2048)
    args = parser.parse_args()

    try:
        host = endpoint(args.host)
        status = request_json(host + "/api/ps", timeout=min(args.timeout, 30))
        loaded = model_names(status)
        if args.list:
            print(json.dumps({"host": host, "loaded_models": loaded}, indent=2))
            return 0

        chosen = select_model(loaded, args.model)
        if not chosen:
            raise RuntimeError("no Ollama model is resident; refusing to load one")
        if chosen not in loaded and not args.allow_load:
            raise RuntimeError(f"{chosen!r} is not resident; refusing possible VRAM eviction")

        prompt = args.prompt if args.prompt is not None else sys.stdin.read()
        if not prompt.strip():
            raise ValueError("provide a prompt argument or pipe one on stdin")

        payload = {
            "model": chosen,
            "stream": False,
            "think": False,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a local junior implementer. Solve only the bounded task given. "
                        "Do not claim to edit files or run commands. State assumptions briefly. "
                        "Prefer a unified diff or the exact structured output requested."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "options": {"temperature": 0.2, "num_predict": args.max_tokens},
        }
        result = request_json(host + "/api/chat", payload, args.timeout)
        content = result.get("message", {}).get("content")
        if not content:
            raise RuntimeError("Ollama returned no message content")
        content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL).lstrip()
        print(content)
        print(f"[local draft from {chosen}; frontier validation required]", file=sys.stderr)
        return 0
    except (ValueError, RuntimeError, urllib.error.URLError, TimeoutError) as error:
        print(f"ollama_delegate: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
