// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.2/firebase-app.js";
import { getAuth, onAuthStateChanged, signInWithEmailAndPassword, signOut } from "https://www.gstatic.com/firebasejs/9.1.2/firebase-auth.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyACKLkhphco7AcrxbdhcE12K6Fsz1StmFw",
    authDomain: "cyberpulse-project.firebaseapp.com",
    projectId: "cyberpulse-project",
    storageBucket: "cyberpulse-project.appspot.com",
    messagingSenderId: "1019060348990",
    appId: "1:1019060348990:web:1274ad1163098a44a2496f"
  };
  
  

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Example: Firebase Auth listener
onAuthStateChanged(auth, (user) => {
  if (user) {
    // User is signed in
    console.log("User signed in:", user);
  } else {
    // User is signed out
    console.log("User signed out");
  }
});