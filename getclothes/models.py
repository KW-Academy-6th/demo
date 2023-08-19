from django.db import models

class GC(models.Model):
    no = models.AutoField(db_column='no', primary_key=True)
    date = models.CharField(db_column='date', max_length=255)
    top = models.CharField(db_column='top', max_length=255)
    bottom = models.CharField(db_column='bottom', max_length=255)
    vehicle = models.IntegerField(db_column='vehicle')
    inout = models.IntegerField(db_column='inout')
    high = models.FloatField(db_column='high')
    low = models.FloatField(db_column='low')
    now = models.FloatField(db_column='now')
    hum = models.FloatField(db_column='hum')
    rain = models.FloatField(db_column='rain')
    prob = models.FloatField(db_column='prob')

    @classmethod
    def get_row_count(cls):
        return cls.objects.count()

    class Meta:
        managed = False
        db_table = 'get'