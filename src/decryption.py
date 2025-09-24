from src import encryption
from Crypto.Cipher import AES
import chardet

#Класс для дешифровки данных
class Decryption(encryption.EncryptionText):
    def __init__(self, data:str):
        super().__init__(data)
    
    #Функция для дешифровки данных 
    def decryption(self):
        try:
            decrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
            enc_file = self.data
            decrypt_data = decrypt.decrypt(enc_file)
            decrypt_data = decrypt_data.decode(chardet.detect(decrypt_data)['encoding'])
            return decrypt_data
        except ValueError:
            return 'Encryption keys were not found'