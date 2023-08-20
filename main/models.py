from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return self.name


class Table(models.Model):
    img = models.ImageField()
    team = models.CharField(max_length=255)
    o = models.IntegerField()
    g = models.IntegerField()
    d = models.IntegerField()
    m = models.IntegerField()
    t_f = models.CharField(max_length=255)


class Player(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    number = models.IntegerField()
    games = models.IntegerField(default=0)
    type = models.IntegerField(choices=(
        (1, "Darvozabon"),
        (2, "Himoya"),
        (3, "Markaz"),
        (4, "Hujumchi")
    ))
    start = models.IntegerField(default=0)
    sub_off = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField()


class Arena(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    kvm = models.IntegerField()
    places = models.IntegerField()
    sector = models.IntegerField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    arena_photo = models.ManyToManyField(Photo)

    def __str__(self):
        return self.name


class Sponsors(models.Model):
    logo = models.ImageField()


class Info(models.Model):
    logo = models.ImageField()
    short = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    ins = models.URLField()
    tg = models.URLField()
    fb = models.URLField()
    yt = models.URLField()
    tw = models.URLField()


class NewDetail(models.Model):
    photo = models.ImageField()
    short_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Press(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()


class Club(models.Model):
    description = RichTextField()


class Advice(models.Model):
    photo = models.ImageField(upload_to="advice/")
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Training(models.Model):
    training = RichTextField()


class ArenaHistory(models.Model):
    history = RichTextField()


