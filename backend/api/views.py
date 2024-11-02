from django.shortcuts import render
from django.http import JsonResponse
from .models import Yarn
from .models import Pattern as pattern
from .models import User as user
from .models import Project as project
from .models import PatternYarn as patternyarn
import json

def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

# Yarn API view
def yarn_api_view(request):
    if request.method == 'GET':
        return yarn_get(request)
    if request.method == 'POST':
        return yarn_post(request)
    if request.method == 'DELETE':
        return yarn_delete(request)

def yarn_get(request):
    yarns = list(Yarn.objects.all().values())
    return JsonResponse({'yarns': yarns})

def yarn_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        yarn = Yarn.objects.create(
            brand=data['brand'],
            weight=data['weight'],
            colour=data['colour'],
            material=data['material'],
            price=data['price'],
            yardage=data['yardage'],
            hook_size=data['hook_size']
        )
        return JsonResponse({'message': 'Yarn created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def yarn_put(request,id):
    if request.method == 'PUT':
        try:
            yarn = Yarn.objects.get(id=id)
            data= json.loads(request.body)
            yarn.brand = data.get('brand', yarn.brand)
            yarn.weight = data.get('weight', yarn.weight)
            yarn.colour = data.get('colour', yarn.colour)
            yarn.material = data.get('material', yarn.material)
            yarn.price = data.get('price', yarn.price)
            yarn.yardage = data.get('yardage', yarn.yardage)
            yarn.hook_size = data.get('hook_size', yarn.hook_size)
            yarn.save()
            return JsonResponse({'message': 'Yarn updated successfully'})
        except Yarn.DoesNotExist:
            return JsonResponse({'error': 'Yarn not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def yarn_delete(request):
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

 # Pattern API view
def pattern_api_view(request):
    if request.method == 'GET':
        return pattern_get(request)
    if request.method == 'POST':
        return pattern_post(request)
    if request.method == 'DELETE':
        return pattern_delete(request)

def pattern_get(request):
    patterns = list(pattern.objects.all().values())
    return JsonResponse({'patterns': patterns})

def pattern_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pattern_obj = pattern.objects.create(
            title=data['title'],
            description=data['description'],
            published=data['published'],
            link=data['link'],
            transcript=data['transcript']
        )
        return JsonResponse({'message': 'Pattern created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def pattern_put(request, id):
    if request.method == 'PUT':
        try:
            pattern_obj = pattern.objects.get(id=id)
            data = json.loads(request.body)
            pattern_obj.title = data.get('title', pattern_obj.title)
            pattern_obj.description = data.get('description', pattern_obj.description)
            pattern_obj.published = data.get('published', pattern_obj.published)
            pattern_obj.link = data.get('link', pattern_obj.link)
            pattern_obj.transcript = data.get('transcript', pattern_obj.transcript)
            pattern_obj.save()
            return JsonResponse({'message': 'Pattern updated successfully'})
        except pattern.DoesNotExist:
            return JsonResponse({'error': 'Pattern not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def pattern_delete(request):
    if request.method == 'DELETE':
        pattern_id = request.GET.get('id')
        if not pattern_id:
            return JsonResponse({'error': 'No pattern id provided'}, status=400)
        try:
            pattern_obj = pattern.objects.get(id=pattern_id)
            pattern_obj.delete()
            return JsonResponse({'message': 'Pattern deleted successfully'})
        except pattern.DoesNotExist:
            return JsonResponse({'error': 'Pattern not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# User API view
def user_api_view(request):
    if request.method == 'GET':
        return user_get(request)
    if request.method == 'POST':
        return user_post(request)
    if request.method == 'PUT':
        return user_put(request)
    if request.method == 'DELETE':
        return user_delete(request)

def user_get(request):
    users = list(user.objects.all().values())
    return JsonResponse({'users': users})

def user_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_obj = user.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def user_put(request, id):
    if request.method == 'PUT':
        try:
            user_obj = user.objects.get(id=id)
            data = json.loads(request.body)
            user_obj.username = data.get('username', user_obj.username)
            user_obj.email = data.get('email', user_obj.email)
            user_obj.password = data.get('password', user_obj.password)
            user_obj.save()
            return JsonResponse({'message': 'User updated successfully'})
        except user.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def user_delete(request):
    if request.method == 'DELETE':
        user_id = request.GET.get('id')
        if not user_id:
            return JsonResponse({'error': 'No user id provided'}, status=400)
        try:
            user_obj = user.objects.get(id=user_id)
            user_obj.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except user.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Project API view
def project_api_view(request):
    if request.method == 'GET':
        return project_get(request)
    if request.method == 'POST':
        return project_post(request)
    if request.method == 'PUT':
        return project_put(request)
    if request.method == 'DELETE':
        return project_delete(request)

def project_get(request):
    projects = list(project.objects.all().values())
    return JsonResponse({'projects': projects})

def project_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_obj = project.objects.create(
            name=data['name'],
            description=data['description'],
            status=data['status'],
            user_id=data['user_id']
        )
        return JsonResponse({'message': 'Project created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def project_put(request, id):
    if request.method == 'PUT':
        try:
            project_obj = project.objects.get(id=id)
            data = json.loads(request.body)
            project_obj.name = data.get('name', project_obj.name)
            project_obj.description = data.get('description', project_obj.description)
            project_obj.status = data.get('status', project_obj.status)
            project_obj.user_id = data.get('user_id', project_obj.user_id)
            project_obj.save()
            return JsonResponse({'message': 'Project updated successfully'})
        except project.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def project_delete(request):
    if request.method == 'DELETE':
        project_id = request.GET.get('id')
        if not project_id:
            return JsonResponse({'error': 'No project id provided'}, status=400)
        try:
            project_obj = project.objects.get(id=project_id)
            project_obj.delete()
            return JsonResponse({'message': 'Project deleted successfully'})
        except project.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# PatternYarn API view
def patternyarn_api_view(request):
    if request.method == 'GET':
        return patternyarn_get(request)
    if request.method == 'POST':
        return patternyarn_post(request)
    if request.method == 'PUT':
        return patternyarn_put(request)
    if request.method == 'DELETE':
        return patternyarn_delete(request)

def patternyarn_get(request):
    patternyarns = list(patternyarn.objects.all().values())
    return JsonResponse({'patternyarns': patternyarns})

def patternyarn_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        patternyarn_obj = patternyarn.objects.create(
            pattern_id=data['pattern_id'],
            yarn_id=data['yarn_id']
        )
        return JsonResponse({'message': 'PatternYarn created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def patternyarn_put(request, id):
    if request.method == 'PUT':
        try:
            patternyarn_obj = patternyarn.objects.get(id=id)
            data = json.loads(request.body)
            patternyarn_obj.pattern_id = data.get('pattern_id', patternyarn_obj.pattern_id)
            patternyarn_obj.yarn_id = data.get('yarn_id', patternyarn_obj.yarn_id)
            patternyarn_obj.save()
            return JsonResponse({'message': 'PatternYarn updated successfully'})
        except patternyarn.DoesNotExist:
            return JsonResponse({'error': 'PatternYarn not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def patternyarn_delete(request):
    if request.method == 'DELETE':
        patternyarn_id = request.GET.get('id')
        if not patternyarn_id:
            return JsonResponse({'error': 'No patternyarn id provided'}, status=400)
        try:
            patternyarn_obj = patternyarn.objects.get(id=patternyarn_id)
            patternyarn_obj.delete()
            return JsonResponse({'message': 'PatternYarn deleted successfully'})
        except patternyarn.DoesNotExist:
            return JsonResponse({'error': 'PatternYarn not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)