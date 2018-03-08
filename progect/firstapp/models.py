# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Metadata(models.Model):
    handleid = models.CharField(db_column='HandleID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daid = models.CharField(db_column='DAID', primary_key=True, max_length=100)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', blank=True, null=True)  # Field name made lowercase.
    modificationtime = models.DateTimeField(db_column='ModificationTime', blank=True, null=True)  # Field name made lowercase.
    registrationtime = models.DateTimeField(db_column='RegistrationTime', blank=True, null=True)  # Field name made lowercase.
    securitylevel = models.CharField(db_column='SecurityLevel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publickey = models.CharField(db_column='PublicKey', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255)  # Field name made lowercase.
    localurl = models.CharField(db_column='LocalURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aessk = models.CharField(db_column='AESSK', max_length=256, blank=True, null=True)  # Field name made lowercase.
    aesiv = models.CharField(db_column='AESIV', max_length=256, blank=True, null=True)  # Field name made lowercase.
    rsapk = models.CharField(db_column='RSAPK', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    rsa_aes_field = models.CharField(db_column='RSA(AES)', max_length=1024, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dataownerid = models.ForeignKey('User', models.DO_NOTHING, db_column='DataOwnerID', blank=True, null=True)  # Field name made lowercase.
    datarecordid = models.ForeignKey('Record', models.DO_NOTHING, db_column='DataRecordID', blank=True, null=True)  # Field name made lowercase.
    datapublickeyid = models.ForeignKey('Publickey', models.DO_NOTHING, db_column='DataPublicKeyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metadata'


class Ownership(models.Model):
    ownerid = models.CharField(db_column='OwnerID', primary_key=True, max_length=100)  # Field name made lowercase.
    dataowner = models.CharField(db_column='DataOwner', max_length=50)  # Field name made lowercase.
    dataproducer = models.CharField(db_column='DataProducer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datauser = models.CharField(db_column='DataUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataagent = models.CharField(db_column='DataAgent', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ownership'


class Publickey(models.Model):
    publickeyid = models.CharField(db_column='PublicKeyID', primary_key=True, max_length=100)  # Field name made lowercase.
    identificationid = models.CharField(db_column='IdentificationID', max_length=50)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exist = models.CharField(db_column='Exist', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publickey'


class Record(models.Model):
    recordid = models.CharField(db_column='RecordID', primary_key=True, max_length=100)  # Field name made lowercase.
    field_recordtime = models.DateTimeField(db_column=' RecordTime')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    authorizer = models.CharField(db_column='Authorizer', max_length=100)  # Field name made lowercase.
    authorizedperson = models.CharField(db_column='AuthorizedPerson', max_length=255)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'record'


class RecordTest(models.Model):
    recordid = models.AutoField(db_column='RecordID', primary_key=True)  # Field name made lowercase.
    dataid = models.ForeignKey(Metadata, models.DO_NOTHING, db_column='DataID')  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    authorizer = models.CharField(db_column='Authorizer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authorizedperson = models.CharField(db_column='AuthorizedPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'record_test'


class TestLittlerecord(models.Model):
    identification = models.CharField(db_column='Identification', primary_key=True, max_length=255)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    md5 = models.CharField(db_column='MD5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', blank=True, null=True)  # Field name made lowercase.
    modificationtime = models.DateTimeField(db_column='ModificationTime', blank=True, null=True)  # Field name made lowercase.
    registrationtime = models.DateTimeField(db_column='RegistrationTime', blank=True, null=True)  # Field name made lowercase.
    data_owner = models.CharField(db_column='Data_Owner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_user = models.CharField(db_column='Data_User', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_littlerecord'


class TestRecord(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    identification = models.CharField(db_column='Identification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    newurl = models.CharField(db_column='NewURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_record'


class User(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=50)  # Field name made lowercase.
    identificationid = models.CharField(db_column='IdentificationID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publickey = models.CharField(db_column='PublicKey', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
