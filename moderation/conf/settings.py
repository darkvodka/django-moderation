from __future__ import unicode_literals

import warnings

from django.conf import settings


MODERATORS = getattr(settings, "DJANGO_MODERATION_MODERATORS", ())
if MODERATORS:
    warnings.warn(
        "`%s` is deprecated, use `%s` instead." %
        ("DJANGO_MODERATION_MODERATORS", "MODERATION_MODERATORS"),
        self.deprecation_warning, 2)
MODERATORS = getattr(settings, "MODERATION_MODERATORS", ())

AUTODISCOVER = getattr(settings, "MODERATION_AUTODISCOVER", False)

SOUTH_MIGRATION_MODULES = getattr(settings, "SOUTH_MIGRATION_MODULES", {})
SOUTH_MIGRATION_MODULES['moderation'] = 'moderation.migrations-pre17'
