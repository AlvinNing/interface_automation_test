from django.db import models

# Create your models here.
class result(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False,  help_text='测试执行人')
    version_num = models.PositiveIntegerField(blank=False,  help_text='版本号')
    anr_num = models.IntegerField(blank=True,  help_text='ANR异常数')
    crash_num = models.IntegerField(blank=True,  help_text='crash异常数')
    exception_num = models.IntegerField(blank=True,  help_text='exception异常数')
    monkey_is_finish = models.BooleanField(default=False, help_text='是否正常结束')
    bug_num = models.IntegerField(blank=True, null=False, help_text='bug统计总数量')
    remark = models.CharField(max_length=30, blank=False, null=False, help_text="备注")