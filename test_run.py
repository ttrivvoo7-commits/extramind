import os
import json
from core.fsm.machine import FSM

def main():
    try:
        brain = FSM()
        # Testataan logiikka
        state, stress = brain.step("Python 3.12.1 testi käynnissä!")
        
        report = {
            "version": "4.0.0-X",
            "env": "Codespaces / Python 3.12.1",
            "test_output": {
                "state": state.value,
                "stress": stress
            }
        }
        
        # Tallennetaan raportti
        os.makedirs('data/reports', exist_ok=True)
        with open('data/reports/initial_validation.json', 'w') as f:
            json.dump(report, f, indent=4)
            
        print(f"✅ TESTI OK: Tila = {state.value}, Stressi = {stress}")
    except Exception as e:
        print(f"❌ VIRHE: {e}")

if __name__ == "__main__":
    main()
