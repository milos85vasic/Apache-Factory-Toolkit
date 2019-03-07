import socket, errno


def is_port_available(port_number):
    success = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port_number))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            success = False
            print("Port is already in use")
        else:
            print(e)
    s.close()
    return success
