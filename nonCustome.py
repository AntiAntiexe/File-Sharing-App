import httpFunctions
from httpFunctions import startWithIndex
from httpFunctions import startWithFile
import socket
from tkinter import Tk
from tkinter.filedialog import askdirectory


class ShareFile:
    def __init__(self):
        self.file_path = None
        self.server = None
        self.hostname = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.hostname)

    def getDirectory(self):
        path = askdirectory(title='Select Folder (if no folder selected use current directory): ') # shows dialog box and return the path
        print(path)

        self.file_path = path  

    def getPort(self):
        port = input("Enter the port number: ")
        try:
            self.port = int(port)
        except ValueError:
            print("Invalid port number. Using default port 8000.")
            self.port = 8000
        print("Port number is: ", self.port)

    def start(self):
        self.getDirectory()
        self.getPort()

        if self.file_path:
            startWithFile(self.IPAddr, self.port, self.file_path)

ShareFile = ShareFile()
ShareFile.start()

