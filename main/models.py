from django.contrib.auth.models import User
from django.db import models
from io import BytesIO
from django.core.files import File
from django.urls import reverse
from PIL import Image



# Create your models here.
class Guide(models.Model):
    name=models.CharField('Имя', max_length=100)
    email = models.EmailField(blank=True, null=True)
    description=models.TextField('О себе', blank=True, null=True)
    img=models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name




class Tour(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    rating=models.FloatField(blank=True,null=True, default=0)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media', blank=True, null=True)
    price=models.CharField('Цена', max_length=30, blank=True, null=True, default=0)
    guide = models.ForeignKey(Guide, on_delete=models.SET_NULL, blank=True, null=True, related_name='tours')
    view=models.IntegerField(default=0)
    type=models.CharField(max_length=100, blank=True, null=True)
    duration=models.CharField(max_length=50, blank=True, null=True)
    group=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tourpage', args=[self.slug, self.id])

    class Meta:
        index_together = (('id', 'slug'),)
        verbose_name="Экскурсия"
        verbose_name_plural="Экскурсии"

    def get_rating(self):
        total=sum(int(rating['rating']) for rating in self.ratings.values())
        if self.ratings.count()>0:
            return total/self.ratings.count()
        else:
            return 0

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_guide(self):
        return reverse('guide', args=[self.guide.id])

class Sim_tour(models.Model):
    tour=models.ForeignKey(Tour,on_delete=models.SET_NULL, blank=True, null=True, related_name='seachtour')
    sim_tours=models.CharField(max_length=150, blank=True)

class Views (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='views')
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, related_name='views')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ratings' )
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, related_name='ratings' )
    rating = models.IntegerField()


class Images(models.Model):
    product = models.ForeignKey(Tour, related_name='images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='media', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, related_name='orders')
    order=models.BooleanField(default=False)
    time=models.CharField('Предполагаемое время',blank=True, max_length=100)
    msg=models.TextField('Сообщение', blank=True)

    def get_tour(self):
        return reverse('tourpage', args=[self.tour.id])