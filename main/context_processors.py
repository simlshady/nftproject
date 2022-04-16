from .models import CopyLink


def my_copy_links(request):
    return {
        'copy_link': CopyLink.objects.first()
    }