from flask import Flask,render_template
from threading import Thread
from datetime import datetime

import ScheduleTask #package


app = Flask(__name__)

@app.route('/')
def home():
    #return 'Fee Reminder Service'
    #return render_template('index.html')
    return render_template("file:///E:/Jay-Files/Code/Projects/muscle-magic/fee-remainder/connect-plus-1.0.0/index.html")


image_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Fee_remainder.png"
attachment_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Pricing.pdf" 

#Company Information
CEO_Name='Karthick A'
Contact=9626729799

if __name__ == '__main__':
    print("Starting Flask app...")
    ScheduleTask.run_schedule_task(CEO_Name,Contact,image_path,attachment_path)
    app.run(port=3000)