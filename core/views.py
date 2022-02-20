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
            'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
            'form_url': reverse('create_user')
        })
        return context