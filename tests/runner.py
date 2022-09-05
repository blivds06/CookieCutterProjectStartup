
import sys

import pytest

if __name__ == "__main__":
    args = sys.argv
    pytestargs = ["-o","nocursedirs=env"]
    if len(args) > 1:
        pytestargs.append("--junitxml")
        pytestargs.append(f"(args[1])\\test-results.xml")
        args.remove(args[1])
    pytest.main(pytestargs)