from django.db import models


class Customer(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name='Kullanıcı')
  tc = models.CharField(verbose_name='Tc Numarası',max_length=11, unique=True)
  name = models.CharField(max_length=50, verbose_name='İsim')
  surname = models.CharField(max_length=50, verbose_name='Soyisim')
  phone = models.CharField(verbose_name='Telefon Numarası', max_length=11)
  city = models.CharField(max_length=50, verbose_name='Şehir')
  district = models.CharField(max_length=50, verbose_name='İlçe')
  created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

  def __str__(self):
    return self.name