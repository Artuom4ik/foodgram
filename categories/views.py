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


def detail_information_card_api(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
        products = card.products.all()
        detail_information = {
            'title': card.title,
            'scope_of_application': [],
            'diameters': [],
            'length': [],
            'colors': [],
            'image': ''
        }

        for product in products:
            if product.scope_of_application not in detail_information['scope_of_application']:
                detail_information['scope_of_application'].append(product.scope_of_application)
            
            elif product.diametr not in detail_information['diameters']:
                detail_information['diameters'].append(product.diametr)
            
            elif product.length not in detail_information['length']:
                detail_information['length'].append(product.length)
            
            elif product.color not in detail_information['colors']:
                detail_information['colors'].append(product.color)
            
            elif product.image and not detail_information['image']:
                detail_information['image'] = product.image.url
        
        return JsonResponse(detail_information, safe=False, json_dumps_params={
            'ensure_ascii': False,
            'indent': 4,
        })
    
    except Card.DoesNotExist:
        return JsonResponse(
            {'Error': 'card does not exist'},
            safe=False,
            json_dumps_params={
                'ensure_ascii': False,
                'indent': 4,}
        )

