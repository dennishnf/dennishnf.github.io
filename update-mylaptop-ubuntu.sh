#!/bin/bash
#
# Usage:
#   ./update-mylaptop-ubuntu.sh          -> build + amend commit + force push (daily)
#   ./update-mylaptop-ubuntu.sh clear    -> same, but wipes history and shrinks .git
#   ./update-mylaptop-ubuntu.sh sync     -> pull remote state, DISCARDS local changes
#
# Run "sync" first when switching machines, before editing anything.
# History is rewritten on every run: the remote keeps only one commit.
#
set -e

REPO="/home/dennishnf/Documents/dennishnf.github.io"
cd "$REPO"

case "${1:-update}" in

  sync)
    git fetch origin
    git reset --hard origin/main
    git clean -fd
    ;;

  update)
    python3 md2html.py "$REPO"
    git add -A
    git commit --amend -m "making website"
    git push --force origin main
    ;;

  clear)
    python3 md2html.py "$REPO"
    git checkout --orphan tmp-clean
    git add -A
    git commit -m "making website"
    git branch -D main
    git branch -m main
    git push --force origin main
    git reflog expire --expire=now --expire-unreachable=now --all
    git gc --prune=now --aggressive
    du -sh .git
    ;;

  *)
    echo "usage: $0 [update|clear|sync]"
    exit 1
    ;;
esac