# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Line(models.Model):
  number = models.IntegerField(_('number'))
  monthly_fee_amount = models.DecimalField(_('monthly fee amount'), max_digits=19, decimal_places=0)

  def __unicode__(self):
    return u"Línea {0}".format(self.number)

  class Meta:
    verbose_name = _('line')
    verbose_name_plural = _('lines')


class Person(models.Model):
  name = models.CharField(_('name'), max_length=155)
  surname = models.CharField(_('surname'), max_length=200)
  personal_id = models.CharField(_('personal id'), max_length=150)

  def __unicode__(self):
    return u"{0} {1}".format(self.name, self.surname).title()

  class Meta:
    verbose_name = _('person')
    verbose_name_plural = _('people')


class Taxicab(models.Model):
  belongs_to = models.ForeignKey(Person, related_name='belongs_to', verbose_name=_('belongs to'))
  line = models.ForeignKey(Line, verbose_name=_('line'))

  ppu = models.CharField(_('ppu'), max_length=100)
  motor_number = models.CharField(_('motor number'), max_length=100)
  chassis_number = models.CharField(_('chasis number'), max_length=100)
  serie_number = models.CharField(_('serie number'), max_length=100)
  inscription_date = models.DateField(_('inscription date'))
  internal_identifier = models.CharField(_('internal identifier'), max_length=100)
  check_up_expires_at = models.DateField(_('check up expires at'))

  def __unicode__(self):
    return u"{0} ({1})".format(self.ppu, self.line)

  class Meta:
    verbose_name = _('taxiscab')
    verbose_name_plural = _('taxicabs')

