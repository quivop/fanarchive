from django.http import HttpResponse
import os
from archive.settings import BASE_DIR


def TestView(request):
    template_name = 'test' # noqa
    base_url = BASE_DIR
    static_url = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles/'))
    debug = format(os.getenv("DEBUG"))
    p = "<p></p>"

    return HttpResponse(base_url + p + static_url + p + debug)
