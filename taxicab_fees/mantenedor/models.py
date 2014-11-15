# -*- coding: utf-8 -*-

from django.db import models


class Line(models.Model):
  number = models.IntegerField()
  monthly_fee_amount = models.DecimalField(max_digits=19, decimal_places=0)

  def __unicode__(self):
    return u"Línea {0}".format(self.number)


class Person(models.Model):
  name = models.CharField(max_length=155)

  def __unicode__(self):
    return u"{0}".format(self.name)


class Taxicab(models.Model):
  belongs_to = models.ForeignKey(Person, related_name="belongs_to")
  line = models.ForeignKey(Line)

  ppu = models.CharField(max_length=100)
  motor_number = models.CharField(max_length=100)
  chassis_number = models.CharField(max_length=100)
  serie_number = models.CharField(max_length=100)
  vin_number = models.CharField(max_length=100)
  manufacture_year = models.IntegerField()
  acquisition_date = models.DateField()
  inscription_date = models.DateField()
  internal_identifier = models.CharField(max_length=100)
  taxicab_check_up_expires_at = models.DateField()

  def __unicode__(self):
    return u"{0}-{1}".format(self.ppu, self.line)
