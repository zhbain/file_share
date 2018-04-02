from django.db import models
from datetime import datetime

class File(models.Model):
    # 访问该页面的次数
    visit_count = models.IntegerField(verbose_name=u'访问次数', default=0)
    # 唯一标识一个文件
    code = models.CharField(max_length=8, verbose_name=u'code')
    # 文件上传的时间
    date_time = models.DateTimeField(default=datetime.now, verbose_name=u'上传时间')
    # 文件存储的路径
    path = models.CharField(max_length=32, verbose_name=u'下载路径')
    # 文件名
    name = models.CharField(max_length=32, verbose_name=u'文件名', default='')
    # 文件大小
    file_size = models.CharField(max_length=10, verbose_name=u'文件大小')
    # 上传文件的IP
    ip_address = models.CharField(max_length=32, verbose_name=u'IP地址', default='')
    
    class Meta():  # Meta 可用于定义数据表名，排序方式等。
        ordering = ['-date_time']
        verbose_name='file' #指明一个易于理解和表示的单词形式的对象。
        db_table = 'file'#声明数据表的名。

    def __str__(self):
        return self.name 
