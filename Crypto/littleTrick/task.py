import socketserver
import os
import sys
import signal
import string
import random
from hashlib import sha256
from Crypto.Util.number import *
from Crypto.Cipher import AES
from secret import flag

BANNER = br'''
   ___        _____                      
  / _ \      / ____|                     
 | | | |_  _| |  __  __ _ _ __ ___   ___ 
 | | | \ \/ / | |_ |/ _` | '_ ` _ \ / _ \
 | |_| |>  <| |__| | (_| | | | | | |  __/
  \___//_/\_\\_____|\__,_|_| |_| |_|\___|
  _ _ _   _   _   _______   _      _     
 | (_) | | | | | |__   __| (_)    | |    
 | |_| |_| |_| | ___| |_ __ _  ___| | __ 
 | | | __| __| |/ _ \ | '__| |/ __| |/ / 
 | | | |_| |_| |  __/ | |  | | (__|   <  
 |_|_|\__|\__|_|\___|_|_|  |_|\___|_|\_\ 
'''

MENU = br'''
1. get-flag
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
        proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'Give me XXXX: ')
        if len(x) != 4 or sha256(x+proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True

    def handle(self):
        self.send(BANNER)
        if not self.proof_of_work():
            return

        assert len(flag) == 44
        p, q = getPrime(1024), getPrime(1024)
        self.m = flag.encode()
        self.n = p*q
        self.e = 65537
        self.d = inverse(self.e,(p-1)*(q-1))

        self.send(b"n : " + hex(self.n)[2:].encode())

        while True:
            self.send(MENU, newline=False)
            choice = self.recv()

            if choice == b"1":
                mask = self.recvhex(prompt=b"Your mask (in hex): ")
                mask = long_to_bytes(pow(mask,self.d,self.n))
                if len(mask) >= 44:
                    break
                gift = self.m[:-len(mask)] + mask
                gift = pow(bytes_to_long(gift),self.e,self.n)
                self.send(hex(gift)[2:].encode())
                continue

            self.request.close()
            break


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10004
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
