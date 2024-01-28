from django.contrib import admin

from categories.models import Section, Group, Subgroup, Card


admin.site.register(Section)
admin.site.register(Group)
admin.site.register(Subgroup)
admin.site.register(Card)
