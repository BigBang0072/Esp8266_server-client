import socket as Socket

esp_ip_address='192.168.4.1'
esp_server_port=8080 #for default http connection

esp_socket=Socket.socket(Socket.AF_INET,Socket.Sock_STREAM)
esp_socket.connect((esp_ip_address,esp_server_port))

while True:
    data=esp_socket.recv(512)
    print "data"
    
esp_socket.close()