# Display the hostname and IP
import socket 

def get_host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("hostname", host_name)
        print("IP",host_ip )
    except:
        print("Unable to get hostname and Ip")
get_host_name_IP()
