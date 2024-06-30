"""
npm install firebase

-----------------------------------------------------------------------------------------------------------

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCjIHgsq8O7wo5rpoKgtA4HyZbqfbXLEH4",
  authDomain: "muscle-magic-fees-reminder.firebaseapp.com",
  projectId: "muscle-magic-fees-reminder",
  storageBucket: "muscle-magic-fees-reminder.appspot.com",
  messagingSenderId: "963097010463",
  appId: "1:963097010463:web:fb37a98e0a909bc1e0102a"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
"""

------------------------------------------------------------------------------------------------------------------------------------------

Use npm

Use a <script> tag
If you're already using NPM and a module bundler such as webpack or Rollup, you can run the following command to install the latest SDK (Learn more):

npm install firebase
Then, initialise Firebase and begin using the SDKs for the products that you'd like to use.

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCjIHgsq8O7wo5rpoKgtA4HyZbqfbXLEH4",
  authDomain: "muscle-magic-fees-reminder.firebaseapp.com",
  projectId: "muscle-magic-fees-reminder",
  storageBucket: "muscle-magic-fees-reminder.appspot.com",
  messagingSenderId: "963097010463",
  appId: "1:963097010463:web:fb37a98e0a909bc1e0102a"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
Note: This option uses the modular JavaScript SDK, which provides a reduced SDK size.

Learn more about Firebase for web: Get started, Web SDK API Reference, Samples

------------------------------------------------------------------------------------------------------------------------------------------


Use npm

Use a <script> tag
If you don't use build tools, use this option to add and use the Firebase JS SDK. Use this option to get started, but it's not recommended for production apps. Learn more.

Copy and paste these scripts into the bottom of your <body> tag, but before you use any Firebase services:

<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyCjIHgsq8O7wo5rpoKgtA4HyZbqfbXLEH4",
    authDomain: "muscle-magic-fees-reminder.firebaseapp.com",
    projectId: "muscle-magic-fees-reminder",
    storageBucket: "muscle-magic-fees-reminder.appspot.com",
    messagingSenderId: "963097010463",
    appId: "1:963097010463:web:fb37a98e0a909bc1e0102a"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
</script>
Are you using NPM and a bundler like webpack or Rollup? Take a look at the modular SDK .

Learn more about Firebase for web: Get started, Web SDK API Reference, Samples