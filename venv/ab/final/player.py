class Player(object):
    def __init__(self,client_socket, name):
        self.client_socket = client_socket
        self.name = name