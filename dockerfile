FROM python:3.12

WORKDIR /cicd-pipeline
COPY . .

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libffi-dev \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*

# RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "server.py"]