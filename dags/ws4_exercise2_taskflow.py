import datetime

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'datath',
}


@task()
def print_hello():
    """
    Print Hello World!
    """
    print("Hello World!")
    

@task()
def print_date():
    """
    Print current date
    ref: https://www.w3schools.com/python/python_datetime.asp
    """
    print(datetime.datetime.now())


@dag(default_args=default_args, schedule_interval="@once", start_date=days_ago(1), tags=['exercise'])
def exercise2_taskflow_dag():

    t1 = print_hello()
    t2 = print_date()

    # Exercise2: Fan-out Pipeline
    # ใน exercise นี้จะได้รู้จักกับการแยก pipeline ออกเพื่อให้ทำงานแบบ parallel พร้อมกันได้
    # ซึ่ง TaskFlow แบบใหม่ ก็สามารถใช้งานร่วมกับการเขียน Operator แบบเดิมได้เหมือนกัน

    t3 = # TODO: สร้าง BashOperator เพื่อรัน gsutil ls (hint: ดูตัวอย่างจาก example dag ได้)
    
    # TODO: สร้าง dependency ให้ fan-out โดยที่ t1 ก่อน แล้วค่อยทำ t2, t3 พร้อม ๆ กัน
    

exercise2_dag = exercise2_taskflow_dag()
