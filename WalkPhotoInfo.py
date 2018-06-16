# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import flickrapi
import MySQLController
import re
from GetPhotosInfo import GetPhotosInfo
from DownloadImage import downLoadImg as dwi
import logging
import os


def isCollection (flickr,photoId):
    info = flickr.collections.getInfo(photoId)
    return ''

def getPhotosId(apiKey,apiPsw,textStr,hasGeo,privacyFilter,tableName):

    savePath = 'D:\\ProgramData\\FlickrImage\\'
    tagPattern = re.compile(r'<NIKON>|<D300s>')#把相机型号标签洗掉
    flickr = flickrapi.FlickrAPI(apiKey, apiPsw,cache=True)

    #创建logger新对象
    flickrLog = logging.getLogger(name='FlickLogger')
    flickrLog.setLevel(logging.INFO)

    #创建一个输出日志handler
    fh = logging.FileHandler(filename='flickr.log',mode='w')
    fh.setLevel(logging.INFO)

    # 再创建一个控制台打印handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    #定义handler格式
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    flickrLog.addHandler(fh)
    flickrLog.addHandler(ch)
    print('创建日志成功')

    mysql = MySQLController.MySQLCommand(tableName)
    mysql.connectMysql()
    mysql.creatTable()

    try:
        # 爬取text为Hongcun的照片，这里可以根据需要设置其他参数
        if hasGeo==None:
            photos = flickr.walk(text=textStr, privacy_filter=privacyFilter,
                                 extras='url_o')
        else:
            photos = flickr.walk(text=textStr,has_geo=hasGeo,
                                 privacy_filter=privacyFilter, extras='url_o')
            #has_geo,设置是否要有地理信息

        for photo in photos:
            url = photo.get('url_o')
            if url != None:
                photoId = re.split('/|_', url)[4]
                photoInfo = GetPhotosInfo(flickr=flickr,photoId=photoId,tag_pattern=tagPattern)
                userName = photoInfo.getOwnerUsername()
                realName = photoInfo.getOwnerRealname()
                postDate = photoInfo.getPostDare();
                ownerTimezone = photoInfo.getOwnerTimezone()
                ownerLocation = photoInfo.getOwnerLocation()
                geolatitude = photoInfo.getPhotoGeo()
                tags = photoInfo.getPhotoTags()
                comments = photoInfo.getPhotoComments()

                ImgId = mysql.insertData(PhotoUrl=url, PhotoId=photoId,
                                 OwnerNickname=userName, OwnerRealname=realName,
                                 Postdate=postDate, OwnerTimezone=ownerTimezone, OwnerLocation=ownerLocation,
                                 Geolatitude=geolatitude['latitude'],Geolongitude=geolatitude['longitude'],
                                 Tags=tags['tagStr'], Comments=comments)
                if ImgId=='0':
                    flickrLog.info(msg=url+':'+'MySQL存储失败！')
                    continue
                else:
                    for i in range(5):#考虑到网络问题，所以设置失败再四次机会
                        saveResult = dwi(url=url, imgName=ImgId, savePath=savePath)
                        if saveResult==1:
                            flickrLog.info(msg=url+':'+'ID='+ImgId+'下载成功！')
                            break
                    if saveResult!=1:
                        print(msg=url+':'+'ID='+ImgId+'下载失败！')
    except Exception:

        return 0