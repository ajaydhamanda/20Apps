import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 500)

        # add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 600, 320)
        self.chat_area.setReadOnly(True)


        #add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 600,  40)


        #burtton

        self.button=QPushButton("Send", self)
        self.button.setGeometry(620, 340, 100, 40)
        self.show()
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
