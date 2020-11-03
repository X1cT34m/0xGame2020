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
  \___//_/\_\\_____|\__,_|_| |_| |_|\___|____                 _      
                 | |   | (_)            / __ \               | |     
  _ __   __ _  __| | __| |_ _ __   __ _| |  | |_ __ __ _  ___| | ___ 
 | '_ \ / _` |/ _` |/ _` | | '_ \ / _` | |  | | '__/ _` |/ __| |/ _ \
 | |_) | (_| | (_| | (_| | | | | | (_| | |__| | | | (_| | (__| |  __/
 | .__/ \__,_|\__,_|\__,_|_|_| |_|\__, |\____/|_|  \__,_|\___|_|\___|
 | |                               __/ |                             
 |_|                              |___/                              
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
            data = bytes(bytearray.fromhex(self._recvall().decode('latin-1')))
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
        self.send(BANNER)
        if not self.proof_of_work():
            return

        def padding(s): return s + (16 - len(s) % 16) * \
            long_to_bytes(16 - len(s) % 16)

        m = padding(flag.encode())

        self.key = os.urandom(16)
        iv = os.urandom(16)
        aes = AES.new(self.key, AES.MODE_CBC, IV=iv)
        crypttext = aes.encrypt(m)
        self.send(b"iv : "+iv.hex().encode())
        self.send(b"crypttext : "+crypttext.hex().encode())
        while True:
            self.send(MENU, newline=False)
            choice = self.recv()

            if choice == b"1":
                iv = self.recvhex(prompt=b"Your IV (in hex): ")
                cip = self.recvhex(prompt=b"Your cipher (in hex): ")
                if (not cip) or (not iv) or len(cip) % 16 or (len(iv)-16):
                    break
                temp = AES.new(self.key, AES.MODE_CBC, IV=iv)
                plaintext = temp.decrypt(cip)
                pad = plaintext[-1]
                if pad > 16:
                    self.send(b"pad error")
                    continue
                expected = [pad] * pad
                piece = list(plaintext[-pad:])
                if piece != expected:
                    self.send(b"wrong padding")
                    continue
                self.send(b"success")
                continue

            self.request.close()
            break


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10003
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
