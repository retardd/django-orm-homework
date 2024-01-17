from django.shortcuts import render, redirect

from phones.models import Mobile


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")

    if sort == "max_price":
        phones_obj = Mobile.objects.all().order_by("-price")
    elif sort == "min_price":
        phones_obj = Mobile.objects.all().order_by("price")
    else:
        phones_obj = Mobile.objects.all().order_by("name")

    context = {"phones": phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Mobile.objects.filter(slug=slug)
    context = {"phone": phone[0]}
    return render(request, template, context)
