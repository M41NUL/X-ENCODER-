# ─────────────────────────────────────────
#  X-ENCODER — menu.py
#  Dev: Md. Mainul Islam (MAINUL-X)
# ─────────────────────────────────────────

import os
from encoder import encode_file, encode_folder
from utils   import (clear, print_success, print_error, print_info,
                     print_warn, separator, prompt, pause, progress_bar)
from banner  import show_banner

G  = "\033[92m"
R  = "\033[91m"
O  = "\033[38;5;208m"
W  = "\033[97m"
B  = "\033[1m"
DIM= "\033[2m"
RST= "\033[0m"


def _menu_header():
    print(f"\n  {O}{B}╔══════════════════════════════════════╗{RST}")
    print(f"  {O}{B}║       {G}MAIN MENU  —  X-ENCODER{O}        ║{RST}")
    print(f"  {O}{B}╚══════════════════════════════════════╝{RST}\n")


def _option(num, icon, label, desc):
    print(f"  {O}{B}[{num}]{RST}  {G}{icon}  {B}{label}{RST}")
    print(f"        {DIM}{W}{desc}{RST}\n")


def show_menu():
    while True:
        clear()
        show_banner()
        _menu_header()
        _option("1", "📄", "Encode Single File",
                "Encode one .py file using Marshal+Zlib+Base64")
        _option("2", "📁", "Encode Folder",
                "Encode all .py files inside a folder")
        _option("3", "ℹ ", "About / Info",
                "Developer info & tool details")
        _option("0", "🚪", "Exit",
                "Quit X-ENCODER")
        separator()

        choice = prompt("Select option", color=G)

        if choice == "1":
            _handle_single()
        elif choice == "2":
            _handle_folder()
        elif choice == "3":
            _handle_about()
        elif choice == "0":
            _exit_tool()
            break
        else:
            print_warn("Invalid option. Try again.")
            pause()


# ── Option 1: Single file ──────────────────────────────────────────────────────

def _handle_single():
    clear()
    show_banner()
    print(f"\n  {G}{B}[ ENCODE SINGLE FILE ]{RST}\n")
    separator()

    print(f"  {DIM}{W}Example : /sdcard/myproject/hello.py{RST}\n")
    inp = prompt("Enter file path")
    if not inp:
        print_error("No path entered.")
        pause(); return

    inp = os.path.expandvars(os.path.expanduser(inp))

    if not os.path.isfile(inp):
        print_error(f"File not found: {inp}")
        pause(); return

    if not inp.endswith(".py"):
        print_warn("File does not end with .py — proceeding anyway.")

    print(f"\n  {DIM}{W}Example : hello_encoded{RST}\n")
    out_name = prompt("Enter output name (without .py)")
    if not out_name:
        print_error("No output name entered.")
        pause(); return

    out_dir  = os.path.dirname(os.path.abspath(inp))
    out_path = os.path.join(out_dir, out_name + ".py")

    print()
    progress_bar("Encoding", total=25, color=G)

    success = encode_file(inp, out_path)
    if success:
        print_success(f"Saved: {out_path}")
    else:
        print_error("Encoding failed. Check file for syntax errors.")

    pause()


# ── Option 2: Folder ───────────────────────────────────────────────────────────

def _handle_folder():
    clear()
    show_banner()
    print(f"\n  {G}{B}[ ENCODE FOLDER ]{RST}\n")
    separator()

    print(f"  {DIM}{W}Example : /sdcard/myproject/scripts/{RST}\n")
    inp_folder = prompt("Enter folder path")
    if not inp_folder:
        print_error("No path entered.")
        pause(); return

    inp_folder = os.path.expandvars(os.path.expanduser(inp_folder))

    if not os.path.isdir(inp_folder):
        print_error(f"Folder not found: {inp_folder}")
        pause(); return

    print(f"\n  {DIM}{W}Example : scripts_encoded{RST}\n")
    out_name = prompt("Enter output folder name")
    if not out_name:
        print_error("No output name entered.")
        pause(); return

    parent_dir = os.path.dirname(os.path.normpath(os.path.abspath(inp_folder)))
    out_folder = os.path.join(parent_dir, out_name)

    print()
    progress_bar("Encoding files", total=30, color=G)

    ok, fail, saved = encode_folder(inp_folder, out_folder)

    if ok == 0 and fail == 0:
        print_warn("No .py files found in the folder.")
    else:
        print_success(f"Saved to: {out_folder}/")
        print_info(f"Encoded: {ok} file(s)  |  Failed: {fail} file(s)")
        if fail > 0:
            print_warn("Some files had errors — check for syntax issues.")

    pause()


# ── Option 3: About ────────────────────────────────────────────────────────────

def _handle_about():
    clear()
    show_banner()
    pause()


# ── Exit ───────────────────────────────────────────────────────────────────────

def _exit_tool():
    print(f"\n  {G}{B}Goodbye from X-ENCODER!{RST}")
    print(f"  {O}github.com/M41NUL  |  t.me/mainul_x_official{RST}\n")
