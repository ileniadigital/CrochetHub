from django.shortcuts import render
from django.http import JsonResponse
from .models import Yarn as yarn
from .models import Pattern as pattern


def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

# Yarns API view
def yarns_api_view(request):
    yarns = list(yarn.objects.all().values())
    print(yarns)
    return JsonResponse({'yarns': yarns})

# Patterns API view
def patterns_api_view(request):
    patterns = list(pattern.objects.all().values())
    print(patterns)
    return JsonResponse({'patterns': patterns})