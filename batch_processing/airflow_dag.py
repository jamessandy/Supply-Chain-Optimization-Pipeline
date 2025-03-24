from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('supply_chain_batch_processing', default_args=default_args, schedule_interval='@daily')

extract_data = BashOperator(
    task_id='extract_data',
    bash_command='python extract_data.py',
    dag=dag
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='python transform_data.py',
    dag=dag
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='python load_data.py',
    dag=dag
)

extract_data >> transform_data >> load_data
