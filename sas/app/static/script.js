document.addEventListener("DOMContentLoaded", function () {
    // Wait for the car to reach the center
    setTimeout(() => {
        let waste = document.getElementById("waste");

        if (!waste) {
            console.error("Waste element not found!");
            return;
        }
        waste.style.opacity = "1"; // Make waste visible
        waste.style.left = "52%"; // Position near the car

        // Start the waste falling animation
        waste.style.animation = "fall 2s ease-in forwards";

        // Open homepage when waste reaches the bottom
        setTimeout(() => {
            console.log("Redirecting to homepage...");
            const homepageUrl = document.getElementById("waste").getAttribute("data-homepage-url");
            window.location.href = homepageUrl; // Redirect to the homepage URL
        }, 2000);
    }, 3000); // Waste appears after car movement (3s)
});