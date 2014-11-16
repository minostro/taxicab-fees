# -*- coding: utf-8 -*-
from django.db.models.loading import get_model
from django.db.models.signals import pre_save


def payment_pre_save(sender, instance, **kwargs):
  Fee = get_model('fees', 'Fee')
  instance.fee = Fee.objects.get_or_create(instance)
  return instance

def payment_post_save(sender, instance, **kwargs):
  Fee = get_model('fees', 'Fee')
  instance.fee.update_status()
  return instance
