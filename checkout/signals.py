from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

import logging

from allauth.account.signals import user_logged_in
from django.dispatch import receiver

logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def login_logger(request, user, **kwargs):
    logger.info("{} logged in with {}".format(user.email, request))

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
