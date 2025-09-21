from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
import json

#Подготовка ключей к шифрованию
class PreparationEncryption:
    def __init__(self) -> None:
        with open("config\config.json") as config_file:
            self.config_file = json.load(config_file)
            
        self.sync_key_path = self.config_file["path"]["encryption_keys_path"]["sync_key_path"]
        self.async_public_key_path = self.config_file["path"]["encryption_keys_path"]["async_keys_path"]["public_key_path"]
        self.async_private_key_path = self.config_file["path"]["encryption_keys_path"]["async_keys_path"]["private_key_path"]
        self.vectore_path = self.config_file["path"]["encryption_keys_path"]["vectore_path"]
        
    #Метод получения вектора
    def vectore(self):
        try:
            with open(self.vectore_path, 'rb') as iv:
                iv = iv.read()
            return iv
        except FileNotFoundError:
            return 'Encryption keys were not found'
        
    #Метод расшифровки синхронного ключа
    def decrypt_sync_key(self):
        try:
            with open(self.async_private_key_path, 'rb') as private_key:
                private_key = private_key.read()
                private_key = RSA.import_key(private_key)
                
            with open(self.sync_key_path, 'rb') as sync_key:
                sync_key = sync_key.read()
                
            decrypt = PKCS1_OAEP.new(private_key)
            decrypt = decrypt.decrypt(sync_key)
            
            return decrypt
        except FileNotFoundError:
            return 'Encryption keys were not found'
        
#Класс для шифрования текста
class EncryptionText(PreparationEncryption):
    def __init__(self, data:str):
        super().__init__()
        self.data = data
    #Метод шифрования текста
    def encryption_text(self):
        encrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
        encrypt_text = encrypt.encrypt(bytes(self.data, encoding='utf8'))
        return encrypt_text