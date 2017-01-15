import socket as Socket

esp_ip_address=''
esp_server_port=80 #for default http connection

esp_socket=Socket.socket(Socket.AF_INET,Socket.Sock_STREAM)
esp_socket.connect((esp_ip_address,esp_server_port))
while True:
    