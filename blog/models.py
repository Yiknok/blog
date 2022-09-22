from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category Title')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Category URL')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag Title')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Tag URL')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Post Title')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Post URL')
    author = models.CharField(max_length=100, blank=True, verbose_name='Post Author')
    content = models.TextField(blank=True, verbose_name='Post Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created:')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Post Image')
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Post Category')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True, verbose_name='Post Tags')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
