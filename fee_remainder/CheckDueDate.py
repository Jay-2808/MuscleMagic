from datetime import datetime
import pytz
import GetUserInfo #package
import SendMail #package

def check_due_date(CEO_Name,Contact,image_path,attachment_path):
    users=GetUserInfo.Get_User_Info()
    for user in users:
        due_date_str = str(user["Due_Date"])
        if due_date_str and due_date_str != "None":
            try:
                end_date = datetime.fromisoformat(due_date_str)

                # Get the current date and time
                current_date = datetime.now(pytz.utc)

                # Check for due date
                if current_date <= end_date and ((end_date - current_date).days) <= 7:
                    Due_Date = end_date.strftime("%d/%m/%Y")
                    print(Due_Date)

                    SendMail.send_fee_reminder(
                        user["ClientMail"], user["User_Id"], user["User_Name"],
                        user["Current_Plan"], user["Current_Plan_amount"],
                        user["Status"], Due_Date, CEO_Name, Contact,
                        image_path, attachment_path
                    )
            except ValueError as e:
                print(f"Error parsing date: {due_date_str} - {e}")