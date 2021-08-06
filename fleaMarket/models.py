from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class FleaMarket(models.Model):
    title = models.CharField(max_length=200)    # 제품 제목
    writer = models.CharField(max_length=100)   # 글쓴이
    price = models.CharField(max_length=100)    # 가격
    region = models.CharField(max_length=30)    # 지역
    category_choices = (
        ('디지털기기','디지털기기'),
        ('생활가전','생활가전'),
        ('가구/인테리어','가구/인테리어'),
        ('유아동','유아동'),
        ('생활/가공식품','생활/가공식품'),
        ('스포츠/레저','스포트/레저'),
        ('여성잡회/의류', '여성잡화/의류'),
        ('남성잡화/의류', '남성잡화/의류'),
        ('뷰티/미용', '뷰티/미용'),
        ('도서/티켓/음반', '도서/티켓/음반'),
        ('기타 중고물품', '기타 중고물품'),
    )
    category = models.TextField(choices=category_choices) # 제품 카테고리
    pub_date = models.DateTimeField(auto_now = True) # 게시 날짜
    content = models.TextField()       # 제품 설명
    image = models.ImageField(upload_to='fleaMarket/', blank=False, null=False)  # 제품 사진
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120,100)])  # 썸네일

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]  
