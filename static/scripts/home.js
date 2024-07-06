document.addEventListener('DOMContentLoaded', (event) => {
    // Toggle sidebar
    const sidebarToggleBtn = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');

    sidebarToggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('active');
    });

    // Highlight active menu item
    const menuItems = document.querySelectorAll('header nav ul li a');
    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            menuItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
        });
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    // Define the loginAccess function
    function loginAccess() {
        // Access the login div and set its innerHTML
        var loginDiv = document.getElementById('logindiv');
        if (loginDiv) {
            loginDiv.innerHTML = `
                <div class="main">
                    <h1>Muscle Magic</h1>
                    <h3>Enter your login credentials</h3>
                    <form action="">
                        <label for="first">
                            Username:
                        </label>
                        <input type="text"
                            id="first"
                            name="first"
                            placeholder="Enter your Username" required>

                        <label for="password">
                            Password:
                        </label>
                        <input type="password"
                            id="password"
                            name="password"
                            placeholder="Enter your Password" required>

                        <div class="wrap">
                            <button type="submit">
                                Submit
                            </button>
                        </div>
                    </form>
                </div>`;
        } else {
            console.error('Login div not found!');
        }
    }

    // Event listener for the login button
    const loginBtn = document.getElementById('login-btn');
    if (loginBtn) {
        loginBtn.addEventListener('click', () => {
            loginAccess();
        });
    } else {
        console.error('Login button not found!');
    }
});
