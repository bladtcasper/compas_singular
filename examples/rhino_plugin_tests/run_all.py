"""Run every Rhino-plugin test in one go, each in its own process. No Rhino needed.

    python run_all.py

Each file installs fake ``Rhino`` / ``rhinoscriptsyntax`` modules, and compas
decides whether it is inside Rhino by looking for exactly those -- so sharing one
interpreter would let one file's stub leak into the next. Run it under both
``singular312`` and Rhino 8's own CPython (see README.md).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = sorted(name for name in os.listdir(HERE) if name.startswith("test_") and name.endswith(".py"))


def main():
    failed = []
    for name in TESTS:
        print("\n" + "#" * 62)
        print("# {}".format(name))
        print("#" * 62)
        if subprocess.run([sys.executable, os.path.join(HERE, name)], cwd=HERE).returncode:
            failed.append(name)
    print("\n" + "#" * 62)
    if failed:
        print("# {} of {} FAILED: {}".format(len(failed), len(TESTS), ", ".join(failed)))
        return 1
    print("# all {} test files passed".format(len(TESTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
