from threading import Thread
from datetime import datetime

import ScheduleTask #package

image_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Fee_remainder.png"
attachment_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Pricing.pdf" 

#Company Information
CEO_Name='Karthick A'
Contact=9626729799

if __name__ == '__main__':
    ScheduleTask.run_schedule_task(CEO_Name,Contact,image_path,attachment_path)