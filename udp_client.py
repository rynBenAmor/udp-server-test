# udp_client.py
import socket
from colorama import Fore, Style
import datetime


SERVER_ADD = ('127.0.0.1', 5321)
SERVER_SHARED_ADD = ('255.255.255.255', 5321)
ALL_CHAT = True # Toggle message scope



def client_socket_setup():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print("UDP Client started.")
    print("Type 'exit' to quit.")
    return sock


def main():
    sock = client_socket_setup()
    sock.settimeout(1.0)
    print("Tip: Enter /help for commands list")
    global ALL_CHAT # to make it mutable/reactive inside functions   

    try:
        while True:
            try:
                CHAT_TAG = Fore.GREEN + '[all]:' if ALL_CHAT else Fore.BLUE + '[server]:' # * a string indication like that of LOL
                message = input(f"{CHAT_TAG} Write a message ")
                if message.lower() == "/exit":
                    print(Fore.RED + "Exiting client..." + Style.RESET_ALL)
                    break
                elif message.lower() == "/all":
                    ALL_CHAT = True
                    print(Fore.GREEN + "Switched to ALL_CHAT mode!" + Style.RESET_ALL)
                    continue
                elif message.lower() == "/server":
                    ALL_CHAT = False
                    print(Fore.YELLOW + "Switched to SERVER mode (direct)." + Style.RESET_ALL)
                    continue
                elif message.lower() == "/help":
                    print(Fore.YELLOW + "Commands: /all for broadcast, /server for direct, /help, /exit to quit" + Style.RESET_ALL)

                target = SERVER_SHARED_ADD if ALL_CHAT else SERVER_ADD
                sock.sendto(message.encode(), target)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(Fore.CYAN + f"[{timestamp}] Message sent to {'ALL' if ALL_CHAT else 'SERVER'}!" + Style.RESET_ALL)
                

                try:
                    reply, _ = sock.recvfrom(1024)
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(Fore.MAGENTA + f"[Server Reply - {timestamp}] server received: '{reply.decode()}' " + Style.RESET_ALL)
                except socket.timeout:
                    pass

            except socket.timeout:
                continue

    except KeyboardInterrupt:
        # using crt+C
        print(Fore.RED + "Exiting client..." + Style.RESET_ALL)
    finally:
        sock.close()


if __name__ == "__main__":
    main()