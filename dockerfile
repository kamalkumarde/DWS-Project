# Multi-stage build for security
FROM python:3.11-slim as builder 
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
# Copy only the installed packages and source
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/

# OpenShift requirement: Ensure the container can run as any UID
RUN chgrp -R 0 /app && chmod -R g=u /app

ENV PATH=/root/.local/bin:$PATH
ENTRYPOINT ["python", "-m", "src.core.kafka_client"]

FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/main.py"]