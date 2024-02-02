from django.http import HttpResponse
from .models import School
from django.core.serializers import serialize
# from .serializers import SchoolSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def get_all_schools(request):
    school = School.objects.all()
    # serializer = SchoolSerializer(school, many=True)
    return HttpResponse(" dddd"+serialize('json', school))

@csrf_exempt
@require_POST
def add_school(request):
    data = json.loads(request.body)
    new_school = School.objects.create(**data)
    return HttpResponse("Done")