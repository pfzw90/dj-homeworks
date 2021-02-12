from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_option = request.GET.get('sort')
    if not sort_option:
        sort_option = 'name'

    context = {'sort_option': sort_option,
               'phones': [phone for phone in Phone.objects.order_by(sort_option)],
               'reversed': request.GET.get('reversed')
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first()}
    return render(request, template, context)
