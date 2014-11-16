from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from fees.models import Fee, Payment

class FeeAdminForm(admin.ModelAdmin):
  list_display = ('period', 'taxicab', 'taxicab_owner', 'amount', 'payments_total_amount', 'paid',)
  search_fields = ('taxicab__ppu',)
  list_filter = ('paid',)

  def is_user_allowed_to_change_view(self, user):
    return len(filter(lambda group: group.name == 'externo', user.groups.all())) > 0

  def change_view(self, request, object_id, form_url='', extra_context=None):
    if self.is_user_allowed_to_change_view(request.user):
      messages.error(request, _('Sorry, but editing is NOT ALLOWED'))
      return redirect(request.META['HTTP_REFERER'])
    return super(FeeAdminForm, self).change_view(request, object_id, form_url, extra_context)


class PaymentAdminForm(admin.ModelAdmin):
  list_display = ('period', 'taxicab', 'amount', 'created_at')
  exclude = ('fee',)

class PaymentAdminForm2(admin.ModelAdmin):
  list_display = ('period', 'taxicab', 'amount', 'created_at')
  exclude = ('fee',)


admin.site.register(Fee, FeeAdminForm)
admin.site.register(Payment, PaymentAdminForm)
admin.site.disable_action('delete_selected')
