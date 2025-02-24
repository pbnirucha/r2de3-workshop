from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago


with DAG(
    "exercise3_fan_in_dag",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["exercise"]
) as dag:

    # Exercise3: Fan-in Pipeline
    # ใน exercise นี้จะได้รู้จักการเขียน task ใน pipeline ขั้นตอนเยอะขึ้น
    # ใช้ DummyOperator เป็น task จำลอง
    
    t0 = DummyOperator(task_id="task_0")
    t4 = DummyOperator(task_id="task_4")

    t0 >> t4
    
    # TODO: สร้าง DummyOperator เพื่อสร้าง dependency ที่ซับซ้อน ตามรูป
