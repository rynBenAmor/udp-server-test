import socket


SERVER_ADD = ('127.0.0.1', 5321)
SERVER_SHARED_ADD = ('255.255.255.255', 5321)
ALL_CHAT = True # Toggle message scope
CHAT_TAG = '[all]:' if ALL_CHAT else '[server]:' # * a string indication like that of LOL


def client_socket_setup():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print("UDP Client started.")
    print("Type 'exit' to quit.")
    return sock


def main():
    sock = client_socket_setup()
    sock.settimeout(1.0)
    print("Tip : ('/all' for broadcast, '/server' for direct, 'exit' to quit): ")
    global ALL_CHAT
    try:
        while True:
            try:
                message = input(f"{CHAT_TAG} Write a message ")
                if message.lower() == "exit":
                    break
                elif message.lower() == "/all":
                    ALL_CHAT = True
                    print("Switched to ALL_CHAT mode (broadcast).")
                    continue
                elif message.lower() == "/server":
                    ALL_CHAT = False
                    print("Switched to SERVER mode (direct).")
                    continue
                target = SERVER_SHARED_ADD if ALL_CHAT else SERVER_ADD
                sock.sendto(message.encode(), target)
                print(f"Message sent to {'ALL' if ALL_CHAT else 'SERVER'}!")
            except socket.timeout:
                continue
    except KeyboardInterrupt:
        print("\n[INTERRUPTED] disconnecting from server.")
    finally:
        sock.close()


if __name__ == "__main__":
    main()