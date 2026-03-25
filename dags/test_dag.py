# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# def hello():
#     print("Hello from Airflow")

# with DAG(
#     dag_id="my_first_real_dag",
#     start_date=datetime(2024, 1, 1),
#     schedule=None,
#     catchup=False
# ) as dag:

#     task1 = PythonOperator(
#         task_id="hello_task",
#         python_callable=hello
#     )




# from airflow import DAG
# from airflow.decorators import task
# from datetime import datetime

# with DAG(
#     dag_id="my_first_real_dag",
#     start_date=datetime(2024, 1, 1),
#     schedule=None,
#     catchup=False
# ) as dag:

#     @task
#     def greet():
#         print("Hello from Airflow")

#     greet()








from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="my_first_real_dag",
    start_date=datetime(2024, 1, 1),
    schedule='*/1 * * * *',
    catchup=False
)

def my_dag():

    @task
    def extract():
        return 10

    @task
    def transform(x):
        return x * 2

    @task
    def load(result):
        print(f"Final result: {result}")

    data = extract()
    transformed = transform(data)
    load(transformed)

dag = my_dag()