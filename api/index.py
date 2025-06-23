from __future__ import annotations

from flask import Flask, jsonify, request

from codops.openai_client import run_prompt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def handle() -> tuple[str, int] | tuple[dict[str, str], int]:
    """Vercel entrypoint for codops."""
    prompt = request.args.get("prompt")
    if request.is_json:
        prompt = request.get_json(silent=True).get("prompt") or prompt
    if not prompt:
        return {"error": "Missing prompt"}, 400
    try:
        result = run_prompt(prompt)
    except Exception as exc:  # pragma: no cover - network errors
        return {"error": str(exc)}, 500
    return jsonify(response=result), 200


# Export app for Vercel
handler = app
