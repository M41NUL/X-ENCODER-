#!/usr/bin/env python3
# ─────────────────────────────────────────
#  X-ENCODER — main.py
#  Dev: Md. Mainul Islam (MAINUL-X)
# ─────────────────────────────────────────

import sys, os

# Ensure script dir is in path so sibling modules resolve
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils   import clear, print_success, print_info, separator
from banner  import show_banner
from updater import check_and_update
from menu    import show_menu

G  = "\033[92m"
O  = "\033[38;5;208m"
W  = "\033[97m"
B  = "\033[1m"
RST= "\033[0m"


def main():
    clear()
    show_banner()
    separator(color=O)
    print_info("Initializing X-ENCODER...")
    print()

    # Auto update check (5-second animated check, silent apply)
    try:
        check_and_update()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass  # Never crash on update failure

    print()
    print_success("Ready! Loading main menu...")

    import time
    time.sleep(1)

    # Launch interactive menu
    show_menu()


if __name__ == "__main__":
    main()
