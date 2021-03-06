from django.views.generic import TemplateView
from django.urls import reverse
from django.conf import settings

# Home
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'app_name': settings.APP_NAME,
            'app_description': settings.APP_DESCRIPTION,
            'form_url': reverse('create_user')
        })
        if not settings.DEBUG:
            context.update({'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID})
        return context