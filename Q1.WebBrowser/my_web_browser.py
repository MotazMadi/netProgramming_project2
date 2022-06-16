import sys

# importing Widgtes
from PyQt5.QtWidgets import *

# importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *

# importing QtCore to use Qurl
from PyQt5.QtCore import *

# main window class (to create a window)-sub class of QMainWindow class
class Window(QMainWindow):

    # defining constructor function
    def __init__(self):
        # creating connnection with parent class constructor
        super(Window, self).__init__()

        # ---------------------adding browser-------------------
        self.browser = QWebEngineView()

        # setting url for browser, you can use any other url also
        self.browser.setUrl(QUrl("http://google.com"))

        # to display google search engine on our browser
        self.setCentralWidget(self.browser)

        # -------------------full screen mode------------------
        # to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
        self.showMaximized()

        # ----------------------navbar-------------------------
        # creating a navigation bar for the browser
        navbar = QToolBar()
        # adding created navbar
        self.addToolBar(navbar)

        # -----------------prev Button-----------------
        # creating prev button
        prevBtn = QAction("Prev", self)
        # when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        # adding prev button to the navbar
        navbar.addAction(prevBtn)

        # -----------------next Button---------------
        nextBtn = QAction("Next", self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        # -----------refresh Button--------------------
        refreshBtn = QAction("Refresh", self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        # -----------home button----------------------
        homeBtn = QAction("Home", self)
        # when triggered call home method
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        # ---------------------search bar---------------------------------
        # to maintain a single line
        self.searchBar = QLineEdit()
        # when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        # adding created seach bar to navbar
        navbar.addWidget(self.searchBar)

        # if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)

    # method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    # method to load the required url
    def loadUrl(self):
        # fetching entered url from searchBar
        url = self.searchBar.text()
        # loading url
        self.browser.setUrl(QUrl(url))

    # method to update the url
    def updateUrl(self, url):
        # changing the content(text) of searchBar
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)

# setting application name
QApplication.setApplicationName("TechVidvan Web Browser")

# creating window
window = Window()

# executing created app
MyApp.exec_()
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # creating a QWebEngineView
        self.browser = QWebEngineView()

        # setting default browser url as google
        self.browser.setUrl(QUrl("https://www.bing.com/"))

        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding status bar to the main window
        self.setStatusBar(self.status)

        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")

        # adding this tool bar tot he main window
        self.addToolBar(navtb)

        # adding actions to the tool bar
        # creating a action for back
        back_btn = QAction("Back", self)

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        # adding action to the back button
        # making browser go back
        back_btn.triggered.connect(self.browser.back)

        # adding this action to tool bar
        navtb.addAction(back_btn)

        # similarly for forward action
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")

        # adding action to the next button
        # making browser go forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # similarly for home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # adding a separator in the tool bar
        navtb.addSeparator()

        # creating a line edit for the url
        self.urlbar = QLineEdit()

        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding this to the tool bar
        navtb.addWidget(self.urlbar)

        # adding stop action to the tool bar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # adding action to the stop button
        # making browser to stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # showing all the components
        self.show()

    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Geek Browser" % title)

    # method called by the home action
    def navigate_home(self):
        # open the google
        self.browser.setUrl(QUrl("http://www.google.com"))

    # method called by the line edit when return key is pressed
    def navigate_to_url(self):
        # getting url and converting it to QUrl object
        q = QUrl(self.urlbar.text())

        # if url is scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")

        # set the url to the browser
        self.browser.setUrl(q)

    # method for updating url
    # this method is called by the QWebEngineView object
    def update_urlbar(self, q):
        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Chrome Web Browser")

# creating a main window object
window = MainWindow()

# loop
app.exec_()
