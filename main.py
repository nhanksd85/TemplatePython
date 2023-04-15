import PrivateTasks.private_task_1
import PrivateTasks.private_task_2
import PrivateTasks.main_ui_task
from Scheduler.scheduler import  *
import time

scheduler = Scheduler();
scheduler.SCH_Init()

task1 = PrivateTasks.private_task_1.Task1()
task2 = PrivateTasks.private_task_2.Task2()
main_ui = PrivateTasks.main_ui_task.Main_UI()

scheduler.SCH_Add_Task(task1.Task1_Run, 1000,2000)
scheduler.SCH_Add_Task(task2.Task2_Run, 1000,4000)
scheduler.SCH_Add_Task(main_ui.UI_Refresh, 1, 10)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.01)