document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navList = document.getElementById("nav-list");
  const dropdown = document.getElementById("modules-dropdown");
  const dropBtn = dropdown.querySelector(".dropbtn");

  /* ===== MENU MOBILE ===== */
  menuToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    navList.classList.toggle("active");
  });

  /* ===== DROPDOWN MODULES (CLICK ONLY) ===== */
  dropBtn.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    dropdown.classList.toggle("active");
  });

  /* ===== CERRAR CLICK FUERA ===== */
  document.addEventListener("click", (e) => {
    if (!navList.contains(e.target)) {
      navList.classList.remove("active");
      dropdown.classList.remove("active");
    }
  });

  /* ===== CERRAR AL CLICK EN UN MÓDULO ===== */
  dropdown.querySelectorAll(".dropdown-content a").forEach(link => {
    link.addEventListener("click", () => {
      navList.classList.remove("active");
      dropdown.classList.remove("active");
    });
  });
});
