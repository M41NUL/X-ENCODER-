# ─────────────────────────────────────────
#  X-ENCODER — utils.py
#  Dev: Md. Mainul Islam (MAINUL-X)
# ─────────────────────────────────────────

import sys, time, os

G  = "\033[92m"
R  = "\033[91m"
O  = "\033[38;5;208m"
W  = "\033[97m"
B  = "\033[1m"
RST= "\033[0m"

def clear():
    os.system("clear")

def print_success(msg):
    print(f"{G}{B}  ✔ {RST}{W}{msg}{RST}")

def print_error(msg):
    print(f"{R}{B}  ✘ {RST}{W}{msg}{RST}")

def print_info(msg):
    print(f"{O}{B}  ➤ {RST}{W}{msg}{RST}")

def print_warn(msg):
    print(f"{O}{B}  ⚠ {RST}{W}{msg}{RST}")

def separator(char="─", width=60, color=O):
    print(f"{color}{char*width}{RST}")

def animated_dots(label, duration=5, color=G):
    """Show spinning dots animation for `duration` seconds."""
    frames  = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_at  = time.time() + duration
    i       = 0
    try:
        while time.time() < end_at:
            frame = frames[i % len(frames)]
            sys.stdout.write(f"\r  {color}{B}{frame}{RST}  {W}{label}{RST}  ")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write(f"\r  {G}{B}✔{RST}  {W}{label} — Done!{RST}      \n")
        sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write("\n")

def progress_bar(label, total=30, color=G):
    """Simple progress bar animation."""
    bar_width = 40
    for i in range(total + 1):
        filled  = int(bar_width * i / total)
        bar     = "█" * filled + "░" * (bar_width - filled)
        pct     = int(100 * i / total)
        sys.stdout.write(
            f"\r  {color}{B}[{bar}]{RST} {W}{pct:3d}%  {label}{RST}"
        )
        sys.stdout.flush()
        time.sleep(0.06)
    print()

def prompt(msg, color=O):
    return input(f"\n  {color}{B}➤{RST}  {W}{msg}{RST}  ").strip()

def pause(msg="Press ENTER to continue..."):
    input(f"\n  {O}{msg}{RST}")
