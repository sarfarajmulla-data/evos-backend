# Contributing

## Development setup

Use Python 3.11 or newer, create a virtual environment, install
`requirements.txt`, copy `.env.example` to `.env`, and run `pytest -q`.
Run the API locally with `uvicorn app.main:app --reload`.

## Branches and commits

Create focused branches from `main` using `feature/<name>`, `fix/<name>`, or
`docs/<name>`. Use imperative Conventional Commit messages such as
`feat: add dataset readiness endpoint` or `fix: reject unknown vehicles`.

## Pull requests

Every pull request must explain what changed, why it changed, how it was
tested, and any operational or security risk. Keep changes focused, update
documentation and tests with behavior changes, and wait for the CI workflow
to pass before requesting review. Never include secrets, production exports,
or personal data.
