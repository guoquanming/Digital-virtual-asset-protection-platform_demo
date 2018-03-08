import os, pymysql, django, time
from django.shortcuts import render
from django.http import HttpResponse

from firstapp.models import Metadata, TestLittlerecord
from firstapp.myAES import *
from firstapp.myRSA import *
from os import path
import time, json, rsa
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django1.settings")
django.setup()



def ownership(request):
    """
    复制文件并对其加密
    :param request:
    :return:
    """
    root = "C:\inetpub\wwwroot\datasets\\"
    name = "tx"
    ext = ".txt"
    file_path = root + name + ext

    # 复制文件
    cp = COPY_DATA()
    cpfilename = cp.copy_data(root, name, ext, file_path)

    # 加密文件
    aes = AES_ed()
    print(aes._encrypt(root + cpfilename))

    # 声明复制文件的变量
    cpfile_path = root + cpfilename

    # 注册
    # get_file = GetFileDetail()
    # rsa = RSA_ed()

    # Metadata(
    #     daid=get_file.get_data_identification(cpfile_path),
    #     title=get_file.get_name(cpfile_path),
    #     type=get_file.get_ext(cpfile_path),
    #     creationtime=get_file.get_cdate(cpfile_path),
    #     modificationtime=get_file.get_mdate(cpfile_path),
    #     registrationtime=get_file.get_date(),
    #     # URL形式：( 194.168.1.186\datasets\zh.mp4 )
    #     url=str(get_file.get_ip()) + '\\' + get_file.get_root(cpfile_path)[19:],
    #     localurl=get_file.get_root(cpfile_path),
    #     aessk= aes.r_key_iv()[0],
    #     aesiv = aes.r_key_iv()[1],
    #     # RSA公钥
    #     publickey = rsa.r_key()[0],
    #     # RSA私钥
    #     rsapk = rsa.r_key()[1],
    #     # RSA(AES)
    #     rsa_aes_field = str(rsa.encrypt())
    # ).save()

    return HttpResponse('加密文件成功')

def test_decode(request):
    aes = AES_ed()
    rsaaa = RSA_ed()

    a = Metadata.objects.get(daid='8b994e78fcd311b9d7e2a9762d48cc3df0e856d95e4c4ab668d4736fc97c2706')
    localurl = a.localurl
    publickey = a.publickey
    rsapk = rsa.PrivateKey.load_pkcs1(a.rsapk.encode())
    aessk = a.aessk
    aesiv = a.aesiv
    rsa_aes = a.rsa_aes_field

    # # 解密AES密钥
    # rsaaa.decrypt(rsa_aes, rsapk)
    # 解密文件
    print(aes._decrypt(localurl, aessk, aesiv))

    return HttpResponse("解密文件成功")

