from django.contrib.auth.models import Group
from .models import user, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields=['url', 'username', 'groups', 'age']


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields= ['url', 'name']


class SnippetSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=255)
    code= serializers.CharField(style={'base_template': 'textarea.html'})
    lineos= serializers.BooleanField(required=False)
    language= serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices = STYLE_CHOICES, default='friendlly')


    def create(self, data):
        return Snippet.objects.create(**data)

    def update(self, inst, data):
        inst.title= data.get('title', inst.title)
        inst.code= data.get('code', inst.code)
        inst.lineos= data.get('lineos', inst.lineos)
        inst.language= data.get('language', inst.language)
        inst.style= data.get('style', inst.style)
        inst.save()

        return inst
    


class Modelserializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'lineos', 'language', 'style']