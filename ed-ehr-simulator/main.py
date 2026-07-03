# 🚀 Entry Point
from datetime import datetime

from ed_simulator.core.simulator import EDSimulator

def main():
    simulator = EDSimulator(
        start_time=datetime(2026, 6, 29, 8, 0, 0),
        duration_hours=12
    )

    simulator.run()

if __name__ == "__main__":
    main()