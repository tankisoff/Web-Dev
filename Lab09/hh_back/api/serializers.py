# from rest_framework import serializers
#
# from api.models import Company, Vacancy
#
#
# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(max_length=1000)
#     city = serializers.CharField()
#     address = serializers.CharField()
#
#     def create(self, validated_data):
#         instance = Company(
#             name=validated_data.get('name'),
#             description=validated_data.get('description'),
#             city=validated_data.get('city'),
#             address=validated_data.get('address'))
#         instance.save()
#         return instance
#
#
# class VacancySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(max_length=1000)
#     salary = serializers.FloatField()
#     company_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         instance = Vacancy(
#             name=validated_data.get('name'),
#             description=validated_data.get('description'),
#             salary=validated_data.get('salary'),
#             company_id=validated_data.get('company_id'))
#         instance.save()
#         return instance


from rest_framework import serializers

from api.models import Company, Vacancy



class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(max_length=1000)
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        instance = Company(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            city=validated_data.get('city'),
            address=validated_data.get('address'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.city = validated_data.get("city")
        instance.address = validated_data.get("address")
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField(max_length=1000)
    city = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Company
        fields = ("id", "name", "description", "city", "address")


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(max_length=1000)
    salary = serializers.IntegerField()
    company_id = serializers.IntegerField()

    def create(self, validated_data):
        instance = Company(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            salary=validated_data.get('salary'),
            company_id=validated_data.get('company_id'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.salary = validated_data.get("salary")
        instance.company_id = validated_data.get("company_id")
        instance.save()
        return instance


class VacancySerializer2(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField(max_length=1000)
    salary = serializers.IntegerField()
    company_id = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ("id", "name", "description", "city", "address")