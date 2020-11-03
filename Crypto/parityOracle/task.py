import socketserver
import os
import sys
import signal
import string
import random
from hashlib import sha256
from Crypto.Util.number import *

from secret import flag

BANNER = br'''
   ___        _____                                         
  / _ \      / ____|                                        
 | | | |_  _| |  __  __ _ _ __ ___   ___                    
 | | | \ \/ / | |_ |/ _` | '_ ` _ \ / _ \                   
 | |_| |>  <| |__| | (_| | | | | | |  __/                   
  \___//_/\_\\_____|\__,_|_| |_|_|_|\___|            _      
                  (_) |        / __ \               | |     
  _ __   __ _ _ __ _| |_ _   _| |  | |_ __ __ _  ___| | ___ 
 | '_ \ / _` | '__| | __| | | | |  | | '__/ _` |/ __| |/ _ \
 | |_) | (_| | |  | | |_| |_| | |__| | | | (_| | (__| |  __/
 | .__/ \__,_|_|  |_|\__|\__, |\____/|_|  \__,_|\___|_|\___|
 | |                      __/ |                             
 |_|                     |___/                              

'''

MENU = br'''
1. decrypt
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

    def recvhex(self, prompt=b'> '):
        self.send(prompt, newline=False)
        try:
            data = int(self._recvall().decode('latin-1'), 16)
        except:
            self.send(b"Wrong hex value!")
            self.request.close()
            return None
        return data

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
        assert len(flag)==44 and flag.startswith("0xGame{") and flag.endswith("}")
        e = 65537
        m = bytes_to_long(flag.encode())
        p, q = getPrime(1024), getPrime(1024)
        while p*q%4-3:
            p, q = getPrime(1024), getPrime(1024)
        c = pow(m,e,p*q)
        self.n = p*q
        self.d = inverse(e, (p-1)*(q-1))
        self.send(f"e = {e}\nn = {self.n}\nc = {c}".encode())

        while True:
            self.send(MENU, newline=False)
            choice = self.recv()

            if choice == b"1":
                cip = self.recvhex(prompt=b"Your cipher (in hex): ")
                if not cip:
                    break
                result = pow(cip, self.d, self.n) % 4
                self.send(hex(result)[2:].encode())
                continue

            self.request.close()
            break


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
