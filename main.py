import PrivateTasks.private_task_1
import PrivateTasks.private_task_2
import PrivateTasks.main_ui_task
import PrivateTasks.led_blinky_task
from Scheduler.scheduler import  *
from Utilities.softwaretimer import *
import time

scheduler = Scheduler()
scheduler.SCH_Init()
soft_timer = softwaretimer()

task1 = PrivateTasks.private_task_1.Task1()
task2 = PrivateTasks.private_task_2.Task2()
main_ui = PrivateTasks.main_ui_task.Main_UI()
ledblink = PrivateTasks.led_blinky_task.LedBlinkyTask(soft_timer)

scheduler.SCH_Add_Task(task1.Task1_Run, 1000,2000)
scheduler.SCH_Add_Task(task2.Task2_Run, 1000,4000)
scheduler.SCH_Add_Task(main_ui.UI_Refresh, 1, 10)
scheduler.SCH_Add_Task(soft_timer.Timer_Run, 1, 1)
scheduler.SCH_Add_Task(ledblink.LedBlinkyTask_Run, 1, 1)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)