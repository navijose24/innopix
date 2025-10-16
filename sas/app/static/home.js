document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById('player');
    if (video) {
        console.log("Video element found:", video);

        // Check if video has a direct src or uses a <source> tag
        if (video.src) {
            console.log("Video source (direct):", video.src);
        } else {
            const source = video.querySelector('source');
            if (source) {
                console.log("Video source (from <source> tag):", source.src);
            } else {
                console.log("No video source found.");
            }
        }
    } else {
        console.log("No video element found.");
    }
});