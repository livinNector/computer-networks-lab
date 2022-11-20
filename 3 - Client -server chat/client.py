import socket
def client_program():
    print('type bye to terminate')
    host = socket.gethostname() 
    port = 5000 
    client_socket = socket.socket() 
    client_socket.connect((host, port)) 
    
    while True:
        message = input(">") 
        if message.lower().strip() == 'bye':
            break
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode() 
        print('server: ' , data)
    client_socket.close() 

if __name__ == '__main__':
    client_program()
