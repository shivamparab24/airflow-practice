# Airflow Topics List

## Level 0 - Foundation

- DAG definition (with DAG, @dag)
- Tasks (PythonOperator, @task)
- Task execution model (worker runs tasks)
- Basic dependencies (>> , <<)
- Manual triggering
- Airflow UI (Graph, Logs, XCom)
- XCom basics (return values)
- DAG parsing (scheduler reads files)
- Docker setup

---

## Level 1 - Core Mechanics

- Task lifecycle (scheduled → queued → running → success/failed)
- Scheduler behavior
- Executors (Sequential, Local, Celery)
- Retries and failure handling
- Task dependencies and branching
- Sensors
- Scheduling (cron, @daily)
- Catchup vs backfill
- Logs and debugging

---

## Level 2 - Data & Communication

- XCom deep dive
- TaskFlow API
- Templates (Jinja)
- Variables
- Connections
- Hooks
- Operators

---

## Level 3 - Pipeline Design

- ETL / ELT patterns
- Idempotency
- Data partitioning
- Dynamic task mapping
- Parameterized DAGs
- Task groups
- Dataset scheduling

---

## Level 4 - Reliability

- Failure handling
- Retry strategies
- Timeouts and SLAs
- Stuck DAGs
- Monitoring and alerting
- Logging strategy

---

## Level 5 - Infrastructure

- Celery architecture
- Redis / RabbitMQ
- Metadata DB (Postgres)
- Scaling workers
- DAG parsing performance
- KubernetesExecutor

---

## Level 6 - Security

- Authentication (RBAC)
- User roles
- Secrets management
- Secure connections

---

## Level 7 - Internals

- Scheduler internals
- DAG parsing loop
- TaskInstance lifecycle
- DAG serialization
- Plugins
- Custom operators
- Performance issues

---

## Current Status

- Completed: Foundation
- Next: Core Mechanics + Data

---

## Key Idea

DAG = definition  
Task = execution  
Scheduler = orchestration  
Worker = execution engine  
XCom = small data passing