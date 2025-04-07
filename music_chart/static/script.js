const songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
];

document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("us_button");
    const input = document.getElementById("user_value");
    const result = document.getElementById("result");

    button.addEventListener("click", () => {
        const query = input.value.trim();

        fetch("/api/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        })
        .then(response => response.json())
        .then(data => {
            if (data.found) {
                result.textContent = `✅ Found: "${data.song}" at position №${data.index}`;
                result.style.color = "#28a745";
            } else {
                result.textContent = "❌ Song not found.";
                result.style.color = "#dc3545";
            }
        })
        .catch(error => {
            result.textContent = "⚠️ Error occurred.";
            result.style.color = "#ffc107";
            console.error(error);
        });
    });
});