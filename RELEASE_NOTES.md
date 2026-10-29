## Binance Trade Bot — Windows x64

Windows distribution for an independent fork of [ccxt/binance-trade-bot](https://github.com/ccxt/binance-trade-bot).

### Download

Open **Assets** below and download **`binance-trade-bot-windows-x64.exe`**. Also download `user.cfg.example`, `supported_coin_list`, and `SHA256SUMS.txt`.

The executable is distributed through this release. GitHub's **Source code** archives contain the project source.

### Configuration

1. Place the downloaded files in a dedicated writable folder.
2. Copy `user.cfg.example` to `user.cfg` and enter your own configuration.
3. Review the coin list and use a test environment before enabling live trading. The configuration template uses `testnet=true`.
4. Follow the [README](https://github.com/YOUR_GITHUB_USERNAME/binance-trade-bot-windows#before-running) for the upstream working-directory layout and startup instructions.

### Verify the download

In PowerShell, calculate the downloaded executable's SHA-256:

```powershell
Get-FileHash .\binance-trade-bot-windows-x64.exe -Algorithm SHA256
```

Compare the result with `SHA256SUMS.txt` from this release. A matching checksum confirms the downloaded bytes match that file; it is not a publisher signature.

### Project information

This is an independent fork. Original project: **ccxt/binance-trade-bot**, originally created by **Eden Gaon**. Source code and the original **GPL-3.0** license are available in the repository at this release's tag.

Automated trading can cause losses. This release makes no promise of profit.
