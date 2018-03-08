#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# Copyright 2017 You Yufeng <649602192@qq.com>
"""
:module: firstapp.myRSA
:synopsis: 用RSA对AES加解密
:author: 649602192@qq.com (You Yufeng)

"""

import rsa
from firstapp.myAES import *

class RSA_ed():

    # def encrypt(self):
    #     '''利用RSA公钥加密
    #
    #     :return: crypto     # 加密后的AES密钥
    #     '''
    #     crypto = rsa.encrypt(self.aessk, self.pubkey)
    #     print("加密后的字符串：", crypto)
    #     crypto = crypto.decode('iso-8859-15')
    #     return crypto

    def decrypt(self, rsa_aes, rsa_private):
        '''利用RSA私钥解密

        :param rsa_aes: 被RSA公钥加密后的AES密钥
        :param rsa_private: RSA私钥
        :return:
        '''
        rsa_a = rsa_aes.encode('iso-8859-15')
        # message = rsa.decrypt(rsa_a, rsa_private).decode()
        message = rsa.decrypt(rsa_a, rsa_private)
        print('刚解密后的：',message)
        # print('encode后的：', message.encode('iso-8859-15'))
        return message


if __name__ == "__main__":
    rsaaa = RSA_ed()
    print("加密前的字符串", rsaaa.aessk)
    print(rsaaa.r_key())