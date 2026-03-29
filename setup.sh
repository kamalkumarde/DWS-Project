#!/bin/bash

# Define the root project name
PROJECT_NAME="dws-platform"

echo "🚀 Initializing 1 PB Data Platform: $PROJECT_NAME"

# 1. Create Folder Structure
mkdir -p dags
mkdir -p src/core src/providers src/services/ingestor src/workers
mkdir -p terraform/environments/dev terraform/environments/prod
mkdir -p terraform/modules/bigquery terraform/modules/pubsub terraform/modules/storage terraform/modules/composer terraform/modules/monitoring
mkdir -p tests/unit
mkdir -p warehouse

# 2. Create Core Python Files
touch src/__init__.py src/main.py
touch src/core/__init__.py src/core/interfaces.py src/core/models.py src/core/factory.py src/core/batcher.py src/core/telemetry.py
touch src/providers/__init__.py src/providers/pubsub.py src/providers/gcs.py src/providers/bigquery.py src/providers/dlq.py src/providers/metrics.py
touch src/services/__init__.py src/services/ingestor/__init__.py src/services/ingestor/processor.py src/services/ingestor/worker.py

# 3. Create Orchestration & Config Files
touch dags/gcs_to_bq_ingestion.py
touch terraform/main.tf terraform/variables.tf
touch terraform/environments/dev/terraform.tfvars terraform/environments/prod/terraform.tfvars
touch requirements.txt README.md docker-compose.yml .gitignore

# 4. Populate .gitignore
cat <<EOF > .gitignore
venv/
__pycache__/
*.pyc
.env
.terraform/
*.tfstate
*.tfplan
EOF

# 5. Populate requirements.txtsh
cat <<EOF > requirements.txt
pydantic>=2.0.0
google-cloud-pubsub
google-cloud-storage
google-cloud-bigquery
google-cloud-monitoring
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-google-cloud-trace
EOF

echo "✅ Structure Created Successfully!"
echo "Next: Run 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'"