from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_shipment_email(owner_email, order_name, owner_name):
    """
    Sends a shipment email to the owner of an order.

    Parameters:
        owner_email (str): The email address of the owner.
        order_name (str): The name of the order.
        owner_name (str): The name of the owner.

    Returns:
        None
    """
    subject = f"Your shipment from {owner_name} {order_name}"
    message = f"Hi {owner_name},\n\nYour shipment from {owner_name} {order_name} has been delivered."
    email = EmailMessage(subject, message, to=[owner_email])
    email.send()