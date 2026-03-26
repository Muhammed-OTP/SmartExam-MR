# Development Workflow

## Source Control
- **Main Branch (`main`)**: The stable production baseline.
- **Feature Branches**: Should be named intuitively (e.g., `feature/add-tf-idf`, `bugfix/data-loader`).

## Commit Convention
We follow conventional commits to keep the history readable:
- `feat:` A new feature.
- `fix:` A bug fix.
- `docs:` Documentation only changes.
- `chore:` Maintenance, dependency updates.

## Pull Requests
- Keep PRs small and focused.
- Ensure all tests pass before merging.
- Use the `.github/pull_request_template.md` to structure your PR description.

## Testing Strategy
- Core logic (`src/smartexam_mr/`) must be covered by `pytest`.
- Run `pytest` locally before opening a PR.
- The CI pipeline will enforce code formatting (using `black` and `ruff`) and test execution.
