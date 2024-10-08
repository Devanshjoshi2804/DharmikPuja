import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, updatePassword, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-analytics.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD4dZtktDO1slgeGBLhpvIn1Qk5B0QI_hE",
    authDomain: "dharmikpuja-8dfda.firebaseapp.com",
    projectId: "dharmikpuja-8dfda",
    storageBucket: "dharmikpuja-8dfda.appspot.com",
    messagingSenderId: "125295911724",
    appId: "1:125295911724:web:121965889fb8595d8a0289",
    measurementId: "G-0HLM504L6Y"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();

const user = auth.currentUser;
if (user !== null) {
  user.providerData.forEach((profile) => {
    console.log("Sign-in provider: " + profile.providerId);
    console.log("  Provider-specific UID: " + profile.uid);
    console.log("  Name: " + profile.displayName);
    console.log("  Email: " + profile.email);
    console.log("  Photo URL: " + profile.photoURL);
  });
}

// Example usage of signInWithEmailAndPassword
const email = "example@example.com";
const password = "password123";
signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in 
    const user = userCredential.user;
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    // Handle errors
  });

// Example usage of updatePassword
const newPassword = "newPassword123";
updatePassword(auth.currentUser, newPassword)
  .then(() => {
    // Update successful.
  })
  .catch((error) => {
    // An error ocurred
    // Handle errors
  });

// Example usage of signInWithPopup for Google Sign-in
const provider = new GoogleAuthProvider();
signInWithPopup(auth, provider)
  .then((result) => {
    // Handle successful sign-in
  })
  .catch((error) => {
    // Handle errors
  });

// Initialize Analytics
const analytics = getAnalytics(app);
