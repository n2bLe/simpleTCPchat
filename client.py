import socket 
import threading
# import sys 
# from PyQt6.QtWidgets import * 
# from PyQt6 import uic


# class chatWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUI('chatGUI.ui',self)
#         self.setWindowTitle('ChatApp')



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',5555))


def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'quit':
                client.close()
                break   
            else:
                print(msg)
        
        except:
            print('An error occured')
            client.close()
            break


def write():
    while True:
        msg = input(':')
        client.send(msg.encode('utf-8'))
        

threading.Thread(target=recieve).start()
threading.Thread(target=write).start()


# app = QApplication()
# window = chatWindow()
# window.show()
# sys.exit(app.exec())