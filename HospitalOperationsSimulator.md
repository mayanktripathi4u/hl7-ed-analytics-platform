# Hospital Operations Simulator
Focusing on ED / ER Shift.

# Architceture
Everything revolves around a Simulation Clock.

Without a clock we can't answer:

- What time is it?
- Which patients have arrived?
- Which patient should be processed next?
- How many beds are occupied right now?
- What's the current ED census?

So everything starts here.

```sh
                    Simulation Clock
                           │
      ┌────────────────────┼────────────────────┐
      ▼                    ▼                    ▼
 Patient Arrivals      Event Queue         Facility State
      │                    │                    │
      └────────────────────┼────────────────────┘
                           ▼
                     Expanse Simulator
```

Planning to have **five small components** as:

1. SimulationClock 
    - This becomes the heartbeat.
    - Every service uses THIS clock.
    - Never `datetime.now()` again.
2. ArrivalGenerator
    - Real hospitals don't receive patients every minute.
    - Patient arrivals follow a pattern. 
    - For now... Let's generate 1 patient every 3-12 minutes.
    - Later we'll replace this with a Poisson distribution.
3. JourneyGenerator
    - scenario driven.
2. EventQueue
3. EDSimulator

Every class should have one responsibility.

# Folder Structure
```sh
src_v3/
    services/
    ehr-simulator/
        app/
            simulation_clock.py
            arrival_generator.py
            journey_generator.py
            event_queue.py
            simulator.py

            patient_factory.py
            encounter_factory.py
            timeline_engine.py
```

# Sequence
```sh
Initialize Clock
    ↓
Generate Patient
    ↓
Generate Encounter
    ↓
Generate Journey
    ↓
Publish Events
    ↓
Advance Clock
    ↓
Repeat
    ↓
Replay Event Queue
    ↓
HL7 Builder
    ↓
Output
```

