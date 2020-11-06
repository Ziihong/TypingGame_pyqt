import window
from random import randint
from PyQt5.QtCore import QBasicTimer, QRect, QPointF
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGraphicsScene


kor = ('문자열', '정수', '리스트', '튜플', '딕셔너리',
       '타입', '출력', '반복문', '변수', '파이썬')
eng = ('input', 'int', 'string', 'type', 'list', 'class',
       'print', 'python', 'tuple', 'for', 'if', 'while',
       'thread', 'random', 'with', '__init__', '__del__', 'QPushButton', 'QLineEdit', 'ros',)


FRAME_PER_MS = 16

class CWord:

    def __init__(self, pt, word):
        self.pt = pt
        self.word = word


class Word(QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)
        #self.rect = parent.rect()
        self.timer = QBasicTimer()
        self.timer.start(FRAME_PER_MS, self)
        self.words = []
        self.IsEscape = False





    def gameStart(self, lang, level):
        self.lang = lang
        self.level = level
        self.createWord()



    def createWord(self):
        i=0
        while(i<20):
            if self.lang == 0:  # 한국어 선택
                n = randint(0,len(kor)-1)
                str = kor[n]
            elif self.lang == 1: #영어 선택
                n = randint(0,len(eng)-1)
                str = eng[n]

            x = randint(0, 200)
            y = 0
            w = CWord(QPointF(x,y), str)
            self.words.append(w)
            print(self.words[0])
            i+=1


    def drawWord(self, qp):
        qp.setFont(QFont('맑은 고딕', 12))
        for w in self.words:
            qp.drawText(w.pt, w.word)


    #def downWord(self):




    #def timerEvent(self, event):
     #   self.downWord()

