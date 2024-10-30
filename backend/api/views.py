from django.shortcuts import render
from django.http import JsonResponse
from .models import Yarn
from .models import Pattern as pattern
from .models import User as user
from .models import Project as project
from .models import PatternYarn as patternyarn

def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

# Yarn API view
def yarns_api_view(request):
    if request.method == 'GET':
        return yarns_get(request)
    if request.method == 'DELETE':
        return yarns_delete(request)

def yarns_get(request):
    yarns = list(Yarn.objects.all().values())
    return JsonResponse({'yarns': yarns})

def yarns_delete(request):
    if request.method == 'DELETE':
        yarn_id = request.GET.get('id')
        if not yarn_id:
            return JsonResponse({'error': 'No yarn id provided'}, status=400)
        try:
            yarn = Yarn.objects.get(id=yarn_id)
            yarn.delete()
            return JsonResponse({'message': 'Yarn deleted successfully'})
        except Yarn.DoesNotExist:
            return JsonResponse({'error': 'Yarn not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Patterns API view
def patterns_api_view(request):
    patterns = list(pattern.objects.all().values())
    return JsonResponse({'patterns': patterns})

# PatternYarns API view
def patternyarns_api_view(request):
    patternyarns = list(patternyarn.objects.all().values())
    return JsonResponse({'patternyarns': patternyarns})
# Users API view
def users_api_view(request):
    users = list(user.objects.all().values())
    return JsonResponse({'users': users})

# Projects API view
def projects_api_view(request):
    projects = list(project.objects.all().values())
    return JsonResponse({'projects': projects})
