"""
    Test UDP server. Assigment for U1 A1: Socket UDP.

    Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)

    usage: python server.py
"""

# Standar imports
import logging
import socketserver
import uuid

logging.basicConfig(level='INFO')
LOGGER = logging.getLogger(__name__)

class RequestHandler(socketserver.BaseRequestHandler):
    """
    Request handler class.
    """
    SRV_RESP = "Hello from the other side, {c_uuid}."
    ENCODING = 'UTF-8'
    CLIENTS = {}

    def handle(self):
        """Handle client requests."""
        data = self.request[0].decode(self.ENCODING).strip()
        socket = self.request[1]

        # Creating a uuid for each client, this is just to review the class assigment (U1 A1: Socket UDP).
        c_uuid = self.CLIENTS.setdefault(self.client_address, str(uuid.uuid4()))

        # UDP Server class internally calls recvfrom method to read incoming data and client details.
        LOGGER.info("%s says: %s", c_uuid, data)

        # Send data on socket.
        # a socket serves as an endpoint for sending and receiving data across the network.
        # At this point the client message was already logged.
        LOGGER.info("%s Sending response.", c_uuid)
        resp = self.SRV_RESP.format(c_uuid=c_uuid).encode(self.ENCODING)
        socket.sendto(resp, self.client_address)

if __name__ == "__main__":
    """Control process workflow."""
    LOGGER.info('Starting UDPServer...')

    HOST, PORT = "127.0.0.1", 20001

    LOGGER.info('Listening on port %d', PORT)
    server = socketserver.UDPServer((HOST, PORT), RequestHandler)

    # Start UDP Server
    server.serve_forever()
