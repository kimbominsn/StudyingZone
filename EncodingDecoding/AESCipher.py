import base64
from Crypto import Random
# from Cryptodome.Cipher import AES

import struct, hashlib
import os
import Crypto
from Crypto.Cipher import AES
import string, random

BS=16 #문장 최소값
pad= lambda s:s+(BS- len(s.encode('utf-8'))%BS)*chr(BS-len(s.encode('utf-8'))%BS)
unpad= lambda s:s[:-ord(s[len(s)-1:])]

class Cipher:
    def __init__(self, key):
        self.key=key

    def encrypt(self, raw):
        raw=pad(raw)
        cipher=AES.new(self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        enc=base64.b64decode(enc)
        cipher=AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf-8')

    def get_random_iv(self):
        string_pool=string.ascii_letters + string.digits + string.punctuation

        result=""
        for i in range(AES.block_size):
            result+=random.choice(string_pool)
        
        return result.encode()

    def encrypt_file(self, in_filename, out_filename=None, chunksize=65536):

        if not out_filename:
            out_filename = in_filename + '.enc'
        # iv = b'initialvector123'

        iv=self.get_random_iv()
        
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outfile.write(encryptor.encrypt(chunk))


    def decrypt_file(self, in_filename, out_filename, chunksize=24 * 1024):
        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(origsize)
