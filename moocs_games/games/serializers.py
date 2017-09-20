from rest_framework import serializers
from games.models import ROFR_model, JUDO_model


class ROFR_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ROFR_model
        # fields = '__all__'
        fields = ('id', 'CBS_price_1', 'CBS_price_2', 'NBC_price_1', 'NBC_price_2', 'round_1_step_1', 'round_1_step_2', 'round_2_step_1', 'round_2_step_2', 'last_modify_date', 'created')


class JUDO_Serializer(serializers.ModelSerializer):
    class Meta:
        model = JUDO_model
        # fields = '__all__'
        fields = ('id', 'price', 'quantity', 'last_modify_date', 'created')
