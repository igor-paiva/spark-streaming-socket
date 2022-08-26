import socket
import time
import sys
from threading import Thread
from datetime import datetime
from essential_generators import DocumentGenerator


def on_client(client_socket, addr):
    gen = DocumentGenerator()

    try:
        while True:
            line = f"{gen.sentence()}\n"
            client_socket.send(line.encode())
            time.sleep(0.5)
    except:
        conn.close()


if __name__ == "__main__":

    s = socket.socket()
    s.bind(("", 9999))
    s.listen(5)

    print("Server listening in localhost:9999...\n")

    while True:
        try:
            conn, addr = s.accept()

            now_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"{now_string} => Got connection from {addr[0]}:{addr[1]}\n")

            t = Thread(target=on_client, args=(conn, addr))
            t.start()

        except KeyboardInterrupt:
            print("\nExiting...")
            s.close()
            exit(0)

        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)
