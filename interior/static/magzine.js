// Example of adding interactivity for image hover effects
document.querySelectorAll('.article img').forEach((image) => {
    image.addEventListener('mouseover', () => {
        image.style.transform = "scale(1.05)";
    });
    image.addEventListener('mouseout', () => {
        image.style.transform = "scale(1)";
    });
});
