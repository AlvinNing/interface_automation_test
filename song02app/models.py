from django.db import models

# Create your models here.
class result(models.Model):
    id = models.IntegerField(primary_key=True, name="数据主键id")
    project = models.CharField(max_length=20, name="项目名称")
    case_id = models.CharField(max_length=10, name="用例ID")
    interface_name = models.CharField(max_length=30, default="获取订单列表接口", name="接口名称")
    case_description = models.CharField(max_length=300)
    req_method = models.CharField(max_length=6)
    req_url = models.CharField(max_length=100)
    req_parameter = models.CharField(max_length=100)
    checkpoint = models.CharField(max_length=100)
    request_message = models.CharField(max_length=500)
    response_message = models.CharField(max_length=500)
    people = models.CharField(max_length=10)
    test_res = models.CharField(max_length=10)
    remarks = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
