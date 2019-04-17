from django.db import models


# Create your models here.
class Objective(models.Model):
    department = models.CharField('部门', max_length=20)
    objective = models.CharField('目标', max_length=200)
    key_result = models.CharField('关键结果', max_length=200)
    self_assessment_score = models.IntegerField('部门自评', default=0)
    leader_assessment_score = models.IntegerField('领导评分', default=0)
    code = models.CharField('编号', max_length=20, default='')
    time_description = models.CharField('年度', max_length=20, default='')

    def __str__(self):
        return self.objective


STATUS_CHOICE = (
    (1, 'Pending'),
    (2, 'Done'),
    (3, 'Warning')
)


class Action(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    content = models.CharField('行动内容', max_length=500, default='')
    complete_date = models.DateField('完成时间')
    local_leader = models.CharField('本部门责任人', max_length=100, default='')
    correlative_leader = models.CharField('相关部门责任人', max_length=100, blank=True, default='')
    status = models.IntegerField('状态', choices=STATUS_CHOICE)

    def __str__(self):
        return self.content
