from dotenv import load_dotenv
import os
import socket
import logging
from emoji import demojize
import argparse
import time

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="File to write to, if not provided, it will default to a timestamp")
parser.add_argument("-v", "--verbose", help="Show chat output", action="store_true")
parser.add_argument("-c", "--channel", help="Channel to log", required=True)

args = parser.parse_args()

is_verbose = args.verbose
twitch_channel = args.channel
file_name = args.output if args.output else f"{twitch_channel}_{int(time.time())}.log"

server = 'irc.chat.twitch.tv'
port = 6667
nick = os.environ.get('twitch_user')
token = os.environ.get('twitch_token')
irc_channel = f"#{twitch_channel}"

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nick}\n".encode('utf-8'))
sock.send(f"JOIN {irc_channel}\n".encode('utf-8'))

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S',

        handlers=[logging.FileHandler(file_name, encoding='utf-8')])

while True:
    response = sock.recv(2048).decode('utf-8')
    if response.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    elif len(response) > 0:
        cleaned_response = demojize(response)
        logging.info(cleaned_response)
        if is_verbose:
            print(f"{cleaned_response}\n")

