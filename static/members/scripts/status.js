let jsonData = [
    {"ClientMail": "jai28082004@gmail.com", "User_Id": "user1", "User_Name": "John Doe", "Current_Plan": "Gold", "Current_Plan_amount": "299", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user2", "User_Name": "Jane smith", "Current_Plan": "Elite", "Current_Plan_amount": "599", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user3", "User_Name": "Jay", "Current_Plan": "None", "Current_Plan_amount": "None", "Due_Date": "None", "Status": "no"}
];

function addMember(Data) {
let table = document.getElementById('members-table');
for(let i=0; i<Data.length; i++) {
    let newRow = table.insertRow(table.rows.length);
    try{
        newRow.insertCell(0).innerHTML = i+1;
        newRow.insertCell(1).innerHTML = Data[i].User_Id;
        newRow.insertCell(2).innerHTML = Data[i].User_Name;
        newRow.insertCell(3).innerHTML = Data[i].Current_Plan;
        newRow.insertCell(4).innerHTML = Data[i].Current_Plan_amount;
        newRow.insertCell(5).innerHTML = Data[i].Due_Date;
        newRow.insertCell(6).innerHTML = Data[i].Status;
        newRow.insertCell(7).innerHTML = `<button class="btn btn-success" onclick="updateStatus('${Data[i].User_Id}', '${Data[i].User_Name}', '${Data[i].ClientMail}', '${Data[i].Current_Plan}', '${Data[i].Current_Plan_amount}', '${Data[i].Due_Date}', '${Data[i].Status}')">Send Reminder</button>`;
    }
    catch(error) {
        console.error(error.message);
    }
    
}
}

async function updateStatus(User_Id, User_Name, ClientMail, Current_Plan, Current_Plan_amount, Due_Date, Status) {
    console.log(User_Id, User_Name, ClientMail, Current_Plan, Current_Plan_amount, Due_Date, Status);

    const url = "http://127.0.0.1:5000/api/send-mail";
    
    try {
        const response = await fetch(url,{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "User_Id": User_Id,
                "User_Name": User_Name,
                "ClientMail": ClientMail,
                "Current_Plan": Current_Plan,
                "Current_Plan_amount": Current_Plan_amount,
                "Due_Date": Due_Date,
                "Status": Status
            })
        });
        if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(`Response status: ${response.status}`);
        }

        const responseData = await response.json();
        console.log('Email sent successfully:', responseData.message);

    } catch (error) {
    console.error('Error sending email:', error);
    }

}

//addMember(jsonData);

async function getData() {
    const url = "http://127.0.0.1:5000/api/users";
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        console.log("Total number of members :" + data.length);

        addMember(data);

    } catch (error) {
    console.error(error.message);
    }
}
getData();