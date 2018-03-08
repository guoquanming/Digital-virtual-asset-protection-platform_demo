#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# Copyright 2017 You Yufeng <649602192@qq.com>
"""
:module: firstapp.myAES
:synopsis: 对部门上传的数据进行安全处理
:author: 649602192@qq.com (You Yufeng)

"""
import os, tempfile, time
from cryptokit import AESCrypto

class AES_ed():

    # def _encrypt(self, joinRN):
    #     """加密
    #     对文件进行加密
    #     :param self:
    #     :param joinRN:
    #     :return:
    #     """
    #     maxbuf = 8192
    #     crypto = AESCrypto(self.AES_CBC_KEY, self.AES_CBC_IV)
    #
    #     try:
    #         fileObject = open(joinRN, 'rb')
    #         fileStr = fileObject.read()
    #         fileObject.close()
    #
    #         data_encrypt = crypto.cbc_encrypt(fileStr)
    #
    #         fileObject = open(joinRN, 'wb')
    #         fileObject.write(data_encrypt)
    #         fileObject.close()
    #
    #         return data_encrypt
    #
    #     except:
    #         print('加密时文件被占用，等待1秒再读取')
    #         if fileObject:   fileObject.close()
    #         time.sleep(1)
    #         self._encrypt(joinRN)


    def _decrypt(self, joinRN, aes_key, aes_iv):
        """解密

        :param joinRN:
        :return:
        """
        maxbuf = 8192
        a_key = aes_key.encode('iso-8859-15')
        a_iv = aes_iv.encode('iso-8859-15')
        crypto = AESCrypto(a_key, a_iv)

        try:
            fileObject = open(joinRN, 'rb')
            fileStr = fileObject.read()
            fileObject.close()

            print(fileStr)
            data_decrypt = crypto.cbc_decrypt(fileStr)

            fileObject = open(joinRN, 'wb')
            # fileObject.write(bytes(data_decrypt))
            fileObject.write(bytes(data_decrypt, 'utf-8'))
            fileObject.close()

            return data_decrypt

        except PermissionError:
            print('解密时文件被占用，等待1秒再读取')
            time.sleep(1)
            self._decrypt(joinRN, aes_key, aes_iv)

class COPY_DATA():
    def copy_data(self, root, name, ext, file_path):
        '''拷贝数据
        新文件名由 原文件名+被拷贝时间+后缀名 组成
        :return: filename2      # 被拷贝之后的文件名称
        '''
        open(file_path).close()
        filename2 = name + '.'+ str(time.time()) + ext
        print(file_path, "=>", root + filename2)
        os.system("copy %s %s" % (file_path, root + filename2))
        if os.path.isfile(root + filename2): print("Success")
        print(filename2)
        return filename2

if __name__ == "__main__":
    file_path = "E:\hit\新建文本文档.txt"
    root = "E:\hit\\"
    name = "新建文本文档"
    ext = ".txt"

    aes = AES_ed()
    print(aes._encrypt(file_path))
    time.sleep(2)
    print(aes._decrypt(file_path))

    print(aes.r_key_iv())
    [key, iv] = aes.r_key_iv()
    print(key.encode('iso-8859-15'))

    cp = COPY_DATA()
    cp.copy_data(root, name, ext, file_path)
