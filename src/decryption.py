from src import encryption
from Crypto.Cipher import AES
import chardet
import hashlib

#Класс для дешифровки данных
class Decryption(encryption.EncryptionText):
    def __init__(self, data:str, password):
        super().__init__(data, password)
        self.password = hashlib.sha3_512(bytes(password, encoding='utf-8')).digest()
    
    #Функция для дешифровки данных 
    def decryption(self):
        try:
            decrypt = AES.new(self.decrypt_sync_key(self.password), AES.MODE_CFB, self.vectore())
            enc_file = self.data
            decrypt_data = decrypt.decrypt(enc_file)
            if decrypt_data != b'':
                decrypt_data = decrypt_data.decode(chardet.detect(decrypt_data)['encoding'])
            else:
                decrypt_data = ''
            return decrypt_data
        except ValueError:
            return 'Encryption keys were not found'