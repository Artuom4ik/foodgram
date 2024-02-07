from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Section, Group, Subgroup, Card


def categories_list_api(request):
    sections = Section.objects.all()

    categories = {
        'data': {
            'sections': [{'section': {'title': section.title}} for section in sections],
        }
    }

    return JsonResponse(categories, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def cards_list_api(request, section_id, group_id, subgroup_id):
    section = get_object_or_404(Section, id=section_id)
    group = get_object_or_404(Group, id=group_id)
    subgroup = get_object_or_404(Subgroup, id=subgroup_id)

    sorted_cards = Card.objects.filter(
        subgroup__group__section=section
        ).filter(subgroup__group=group).filter(subgroup=subgroup)

    cards = {
        'data': [{'card': card.title} for card in sorted_cards]
    }

    return JsonResponse(cards, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def detail_information_card_api(request, card_id):
    card = get_object_or_404(Card, id=card_id)
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
        
        if product.diametr not in detail_information['diameters']:
            detail_information['diameters'].append(product.diametr)
        
        if product.length not in detail_information['length']:
            detail_information['length'].append(product.length)
        
        if product.color not in detail_information['colors']:
            detail_information['colors'].append(product.color)
        
        if product.image and not detail_information['image']:
            detail_information['image'] = product.image.url
    
    return JsonResponse(detail_information, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def products_list_api(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    products = {
        'products':[{
            'title': product.title,
            'descriton': product.description,
            'scope_of_application': product.scope_of_application,
            'diametr': product.diametr,
            'length': product.length,
            'color': product.color,
            'image': product.image.url if product.image else ''
        } for product in card.products.all()]}

    return JsonResponse(products, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })
