## U1 A1: Socket UDP

### Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)

## Documentación

El código fuente se encuentra dentro de la carpeta [src](src).

Al correr el cliente se entra en un ciclo que espera un texto del usuario para ser enviado al servidor (presione ENTER).

Cliente abre socket y escribe mensajes sin servidor. (sockets no orientados a conexión)
![](images/udp-001.jpg | width=400)

Cliente y servidor corriendo en procesos independientes.
![](images/udp-002.jpg | width=400)

Cliente (.py), servidor y un cliente adicional usando la utileria `ncat` para enviar mensajes al servidor.
![](images/udp-002.jpg | width=400)

### Validación/Uso

Correr server:
    `python src/server.py`

Correr cliente:
    `python src/client.py`


