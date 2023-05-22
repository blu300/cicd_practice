#lint.py 

import sys 
import os
from pylint import lint  

THRESHOLD = 9  
script_dir = os.path.dirname(os.path.abspath(__file__))
factorial_path = os.path.join(script_dir, "..", "src", "factorial.py")

run = lint.Run([factorial_path], do_exit=False) 

score = run.linter.stats.global_note  # Access the linting score directly

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 
    sys.exit(1) 
    
sys.exit(0) 