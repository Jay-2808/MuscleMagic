from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate(r"E:\Jay-Files\Code\Projects\muscle-magic\musclemagic-80175-firebase-adminsdk-lwua4-6ef322d0bd.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/api/users', methods=['GET'])
def get_users():
    users_ref = db.collection("users")
    docs = users_ref.stream()

    users = []

    for doc in docs:
        user = doc.to_dict()

        membership_ref = db.collection("membership").where("user_id", "==", user['_id'])
        payment_ref = db.collection("payments").where("user_id", "==", user['_id'])

        member = list(membership_ref.stream())
        payment = list(payment_ref.stream())

        if member:
            member = member[0].to_dict()
            current_plan = member["_plan"]
            current_plan_amount = member["_amount"]
            due_date = member["end_date"]
        else:
            current_plan = None
            current_plan_amount = None
            due_date = None

        if payment:
            payment = payment[0].to_dict()
            status = payment["_status"]
        else:
            status = None

        user_info = {
            "ClientMail": user['email'],
            "User_Id": user['_id'],
            "User_Name": user['name'],
            "Current_Plan": current_plan,
            "Current_Plan_amount": current_plan_amount,
            "Due_Date": due_date,
            "Status": status
        }
        users.append(user_info)

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
