document.addEventListener("DOMContentLoaded", () => {
    const scrollBtn = document.getElementById("scrollToTop");

    window.addEventListener("scroll", () => {
        if (window.scrollY > window.innerHeight / 2) {
            scrollBtn.style.display = "flex";
        } else {
            scrollBtn.style.display = "none";
        }
    });

    scrollBtn.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});