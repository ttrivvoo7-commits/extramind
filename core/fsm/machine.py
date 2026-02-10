from enum import Enum
import time
class State(Enum):
    CALM, CURIOUS, STRESSED, CRACK = "calm", "curious", "stressed", "crack"
class FSM:
    def __init__(self):
        self.state, self.stress, self.last_update = State.CALM, 0.0, time.time()
    def step(self, text: str):
        now = time.time()
        self.stress = max(0.0, self.stress - (now - self.last_update) * 0.15)
        self.last_update = now
        if "?" in text: self.stress += 0.15
        if "!" in text: self.stress += 0.30
        if self.stress < 0.35: self.state = State.CALM
        elif self.stress < 0.70: self.state = State.CURIOUS
        elif self.stress < 1.1: self.state = State.STRESSED
        else: self.state = State.CRACK
        return self.state, round(self.stress, 3)
