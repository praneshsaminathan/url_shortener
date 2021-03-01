from django.db import models
from django.utils.translation import ugettext_lazy as _


class URLInfo(models.Model):
    full_url = models.URLField(unique=True, null=False, blank=False, help_text=_('full url'))
    url_hash = models.URLField(unique=True, null=False, blank=False, help_text=_('short url'))
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url_hash} - {self.full_url} - {self.clicks}'

    class Meta:
        db_table = 'urlinfo'
        verbose_name = _('UrlInfo')
        verbose_name_plural = _('UrlInfo')
