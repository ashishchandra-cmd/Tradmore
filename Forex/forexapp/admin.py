from django.contrib import admin

from forexapp.models import *


admin.site.register(Currencies)
admin.site.register(TradingData)
admin.site.register(UserHistory)
admin.site.register(NotifyData)
