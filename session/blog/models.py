from django.db import models

# Create your models here.
# session의 settings.py 에서 INSTALLED_APPS 에 블로그 추가
# blog 폴더의 models.py 에서 Blog 클래스 추가해줘야한다 
class Blog(models.Model):
    title = models.CharField(max_length=20) # 20글자
    content = models.TextField() # text
    writer = models.CharField(max_length=20) # 20글자
    createdAt = models.DateTimeField(auto_now_add=True) # 현재 시각 표기
    github_url = models.URLField(max_length=200, null=True) # URL
    email = models.EmailField(max_length=50, default='example@example.com') # 이메일
    def __str__(self):
        return self.title