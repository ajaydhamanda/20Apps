from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QTextEdit, QLineEdit
import sys
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 400)

        #add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        #add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 50)

        #input buttons
        self.button = QPushButton("Send ->", self)
        self.button.setGeometry(500, 340, 100, 50)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())