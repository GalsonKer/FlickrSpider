# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import flickrapi
import MySQLController
import re
from GetPhotosInfo import GetPhotosInfo
from DownloadImage import downLoadImg as dwi
import logging
import json

def getPhotosId(apiKey,apiPsw,textStr,per_page,hasGeo,savePath):


    # 把相机型号标签洗掉
    tagPattern = re.compile(r'<NIKON.*?>|<D300.*?>|<CZJ.*?>|<m42>|<smc.*?>')
    flickr = flickrapi.FlickrAPI(apiKey, apiPsw,cache=True)

    # 创建logger新对象
    flickrLog = logging.getLogger(name='FlickLogger')
    flickrLog.setLevel(logging.INFO)

    # 创建一个输出日志handler
    fh = logging.FileHandler(filename='flickr.log',mode='w')
    fh.setLevel(logging.INFO)

    # 再创建一个控制台打印handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义handler格式
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    flickrLog.addHandler(fh)
    flickrLog.addHandler(ch)
    flickrLog.info('创建日志成功')

    mysql = MySQLController.MySQLCommand()
    mysql.connectMysql()
    mysql.creatTable()


    try:
        # 爬取text为Hongcun的照片，这里可以根据需要设置其他参数
        if hasGeo == 2:
            page_json = flickr.photos.search(text=textStr,per_page=per_page,extras='url_z',format='json')
        else:
            page_json = flickr.photos.search(text=textStr,has_geo=hasGeo,per_page=per_page,extras='url_z',format='json')
            # has_geo,设置是否要有地理信息
        page_dict = json.loads(page_json)
        pages = page_dict['photos']['pages']
        flickrLog.info('获取页面数量成功,Page='+str(pages))
        for page in range(1,pages+1):
            flickrLog.info('开始获取第'+str(page)+'页数据！')
            try:
                if hasGeo == 2:
                    photos_json = flickr.photos.search(text=textStr, per_page=per_page, extras='url_z', format='json')
                else:
                    photos_json = flickr.photos.search(text=textStr, has_geo=hasGeo, per_page=per_page, extras='url_z',
                                                       format='json')
                photos_dict = json.loads(photos_json)
                photos = photos_dict['photos']['photo']
                for photo in photos:
                    try:
                        url = photo['url_z']
                        if url != None:

                            photoId = photo['id']
                            photoInfo = GetPhotosInfo(flickr=flickr, photoId=photoId, tag_pattern=tagPattern)
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
                                                     Postdate=postDate, OwnerTimezone=ownerTimezone,
                                                     OwnerLocation=ownerLocation,
                                                     Geolatitude=geolatitude['latitude'],
                                                     Geolongitude=geolatitude['longitude'],
                                                     Tags=tags['tagStr'], Comments=comments)
                            if ImgId == '0':
                                flickrLog.info(msg=url + ':' + 'MySQL存储失败！')
                                continue
                            else:
                                for i in range(5):
                                    # 考虑到网络问题，所以设置失败再四次机会
                                    saveResult = dwi(url=url, imgName=ImgId, savePath=savePath)
                                    if saveResult == 1:
                                        flickrLog.info(msg=url + ':' + 'ID=' + ImgId + '下载成功！')
                                        break
                                if saveResult != 1:
                                    flickrLog.info(url + ':' + 'ID=' + ImgId + '下载失败！')
                    except Exception as e:
                        flickrLog('An Exceptoin Has Been Solved!'+str(e))
                        continue
            except Exception as e:
                flickrLog.info('PageError:'+'获取第'+str(page)+'页数据异常:' + str(e))
            pass
    except Exception as e:
        flickrLog.info('获取页面页面数据页数异常:' + str(e))

