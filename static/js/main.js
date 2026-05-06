const body = document.getElementById("app-body");
const toggle = document.getElementById("mode-toggle-checkbox");
const modeKey = "pdfFinderMode";

if (localStorage.getItem(modeKey) === "dark") {
    body.classList.add("dark-mode");
    toggle.checked = true;
}

toggle.addEventListener("change", () => {
    if (toggle.checked) {
        body.classList.add("dark-mode");
        localStorage.setItem(modeKey, "dark");
    } else {
        body.classList.remove("dark-mode");
        localStorage.setItem(modeKey, "light");
    }
});

// THE DROP ZONE LOGIC HAS BEEN REMOVED TO PREVENT ERRORS
