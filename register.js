document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('register-form');

    registerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = registerForm['email'].value;
        const password = registerForm['password'].value;
        const phone = registerForm['phone'].value;

        // Check if phone number is valid (you can add more validation if needed)
        if (!isValidPhoneNumber(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }

        firebase.auth().createUserWithEmailAndPassword(email, password)
            .then((userCredential) => {
                // Registration successful, redirect or perform other actions
                // For example, redirect to login page
                window.location.href = 'login.html';
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                // Handle errors
                console.error(errorMessage);
            });
    });

    function isValidPhoneNumber(phone) {
        // You can add your phone number validation logic here
        // For simplicity, let's just check if it's not empty
        return phone.trim() !== '';
    }
});
