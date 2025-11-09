from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    #get all drinks
    #serialize them
    #return json
    drink = Drink.objects.all()
    serializer = DrinkSerializer(drink , many = True)
    return JsonResponse(serializer.data , safe = False)
    