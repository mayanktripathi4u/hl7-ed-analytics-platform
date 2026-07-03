# Build an ED Analytics Data Mart

My first draft - proposed architecture on what I am trying to build.

```sh
               ┌────────────────────────┐
               │ Simulated EHR System   │
               │ Python HL7 Generator   │
               └───────────┬────────────┘
                           │
                           ▼
                Simulated MEDITECH Expanse
                           │
                    HL7 ADT Messages
                           │
                           ▼
                Data Store (Landing Zone)
        (GCS Bronze + BigQuery Bronze Tables)
                           │
         Parse every HL7 Segment separately
                           │
        ┌──────────┬───────────┬─────────────┐
        ▼          ▼           ▼             ▼
      MSH         PID         PV1           Z Segments
        │          │           │             │
        └──────────┴───────────┴─────────────┘
                           │
                     Transformation
                  (Python / Dataflow)
                           │
                           ▼
                 ED Analytics Data Mart
                (BigQuery Silver / Gold)
                           │
                 Sync latest state to
                    Google Bigtable
                           │
                           ▼
                      FastAPI Service
                           │
                     REST / JSON APIs
                           │
                           ▼
                Streamlit Dashboard
```

# HL7 Segments to Use
Here are the segments I'd parse.

- MSH
  - Purpose
  - Message metadata
  - Useful fields
   
    | HL7 Field           | Dashboard Use   |
    | ------------------- | --------------- |
    | Message Timestamp   | Timeline        |
    | Sending Facility    | Hospital        |
    | Sending Application | Expanse         |
    | Message Type        | ADT A01/A03/A08 |
    | Control ID          | Tracking        |

- EVN
  - Event information
  - Useful: 
    ```sh
    Event Time
    Event Type
    Recorded Time
    ```
    Useful for patient flow timeline.

- PID
  - Patient demographics
  - Dashboard
    ```sh
    MRN
    Age
    Gender
    ZIP Code
    Race
    Ethnicity
    ```    
    Example analytics
  - ED patients by age
  - Pediatric vs Adult
  - Male/Female ratio

- PV1
  - This is the most important segment.
  - Contains nearly everything needed.
  - Useful fields
    ```sh
    Patient Class
    Assigned Location
    Facility
    Building
    Unit
    Room
    Bed
    Attending Physician
    Consulting Physician
    Hospital Service
    Visit Number
    Admission Type
    Financial Class
    ```
    Most ED dashboards are driven almost entirely by PV1.

- Z Segments
  - This is where things get interesting.
  - Hospitals customize these.
  - For ED, I'd include fields like
    ```sh
    ED Arrival Method
    EMS
    Walk-In
    Police
    Helicopter
    Ambulance Number
    Triage Level
    ESI Score
    Waiting Status
    Bed Assignment
    Isolation Flag
    Fast Track
    Stroke Alert
    Trauma Alert
    Sepsis Alert
    Code Status
    Expected Admit
    Observation Status
    ```
    These become your dashboard's "secret sauce."

    
# Configuration
Use a shared `.env` for local development:
```sh
PROJECT_ID=

BQ_BRONZE_DATASET=

BQ_SILVER_DATASET=

BQ_GOLD_DATASET=

BIGTABLE_INSTANCE=

BIGTABLE_TABLE=

GCS_BUCKET=

LOCATION=

LOG_LEVEL=INFO
```

# HL7 Message Generator
This will be my first functional service because everything downstream depends on it.

It will:
- Generate realistic ADT messages.
- Produce different scenarios:
  - Walk-in patient
  - Ambulance arrival
  - Trauma alert
  - Stroke alert
  - Pediatric patient
  - Patient discharge
  - Bed transfer
- Include realistic custom Z-segments.
- Write raw messages to the Bronze GCS bucket (or a local folder during development).

# Expanse Simulator
Consumes the generated HL7 message and simulates how an EHR would forward it to the data repository. Initially, this can simply copy messages from an input folder to the Bronze landing area while adding metadata.

# Scenario-driven Simulator
Instead of generating only random HL7 messages, I'll build a scenario-driven simulator. 

Plan is to define a set of patient encounter scenarios (e.g., ambulance trauma arrival, chest pain walk-in, pediatric fever, stroke alert, discharge after treatment). 

Each scenario will populate the relevant HL7 segments—including custom Z-segments—with realistic values. 

This approach will make the downstream analytics and dashboard much more meaningful because I should  be able to demonstrate real ED / ER workflows rather than arbitrary data.

This also creates a reusable framework: I mean adding a new scenario later is just adding another configuration and message template rather than rewriting the generator.

