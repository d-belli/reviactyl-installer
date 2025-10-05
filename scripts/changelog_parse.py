#!/usr/bin/env python3

import os

__author__ = "André Belli"
__email__ = "andre@arenahosting.com.br"

def read():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    changelog_path = os.path.join(base_dir, "..", "CHANGELOG.md")  # Ajuste conforme necessário
    with open(changelog_path) as f:
        return f.read()

def main():
    changelog = read()
    lines = changelog.split("\n")

    # Identifica as linhas que começam com '## ' (releases)
    release_linenumbers = [i for i, l in enumerate(lines) if l.startswith("## ")]

    if not release_linenumbers:
        print("* No releases found in CHANGELOG.md")
        return

    # Pega apenas a primeira release
    start = release_linenumbers[0]
    end = release_linenumbers[1] if len(release_linenumbers) > 1 else len(lines)

    # Imprime linhas da primeira release
    for i in range(start, end):
        print(lines[i])

if __name__ == "__main__":
    main()
