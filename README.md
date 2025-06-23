# codops

Codops is an AI-assisted command line tool for developers. It provides a
simple interface to OpenAI's ChatGPT for turning natural language into helpful
commands or documentation snippets.

```bash
pip install -e .
# or from PyPI in future
```

## Run directly from GitHub

You can install the latest version straight from a repository without
cloning:

```bash
pip install git+https://github.com/<your-user>/codopsai.git
```

Replace `<your-user>` with the GitHub owner of this project.

## Usage

```bash
codops run "say hello"
```

Use `codops summary --project` to generate project summaries (coming soon).

## Deploy to Vercel

Deploy the API as a serverless function on Vercel:

```bash
vercel --prod
```

Make sure to set the `OPENAI_API_KEY` environment variable in your Vercel
project settings. The API accepts a `prompt` parameter via query string or JSON
body and returns the completion.
