let jsonData = [
    {"ClientMail": "jai28082004@gmail.com", "User_Id": "user1", "User_Name": "John Doe", "Current_Plan": "Gold", "Current_Plan_amount": "299", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user2", "User_Name": "Jane smith", "Current_Plan": "Elite", "Current_Plan_amount": "599", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user3", "User_Name": "Jay", "Current_Plan": "None", "Current_Plan_amount": "None", "Due_Date": "None", "Status": "no"}
];

function addMember(jsonData) {
let table = document.getElementById('members-table');
for(let i=0; i<jsonData.length; i++) {
    let newRow = table.insertRow(table.rows.length);
    try{
        newRow.insertCell(0).innerHTML = i+1;
        newRow.insertCell(1).innerHTML = jsonData[i].User_Id;
        newRow.insertCell(2).innerHTML = jsonData[i].User_Name;
        newRow.insertCell(3).innerHTML = jsonData[i].Current_Plan;
        newRow.insertCell(4).innerHTML = jsonData[i].Due_Date;
    }
    catch(error) {
        console.error(error.message);
    }
    
}
}

//addMember(jsonData);


async function getData() {
    //const url = "https://api.coindesk.com/v1/bpi/currentprice.json"; //dummy api
    //const url = "https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001"; //dummy api


    //const url="http://127.0.0.1:5000/static/data.json";


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



/*
/*let jsonData = [
    {"ClientMail": "jai28082004@gmail.com", "User_Id": "user1", "User_Name": "John Doe", "Current_Plan": "Gold", "Current_Plan_amount": "299", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user2", "User_Name": "Jane smith", "Current_Plan": "Elite", "Current_Plan_amount": "599", "Due_Date": "10/07/2024", "Status": "no"},
    {"ClientMail": "jayachandirank28@gmail.com", "User_Id": "user3", "User_Name": "Jay", "Current_Plan": "None", "Current_Plan_amount": "None", "Due_Date": "None", "Status": "no"}
];

function addMember(data) {
    let table = document.getElementById('members-table');
    data.forEach((member, index) => {
        let newRow = table.insertRow(table.rows.length);
        try {
            newRow.insertCell(0).innerHTML = index + 1;
            newRow.insertCell(1).innerHTML = member.User_Id;
            newRow.insertCell(2).innerHTML = member.User_Name;
            newRow.insertCell(3).innerHTML = member.Current_Plan;
            newRow.insertCell(4).innerHTML = member.Current_Plan_amount;
            newRow.insertCell(5).innerHTML = member.Due_Date;
            newRow.insertCell(6).innerHTML = member.Status;
        } catch (error) {
            console.error(error.message);
        }
    });
}

async function getData() {
    const cachedData = localStorage.getItem('cachedData');
    if (cachedData) {
        console.log("Using cached data");
        return Promise.resolve(JSON.parse(cachedData));
    } else {
        const url = "http://127.0.0.1:5000/api/users"; // Change the URL to your actual API endpoint
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const data = await response.json();
            console.log("Fetched new data");
            localStorage.setItem('cachedData', JSON.stringify(data)); // Cache the data in localStorage
            return data;
        } catch (error) {
            console.error(error.message);
        }
    }
}

// Optional: Function to clear the cache for testing purposes
function clearCache() {
    localStorage.removeItem('cachedData');
    console.log("Cache cleared");
}

// Clear cache for testing if needed
//clearCache();

// Fetch the data and then add the members to the table
getData().then(data => {
    addMember(jsonData);  // Add initial static data
    if (data) {
        addMember(data);  // Add fetched data
    }
});*/
