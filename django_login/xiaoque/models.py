from django.db import models

# Create your models here.
class AddTask(models.Model):
    task_id = models.CharField('任务编号',max_length=10)
    task_name = models.CharField('任务名称',max_length=20)
    inspect_line = models.CharField('巡检线路',max_length=20)
    inspect_user = models.CharField('巡检员',max_length=10)
    state = models.CharField('启用状态',max_length=10)
    pole_beg = models.CharField('起始杆号',max_length=10)
    pole_end = models.CharField('终止杆号',max_length=10)
    df_username = models.CharField('下发人',max_length=20)
    df_date = models.CharField('下发时间',max_length=20)
    class Meta:
        db_table = 'task'