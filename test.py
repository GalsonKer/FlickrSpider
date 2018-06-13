# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import flickrapi
from GetPhotosInfo import GetPhotosInfo
from bs4 import BeautifulSoup
import json
import re
import MySQLController
import DownloadImage
import logging
import os
import shutil

if __name__=="__main__":

    apiKey = input('请输入flickr授权账号：')
    apiPsw = input('请输入flickr账号密码：')
    flickr = flickrapi.FlickrAPI(apiKey, apiPsw, cache=True)
    photoId = ""
    savePath = 'D:\\ProgramData\\FlickrImage\\'

    # mysql = MySQLController.MySQLCommand('demo')
    # mysql.connectMysql()
    # mysql.creatTable()
    #
    # logging.basicConfig(level=logging.INFO,
    #                     filename='flickr.log',
    #                     filemode='w',
    #                     format=
    #                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    #
    #
    # photoInfo = flickr.photos.getInfo(photo_id=photoId,format='json')
    # photoComments = flickr.photos.comments.getList(photo_id=photoId,fsormat='rest')
    # soup = BeautifulSoup(photoComments,"lxml")
    # ownerInfo = flickr.people.getInfo(user_id='130145642@N06', format='json')
    # json_dict = json.loads(photoInfo)
    # owner_dict = json.loads(ownerInfo)
    # postDate = json_dict['photo']['dates']['taken']
    # owner_nickname = json_dict['photo']['owner']['username']
    # owner_realname = json_dict['photo']['owner']['realname']
    # json_dict['photo']['views']
    # tags = json_dict['photo']['tags']['tag']
    # print(owner_dict['person']['username']['_content'])
    # print(owner_dict['person']['realname']['_content'])
    # print(owner_dict['person']['timezone']['timezone_id'])
    # print(soup)
    # if len(tags)!=0:
    #     tagStr = ''
    #     for tag in tags:
    #         tagStr = tagStr+'<'+tag['_content']+'>'
    # else:
    #     print('标签为空')
    # print(tagStr)
    #
    # photoGeo = flickr.photos.geo.getLocation(photo_id=photoId,format='json')
    # geo_dict = json.loads(photoGeo)
    # try:
    #     print(geo_dict['photo']['location']['latitude'])
    #     print(geo_dict['photo']['location']['longitude'])
    # except:
    #     print('不存在！')
    #
    # commentsInfo = dict()
    # comments_json = flickr.photos.comments.getList(photo_id=photoId, format='json')
    # comments_dict = json.loads(comments_json)
    # try:
    #
    #     comments_str = ''
    #     for comment in comments_dict['comments']['comment']:
    #         comments_str = comments_str + '{' + comment['_content'] + '}'
    #
    #     commentsInfo['stat'] = 1
    #     commentsInfo['commentStr'] = comments_str
    #     print(commentsInfo['commentStr'])
    # except:
    #     commentsInfo['stat'] = 0
    #     commentsInfo['commentStr'] = ''
    #     print('没有评论信息')
    #
    # url = 'https://farm2.staticflickr.com/1741/41791409964_01e641bf45_z.jpg'
    # photoInfo = GetPhotosInfo(flickr=flickr, url=url)
    # userName = photoInfo.getOwnerUsername()
    # realName = photoInfo.getOwnerRealname()
    # postDate = photoInfo.getPostDare();
    # ownerLocation = photoInfo.getOwnerLocation()
    # geolatitude = photoInfo.getPhotoGeo()
    # ownerTimezone = photoInfo.getOwnerTimezone()
    # tags = photoInfo.getPhotoTags()
    # comments = photoInfo.getPhotoComments()
    #
    #
    #
    # print(tags['tagStr'])
    #
    # mysql.insertData(PhotoUrl='demo', PhotoId=photoId,
    #                  OwnerNickname=userName, OwnerRealname=realName,
    #                  Postdate=postDate, OwnerTimezone=ownerTimezone, OwnerLocation=ownerLocation,
    #                  Geolatitude=geolatitude['latitude'], Geolongitude=geolatitude['longitude'],
    #                  Tags=tags['tagStr'], Comments=comments['commentStr'])
    #
    # t = flickr.photos.comments.getList(photo_id=photoId,format='json')
    # t = json.loads(t)
    # s = t['comments']['comment'][0]['_content']
    # pattern = re.compile(r'\n|<a href=".+?</a>|&.+?;')
    # r = re.sub(pattern,' ',s)
    # print(r)
    # path = 'D:\\ProgramData\\FlickrImage\\'
    # url = 'https://farm2.staticflickr.com/1744/27643544677_3014f3d1f6_o.jpg'
    # r = DownloadImage.downLoadImg(url=url,imgName='demo',savePath=path)
    # logging.info(msg=r)
    os.remove(savePath)