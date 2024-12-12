FROM python:3.10-slim

WORKDIR /app

COPY generate_csv.py anonymize_csv.py requirements.txt ./

RUN pip install -r requirements.txt


CMD ["python", "generate_csv.py"]
