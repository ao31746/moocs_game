from rest_framework import serializers
from games.models import ROFR_model, JUDO_model,Company_Merger_model,Price_War_model


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

class Company_Merger_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Merger_model
        # fields = '__all__'
        fields = ('company_value', 'input_price', 'profit')

class Price_War_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Price_War_model
        # fields = '__all__'
        fields = ('round1_input_price', 'round1_profit', 'round1_quantity', 'round2_input_price', 'round2_profit', 'round2_quantity', 'round3_input_price', 'round3_profit', 'round3_quantity')
