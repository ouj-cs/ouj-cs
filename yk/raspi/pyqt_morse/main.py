import sys
import thread
import time
import PyQt4.QtCore as C
import PyQt4.QtGui as G
import RPi.GPIO as GPIO
import morse
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
index=0
text="TEXT"
wait=0
working=False
def thread_py(code):
    global working
    working=True
    for length,boolean in code:
        if boolean:
            GPIO.output(21,GPIO.HIGH)
        else:
            GPIO.output(21,GPIO.LOW)
        time.sleep(length)
    working=False
def thread_qt(edit):
    global index,wait
    if working:
        return
    if wait<0:
        wait+=1;
        return
    s=text[:index]+"<b>"+text[index]+"</b>"+text[index+1:]
    edit.is_updating=True
    edit.setText(s)
    edit.is_updating=False
    code=morse.encode(text[index])
    code+=[(0.6,False)]
    thread.start_new_thread(thread_py,(code,))
    index=(index+1)%len(text)
class Edit(G.QTextEdit):
    def __init__(self,parent):
        global text
        super(Edit,self).__init__(parent)
        self.is_updating=False
        self.setPlainText("The quick brown fox jumps over the lazy dog.")
        self.setPlainText("sos")
        self.textChanged.connect(self._textChanged)
        self.setFocus()
        text=str(self.toPlainText())
        self.timer=C.QTimer()
        self.timer.timeout.connect(self._timeout)
        self.timer.start(200)
    def _textChanged(self):
        global index,text,wait
        if self.is_updating:
            return
        text=str(self.toPlainText())
        index=0
        wait=-10
    def _timeout(self):
        thread_qt(self)
class ExitButton(G.QPushButton):
    def __init__(self,parent):
        super(ExitButton,self).__init__("Exit",parent)
        self.clicked.connect(self._f)
    def _f(self):
        GPIO.cleanup()
        C.QCoreApplication.quit()
class BigWidget(G.QWidget):
    def __init__(self,parent):
        super(BigWidget,self).__init__(parent)
        vbox=G.QVBoxLayout(self)
        b=ExitButton(self)
        e=Edit(self)
        vbox.addWidget(b)
        vbox.addWidget(e)
        self.setLayout(vbox)
class Window(G.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.resize(480,320)
        self.move(0,0)
        self.setWindowTitle("title")
        self.setCentralWidget(BigWidget(self))
        self.showFullScreen()
        self.show()
    def keyPressEvent(self,e):
        if e.key()==C.Qt.Key_Escape:
            GPIO.cleanup()
            C.QCoreApplication.quit()
class App(G.QApplication):
    def __init__(self):
        super(App,self).__init__(sys.argv)
        w=Window()
        sys.exit(self.exec_())
if __name__ == "__main__":
    app=App()
