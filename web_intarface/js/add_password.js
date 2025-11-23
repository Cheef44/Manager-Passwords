window.addEventListener('pywebviewready', function () {
    console.log("pywebview готов");
});

async function openModal() {
    document.getElementById("modal-window").style.display = "block";
};

async function closeModal() {
    document.getElementById("modal-window").style.display = "none";
};

async function save_password() {
    var name_record = String(document.getElementById("modal-window__input-name-record").value);
    var site_name = String(document.getElementById("modal-window__input-site-link").value);
    var site_login = String(document.getElementById("modal-window__input-login").value);
    var site_email = String(document.getElementById("modal-window__input-email").value);
    var site_password = String(document.getElementById("modal-window__input-password").value);
    await window.pywebview.api.add_password_api(name_record, site_name, site_login, site_email, site_password);
    await closeModal();
    location.reload();
};

document.getElementById("button-menu__add-password").addEventListener("click", openModal);
document.getElementById("modal-window__close").addEventListener("click", closeModal);
document.getElementById("modal-window__button-save-record").addEventListener("click", save_password);