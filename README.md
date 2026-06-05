<div align="center">

```
 ██╗  ██╗      ███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗
 ╚██╗██╔╝      ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
  ╚███╔╝ █████╗█████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  ██████╔╝
  ██╔██╗ ╚════╝██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
 ██╔╝ ██╗      ███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
 ╚═╝  ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

**Python Source Code Encoder for Termux**

[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen?style=flat-square)](https://github.com/M41NUL/X-ENCODER-)
[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Android-orange?style=flat-square)](https://github.com/M41NUL/X-ENCODER-)
[![Language](https://img.shields.io/badge/language-Python%203-blue?style=flat-square)](https://github.com/M41NUL/X-ENCODER-)
[![License](https://img.shields.io/badge/license-MIT-red?style=flat-square)](https://github.com/M41NUL/X-ENCODER-)
[![Author](https://img.shields.io/badge/dev-𝐂𝐎𝐃𝐄𝐗-𝐌𝟒𝟏𝐍𝐔𝐋-yellow?style=flat-square)](https://github.com/M41NUL)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-2CA5E0?style=flat-square&logo=telegram)](https://t.me/codexm41nul)
[![Stars](https://img.shields.io/github/stars/M41NUL/X-ENCODER-?style=flat-square&color=yellow)](https://github.com/M41NUL/X-ENCODER-/stargazers)
[![Forks](https://img.shields.io/github/forks/M41NUL/X-ENCODER-?style=flat-square&color=blue)](https://github.com/M41NUL/X-ENCODER-/network/members)
[![Issues](https://img.shields.io/github/issues/M41NUL/X-ENCODER-?style=flat-square&color=red)](https://github.com/M41NUL/X-ENCODER-/issues)
[![Last Commit](https://img.shields.io/github/last-commit/M41NUL/X-ENCODER-?style=flat-square&color=brightgreen)](https://github.com/M41NUL/X-ENCODER-/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/M41NUL/X-ENCODER-?style=flat-square&color=orange)](https://github.com/M41NUL/X-ENCODER-)

</div>

---

## 📌 What is X-ENCODER?

**X-ENCODER** is a Termux-based Python source code protection tool. It encodes your `.py` files using **3 layers of obfuscation** — making them extremely difficult to read or reverse-engineer, while still being fully executable.

> Protect your scripts before sharing them. Keep your logic private.

---

## 🔐 Encoding Layers

```
Original .py  ──►  Marshal (bytecode)  ──►  Zlib (compress)  ──►  Base64 (encode)  ──►  Encoded .py
```

| Layer | Method | Purpose |
|-------|--------|---------|
| 1st | `marshal` | Compiles source to Python bytecode (code object) |
| 2nd | `zlib` | Compresses marshalled bytes (level 9) |
| 3rd | `base64` | Encodes compressed bytes to ASCII-safe string |

The output file is **self-executing** — no decoder needed. Just run it normally with `python file.py`.

---

## 📂 Project Structure

```
X-ENCODER-/
├── main.py        — Entry point (banner → update check → menu)
├── config.py      — Tool config, version, developer info
├── banner.py      — ASCII banner + info box renderer
├── updater.py     — Auto update from GitHub
├── encoder.py     — Core 3-layer encoding logic
├── menu.py        — Interactive menu & input handlers
├── utils.py       — Colors, animations, progress bar, prompts
└── installer.sh   — Auto installer + storage permission + launcher
```

---

## ⚡ Installation & Usage

### Step 1 — Clone the repo

```bash
git clone https://github.com/M41NUL/X-ENCODER-.git
cd X-ENCODER-
```

### Step 2 — Run installer

```bash
bash installer.sh
```

The installer will:
- Update Termux packages
- Install Python, pip, git
- Request Android `/sdcard` storage permission via `termux-setup-storage`
- Show animated progress bars for each step
- Auto-launch `main.py` after a **3-second countdown**

### Step 3 — Run manually (after first install)

```bash
cd X-ENCODER-
python main.py
```

---

## 🖥️ All Commands

| Command | Description |
|---------|-------------|
| `git clone https://github.com/M41NUL/X-ENCODER-.git` | Clone the repo |
| `cd X-ENCODER-` | Enter project folder |
| `bash installer.sh` | Install dependencies + launch |
| `python main.py` | Run tool manually |
| `git pull origin main` | Pull latest update manually |
| `rm -rf X-ENCODER-` | Remove / uninstall the tool |

---

## 🗑️ Uninstall

To completely remove X-ENCODER from your device:

```bash
cd /sdcard   # or wherever you cloned it
rm -rf X-ENCODER-
```

---

## 🛠 Menu Options

```
[1]  Encode Single File   — Encode one .py file
[2]  Encode Folder        — Encode all .py files in a folder
[3]  About / Info         — Developer info
[0]  Exit
```

---

## 📄 Single File Example

```
Enter file path : /sdcard/myproject/hello.py
Enter output name (without .py) : hello_encoded
```

```
✔ Saved: /sdcard/myproject/hello_encoded.py
```

---

## 📁 Folder Example

```
Enter folder path : /sdcard/myproject/scripts/
Enter output folder name : scripts_encoded
```

```
✔ Saved to: /sdcard/myproject/scripts_encoded/
```

All `.py` files inside the folder are encoded. Output folder is created as a sibling of the input folder.

---

## 📝 Encoded File Header

Every encoded file includes this comment block at the top:

```python
# Tool    : X-ENCODER
# Type    : Marshal + Zlib + Base64
# Date    : 2025-01-01 12:00:00
# Dev     : Md. Mainul Islam (CODEX-M41NUL)
# GitHub  : https://github.com/M41NUL
# Warning : This file is encoded. Do not edit.
```

---

## 🎨 Color Scheme

| Color | Hex / ANSI | Usage |
|-------|-----------|-------|
| Green | `\033[92m` | Primary, success |
| Red | `\033[91m` | Errors, secondary |
| Orange | `\033[38;5;208m` | Accent, prompts |
| White | `\033[97m` | Dim text, body |

---

## 👨‍💻 Developer

<div align="center">

| | |
|--|--|
| **Name** | Md. Mainul Islam |
| **Brand** | CODEX-M41NUL |
| **GitHub** | [github.com/M41NUL](https://github.com/M41NUL) |
| **Telegram** | [t.me/mdmainulislaminfo](https://t.me/mdmainulislaminfo) |
| **Channel** | [t.me/codexm41nul](https://t.me/codexm41nul) |
| **Group** | [t.me/codex_m41nul](https://t.me/codex_m41nul) |
| **YouTube** | [youtube.com/@codexm41nul](https://youtube.com/@codexm41nul) |
| **Email** | devmainulislam@gmail.com |

</div>

---

## ⭐ Support

If this tool helped you, give it a **star** on GitHub and join the Telegram channel for updates!

[![Star on GitHub](https://img.shields.io/github/stars/M41NUL/X-ENCODER-?style=social)](https://github.com/M41NUL/X-ENCODER-)
[![Telegram](https://img.shields.io/badge/Join-Telegram%20Channel-2CA5E0?style=flat-square&logo=telegram)](https://t.me/codexm41nul)

---

<div align="center">
<sub>Made with ❤️ by <b>CODEX-M41NUL</b> | © 2026</sub>
</div>
