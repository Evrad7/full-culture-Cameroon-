from vitrine.models import Company, Sector, Region


def get_global_context(request):
    context = {}
    try:
        company = Company.objects.first()
    except:
        company = None
    context["company"] = company
    context["sectors"] = Sector.objects.all()
    context["regions"] = Region.objects.all()

    return context
