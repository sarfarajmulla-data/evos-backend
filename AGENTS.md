# Agent instructions

- Keep domain logic in `app/services`, algorithms in `app/algorithms`, and
  HTTP concerns in `app/api`.
- Do not claim live dataset, Supabase, or deployment verification without
  executed evidence and configured credentials.
- Add or update tests for behavior changes.
- Run `pytest -q` and `python -m compileall app` before handoff.
- Never commit `.env`, database files, credentials, or generated build output.
