# Display the hostname and IP
#gethostname() : The gethostname function retrieves the standard host name for the local computer.
#gethostbyname() : The gethostbyname function retrieves host information corresponding to a host name from a host database.

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
