from rest_framework import seralizers
from .models import Drink

class DrinkSerializer(seralizers.ModelSerializer):
    class meta:
        models = Drink
        fields = ['id', 'name', 'description']