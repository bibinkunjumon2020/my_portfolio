from django.views.generic import TemplateView
class HomePageView(TemplateView):
    #template_name = "home/homepage.html"
    template_name = "home/pages/about_me.html"


class AboutUsView(TemplateView):
    template_name = "home/pages/about_me.html"

class AuthorView(TemplateView):
    template_name = "home/pages/about_me.html"

class ContactUsView(TemplateView):
    template_name = "home/pages/about_me.html"
