from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from core.models import URLInfo


class ShorterIRLSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=250, min_length=None, allow_blank=False, label=_('URL'), help_text=_('URL'))

