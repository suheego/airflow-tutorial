from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

args = {
    "owner": "shg",
    "start_date": datetime(2022, 1, 1),
}

dag = DAG(dag_id="git_pull_dag", default_args=args, schedule_interval="@once")

git_pull = BashOperator(
    task_id="git_pull", bash_command="git checkout main \n git pull", dag=dag
)

git_pull
