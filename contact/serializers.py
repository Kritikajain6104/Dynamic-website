from rest_framework import serializers
from contact.models import contact1

#contact serilizers
class contactserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=contact1
        fields="__all__"
