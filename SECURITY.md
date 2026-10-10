# Security policy

## Supported versions

Security fixes are applied to the default branch. Deployments should use a
reviewed commit and should not expose the development docs in production.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability. Report it privately
through the repository's GitHub security advisory flow or to the maintainers
listed in the repository settings. Include the affected commit, endpoint or
module, reproduction steps, impact, and a suggested mitigation when known.

Allow maintainers reasonable time to investigate before public disclosure.
Do not send credentials, tokens, or real customer data in a report.

## Operational requirements

Keep `.env` out of version control, rotate exposed credentials immediately,
use a restricted database role for the API, and set a non-default
`SECRET_KEY` in every deployed environment.
