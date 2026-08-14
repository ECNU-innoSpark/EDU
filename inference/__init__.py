import os
import sys

_INFERENCE_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR   = os.path.dirname(_INFERENCE_DIR)
ROOT_DIR       = os.path.dirname(_SCRIPTS_DIR)

sys.path.insert(0, _SCRIPTS_DIR)

RESULTS_DIR = os.path.join(ROOT_DIR, "results")
