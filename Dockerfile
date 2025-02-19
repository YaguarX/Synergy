
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y
    python3
    python3-pip
    && rm -rf /var/lib/apt/lists/*

COPY script.py /usr/src/app/script.py

WORKDIR /usr/src/app

CMD ["python3", "script.py"]

