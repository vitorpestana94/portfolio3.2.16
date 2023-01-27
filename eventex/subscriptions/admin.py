from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CPF', 'email', 'telefone', 'created_at', 
                    'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'email', 'CPF', 'telefone', 'created_at')
    list_filter = ('paid', 'created_at')

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)