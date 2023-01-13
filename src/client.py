"""
    Test UDP client. Assigment for U1 A1: Socket UDP.

    Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)

    usage: python client.py
"""
# Standar imports
import socket
import logging

REMOTE_IP = "127.0.0.1"
REMOTE_PORT = 20001
BUFFER_SIZE = 1024
ENCODING = 'UTF-8'

logging.basicConfig(level='INFO')
LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    """Control workflow."""
    LOGGER.info('Starting client...')
    LOGGER.info('Please write your message and press ENTER')

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    client_socket.settimeout(1)

    # Stating Loop to keep sending messages.
    while True:
        data = input('> ').encode(ENCODING)
        # Skip empty messages.
        if not data:
            continue

        # Sending data to server.
        client_socket.sendto(data, (REMOTE_IP, REMOTE_PORT))

        # Data delivery is not guaranteed, trying to get a response from server (if any!).
        try:
            # Checking if server replied.
            resp = client_socket.recvfrom(BUFFER_SIZE)
            resp = resp[0].decode(ENCODING)
            LOGGER.info('Servers response: %s', resp)
        except socket.timeout:
            LOGGER.error('Timeout: No response.')
