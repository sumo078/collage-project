
document.getElementById('appointmentDate').addEventListener('input', function() {
    const selectedDate = new Date(this.value);
    const today = new Date();
    
    if (selectedDate < today.setHours(0, 0, 0, 0)) {
        alert("Please select a future date.");
        this.value = '';
    }
});

// Dynamic time slot update based on selected service
document.getElementById('services').addEventListener('change', function() {
    const service = this.value;
    const timeSlotSelect = document.getElementById('timeSlot');

    // Clear previous time options
    timeSlotSelect.innerHTML = '<option value="">Select Time</option>';

    let timeSlots = [];

    if (service === 'consultation') {
        timeSlots = ['9:00 AM', '10:30 AM', '2:00 PM'];
    } else if (service === 'design_plan') {
        timeSlots = ['11:00 AM', '1:30 PM', '3:00 PM'];
    } else if (service === 'full_service') {
        timeSlots = ['9:30 AM', '12:00 PM', '3:30 PM'];
    }

    // Populate time slot options
    timeSlots.forEach(function(time) {
        const option = document.createElement('option');
        option.value = time;
        option.textContent = time;
        timeSlotSelect.appendChild(option);
    });
});
// Function to handle time slots based on selected service
document.getElementById("services").addEventListener("change", function() {
    const timeSlotSelect = document.getElementById("timeSlot");
    const selectedService = this.value;
    let options = [];

    if (selectedService === "consultation") {
        options = ["9:00 AM", "11:00 AM", "2:00 PM"];
    } else if (selectedService === "design_plan") {
        options = ["10:00 AM", "1:00 PM", "3:00 PM"];
    } else if (selectedService === "full_service") {
        options = ["8:00 AM", "12:00 PM", "4:00 PM"];
    }
    else if (selectedService === "sofa_design") {
        options = ["8:00 AM", "12:00 PM", "4:00 PM"];
    }
    else if (selectedService === "table_design") {
        options = ["8:00 AM", "12:00 PM", "4:00 PM"];
    }
    else if (selectedService === "full_kitchen") {
        options = ["8:00 AM", "12:00 PM", "4:00 PM"];
    }
    else if (selectedService === "full_service") {
        options = ["8:00 AM", "12:00 PM", "4:00 PM"];
    }


    // Clear existing time slots and add new options
    timeSlotSelect.innerHTML = "<option value=''>Select Time</option>";
    options.forEach(function(time) {
        const option = document.createElement("option");
        option.value = time;
        option.textContent = time;
        timeSlotSelect.appendChild(option);
    });
});


    if (!name || !email || !phone || !appointmentDate || !services || !timeSlot) {
        alert("Please fill in all the fields.");
        return;
    }


