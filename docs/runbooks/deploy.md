# Deploy

1. Review the target commit and migration plan.
2. Set secrets through the platform secret manager.
3. Run the image build and CI checks.
4. Apply database migrations.
5. Verify `/health`, `/ready`, and a read-only API call.
6. Monitor errors before increasing traffic.
