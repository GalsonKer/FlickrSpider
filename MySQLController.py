# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import pymysql

class MySQLCommand(object):
    # 类的初始化
    def __init__(self,tableName):
        self.host = 'localhost'
        self.port = 3306                 # 端口号
        self.user = 'root'               # 用户名
        self.password = "lyp82nlf"       # 密码
        self.db = "gsk"                  # 库
        self.Photo_table = tableName     # 表
        self.charset ='utf8mb4'          # 编码使用utf8mb4可以存储emoji表情符号

        # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
            print('连接MySQL成功')
        except:
            print('connect mysql error.')

    def creatTable(self):
        #数据表如果之前存在则删除，重新创建数据
        creat_sql = "create table "+self.Photo_table+\
                    " ( Id int auto_increment primary key," \
                    "Photourl VARCHAR(100) NOT NULL," \
                    "Photoid VARCHAR(100) NOT NULL," \
                    "OwnerNickname VARCHAR(255) NOT NULL," \
                    "OwnerRealname VARCHAR(255) NOT NULL," \
                    "OwnerLocation VARCHAR(255)," \
                    "OwnerTimezone VARCHAR(255)," \
                    "Postdate VARCHAR(255) NOT NULL," \
                    "Geolatitude VARCHAR(255)," \
                    "Geolongitude VARCHAR(255)," \
                    "Tags TEXT," \
                    "Comments TEXT)AUTO_INCREMENT=1"


        delete_sql = "drop table if exists "+ self.Photo_table
        self.cursor.execute(delete_sql)
        self.cursor.execute(creat_sql)
        print('创建MySQL成功')


    def insertData(self,PhotoUrl,PhotoId,
                   OwnerNickname,OwnerRealname,Postdate,
                   OwnerTimezone,OwnerLocation,Geolatitude,
                   Geolongitude,Tags,Comments):
        try:

            table = self.Photo_table
            photo_property = "Photourl,Photoid," \
                             "OwnerNickname,OwnerRealname," \
                             "Postdate,OwnerLocation,OwnerTimezone,Geolatitude," \
                             "Geolongitude,Tags,Comments"


            Comments = self.conn.escape(Comments)

            photo_data = '"'+PhotoUrl+'"'+','\
                         +'"'+PhotoId+'"'+','\
                         +'"'+OwnerNickname+'"'+','\
                         +'"'+OwnerRealname+'"'+','\
                         +'"'+Postdate+'"'+',' \
                         +'"'+OwnerLocation+'"'+',' \
                         +'"'+OwnerTimezone+'"'+',' \
                         +'"'+Geolatitude+'"'+','\
                         +'"'+Geolongitude+'"'+','\
                         +'"'+Tags+'"'+','\
                         +'"'+Comments+'"'
            sql = "INSERT INTO "+ table + "(%s) VALUES (%s)" %(photo_property,photo_data)
            result = self.cursor.execute(sql)
            id = str(self.conn.insert_id())
            self.conn.commit()
            if result==1:
                return id
            else:
                return '0'
        except:
            return '0'