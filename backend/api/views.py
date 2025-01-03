from venv import logger
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

def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user.username
    except User.DoesNotExist:
        return None
    
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

# def project_get(request):
#     projects = list(Project.objects.all().values())
#     return JsonResponse({'projects': projects})

def project_get(request):
    projects = Project.objects.all()
    project_list = []
    for project in projects:
        yarns= PatternYarn.objects.filter(pattern=project.pattern)
        yarn_info = [
            {
                'brand': yarn.yarn.brand,
                'colour': yarn.yarn.colour,
                'material': yarn.yarn.material,
            }
            for yarn in yarns
        ]
        project_info = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'pattern_id': project.pattern.id,
            'pattern': project.pattern.title,
            'user_id': project.user.id,
            'user': project.user.username,
            'date_started': project.date_started,
            'finished': project.finished,
            'date_finished': project.date_finished,
            'notes': project.notes,
            # 'yarn_ids': yarn_ids,
            'yarns': yarn_info

        }
        project_list.append(project_info)
    return JsonResponse({'projects': project_list})


def project_post(request):
    if request.method == 'POST':
        logger.debug(f"Request body: {request.body}")
        data = json.loads(request.body)
        user = get_object_or_404(User, id=data['user'])
        pattern = get_object_or_404(Pattern, id=data['pattern'])
        project_obj = Project.objects.create(
            title=data['title'],
            description=data['description'],
            pattern=pattern,
            user=user,
            date_started=data.get('date_started'),
            finished=data.get('finished'),
            date_finished=data.get('date_finished'),
            notes=data.get('notes', '')
        )

        pattern_yarns = PatternYarn.objects.filter(pattern=pattern)
        for pattern_yarn in pattern_yarns:
            PatternYarn.objects.create(
                pattern=pattern,
                yarn=pattern_yarn.yarn,
                quantity=pattern_yarn.quantity
            )

        project_obj.save()
        return JsonResponse({'message': 'Project created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def project_put(request, id):
    if request.method == 'PUT':
        try:
            project_obj = Project.objects.get(id=id)
            data = json.loads(request.body)
            user = get_object_or_404(User, id=data['user_id'])
            pattern = get_object_or_404(Pattern, id=data['pattern_id'])
            project_obj.title = data.get('title', project_obj.title)
            project_obj.description = data.get('description', project_obj.description)
            project_obj.pattern = pattern
            project_obj.user = user
            project_obj.date_started = data.get('date_started', project_obj.date_started)
            project_obj.finished = data.get('finished', project_obj.finished)
            project_obj.date_finished = data.get('date_finished', project_obj.date_finished)
            project_obj.notes = data.get('notes', project_obj.notes)
            project_obj.save()
            logger.debug(f"Project updated: {project_obj}")
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
    
def get_yarn_by_id(yarn_id):
    try:
        yarn = Yarn.objects.get(id=yarn_id)
        return {
            'brand': yarn.brand,
            'colour': yarn.colour,
            'material': yarn.material,
            'weight': yarn.weight,
        }
    except Yarn.DoesNotExist:
        return None

def get_pattern_by_id(pattern_id):
    try:
        pattern = Pattern.objects.get(id=pattern_id)
        return {
            'title': pattern.title,
            'link': pattern.link
        }
    except Pattern.DoesNotExist:
        return None
    
def patternyarn_get(request):
    try:
        patternyarns = PatternYarn.objects.all()
        patternyarn_list = []
        for patternyarn in patternyarns:
            # Get the yarn name
            yarn_name = f"{patternyarn.yarn.brand} {patternyarn.yarn.colour} {patternyarn.yarn.material}"
            
            # Construct the patternyarn information
            patternyarn_info = {
                'id': patternyarn.id,
                'pattern_id': patternyarn.pattern.id,
                'pattern': patternyarn.pattern.title,
                'yarn_id': patternyarn.yarn.id,
                'yarn': yarn_name, 
                'quantity': patternyarn.quantity
            }
            patternyarn_list.append(patternyarn_info)
        return JsonResponse({'patternyarns': patternyarn_list})
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': str(e)}, status=500)

def patternyarn_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pattern_id= data.get('pattern')
        yarn_id= data.get('yarn')
        quantity= data.get('quantity')

        pattern= get_object_or_404(Pattern, id=pattern_id)
        yarn= get_object_or_404(Yarn, id=yarn_id)

        patternyarn_obj = PatternYarn.objects.create(
            pattern=pattern,
            yarn=yarn,
            quantity=quantity
        )
        logger.debug(f"PatternYarn created: {patternyarn_obj}")
        return JsonResponse({'message': 'PatternYarn created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def patternyarn_put(request, id):
    if request.method == 'PUT':
        try:
            patternyarn_obj = PatternYarn.objects.get(id=id)
            data = json.loads(request.body)
            pattern_id = data.get('pattern_id')
            yarn_id = data.get('yarn_id')
            quantity = data.get('quantity')

            if not all([pattern_id, yarn_id, quantity]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)


            pattern = get_object_or_404(Pattern, id=pattern_id)
            yarn = get_object_or_404(Yarn, id=yarn_id)

            patternyarn_obj.pattern = pattern
            patternyarn_obj.yarn = yarn
            patternyarn_obj.quantity = quantity
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
