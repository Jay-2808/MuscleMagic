import schedule
import time
from threading import Thread

import CheckDueDate

def schedule_task(CEO_Name,Contact,image_path,attachment_path):
    print("Starting scheduled task...")
    CheckDueDate.check_due_date(CEO_Name,Contact,image_path,attachment_path)

def run_schedule_task(CEO_Name,Contact,image_path,attachment_path):
    schedule.every().day.at("01:00").do(schedule_task,CEO_Name,Contact,image_path,attachment_path)

    while True:
        schedule.run_pending()
        time.sleep(15)
