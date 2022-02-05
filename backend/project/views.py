from django.shortcuts import render

from apps.order.models import Order


def index(request):

    context = {}

    owner = request.user

    if owner.is_authenticated:

        context["pending_count"] = Order.objects.filter(
            status=0, owner=owner).count()
        context["accepted_count"] = Order.objects.filter(
            status=1, owner=owner).count()
        context["rejected_count"] = Order.objects.filter(
            status=2, owner=owner).count()

    return render(request, "index.html", context)
