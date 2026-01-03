document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navList = document.getElementById("nav-list");

  menuToggle.addEventListener("click", () => {
    navList.classList.toggle("active");
    menuToggle.classList.toggle("active");
  });

  // Cerrar menú al hacer click en un link (mobile)
  document.querySelectorAll("#nav-list a").forEach(link => {
    link.addEventListener("click", () => {
      navList.classList.remove("active");
      menuToggle.classList.remove("active");
    });
  });
});
