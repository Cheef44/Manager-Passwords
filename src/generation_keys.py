from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json
import os

#Класс для функция связанных с ключами
class Keys:
    def __init__(self):
        with open("config/config.json") as config_file:
            self.config_file = json.load(config_file)
        self.sync_key_path = self.config_file["path"]["encryption_keys_path"]["sync_key_path"]
        self.async_public_key_path = self.config_file["path"]["encryption_keys_path"]["async_keys_path"]["public_key_path"]
        self.async_private_key_path = self.config_file["path"]["encryption_keys_path"]["async_keys_path"]["private_key_path"]
        self.vectore_path = self.config_file["path"]["encryption_keys_path"]["vectore_path"]
        os.mkdir("data") if not os.path.exists("data") else None
    
    #Метод генерации вектора
    def vectore(self):
        if not os.path.exists(self.vectore_path):
            with open(self.vectore_path, 'wb') as vectore:
                vectore_data = os.urandom(16)
                vectore.write(vectore_data)
    
    #Метод генерации синхронного ключа
    def gen_sync_key(self):
        with open(self.sync_key_path, 'wb') as key:
            key.write(get_random_bytes(32))
    
    #Метод генерации асинхронного ключа
    def gen_async_key(self):
        keys = RSA.generate(1024)
        with open(self.async_public_key_path, 'wb') as key_pub:
            key_pub.write(keys.public_key().export_key())
        with open(self.async_private_key_path, 'wb') as key_private:
            key_private.write(keys.export_key())
    
    #Метод шифрования синхронного ключа с помощью асинхронного шифрования
    def synchronous_key_encryption(self):
        with open(self.sync_key_path, 'rb') as sync_key:
            sync_key = sync_key.read()
        with open(self.async_public_key_path, 'rb') as async_key:
            async_key = RSA.import_key(async_key.read())
        
        encrypt = PKCS1_OAEP.new(async_key)
        encrypt = encrypt.encrypt(sync_key)
        with open(self.sync_key_path, 'wb') as sync_key:
            sync_key.write(encrypt)
            
    #Функция для запуска всех методов      
    def run(self):
        if not os.path.exists(self.sync_key_path):
            self.vectore()
            self.gen_sync_key()
            self.gen_async_key()
            self.synchronous_key_encryption()