"""Configure documentation links for an independent fork. Standard library only."""
import argparse
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('owner', help='GitHub user or organization')
    parser.add_argument('repository', nargs='?', default='binance-trade-bot-windows')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?', args.owner):
        parser.error('Use a GitHub login without slashes, spaces, or consecutive hyphens.')
    if '--' in args.owner:
        parser.error('GitHub logins cannot contain consecutive hyphens.')
    if not re.fullmatch(r'[A-Za-z0-9_.-]{1,100}', args.repository) or args.repository in {'.', '..'}:
        parser.error('Invalid repository name.')
    root = Path(__file__).resolve().parents[1]
    old = 'https://github.com/YOUR_GITHUB_USERNAME/binance-trade-bot-windows'
    new = f'https://github.com/{args.owner}/{args.repository}'
    changed = 0
    for name in ('README.md', 'RELEASE_NOTES.md'):
        path = root / name
        original = path.read_text(encoding='utf-8')
        if old in original:
            path.write_text(original.replace(old, new), encoding='utf-8')
            print(f'Updated {name}')
            changed += 1
    if not changed:
        parser.error('No template links remain. Edit already configured links manually.')


if __name__ == '__main__':
    main()
