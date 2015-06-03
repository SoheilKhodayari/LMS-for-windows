__author__ = 'soheil'
import sys
import os
import utils


from PyQt4 import QtGui,QtCore
class WIDGET(QtGui.QWidget):

    def __init__(self,layout):
        super(WIDGET, self).__init__()
        self.layout=layout
        self.initUI()
    def initUI(self):
        self.setLayout(self.layout)
        self.show()




class SlideShowPics(QtGui.QWidget):

    """ SlideShowPics class defines the methods for UI and
        working logic
    """
    def __init__(self, imgLst, parent=None):
        super(SlideShowPics, self).__init__(parent)
        # self._path = path
        self._imageCache = []
        self._imagesInList = imgLst
        self._pause = False
        self._count = 0
        self.animFlag = True
        self.updateTimer = QtCore.QTimer()
        self.connect(self.updateTimer, QtCore.SIGNAL("timeout()"), self.nextImage)
        self.prepairWindow()
        self.nextImage()

    def prepairWindow(self):
        # Centre UI
        screen = QtGui.QDesktopWidget().screenGeometry(self)
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        self.setStyleSheet("QWidget{background-color: #000000;}")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.buildUi()
        self.showFullScreen()
        self.playPause()

    def buildUi(self):
        self.label = QtGui.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.setCentralWidget(self.label)
        Hbox=QtGui.QHBoxLayout()
        Hbox.addWidget(self.label)
        self.setLayout(Hbox)

    def nextImage(self):
        """ switch to next image or previous image
        """
        if self._imagesInList:
            if self._count == len(self._imagesInList):
                self._count = 0

            self.showImageByPath(
                    self._imagesInList[self._count])

            if self.animFlag:
                self._count += 1
            else:
                self._count -= 1


    def showImageByPath(self, path):
        if path:
            image = QtGui.QImage(path)
            pp = QtGui.QPixmap.fromImage(image)
            self.label.setPixmap(pp.scaled(
                    self.label.size(),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation))

    def playPause(self):
        if not self._pause:
            self._pause = True
            self.updateTimer.start(2500)
            return self._pause
        else:
            self._pause = False
            self.updateTimer.stop()

    def keyPressEvent(self, keyevent):
        """ Capture key to exit, next image, previous image,
            on Escape , Key Right and key left respectively.
        """
        event = keyevent.key()
        if event == QtCore.Qt.Key_Escape:
            self.close()
        if event == QtCore.Qt.Key_Left:
            self.animFlag = False
            self.nextImage()
        if event == QtCore.Qt.Key_Right:
            self.animFlag = True
            self.nextImage()
        if event == 32:
            self._pause = self.playPause()

# def main(paths):
#     if isinstance(paths, list):
#         imgLst = utils.imageFilePaths(paths)
#     elif isinstance(paths, str):
#         imgLst =  utils.imageFilePaths([paths])
#     else:
#         print " You can either enter a list of paths or single path"
#     app = QtGui.QApplication(sys.argv)
#     if imgLst:
#         window =  SlideShowPics(imgLst)
#         window.show()
#         window.raise_()
#         app.exec_()
#     else:
#         msgBox = QtGui.QMessageBox()
#         msgBox.setText("No Image found in any of the paths below\n\n%s" % paths)
#         msgBox.setStandardButtons(msgBox.Cancel | msgBox.Open);
#         if msgBox.exec_() == msgBox.Open:
#             main(str(QtGui.QFileDialog.getExistingDirectory(None,
#                 "Select Directory to SlideShow",
#                 os.getcwd())))




