# ─────────────────────────────────────────
#  X-ENCODER — updater.py
#  Dev: Md. Mainul Islam (MAINUL-X)
# ─────────────────────────────────────────

import urllib.request, urllib.error, re, os, sys, time
from config import VERSION, GITHUB_RAW, GITHUB_USER, GITHUB_REPO
from utils  import animated_dots, print_success, print_info, print_warn, print_error

G  = "\033[92m"
R  = "\033[91m"
O  = "\033[38;5;208m"
W  = "\033[97m"
B  = "\033[1m"
RST= "\033[0m"

FILES_TO_UPDATE = [
    "main.py", "config.py", "banner.py", "updater.py",
    "encoder.py", "menu.py", "utils.py"
]

def _fetch(url: str) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "X-ENCODER/updater"})
        with urllib.request.urlopen(req, timeout=8) as r:
            return r.read().decode("utf-8")
    except Exception:
        return None

def _parse_version(raw: str) -> str | None:
    m = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', raw)
    return m.group(1) if m else None

def _version_tuple(v: str):
    try:    return tuple(int(x) for x in v.strip().split("."))
    except: return (0,)

def check_and_update(silent=False) -> bool:
    """
    Check GitHub for a newer version.
    Show 5-second animated check → apply update silently if available.
    Returns True if updated.
    """
    animated_dots("Checking for updates", duration=5, color=G)

    raw = _fetch(f"{GITHUB_RAW}/config.py")
    if raw is None:
        print_warn("Could not reach GitHub. Skipping update check.")
        return False

    remote_ver = _parse_version(raw)
    if remote_ver is None:
        print_warn("Could not parse remote version.")
        return False

    if _version_tuple(remote_ver) <= _version_tuple(VERSION):
        print_success(f"Already up to date  (v{VERSION})")
        return False

    # Update available — download silently
    print_info(f"Update found: v{VERSION} → v{remote_ver}")
    _apply_update(remote_ver)
    return True

def _apply_update(new_ver: str):
    """Download all source files from GitHub and overwrite local copies."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    failed   = []
    ok       = []

    for fname in FILES_TO_UPDATE:
        url  = f"{GITHUB_RAW}/{fname}"
        data = _fetch(url)
        if data is None:
            failed.append(fname)
            continue
        dst = os.path.join(base_dir, fname)
        try:
            with open(dst, "w", encoding="utf-8") as f:
                f.write(data)
            ok.append(fname)
        except Exception as e:
            failed.append(fname)

    if failed:
        print_warn(f"Some files failed to update: {', '.join(failed)}")
    else:
        print_success(f"Updated to v{new_ver} successfully!")
        time.sleep(1)
