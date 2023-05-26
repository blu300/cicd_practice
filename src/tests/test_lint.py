# lint.py

import sys
from pylint import lint  # type: ignore

THRESHOLD = 9

run = lint.Run([ "./src/*.py"
    #"./src/tests/test_lint.py", "./src/factorial.py"
                ], do_exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
