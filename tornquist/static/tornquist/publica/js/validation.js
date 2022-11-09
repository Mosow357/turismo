const nombre = document.getElementById("name");
const mail = document.getElementById("email");
const asunto = document.getElementById("affair");
const form = document.getElementById("form");
const alerta = document.getElementById("warnings");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let warnings = "";
  let regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let access = false;
  alerta.innerHTML = "";
  if (nombre.value.length < 5) {
    warnings += `Nombre Completo no es valido <br>`;
    access = true;
  }
  if (!regEmail.test(mail.value)) {
    warnings += `El email no es valido`;
    access = true;
  }
  if (access) {
    alerta.innerHTML = warnings;
  } else {
    alerta.innerHTML = "Enviado";
  }
});