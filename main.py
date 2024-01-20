from PyQt5.QtWidgets import*

app=QApplication([])
from main_window import*
main_win=QWidgets()
main_win.rasize(600,500)
main_win.setWindowTitle("Memory Card")
main_win.move(300,300)

main_win.setLayot(line)

btn_answer.cliked.connect(swich_screen)

main_win.show()

app.exec()
