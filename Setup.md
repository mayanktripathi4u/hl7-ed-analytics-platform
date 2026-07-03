```sh
git clone https://github.com/mayanktripathi4u/hl7-ed-analytics-platform.git

cd hl7-ed-analytics-platform

poetry --version

poetry init

poetry add faker

poetry run pip show faker yaml rich pydantic 

poetry install --no-root

poetry run python src_v1/services/ehr-simulator/main.py

poetry add jinja2

poetry run python src_v2/services/ehr-simulator/main.py
```


ed-ehr-simulator:
```sh
poetry run python ed-ehr-simulator/main.py


```
