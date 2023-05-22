#lint.py

import sys
from pylint import lint

THRESHOLD = 6

run = lint.Run([ './src/tests/test_lint.py'
                ,'./src/factorial.py'
                ], do_exit=False)

score = run.linter.stats.global_note  # Access the linting score directly

if score < THRESHOLD:

    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
