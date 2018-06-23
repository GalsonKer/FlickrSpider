# -*- coding: utf-8 -*-
# Author:cs.liuxiaoqing@gmail.com

import re
from urllib import request

def downLoadImg(url,imgName,savePath):
    try:
        imgType = re.split('\.', url)[-1]
        file = savePath+imgName+'.'+imgType
        request.urlretrieve(url,file)
        return 1
    except Exception as e:
        print(repr(e))
        return 0