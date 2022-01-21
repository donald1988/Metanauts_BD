from airflow import DAG
from  airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import os
from datetime import datetime, timedelta

default_args = {
    "owner" : "airflow",
    "depends_on_past":False,
    "retries":1,
    "retry_delay":timedelta(minutes =5)
}

with DAG("first_dag", 
         default_args = default_args,
         start_date = datetime(2022, 2, 2),
         schedule_interval="@daily", 
         catchup=False,
         ) as dag:
    t1 = BashOperator(task_id = "start hadoop",
          bash_command = os.system['start-all.sh'],
          dag = dag)
    
    t2= BashOperator(task_id = "start spark",
                     bash_command =os.system['pyspark'], dag = dag)
    
    t3 = BashOperator(task_id ="start kafka",
                      bash_command = os.system['bin/zookeeper-server-start.sh  		config/zookeeper.properties'] + 
                                      os.system ['bin/kafka-server-start.sh 		config/server.properties'], dag = dag)
    
t1 > t2 > t3
