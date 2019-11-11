from rest_framework_json_api.views import ModelViewSet
from rest_framework_json_api import serializers

from api.models import Example


class ExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Example
        fields = '__all__'


class ExampleViewSet(ModelViewSet):
    serializer_class = ExampleSerializer

    def get_queryset(self):
        using = self.request.query_params.get('using', 'default')
        return Example.objects.using(using).all()

