# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import flickrapi
import json
import re

class GetPhotosInfo(object):

    def __init__(self,flickr,photoId):
        self.photoId = photoId
        self.flickr = flickr
        photoInfo = self.flickr.photos.getInfo(photo_id=photoId,format='json')
        self.info_dict = json.loads(photoInfo)


    def getOwnerUsername(self):
        '''
        :return:返回图片拥有者昵称信息
        '''

        try:
            ownerId = self.info_dict['photo']['owner']['nsid']
            ownerInfo = self.flickr.people.getInfo(user_id=ownerId, format='json')
            owner_dict = json.loads(ownerInfo)
            username = owner_dict['person']['username']['_content']
            return username
        except:
            # print(self.info_dict['photo']['owner']['nsid'] + ':' + '图片所有者信息不可获取！')
            username = 'Refusing to Collect'
            return username

    def getOwnerRealname(self):
        '''
        :return:返回用户真实姓名
        '''

        try:
            ownerId = self.info_dict['photo']['owner']['nsid']
            ownerInfo = self.flickr.people.getInfo(user_id=ownerId, format='json')
            owner_dict = json.loads(ownerInfo)
            realname = owner_dict['person']['realname']['_content']
            return realname
        except:
            # print(self.info_dict['photo']['owner']['nsid'] + ':' + '图片所有者信息不可获取！')
            realname = 'Refusing to Collect'
            return realname


    def getOwnerTimezone(self):
        '''
        :return: 如果可以过去到所在位置时区信息，则返回，否则返回空
        '''

        try:
            ownerId = self.info_dict['photo']['owner']['nsid']
            ownerInfo = self.flickr.people.getInfo(user_id=ownerId, format='json')
            owner_dict = json.loads(ownerInfo)
            ownerTimezone =  owner_dict['person']['timezone']['timezone_id']
            return ownerTimezone
        except:
            return ''

    def getOwnerLocation(self):

        try:
            ownerId = self.info_dict['photo']['owner']['nsid']
            ownerInfo = self.flickr.people.getInfo(user_id=ownerId, format='json')
            owner_dict = json.loads(ownerInfo)
            ownerLocation = owner_dict['person']['location']['_content']
            return ownerLocation
        except:
            return ''


    def getPostDare(self):
        '''
        :return: 返回图片上传日期
        '''

        try:
            return self.info_dict['photo']['dates']['taken']
        except:
            print(self.photoId+':'+'获取图片上传时间异常！')
            return 'ERROR'


    def getPhotoTags(self):
        '''
        :return:stat(0，表示没有标签;1，表示存在标签;2,表示出错;)
        '''

        tagDict = dict()
        try:
            tagList = self.info_dict['photo']['tags']['tag']

            tagStr = ''
            if len(tagList)!=0:
                tagDict['stat'] = 1
                for tag in tagList:
                    tagStr = tagStr + '<'+tag['raw']+'  '+'>'
                    tagDict['tagStr'] = tagStr

            else:
                tagDict['stat'] = 0
                tagDict['tagStr'] = ''
            return tagDict
        except:
            print(self.photoId+':'+'获取图片标签异常！')
            tagDict['stat'] = 2
            tagDict['tagStr'] = 'ERROR'

    def getPhotoGeo(self):
        photoGeo = self.flickr.photos.getInfo(photo_id=self.photoId,format='json')
        geoInfo = dict()
        try:
            geo_dict = json.loads(photoGeo)
            geoInfo['latitude'] = geo_dict['photo']['location']['latitude']
            geoInfo['longitude'] = geo_dict['photo']['location']['longitude']

            return geoInfo
        except:
            geoInfo['latitude'] = ''
            geoInfo['longitude'] = ''
            return geoInfo

    def getPhotoComments(self):
        '''
        :return:返回用户评论信息;stat=0,没有评论;stat=1
        '''

        commentsInfo = dict()
        comments_json = self.flickr.photos.comments.getList(photo_id=self.photoId, format='json')
        comments_dict = json.loads(comments_json)
        try:

            comments_str = ''
            for comment in comments_dict['comments']['comment']:
                comments_str = comments_str + '<'+comment['_content']+'>'
            pattern = re.compile(r'\n|<a href=".+?</a>|&.+?;')
            comments_s = re.sub(pattern, ' ', comments_str)
            commentsInfo['stat'] = 1
            commentsInfo['commentStr'] = comments_s

        except:
            commentsInfo['stat'] = 0
            commentsInfo['commentStr'] = ''

        return commentsInfo