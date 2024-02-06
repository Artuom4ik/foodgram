from django.shortcuts import render
from django.http import JsonResponse

from .models import Section, Group, Subgroup, Card


def categories_list_api(request):
    sections = Section.objects.all()

    categories = {
        'data': [{'section': {'title': section.title}} for section in sections]
    }

    return JsonResponse(categories, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def cards_list_api(request):
    pass

