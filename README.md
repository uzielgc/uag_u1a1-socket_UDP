## U1 A1: Socket UDP

### Author: Eloy Uziel García Cisneros (eloy.garcia@edu.uag.mx)
#### Repo: https://github.com/uzielgc/uag_u1a1-socket_UDP

## Documentación

El código fuente se encuentra dentro de la carpeta [src](src).
La evidencia en imagenes se encuentra en la carpera [images](images).
El código esta comentado en los puntos clave del proceso.

Al correr el cliente se entra en un ciclo que espera un texto del usuario, para enviar al servidor presione ENTER.

Cliente abre socket y escribe mensajes sin servidor. (sockets no orientados a conexión)

![](images/udp-001.jpg)

Cliente y servidor corriendo en procesos independientes.

![](images/udp-002.jpg)

Cliente (.py), servidor y un cliente adicional usando la utilería `ncat` (nc -u <IP> <PUERTO>)
donde -u utiliza UDP en lugar de la opción por default (TCP).

![](images/udp-002.jpg)

### Validación/Uso

Correr server:
    `python src/server.py`

Correr cliente:
    `python src/client.py`


