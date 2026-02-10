from enum import Enum
import time

class State(Enum):
    CALM = "calm"
    CURIOUS = "curious"
    STRESSED = "stressed"
    CRACK = "crack"

class FSM:
    def __init__(self):
        self.state = State.CALM
        self.stress = 0.0
        self.last_update = time.time()

    def step(self, text: str):
        now = time.time()
        dt = now - self.last_update
        self.last_update = now
        self.stress = max(0.0, self.stress - dt * 0.15)
        
        if "?" in text: self.stress += 0.12
        if "!" in text: self.stress += 0.28
        
        if self.stress < 0.35: self.state = State.CALM
        elif self.stress < 0.65: self.state = State.CURIOUS
        elif self.stress < 1.1: self.state = State.STRESSED
        else: self.state = State.CRACK
        
        return self.state, round(self.stress, 3)
