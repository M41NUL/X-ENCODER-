# ─────────────────────────────────────────
#  X-ENCODER — config.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

from datetime import datetime

TOOL_NAME    = "X-ENCODER"
VERSION      = "1.0.0"
GITHUB_USER  = "M41NUL"
GITHUB_REPO  = "X-ENCODER-"

GITHUB_RAW   = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main"
GITHUB_API   = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}"
VERSION_URL  = f"{GITHUB_RAW}/config.py"

# ── Developer Info ────────────────────────────────────────────────────────────
DEV_NAME     = "Md. Mainul Islam"
DEV_BRAND    = "CODEX-M41NUL"
DEV_GITHUB   = "github.com/M41NUL"
DEV_TELEGRAM = "t.me/mdmainulislaminfo"
DEV_CHANNEL  = "t.me/codexm41nul"
DEV_GROUP    = "t.me/codex_m41nul"
DEV_EMAIL    = "devmainulislam@gmail.com"
DEV_YOUTUBE  = "youtube.com/@codexm41nul"
DEV_WHATSAPP = "+8801308850528"

YEAR         = datetime.now().year
COPYRIGHT    = f"© {YEAR} CODEX-M41NUL. All Rights Reserved."

# ── Encoded file header ───────────────────────────────────────────────────────
ENCODE_HEADER = """\
# Tool    : X-ENCODER
# Type    : Marshal + Zlib + Base64
# Date    : {date}
# Dev     : Md. Mainul Islam (CODEX-M41NUL)
# GitHub  : https://github.com/M41NUL
# Repo    : https://github.com/M41NUL/X-ENCODER-
# Warning : This file is encoded. Do not edit.
"""
