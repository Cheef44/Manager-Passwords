var table = document.getElementById('table-password__body');

window.addEventListener('pywebviewready', async function() {
    
    console.log("PyWebView API ready!");

    try {
        window.pywebview.api.resize_window_api(1000, 800);
        var data = await window.pywebview.api.data_passwords_api();
        console.log("Получены данные от Python:", data);

        if (!Array.isArray(data)) {
            console.error("Ожидался массив, но пришло:", typeof data);
            return;
        }

        table.innerHTML = "";

        for (var i = 0; i < data.length; i++) {
            var row = document.createElement('tr');
            row.id = 'table-password__data';
            var data_item = data[i];

            for (var j = 0; j < data_item.length; j++) {
                var cell = document.createElement('td');
                if (j === 0) {
                    cell.id = 'table-password__id';
                }
                if ((i+1)%2 === 0){
                    row.style.backgroundColor = '#D9D9D9';
                }
                else{
                    row.style.backgroundColor = '#AFAEAE';
                }
                cell.innerText = data_item[j];
                row.appendChild(cell);
            }

            table.appendChild(row);
        }

    } catch (err) {
        console.error("Ошибка при получении данных:", err);
    }
});