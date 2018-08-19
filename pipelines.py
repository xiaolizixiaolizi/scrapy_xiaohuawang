# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from  scrapy.pipelines.images import ImagesPipeline
from  .settings import  IMAGES_STORE
import  os
class XiaohuaImagePipeline(ImagesPipeline):
    #请求之前的准备带上item以便于file_path传值
    def get_media_requests(self, item, info):
        request_objs=super(XiaohuaImagePipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item
        return  request_objs
    #images/category(各个名字作文文件夹)/image_name.jpg
    def file_path(self, request, response=None, info=None):
        path=super(XiaohuaImagePipeline,self).file_path(request,response,info)

        category=request.item.get('name')
        image_store=IMAGES_STORE
        category_path=os.path.join(image_store,category)
        if not category_path:
            os.mkdir(category_path)

        image_name=path.replace('full/','')
        image_path=os.path.join(category_path,image_name)
        return  image_path










class XiaohuaPipeline(object):
    def process_item(self, item, spider):
        return item
