# Pensieve Commands Cheatsheet

Your full reference for everything we've built together. Bookmark this and come back whenever you forget a step.

---

## 1. Open a terminal and get into the project

Every session starts here:

```bash
cd /Users/jamesrane/pensieve
```

> Tip: if you ever lose your terminal, open **Terminal.app** (Spotlight: ⌘+Space, type "Terminal") and run that command.

---

## 2. Using the Pensieve (CLI)

### Save a memory
```bash
python3 pensieve.py add "what you want to remember"
```
Always wrap the text in **double quotes** — otherwise the shell treats each word as a separate argument.

### See all memories
```bash
python3 pensieve.py list
```

### Search for a keyword
```bash
python3 pensieve.py search "claude"
```
Case-insensitive. Matches any substring inside a memory.

### Edit a memory
```bash
python3 pensieve.py edit 1 "new text for memory #1"
```
Replace `1` with the actual id of the memory you want to update. The timestamp is preserved.

### Delete a memory
```bash
python3 pensieve.py delete 3
```
Replace `3` with the id you want to remove. Remaining memories are renumbered.

### See available commands
```bash
python3 pensieve.py
```

---

## 3. Using the web UI

### Start the Pensieve in your browser
```bash
python3 app.py
```
Then open **[http://localhost:5050](http://localhost:5050)**.

> Why port 5050? Port 5000 is hijacked by macOS AirPlay Receiver. If you ever see "site can't be reached", check that you're using **5050**, not 5000.

### Stop the web server
In the terminal where it's running, press **Ctrl + C**.

### First-time setup (only needed once per machine)
```bash
pip3 install -r requirements.txt
```

---

## 4. Where your memories live

All memories are saved locally in:
```
/Users/jamesrane/pensieve/memories.json
```
This file is **gitignored**, so your memories never get pushed to GitHub. The CLI and web UI both read/write the same file — they stay in sync automatically.

---

## 5. Git + GitHub workflow (shipping a change)

When you (or I) add a new feature, the rhythm is always the same. Run from inside the project folder.

### Make sure you're up to date
```bash
git checkout main
git pull
```

### Start a new branch for your change
```bash
git checkout -b feat/some-short-name
```
Use `feat/` for features, `fix/` for bug fixes, `docs/` for documentation.

### After editing files — see what changed
```bash
git status
git diff
```

### Save your changes
```bash
git add <filename>           # add a specific file, or
git add .                    # add everything you changed
git commit -m "Short description of the change"
```

### Push to GitHub
```bash
git push -u origin feat/some-short-name
```
(The `-u origin <branch>` is only needed the first push of a new branch — after that, just `git push`.)

### Open a pull request
```bash
/opt/homebrew/bin/gh pr create
```
It'll prompt you for a title and body, then give you the URL. Open it in your browser to merge.

### Merge via the GitHub website
On the PR page, click the green **Merge pull request** button → **Confirm merge**.

### After merging, clean up locally
```bash
git checkout main
git pull
```

---

## 6. Useful one-offs

### See the project's git history
```bash
git log --oneline
```

### See your open PRs
```bash
/opt/homebrew/bin/gh pr list
```

### Check GitHub auth status
```bash
/opt/homebrew/bin/gh auth status
```

### Make `gh` always work without the full path
Add this line to your `~/.zshrc` once, then restart Terminal:
```bash
export PATH="/opt/homebrew/bin:$PATH"
```
After that, you can just type `gh` instead of `/opt/homebrew/bin/gh`.

---

## 7. Your repos

- **Pensieve**: [github.com/triprane9-Aub/pensieve](https://github.com/triprane9-Aub/pensieve)
- **First PR practice**: [github.com/triprane9-Aub/first-pr](https://github.com/triprane9-Aub/first-pr)

---

*Built day by day. One percent better.*
