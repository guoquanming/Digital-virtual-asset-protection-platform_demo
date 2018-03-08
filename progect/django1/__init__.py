import pymysql

pymysql.install_as_MySQLdb()

#py3.0以后用pymysql代替mysqldb，需要在这个位置声明一下，来匹配mysqldb模型，没有这个会报错没找到mydqldb模型。