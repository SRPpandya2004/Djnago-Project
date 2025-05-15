document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
    if (signupForm) {
        signupForm.addEventListener('submit', (event) => {
            const fullName = document.getElementById('fullName').value;
            const contact = document.getElementById('contact').value;
            const email = document.getElementById('email').value;
            const createPassword = document.getElementById('createPassword').value;
            if (!fullName || !contact || !email || !createPassword) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
});