# ─────────────────────────────────────────
#  X-ENCODER — encoder.py
#  Dev: Md. Mainul Islam (MAINUL-X)
# ─────────────────────────────────────────

import marshal, zlib, base64, py_compile, os, tempfile
from datetime import datetime
from config import ENCODE_HEADER

G  = "\033[92m"
R  = "\033[91m"
O  = "\033[38;5;208m"
W  = "\033[97m"
B  = "\033[1m"
RST= "\033[0m"


def _encode_source(source: str) -> str:
    """
    3-layer encoding:
      1. Marshal  — compile source to Python bytecode (code object)
      2. Zlib     — compress the marshalled bytes
      3. Base64   — encode compressed bytes to ASCII-safe string
    Returns a runnable Python file string.
    """
    # Layer 1 — compile to code object via a temp file
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as tf:
        tf.write(source)
        tmp_path = tf.name
    try:
        code_obj = compile(source, tmp_path, "exec")
    finally:
        os.unlink(tmp_path)

    # Layer 2 — marshal → bytes
    marshalled = marshal.dumps(code_obj)

    # Layer 3 — zlib compress
    compressed = zlib.compress(marshalled, level=9)

    # Layer 4 — base64 encode
    encoded = base64.b64encode(compressed).decode("utf-8")

    # Build self-executing loader
    loader = (
        "import marshal, zlib, base64\n"
        f"exec(marshal.loads(zlib.decompress(base64.b64decode({repr(encoded)}))))\n"
    )
    return loader


def encode_file(input_path: str, output_path: str) -> bool:
    """Encode a single .py file. Returns True on success."""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            source = f.read()

        encoded_body = _encode_source(source)

        header = ENCODE_HEADER.format(
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        final = header + "\n" + encoded_body

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final)

        return True
    except SyntaxError as e:
        print(f"{R}{B}  ✘ Syntax error in {input_path}: {e}{RST}")
        return False
    except Exception as e:
        print(f"{R}{B}  ✘ Failed: {e}{RST}")
        return False


def encode_folder(input_folder: str, output_folder: str) -> tuple:
    """
    Encode all .py files in input_folder into output_folder.
    Returns (success_count, fail_count, output_paths).
    """
    ok, fail, saved = 0, 0, []
    input_folder  = os.path.normpath(input_folder)
    output_folder = os.path.normpath(output_folder)

    py_files = [
        f for f in os.listdir(input_folder)
        if f.endswith(".py") and os.path.isfile(os.path.join(input_folder, f))
    ]

    if not py_files:
        return 0, 0, []

    for fname in py_files:
        src  = os.path.join(input_folder, fname)
        dst  = os.path.join(output_folder, fname)
        if encode_file(src, dst):
            ok += 1
            saved.append(dst)
        else:
            fail += 1

    return ok, fail, saved
