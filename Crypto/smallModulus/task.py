import socketserver
from Crypto.Util.number import *
import os
import signal
import string
import random
from hashlib import sha256
from secret import flag

BANNER = br'''
   ___        _____                      
  / _ \      / ____|                     
 | | | |_  _| |  __  __ _ _ __ ___   ___ 
 | | | \ \/ / | |_ |/ _` | '_ ` _ \ / _ \
 | |_| |>  <| |__| | (_| | | | | | |  __/
  \___//_/\_\\_____|\__,_|_| |_| |_|\___|

'''

MENU = br'''
1. flag
2. exit
'''


class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'> '):
        self.send(prompt, newline=False)
        return self._recvall()

    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join(
            [random.choice(string.ascii_letters+string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'Give me XXXX: ')
        if len(x) != 4 or sha256(x+proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True

    def handle(self):
        signal.alarm(1200)

        self.send(BANNER)
        if not self.proof_of_work():
            return

        m = bytes_to_long(flag)
        assert m.bit_length() < 512

        while True:
            self.send(MENU, newline=False)
            choice = self.recv()
            if choice == b"1":
                module = getPrime(64)
                self.send(("flag mod {} (in hex) : {}".format(
                    hex(module)[2:], hex(m % module)[2:])).encode())
                continue
            self.request.close()
            break


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10000
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
