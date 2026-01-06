document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("graphics");
    const data = localStorage.getItem("lastGraph");

    if (data) {
        const img = document.createElement("img");
        img.src = "data:image/png;base64," + data;
        container.appendChild(img);
    } else {
        container.textContent = "⚠️ No graphic available.";
    }
});