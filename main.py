# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import WalkPhotoInfo
import yaml,os

if __name__=="__main__":
    '''
    'privacyFilter':
        1 public photos
        2 private photos visible to friends
        3 private photos visible to family
        4 private photos visible to friends & family
        5 completely private photos

    'hasGeo':
        if the value is "0" any photo that has not been geotagged.
    '''

    textStr = input('请输入搜索主题：')
    '''
    per_page:最大可以是250
    hasGeo:1为含有地理信息，0为不含，None为全部
    tableName:为MySQL数据库中表的名称
    MySQL_User:MySQL数据库名
    MySQL_Psw:MySQL密码
    MySQL_Db:MySQL数据库名称
    '''
    with open('APISetting.yml','r') as fp:
        ApiInfo = yaml.load(fp)
    result = WalkPhotoInfo.getPhotosId(apiKey=ApiInfo['ApiKey'],
                                       apiPsw=ApiInfo['ApiSecret'],
                                       hasGeo=ApiInfo['hasGeo'],
                                       textStr=textStr,
                                       per_page=ApiInfo['per_page'],
                                       savePath=ApiInfo['savePath'])