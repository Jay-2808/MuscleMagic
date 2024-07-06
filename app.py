from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
import os
from fee_remainder.GetUserInfo import Get_User_Info
from fee_remainder.SendMail import send_fee_reminder
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/static/data.json')
def get_data():
    return app.send_static_file('data.json')


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(Get_User_Info())

@app.route('/api/send-mail', methods=['POST'])
def send_mail():

    image_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Fee_remainder.png"
    attachment_path = r"E:\Jay-Files\Code\Projects\muscle-magic\img\MuscleMagic_Pricing.pdf" 

    #Company Information
    CEO_Name='Karthick A'
    Contact=9626729799

    data = request.json
    User_Id = data['User_Id']
    User_Name = data['User_Name']
    Current_Plan = data['Current_Plan']
    Current_Plan_amount = data['Current_Plan_amount']
    Due_Date = data['Due_Date']
    Status = data['Status']
    to = data['ClientMail']
    return send_fee_reminder(to, User_Id,User_Name,Current_Plan,Current_Plan_amount,Status,Due_Date,CEO_Name,Contact, image_path, attachment_path)

if __name__ == '__main__':
    app.run(debug=True)




