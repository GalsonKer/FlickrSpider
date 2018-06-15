# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import WalkPhotoInfo

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

    apiKey = input('请输入您的Flickr授权账号：')
    apiPsw = input('请输入账户密钥：')
    textStr = input('请输入搜索主题：')
    result = WalkPhotoInfo.getPhotosId(apiKey=apiKey, apiPsw=apiPsw,privacyFilter=1,
                                       hasGeo=1, textStr=textStr,
                                       tableName="PhotoData")