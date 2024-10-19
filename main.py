from fileinput import filename
from PyQt5.QtWidgets import *
import os
app = QApplication([])

window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(700,400)

btn_dir = QPushButton("Папка")
list_files = QListWidget()

lbl_image = QLabel("Картинка")
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Відзеркалення")
btn_sharp = QPushButton("Різкість")
btn_black = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(list_files)


col2.addWidget(lbl_image,95)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_black)
col2.addLayout(row_tools)

row.addLayout(col1,20)
row.addLayout(col2,80)

window.setLayout(row)

window.show()

workdir = ""

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def filter(files,extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    extensions = [".jpg",".png", ".jpeg", ".gif", ".bmp"]
    chooseWorkDir()
    filenames = filter(os.listdir(workdir), extensions)
    list_files.clear()
    for filename in filenames:
        list_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)


app.exec_()
