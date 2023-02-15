from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QTextEdit, QLineEdit
from PyQt6.QtCore import Qt, QObject
import sys
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(600, 400)

        # chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 50)
        self.input_field.returnPressed.connect(self.send_message)

        # input buttons
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 50)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me:{user_input}")
        self.input_field.clear()

        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot:{response}")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())