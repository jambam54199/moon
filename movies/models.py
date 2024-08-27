from django.db import models

# Create your models here.
class movies_post(models.Model):
    title = models.CharField("영화제목", max_length=50)
    image = models.ImageField("포스터", upload_to="post")
    storyline = models.TextField("줄거리")
    runningtime = models.IntegerField("러닝타임", default=0)
    gnere = models.CharField("장르", max_length=10)
    director = models.CharField("감독", max_length=20)
    year = models.CharField("개봉년도", max_length=10)
    agelimit = models.CharField("연령제한", max_length=10)
    country = models.CharField("국가", max_length=10)
    famousline = models.TextField("명대사", blank=True)

    def __str__(self):
        return f"{self.title}"