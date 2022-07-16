from moviesUI import Ui_mainWindow
from PyQt5 import QtWidgets
from connect import Movies
import sys


class MovieWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MovieWindow,self).__init__()

        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.movies=Movies()

        self.ui.btnTopRated.clicked.connect(self.getMovies)
        self.ui.btnComingSoon.clicked.connect(self.getMovies)
        self.ui.btnNowPlaying.clicked.connect(self.getMovies)
        self.ui.btnSearch.clicked.connect(self.getMovies)
        
        self.ui.tableMovies.setRowCount(20)
        self.ui.tableMovies.setColumnCount(3)
        self.ui.tableMovies.setHorizontalHeaderLabels(["Title","Date","Rate"])
        
        self.ui.tableMovies.setColumnWidth(0,300) # sadece movie name iin ayarladık 

    def getMovies(self):
        buttonName=self.sender().text()
        keyword=self.ui.txtSearch.text()

        if buttonName=="Search":
            if keyword is not None:
                result=self.movies.searchMovieByName(keyword)
                # result["total_results"] # toplam gelen kayıt sayısını verir
                # self.ui.tableMovies.setRowCount(result["total_results"]) # satır sayısını belirttik
             
        elif buttonName=="Top Rated":
            result=self.movies.topRatedMovies()
        elif buttonName=="Popular":
            result=self.movies.upComingMovies()
        elif buttonName=="Now Playing":
            result=self.movies.nowPlayingMovies()

        rowIndex=0 
        for movie in result['results']:
            self.ui.tableMovies.setItem(rowIndex,0,QtWidgets.QTableWidgetItem(movie["title"]))
            self.ui.tableMovies.setItem(rowIndex,1,QtWidgets.QTableWidgetItem(movie["release_date"]))
            self.ui.tableMovies.setItem(rowIndex,2,QtWidgets.QTableWidgetItem(str(movie["vote_average"])))
            rowIndex +=1
        



def movieApp():
    mApp=QtWidgets.QApplication(sys.argv)
    win=MovieWindow()
    win.show()
    sys.exit(mApp.exec_())
    

movieApp()