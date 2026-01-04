from scripts.main import LogInApp
from PySide6.QtWidgets import QApplication
import sys
from src import api

def on_exit():
    api.API.del_password_api(None,name_service="PASSWORD_LOG_IN")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogInApp()
    window.show()
    app.aboutToQuit.connect(on_exit)
    sys.exit(app.exec())
    print(api.API.get_password_cache_api(None, "PASSWORD_LOG_IN"))