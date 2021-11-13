from .models import Region


def get_regions(request):
    regions = Region.objects.filter(parent__isnull=True)
    return {'regions': regions}