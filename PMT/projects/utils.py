from projects.models import ApplicationRequest

def get_application_request_or_false(sender, receiver):
    try:
        return ApplicationRequest.object.get(sender=sender, receiver=receiver, is_active=True)
    except ApplicationRequest.DoesNotExist:
        return False

