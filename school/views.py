from django.http import HttpResponse
from .models import School
from django.core.serializers import serialize
# from .serializers import SchoolSerializer

def get_all_schools(request):
    school = School.objects.all()
    # serializer = SchoolSerializer(school, many=True)
    return HttpResponse(" dddd"+serialize('json', school))