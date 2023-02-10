from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)  # -> varchar(32)
    pwd = models.CharField(max_length=32)  # -> varchar(32)


class Press(models.Model):
    id = models.AutoField(primary_key=True)  # id 主键
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id 主键
    title = models.CharField(max_length=30)  # 书名
    # Django 1.11 默认就是级联删除,Django 2.0 之后必须指定on_delete
    # to = 关联的表名, 默认会添加对应的id.
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)  # id 主键
    name = models.CharField(max_length=32)  # 作者名字
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name




# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
