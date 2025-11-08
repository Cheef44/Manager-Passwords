//Функция регистрации

async function registration() {
    var user_name = String(document.getElementById("user-input__user-name").value);
    var password_1 = String(document.getElementById("user-input__password1").value);
    var password_2 = String(document.getElementById("user-input__password2").value);
    if (password_1 === password_2) {
        var ckeck_registration = await window.pywebview.api.registration_api(user_name, password_1);
        
        if (ckeck_registration === true){
            await window.pywebview.api.open_html_inteface_api("web_intarface/index.html");
        }
    }
}

//Функция входа
async function log_in() {
    var user_name = String(document.getElementById("user-input__user-name").value);
    var password_1 = String(document.getElementById("user-input__password1").value);
    var password_2 = String(document.getElementById("user-input__password2").value);
    if (password_1 === password_2) {
        var ckeck_registration = await window.pywebview.api.log_in_api(user_name, password_1);
        
        if (ckeck_registration === true){
            await window.pywebview.api.open_html_inteface_api("web_intarface/main_window.html");
        }
    }
}

document.getElementById("user-button__registration").addEventListener("click", registration);
document.getElementById("user-button__log-in").addEventListener("click", log_in)
