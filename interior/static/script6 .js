function getInTouch() {
    alert("Thank you for reaching out! We'll contact you soon.");
}

// Handle account registration form submission
document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert("Registration successful!");
});

// Handle contact form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert("Your message has been sent!");
});
