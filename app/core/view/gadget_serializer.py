import random
from rest_framework import serializers
from django.utils.timezone import now
from core.models import gadgets, Status
from rest_framework import viewsets, status

class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = gadgets
        fields = ['id', 'name', 'status']  # Only the fields you specified

    def create(self, validated_data):
        # Automatically generate a unique codename and assign it to the `name` field
        validated_data['name'] = f"The {random.choice(['Nightingale', 'Kraken', 'Phoenix', 'Titan'])}"
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Handle decommission logic: if status is set to "Decommissioned"
        if validated_data.get('status') == Status.DECOMMISSIONED:
            pass
        return super().update(instance, validated_data)
    
class GadgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle Gadget inventory operations.
    """

    queryset = gadgets.objects.all()
    serializer_class = GadgetSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Override DELETE to mark gadgets as "Decommissioned" instead of removing them.
        """
        instance = self.get_object()
        instance.status = Status.DECOMMISSIONED
        instance.save()
        return Response(
            {'detail': 'Gadget marked as decommissioned.'}, status=status.HTTP_200_OK
        )
