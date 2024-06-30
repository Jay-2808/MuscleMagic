import firebase_admin
from firebase_admin import credentials,firestore


cred = credentials.Certificate(r"E:\Jay-Files\Code\Projects\muscle-magic\musclemagic-80175-firebase-adminsdk-lwua4-6ef322d0bd.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection("users")
docs = users_ref.stream()

def Get_User_Info():
    Users=[]

    for doc in docs:
        user=doc.to_dict()

        membership_ref=db.collection("membership").where("user_id","==",user['_id'])
        payment_ref=db.collection("payments").where("user_id","==",user['_id'])
        
        member=list(membership_ref.stream())
        payment = list(payment_ref.stream())

        if member:
            member = member[0].to_dict()

            Current_Plan=member["_plan"]
            Current_Plan_amount=member["_amount"]
            Due_Date=member["end_date"]
        
        else:
            Current_Plan = None
            Current_Plan_amount = None
            Due_Date = None       
        

        if payment:
            payment = payment[0].to_dict()
            Status=payment["_status"]

        else:
            Payment_Status = None

        UserInfo = {
            "ClientMail" : user['email'],
            "User_Id":user['_id'],
            "User_Name":user['name'],
            "Current_Plan":Current_Plan,
            "Current_Plan_amount":Current_Plan_amount,
            "Due_Date":Due_Date,
            "Status":Status
        }
        Users.append(UserInfo)
    return Users