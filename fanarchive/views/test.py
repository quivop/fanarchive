from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'fanarchive/test.html' # noqa

    def get_context_data(self):
        context = {
            "head1": "my first header",
            "head2": "My second header",
            "head3": "My THIRD header",
            "head4": "My fourth header...",
            "head5": "mah fifth! header",
            "head6": "my sixth header, uwu",
        }
        return context
