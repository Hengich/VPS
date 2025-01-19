from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import VPS
from .serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram', 'hdd', 'status']

    @action(detail=True, methods=['patch'])
    def change_status(self, request, pk=None):
        vps = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(VPS.STATUS_CHOICES):
            return Response(
                {"error": "Неверный статус."},
                status=status.HTTP_400_BAD_REQUEST
            )
        vps.status = new_status
        vps.save()
        return Response({"status": "Успешно обновлён."})
