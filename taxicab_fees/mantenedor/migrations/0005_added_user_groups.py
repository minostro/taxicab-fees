# -*- coding: utf-8 -*-
from django.db import models, migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def get_permission(action, model_name, content_type):
  return Permission.objects.filter(
    content_type=content_type,
    codename='{0}_{1}'.format(action, model_name)
  )[0]


def add_group_externo():
  fee_content_type = ContentType.objects.get(app_label="fees", model="fee")
  externo_group = Group.objects.create(name='externo')
  change_fee_permission = get_permission('change', 'fee', fee_content_type)
  externo_group.permissions.add(change_fee_permission)
  externo_group.save()


def add_group_accounting():
  fee_content_type = ContentType.objects.get(app_label="fees", model="payment")
  mantenedor_content_type = ContentType.objects.get(app_label="mantenedor", model="taxicab")
  change_payment_permission = get_permission('add', 'payment', fee_content_type)
  add_payment_permision = get_permission('change', 'payment', fee_content_type)
  change_taxicab_permission = get_permission('add', 'taxicab', mantenedor_content_type)
  add_taxicab_permision = get_permission('change', 'taxicab', mantenedor_content_type)
  accounting_group = Group.objects.create(name='tesorero')
  accounting_group.permissions = [
    change_payment_permission,
    add_payment_permision,
    change_taxicab_permission,
    add_taxicab_permision
  ]
  accounting_group.save()


def add_user_groups(apps, schema_editor):
  add_group_externo()
  add_group_accounting()


class Migration(migrations.Migration):
  dependencies = [
    ('mantenedor', '0001_initial'),
  ]

  operations = [
    migrations.RunPython(add_user_groups),
  ]
