from django.db import models

# Create your models here.

class ROFR_model(models.Model):
    CBS_price_1 = models.TextField(default="0")
    CBS_price_2 = models.TextField(default="0")
    NBC_price_1 = models.TextField(default="0")
    NBC_price_2 = models.TextField(default="0")
    round_1_step_1 = models.TextField(default="0")
    round_1_step_2 = models.TextField(default="0")
    round_2_step_1 = models.TextField(default="0")
    round_2_step_2 = models.TextField(default="0")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "game_ROFR"

class JUDO_model(models.Model):
    price = models.TextField(default="0")
    quantity = models.TextField(default="0")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "game_JUDO"

class Company_Merger_model(models.Model):
    company_value = models.TextField(default="0")
    input_price = models.TextField(default="0")
    profit = models.TextField(default="0")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "game_Company_Merger"

class Price_War_model(models.Model):
    round1_input_price = models.TextField(default="0")
    round1_profit = models.TextField(default="0")
    round1_quantity = models.TextField(default="0")
    round2_input_price = models.TextField(default="0")
    round2_profit = models.TextField(default="0")
    round2_quantity = models.TextField(default="0")
    round3_input_price = models.TextField(default="0")
    round3_profit = models.TextField(default="0")
    round3_quantity = models.TextField(default="0")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "game_Price_War"