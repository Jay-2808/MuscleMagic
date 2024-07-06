# MuscleMagic

MuscleMagic is an intern project, a comprehensive project management tool designed for gym administrators. It provides functionalities for managing gym memberships, sending fee reminders, and viewing user activities through an admin interface.

# Introduction

**MuscleMagic** is a comprehensive project management tool designed for gym administrators to streamline **membership management** and enhance **user engagement**. Built with **Python** and **Flask**, **MuscleMagic** offers robust functionalities for managing **gym memberships**, sending **automated and manual fee reminders**, and gaining insights into **member activities** through an intuitive **admin interface**. Leveraging **Firebase Firestore** for data storage, **MuscleMagic** ensures efficient data management and real-time access to **member information**. With ongoing development to introduce features like **interactive dashboards** and **AI/ML integration**, **MuscleMagic** aims to revolutionize gym management by combining cutting-edge technology with **user-centric design**.

- **Member Management:**
  - View and manage gym members' details stored in Firebase Firestore.
  - Add, edit, and delete member information.

- **Manual Fee Reminders:**
  - Send manual fee reminders to members via email.
  - Admins can view members nearing their fee due dates and send reminders directly.

- **Dashboard (Under Development):**
  - Monitor member activities, subscription statuses, and overall gym performance through interactive dashboards.
  - Track member engagement and subscription renewals.

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: Firestore

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Jay-2808/MuscleMagic.git
   cd MuscleMagic

2. Set up a virtual environment and install dependencies:
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt

3. Set up Firestore:
    1.Obtain the Firebase Admin SDK JSON file.
    2.Place the JSON file in the project directory.
    3.Update the path in your GetUserInfo.py file.


### Usage

To start accessing member information and sending manual fee reminders:

1. **Start the Flask Application:**
     ```bash
     python main.py
     ```
This command initializes the Flask server.

2. **Access the Web Application:**
Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. **Navigating Through the Application:**

- **Home Page:** Upon accessing the application, you will land on the homepage (`home.html`), where you can explore general information about MuscleMagic.

- **Viewing Members:** Navigate to the "Members" section to view details of all members stored in Firestore. Clicking on the "Members" link directs you to a page (`members.html`) displaying member data.

- **Sending Manual Fee Reminders:** Within the "Member Status" section of the website, you can manually send fee reminders to members via email. Each member listed will have a "Send Reminder" button for this purpose.

- **Dashboard and Other Features:** Additional functionalities, such as the dashboard and other pages (`dashboard.html`, `payments.html`, `courses.html`, etc.), are under development and will be accessible once implemented.

4. **Exploring Features:**
Navigate through the website to explore different sections and functionalities related to managing MuscleMagic subscriptions and member interactions.


# Automating Fee Reminders in MuscleMagic

Automating fee reminders is crucial for managing subscriptions and ensuring timely payments in MuscleMagic. Here’s how you can set it up using Python scripts.

## Steps to Automate Fee Reminders

1. **Navigate to the `fee_remainder` Folder:**
   - Open your terminal or command prompt.
   - Change directory to where your `main.py` and `ScheduleTask.py` are located:
     ```bash
     cd path/to/your/fee_remainder
     ```

2. **Run `main.py`:**
   - `main.py` initializes the scheduling of fee reminders:
     ```bash
     python main.py
     ```
     - Adjust the command based on your Python environment setup.

3. **Understanding `main.py`:**
   - This script kicks off the automated process. It typically imports necessary modules and starts running tasks defined in `ScheduleTask.py`.

4. **Edit Scheduling Time in `ScheduleTask.py`:**
   - Open `ScheduleTask.py` in a text editor or IDE.
   - Locate the scheduling logic, often found in a function like `run_schedule_task()`.
     ```python         schedule.every().day.at("09:00").do(send_fee_reminder)
     ```
     - Modify `"09:00"` to your preferred time, e.g., `"10:00"` for 10 AM.

5. **Advantages of Automation:**
   - **Efficiency:** Automating fee reminders eliminates manual effort, saving time for administrative tasks.
   - **Consistency:** Reminders are sent at predefined intervals without human oversight, reducing the risk of missed notifications.
   - **Scalability:** Easily scale reminders as your user base grows, without increasing administrative workload.
   - **Improved Cash Flow:** Timely reminders encourage prompt payments, improving cash flow management for your fitness club.

6. **Continuous Execution:**
   - Keep `main.py` running continuously in your development environment or as part of your deployment strategy to ensure reminders are sent as scheduled.

7. **Customization and Deployment:**
   - Customize the reminder content and scheduling logic to fit specific business needs.
   - Deploy your application to a cloud platform (like AWS, Heroku, or Vercel) for automated, scalable execution in production environments.

### Conclusion

Automating fee reminders through `main.py` and `ScheduleTask.py` not only simplifies administrative workflows but also enhances user satisfaction by ensuring timely communication and payments. The ability to manually send fee reminders via the "Member Status" section of the website adds flexibility and personalization to member interactions, fostering a proactive approach to member engagement. Additionally, the feature to view detailed member information provides administrators with valuable insights into member demographics and subscription statuses, facilitating informed decision-making.

By leveraging Python’s robust scheduling capabilities and integrating these features into the MuscleMagic platform, the organization improves operational efficiency, reduces manual workload, and enhances financial predictability. Implementing automated and manual fee reminders underscores MuscleMagic's commitment to maintaining a robust membership experience, driving member retention, and promoting sustainable growth in the fitness industry.

## Future Enhancements
    Implement Bootstrap or React.js for frontend improvements.
    Add AI/ML features for advanced user analytics.
    Deploy the project on Vercel or AWS.


## Contact
For any questions or feedback, please reach out at jayachandirank28@gmail.com
