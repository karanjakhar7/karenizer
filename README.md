# ⚡ KARENIZER

Transform your grievances into legendary Karen-level complaint letters.

Users describe what went wrong, pick a Karen intensity level (0 = politely disappointed → 5 = PEAK KAREN), and the app drafts a dramatic complaint letter via LiteLLM.

## Stack

- **FastAPI** — Python web framework
- **LiteLLM** — unified LLM gateway (supports OpenAI, Anthropic, Gemini, and more)
- **Jinja2** — HTML templating
- **uv** — package manager
- **Vercel** — deployment (Python serverless via `@vercel/python`)

## Local Development

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env and set LITELLM_MODEL and the matching API key
```

### 3. Run

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000.

## Deploy to Vercel

1. Push this repo to GitHub.
2. Import the project in the [Vercel dashboard](https://vercel.com/new).
3. Add environment variables in **Settings → Environment Variables**:
   - `LITELLM_MODEL` — e.g. `gpt-4o-mini`
   - The matching API key (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.)
4. Deploy. The `vercel.json` routes all traffic to `api/index.py`.

> **No Vercel CLI required** — the `vercel.json` config file handles everything.

## Supported Models (via LiteLLM)

| Provider   | Example model string          |
|------------|-------------------------------|
| OpenAI     | `gpt-4o-mini`, `gpt-4o`       |
| Anthropic  | `claude-haiku-4-5`            |
| Gemini     | `gemini/gemini-2.0-flash`     |

Set `LITELLM_MODEL` to any [LiteLLM-supported model](https://docs.litellm.ai/docs/providers).

## Karen Levels

| Level | Name                  | Description                                              |
|-------|-----------------------|----------------------------------------------------------|
| 0     | 😊 Politely Disappointed | Calm, professional, factual                           |
| 1     | 😒 Mildly Frustrated  | Passive-aggressive, hints at leaving                     |
| 2     | 😤 Noticeably Upset   | Clear frustration, mentions negative reviews             |
| 3     | 😡 Full Karen Mode    | DEMANDS manager, CAPS emphasis, social media threats     |
| 4     | 🤬 Nuclear Option     | Lawyers, BBB, community Facebook groups, demands comp    |
| 5     | 💥 PEAK KAREN         | CEO addressed directly, national media, near-biblical    |

## Project Structure

```
karenizer/
├── api/
│   └── index.py                  # Vercel entry point
├── app/
│   ├── main.py                   # FastAPI app
│   ├── config.py                 # Env-var settings
│   ├── routers/
│   │   ├── apis.py               # POST /api/generate
│   │   └── main_routes.py        # GET /
│   ├── services/
│   │   └── complaint_generator.py  # LiteLLM logic
│   ├── dependencies/
│   │   └── schemas.py            # Pydantic request/response models
│   └── templates/
│       └── index.html            # Single-page UI
├── vercel.json
├── requirements.txt              # For Vercel runtime
└── pyproject.toml                # uv project config
```
