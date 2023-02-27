import multiprocessing
import socket
import threading
from usersfinal import *
import hashlib
from player import *

class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.userDb = User()
       self.players = []


   def start(self):
       try:
           print('server starting up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.sock.bind((self.ip, self.port))
           self.sock.listen(3)

           while True:
               print('waiting for a new client')
               clientSocket, client_addresses = self.sock.accept()
               print('new client entered')
               clientSocket.send('Hello this is server'.encode())
               self.count += 1
               print(self.count)
               # implement here your main logic
               self.handleClient(clientSocket, self.count)
       except socket.error as e:
           print(e)

   def handleClient(self, clientSock, current):
       client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
       client_handler.start()

   def handle_client_connection(self, client_socket, current):
       not_crash = True
       print(not_crash)
       while self.running:
           while not_crash:
               try:
                   server_data = client_socket.recv(1024).decode('utf-8')
                   #insert,email,password,firstname
                   arr = server_data.split(",")
                   print(server_data)
                   if arr!=None and arr[0]=="register" and len(arr)==4:
                       print("register user")
                       print(arr)
                       server_data=self.userDb.insert_user(arr[1], arr[2], arr[3])
                       print("server data:",server_data)
                       if server_data:
                           client_socket.send("success register".encode())
                       else:
                           client_socket.send("failed register check if you have @ in gamil".encode())
                   elif arr!=None and arr[0]=="login" and len(arr)==3:
                       print("login user")
                       print(arr)
                       server_data=self.userDb.return_user_by_email_password(arr[1], arr[2])
                       print("server data:",server_data)
                       if server_data:
                           client_socket.send(server_data.encode())
                           message = "welcome: " + str(server_data)
                           client_socket.send(message.encode())
                       elif not server_data:
                           client_socket.send("failed".encode())
                           client_socket.send("failed login".encode())
                   elif arr!=None and arr[0]== "lobby" and len(arr)==2:
                       print("lobby")
                       self.wating_room(client_socket,arr)
                   else:
                       server_data="False"
               except:
                   print("error")
                   not_crash = False
                   break

   def wating_room(self, client_socket, arr):
      player = Player(client_socket, arr[1])
      self.players.append(player)
      if (len(self.players) == 1):
        data = ["player1", "wait"]
        join_data = ",".join(data)
        client_socket.send(join_data.encode())
      elif (len(self.players)==2):
        player1 = self.players[0]
        player2 = self.players[1]
        socket1 = player1.client_socket
        socket2 = player2.client_socket
        data1 = ["player1", "start"]
        data2 = ["player2", "start"]
        str_data1 = ",".join(data1)
        str_data2 = ",".join(data2)
        socket1.send(str_data2.encode())
        socket2.send(str_data1.encode())



   def show_message_box():
      messagebox.showerror("Error", "Failed")




if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1804
   s = Server(ip, port)
   s.start()

