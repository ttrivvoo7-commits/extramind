import random
from core.fsm.machine import State

def get_hiki_params(state, stress):
    params = {
        "state": state.value,
        "stress": stress,
        "intensity": 1.0 + (stress * 0.4),
        "timing_drift": 1.0,
        "micro_fail": False
    }
    
    if state == State.STRESSED:
        params["timing_drift"] = random.uniform(0.9, 1.1)
        params["micro_fail"] = random.random() < 0.2
    elif state == State.CRACK:
        params["timing_drift"] = random.uniform(0.7, 1.4)
        params["micro_fail"] = True
        
    return params
