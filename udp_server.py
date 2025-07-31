# udp_server.py
import socket
from colorama import Fore, Style
import datetime

HOST = '0.0.0.0' # let server decide the ip
PORT = 5321
BUFFER_SIZE = 1024

def server_socket_setup():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(Fore.GREEN + f"[STARTED] UDP server listening on {HOST}:{PORT}", Style.RESET_ALL)
    return sock

def main():
    sock = server_socket_setup()
    sock.settimeout(1.0)  # 1 second timeout to allow for KeyboardInterrupt
    try:
        while True:
            try:
                data, addr = sock.recvfrom(BUFFER_SIZE)
                try:
                    message = data.decode()
                except UnicodeDecodeError:
                    message = repr(data)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Received from {addr}: {message}")

                sock.sendto(message.encode(), addr)# send it back

            except socket.timeout:
                continue  # Allows KeyboardInterrupt to be caught
    except KeyboardInterrupt:
        print(Fore.RED + "\n[INTERRUPTED] Server shutting down.", Style.RESET_ALL)
    finally:
        sock.close()


if __name__ == "__main__":
    main()