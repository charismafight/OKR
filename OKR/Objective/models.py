from django.db import models


# Create your models here.
class Objective(models.Model):
    department = models.CharField(max_length=20)
    objective = models.CharField(max_length=200)
    key_result = models.CharField(max_length=200)
    self_assessment_score = models.IntegerField(default=0)
    leader_assessment_score = models.IntegerField(default=0)
    code = models.CharField(max_length=20, default='')
    time_description = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.objective


STATUS_CHOICE = (
    (1, 'Pending'),
    (2, 'Done'),
    (3, 'Warning')
)


class Action(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, default='')
    complete_date = models.DateField()
    local_leader = models.CharField(max_length=10, default='')
    correlative_leader = models.CharField(max_length=10, blank=True, default='')
    status = models.IntegerField(choices=STATUS_CHOICE)

    def __str__(self):
        return self.content
