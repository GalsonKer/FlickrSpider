FlickrSpider
==
@Author:GalsonKer
**cs.liuxiaoqing@gmail.com**

 - SearchText:输入搜索主题 在flickr上获取关于主题的图片
 
 - Data:图片、作者信息(作者昵称、真实姓名、地理位置、所处时区)、图片上传日期、图片拍摄地理位置、标签和评论
 
 - Database:MySQL-pymysql
 
 - Code:python3.6
 
 - Date:From 2018/6/5
 
FileFunction
==
 - main.py:执行主文件
 - GetPhotosInfo.py:获取图像信息功能函数文件
 - DownloadImage.py:下载图片到本地
 - MySQLController.py:数据库操作
 - WalkPhotoInfo.py:爬去图像信息并存储到本地数据库中
 
Package&Version
==
    Package         Version
------------------- -------------
 - attrs               18.1.0
 - Automat             0.6.0
 - beautifulsoup4      4.6.0
 - bs4                 0.0.1
 - flickrapi           2.4.0
 - h5py                2.8.0
 - Keras               2.2.0
 - lxml                4.2.1
 - numpy               1.14.4
 - pandas              0.23.0
 - parsel              1.4.0
 - PyMySQL             0.8.1
 - pypiwin32           223
 - pytz                2018.4
 - pywin32             223
 - PyYAML              3.12
 - request             1.0.2
 - requests            2.18.4
 - scipy               1.1.0
 - Scrapy              1.5.0
 - selenium            3.12.0
 - Twisted             18.4.0
 - urllib3             1.22
 - w3lib               1.19.0
 - wxpy                0.3.9.8
 
 声明
 --
 
 由于个人时间原因，对于个别会因为编码问题抛出异常，暂时没有完全处理，以及数据库信息的设置比较简陋，所以欢迎fork指教，我会在后续的学习和工作中不断的完善。
 
