"""Try every import statement found in the Python snippets and report the ones that fail.

Use it to see where the book's names have drifted from the packages you installed:

    pip install -r requirements.txt && python scripts/check_imports.py

Names the snippets define locally (prompts, helpers, tools, middleware, lib) are skipped.
"""
import ast
import importlib
import pathlib
import sys

LOCAL = {"prompts", "helpers", "tools", "middleware", "lib", "managed_deepagents"}
failures, checked = [], 0
for path in sorted(pathlib.Path("chapters").rglob("*.py")) + sorted(pathlib.Path("build-alongs").rglob("*.py")):
    tree = ast.parse(path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            targets = [(a.name, None) for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            targets = [(node.module, a.name) for a in node.names]
        else:
            continue
        for module, name in targets:
            if module.split(".")[0] in sys.stdlib_module_names or module.split(".")[0] in LOCAL:
                continue
            checked += 1
            try:
                mod = importlib.import_module(module)
                if name and name != "*" and not hasattr(mod, name):
                    try:
                        importlib.import_module(f"{module}.{name}")
                    except Exception:
                        raise ImportError(f"cannot import name {name!r} from {module!r}")
            except Exception as e:  # noqa: BLE001
                failures.append((str(path), module, name, f"{type(e).__name__}: {e}"))
print(f"{checked} imports checked, {len(failures)} failed")
for f in failures:
    print(" -", f[0], "|", f[1], f[2] or "", "|", f[3])
sys.exit(1 if failures else 0)
