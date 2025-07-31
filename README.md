# UDP Test Scripts

A simple for fun Python project to explore and understand UDP communication using a client and server.

# Setup
0. git clone https://github.com/rynBenAmor/udp-server-test.git
1. python -m venv venv
2. venv/scripts/activate
3. pip install -r requirements.txt

## How to Run

1. Start the server:
    ```
    python udp_server.py
    ```
2. Start the client (in a separate terminal):
    ```
    python udp_client.py
    ```

## Client Commands

- `/help`  Show available commands
- `/all`  Switch to broadcast mode (send to all on the network)
- `/server` Switch to direct mode (send only to the server)
- `/exit`  Exit the client

## Features

- Colored terminal output (using `colorama`)
- Switch between broadcast and direct messaging like that of League of legends
- Timestamped messages and replies
