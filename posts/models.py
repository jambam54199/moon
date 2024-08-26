from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey("users.User", # 앱이름.모델이름
                             verbose_name = "작성자",
                             on_delete = models.CASCADE) # 작성자 데이터 삭제되면 Post도 같이 삭제
    review = models.TextField("리뷰", blank = True)
    short_comment = models.CharField("한줄평", max_length = 50)
    created = models.DateTimeField("작성일시", auto_now_add = True)

class Comment(models.Model):
    user = models.ForeignKey("users.User",
                             verbose_name = "작성자",
                             on_delete = models.CASCADE)
    post = models.ForeignKey(Post,
                             verbose_name = "포스트",
                             on_delete = models.CASCADE)
    content = models.TextField("댓글 내용")
    created = models.DateTimeField("작성일시", auto_now_add = True)
    
