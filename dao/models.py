from django.db import models
from django.utils import timezone

# Create your models here.

class TwoColorBall(models.Model):
    number_one = models.IntegerField()
    number_two = models.IntegerField()
    number_three = models.IntegerField()
    number_four = models.IntegerField()
    number_five = models.IntegerField()
    number_six = models.IntegerField()
    number_blue = models.IntegerField()
    data_time = models.DateTimeField()
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    update_time = models.DateTimeField('最后更新时间', default=timezone.now)

    def __str__(self):
        return f'red ball: {self.number_one} {self.number_two} {self.number_three} {self.number_four} {self.number_five} {self.number_six}  blue ball: {self.number_blue}'

    class Meta:
        unique_together = ['data_time']

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_time = timezone.now()
        self.update_time = timezone.now()
        return super(TwoColorBall, self).save(*args, **kwargs)


class BigLotto(models.Model):
    number_one = models.IntegerField()
    number_two = models.IntegerField()
    number_three = models.IntegerField()
    number_four = models.IntegerField()
    number_five = models.IntegerField()
    blue_one = models.IntegerField()
    blue_two = models.IntegerField()
    data_time = models.DateTimeField()
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    update_time = models.DateTimeField('最后更新时间', default=timezone.now)

    def __str__(self):
        return f'red ball: {self.number_one} {self.number_two} {self.number_three} {self.number_four} {self.number_five}  blue ball: {self.blue_one} {self.blue_two}'

    class Meta:
        unique_together = ['data_time']

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_time = timezone.now()
        self.update_time = timezone.now()
        return super(BigLotto, self).save(*args, **kwargs)