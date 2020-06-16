# coding=utf-8

from Crypto.Cipher import AES
from Crypto import Random
import binascii

key = '1234567890!@#$%^'   #秘钥，必须是16、24或32字节长度
iv = Random.new().read(16) #随机向量，必须是16字节长度

cipher1 = AES.new(key,AES.MODE_CFB,iv)  #密文生成器,MODE_CFB为加密模式

encrypt_msg =  iv + cipher1.encrypt('我是明文')  #附加上iv值是为了在解密时找到在加密时用到的随机iv
print ('加密后的值为：',binascii.b2a_hex(encrypt_msg))   #将二进制密文转换为16机制显示


cipher2 = AES.new(key,AES.MODE_CFB,iv) #解密时必须重新创建新的密文生成器
decrypt_msg = cipher2.decrypt(encrypt_msg[16:]) #后十六位是真正的密文
print ('解密后的值为：',decrypt_msg.decode('utf-8'))