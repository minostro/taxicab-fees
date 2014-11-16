# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from mantenedor import models as mantenedor_models
from signals import payment_pre_save, payment_post_save


class BaseModel(models.Model):
  MONTH_OF_THE_YEAR = (
    ("01", _("January")),
    ("02", _("February")),
    ("03", _("March")),
    ("04", _("April")),
    ("05", _("May")),
    ("06", _("June")),
    ("07", _("July")),
    ("08", _("August")),
    ("09", _("September")),
    ("10", _("October")),
    ("11", _("November")),
    ("12", _("December")),
  )

  taxicab = models.ForeignKey(mantenedor_models.Taxicab, verbose_name=_('taxicab'))
  month = models.CharField(_('month'), max_length=2, choices=MONTH_OF_THE_YEAR)
  year = models.CharField(_('year'), max_length=4)
  amount = models.DecimalField(_('amount'), max_digits=19, decimal_places=0)
  created_at = models.DateTimeField(_('created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('updated at'), auto_now=True)

  def period(self):
    return "{0}-{1}".format(self.month, self.year)

  def taxicab_owner(self):
    return self.taxicab.belongs_to

  class Meta:
    abstract = True


class FeeManager(models.Manager):
  def get_or_create(self, payment):
    taxicab = payment.taxicab
    month = payment.month
    year = payment.year
    arel = self.filter(taxicab=taxicab, month=month, year=year, paid=False)

    if arel.count() == 0 :
      fee = self.create(taxicab=taxicab,
                        month=month,
                        year=year,
                        amount=taxicab.line.monthly_fee_amount)
    else:
      fee = arel[0]
    return fee


class Fee(BaseModel):
  paid = models.BooleanField(_('paid'), default=False)

  def update_status(self):
    total_amount = self.payments_total_amount()
    if total_amount >= self.amount:
      self.paid = True
      self.save()

  def payments_total_amount(self):
    return sum(map(lambda payment: payment.amount, self.payment_set.all()))

  def __unicode__(self):
    return u"{0} | {1}".format(self.period(), self.taxicab)

  objects = FeeManager()

  class Meta:
    verbose_name = _('fee')
    verbose_name_plural = _('fees')


class Payment(BaseModel):
  fee = models.ForeignKey(Fee, blank=True, null=True)

  def __unicode__(self):
    return u"{0} | {1}".format(self.amount, self.taxicab)

  class Meta:
    verbose_name = _('payment')
    verbose_name_plural = _('payments')


pre_save.connect(payment_pre_save, sender=Payment, weak=False)
post_save.connect(payment_post_save, sender=Payment, weak=False)
