from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Yarn
from .models import Pattern
from .models import User
from .models import Project
from .models import PatternYarn
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
    if request.method == 'PUT':
        return yarn_put(request)
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

def yarn_delete(request, id):
    if request.method == 'DELETE':
        try:
            yarn = Yarn.objects.get(id=id)
            yarn.delete()
            return JsonResponse({"message": "Yarn deleted successfully"})
        except Yarn.DoesNotExist:
            return JsonResponse({"error": "Yarn not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=405)

 # Pattern API view
def pattern_api_view(request):
    if request.method == 'GET':
        return pattern_get(request)
    if request.method == 'POST':
        return pattern_post(request)

def pattern_get(request):
    patterns = list(Pattern.objects.all().values())
    return JsonResponse({'patterns': patterns})

def pattern_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pattern_obj = Pattern.objects.create(
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
            pattern_obj = Pattern.objects.get(id=id)
            data = json.loads(request.body)
            pattern_obj.title = data.get('title', pattern_obj.title)
            pattern_obj.description = data.get('description', pattern_obj.description)
            pattern_obj.published = data.get('published', pattern_obj.published)
            pattern_obj.link = data.get('link', pattern_obj.link)
            pattern_obj.transcript = data.get('transcript', pattern_obj.transcript)
            pattern_obj.save()
            return JsonResponse({'message': 'Pattern updated successfully'})
        except Pattern.DoesNotExist:
            return JsonResponse({'error': 'Pattern not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def pattern_delete(request, id):
    if request.method=='DELETE':
        pattern= Pattern.objects.get(id=id)
        pattern.delete()
        return JsonResponse({"message": "Pattern deleted succesfully"})
    return JsonResponse({"error": "Invalid"}, status=405)

# User API view
def user_api_view(request):
    if request.method == 'GET':
        return user_get(request)
    if request.method == 'POST':
        return user_post(request)

def user_get(request):
    users = list(User.objects.all().values())
    return JsonResponse({'users': users})

def user_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_obj = User.objects.create(
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
            user_obj = User.objects.get(id=id)
            data = json.loads(request.body)
            user_obj.username = data.get('username', user_obj.username)
            user_obj.email = data.get('email', user_obj.email)
            user_obj.password = data.get('password', user_obj.password)
            user_obj.save()
            return JsonResponse({'message': 'User updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def user_delete(request, id):
    if request.method=='DELETE':
        user= User.objects.get(id=id)
        user.delete()
        return JsonResponse({"message": "User deleted succesfully"})
    return JsonResponse({"error": "Invalid"}, status=405)

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
    projects = list(Project.objects.all().values())
    return JsonResponse({'projects': projects})

def project_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_obj = Project.objects.create(
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
            project_obj = Project.objects.get(id=id)
            data = json.loads(request.body)
            project_obj.name = data.get('name', project_obj.name)
            project_obj.description = data.get('description', project_obj.description)
            project_obj.status = data.get('status', project_obj.status)
            project_obj.user_id = data.get('user_id', project_obj.user_id)
            project_obj.save()
            return JsonResponse({'message': 'Project updated successfully'})
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def project_delete(request, id):
    if request.method=='DELETE':
        project= Project.objects.get(id=id)
        project.delete()
        return JsonResponse({"message": "Project deleted succesfully"})
    return JsonResponse({"error": "Invalid"}, status=405)

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
    patternyarns = list(PatternYarn.objects.all().values())
    return JsonResponse({'patternyarns': patternyarns})

def patternyarn_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        patternyarn_obj = PatternYarn.objects.create(
            pattern_id=data['pattern_id'],
            yarn_id=data['yarn_id']
        )
        return JsonResponse({'message': 'PatternYarn created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def patternyarn_put(request, id):
    if request.method == 'PUT':
        try:
            patternyarn_obj = PatternYarn.objects.get(id=id)
            data = json.loads(request.body)
            patternyarn_obj.pattern_id = data.get('pattern_id', patternyarn_obj.pattern_id)
            patternyarn_obj.yarn_id = data.get('yarn_id', patternyarn_obj.yarn_id)
            patternyarn_obj.save()
            return JsonResponse({'message': 'PatternYarn updated successfully'})
        except PatternYarn.DoesNotExist:
            return JsonResponse({'error': 'PatternYarn not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def patternyarn_delete(request, id):
    if request.method=='DELETE':
        patternyarn= PatternYarn.objects.get(id=id)
        patternyarn.delete()
        return JsonResponse({"message": "PatternYarn deleted succesfully"})
    return JsonResponse({"error": "Invalid"}, status=405)
