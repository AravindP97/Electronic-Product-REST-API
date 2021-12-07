from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Producttable, Laptoptable, Mobiletable
from rest_framework.response import Response


class MobiletableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiletable
        fields = ('id', 'screen_size', 'color')


class LaptoptableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptoptable
        fields = ('id', 'hd_capacity')


class ProducttableSerializer(serializers.ModelSerializer):
    laptop = LaptoptableSerializer()
    mobile = MobiletableSerializer()

    class Meta:
        model = Producttable
        fields = ('id', 'name', 'description', 'category','processor', 'ram', 'laptop', 'mobile')
        depth = 3
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'category': {'required': True},
            'processor': {'required': True},
            'ram': {'required': True},
        }

    def validate(self, data):
        if data['name'] and data['description'] and data['category'] and data['processor'] and data['ram']:
            if data['category'] == 'L':
                lap_data = data['laptop']
                if lap_data['hd_capacity']:
                    return data
                else:
                    raise ValidationError('You have select the product Laptop. Please select the HD Capacity')
            elif data['category'] == 'M':
                mobile_data = data['mobile']
                if mobile_data['screen_size'] and mobile_data['color']:
                    return data
                else:
                    raise ValidationError('You have select the product Mobile. Please select the Screen size and color')
        else:
            raise ValidationError('Json Parse mismatched')

    def create(self, validated_data):
        name = self.data['name']
        description = self.data['description']
        category = self.data['category']
        processor = self.data['processor']
        ram = self.data['ram']
        hd_capacity = self.data['laptop']['hd_capacity']
        screen_size = self.data['mobile']['screen_size']
        color = self.data['mobile']['color']
        if category == 'L':
            screen_size = ''
            color = ''
        else:
            hd_capacity = ''
        laptop = Laptoptable(
            hd_capacity=hd_capacity
        )
        laptop.save()
        laptop_obj = Laptoptable.objects.get(id=laptop.id)

        mobile = Mobiletable(
            screen_size=screen_size,
            color = color
        )
        mobile.save()
        mobile_obj = Mobiletable.objects.get(id=mobile.id)
        Producttable(
            name=name,
            description=description,
            category=category,
            processor= processor,
            ram = ram,
            laptop=laptop_obj,
            mobile=mobile_obj
        ).save()
        response_data = {
            'message': 'Product Saved Successfully'
        }
        return Response(response_data)
    
    def update(self,*args, **kwargs):
        data = self.data
        for arg in args:
            if type(arg) == dict:
                name = arg['name']
                description = arg['description']
                processor = arg['processor']
                ram = arg['ram']
                category = arg['category']
                hd_capacity = arg['laptop']['hd_capacity']
                screen_size = arg['mobile']['screen_size']
                color = arg['mobile']['color']
                if category == 'L':
                    screen_size = ''
                    color = ''
                else:
                    hd_capacity = ''
            else:
                continue
            
        Laptoptable(
            hd_capacity=hd_capacity,
            id=data['laptop']['id']
        ).save()
        laptop_obj = Laptoptable.objects.get(id=data['laptop']['id'])
        Mobiletable(
            screen_size=screen_size,
            color=color,
            id=data['mobile']['id']
        ).save()
        mobile_obj = Mobiletable.objects.get(id=data['mobile']['id'])
        Producttable(
            name=name,
            description=description,
            category=category,
            processor=processor,
            ram=ram,
            laptop=laptop_obj,
            mobile=mobile_obj,
            id=data['id']
        ).save()
        response_data = {
            'message': 'Product Updated Successfully'
        }
        return Response(response_data)

