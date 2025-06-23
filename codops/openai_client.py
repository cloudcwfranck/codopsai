"""OpenAI client wrapper."""

from __future__ import annotations

import os

import openai

_MODEL = "gpt-3.5-turbo"


def run_prompt(prompt: str) -> str:
    """Send prompt to OpenAI and return completion.

    Uses OPENAI_API_KEY env var. Raises RuntimeError if key missing.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not configured")

    client = openai.OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model=_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()
