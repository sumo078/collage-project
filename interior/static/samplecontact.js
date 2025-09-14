// Google Map Initialization
function initMap() {
    const location = { lat: 40.7128, lng: -74.0060 };  // Example coordinates (New York City)
    
    // Create map instance
    const map = new google.maps.Map(document.getElementById('googleMap'), {
        zoom: 12,  // Zoom level
        center: location,  // Center of the map
    });

    // Create a marker
    const marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "AR Architect Location"
    });
}

// Form Submission Handling (Optional)
// function handleFormSubmit() {
//     // You can add form validation here if needed
//     // You can also customize how data is sent (e.g., AJAX, API)
//     alert("Thank you for reaching out. You will be redirected to the Thank You page.");
//     return true;  // Allow form submission to proceed (redirect to thankyou.html)
// }
function initMap() {
    const location = { lat: 40.7128, lng: -74.0060 };  // Set your coordinates here

    const map = new google.maps.Map(document.getElementById('googleMap'), {
        zoom: 12,
        center: location
    });

    const marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "AR Architect Location"
    });
}
