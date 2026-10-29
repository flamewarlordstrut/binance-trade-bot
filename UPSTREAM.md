# Source provenance

- Upstream: https://github.com/ccxt/binance-trade-bot
- Revision: `55f8cbbe082bd083a722cba697f708a07f5add16`
- Revision link: https://github.com/ccxt/binance-trade-bot/commit/55f8cbbe082bd083a722cba697f708a07f5add16
- Preparation date: 2026-10-29 (Europe/Moscow)
- Original author credited in upstream README: Eden Gaon.
- Original LICENSE is retained unchanged.

## Changes in this package

- Preserved the upstream Python implementation and requirements without changing trading logic.
- Preserved the original README as `README.upstream.md`.
- Added a download-oriented README, release description, Russian publishing guide, and repository-link configuration helper.
- Replaced example API values in `.user.cfg.example` with blank fields and set the example to `testnet=true`.
- Added ignore patterns for local virtual environments, build outputs, executables, and release staging.
- Omitted upstream deployment automation (`.do` and `.github/workflows/cicd.yaml`) from the distribution archive because it targets the original project's deployment infrastructure.
- This package does not include a compiled Windows executable. No Windows build, dependency installation, trading session, or exchange connection was tested.

The original upstream README is an unchanged historical reference. Its configuration examples and deployment links should be read in that context; use `.user.cfg.example` from this fork for a new local configuration.
