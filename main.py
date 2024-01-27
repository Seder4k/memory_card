from PyQt5.QtWidgets import*

app=QApplication([])

from main_window import*
from random import choice, shuffle
class Question():
    def __init__(self, question, answer, w_answer1, w_answer2, w_answer3):
        self.question=question
        self.answer=answer
        self.w_answer1=w_answer1
        self.w_answer2=w_answer2
        self.w_answer3=w_answer3
        self.attempts=0
        self.correct=0
    def got_right(self):
        self.attempts+=1
        self.correct+=1
        print('Це правильна відповіть!')

    def got_wrong(self):
        self.attempts+=1
        print('Відповіть не вірна')
def new_question(question,radio_list):
    random_quesyion=choice(question)
    text_qwestion.setText(random_quesyion.question)
    right_answer.setText(random_quesyion.answer)
    answer=radio_list[0]
    wrong_answer1,wrong_answer2,wrong_answer3=radio_list[1],radio_list[2],radio_list[3]
    answer.setText(random_quesyion.answer)
    wrong_answer1.setText(random_quesyion.w_answer1)
    wrong_answer2.setText(random_quesyion.w_answer2)
    wrong_answer3.setText(random_quesyion.w_answer3)
    return random_quesyion
def switch_screen():
    global random_quesyion
    if btn_answer.text()=="Віповісти":
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Наступне питання")
    else:
        qwestion_group.show()
        answer_group.hide()
        btn_answer.setText("Відповісти")
        random_quesyion=new_question(question,radio_list)

q1=Question("Яблуко","apple","aple","apalke","aplle")
q2=Question("Машина","car","mashuna","karr","mah")
q3=Question("Будинок","house","hose","hom","haus")
question=[q1,q2,q3]
radio_list=[rbtn1,rbtn2,rbtn3,rbtn4]
shuffle(radio_list)
main_win=QWidget()
main_win.resize(600,500)
main_win.setWindowTitle("Memory Card")
main_win.move(300,300)

main_win.setLayout(line)

btn_answer.clicked.connect(switch_screen)

main_win.show()

app.exec()
