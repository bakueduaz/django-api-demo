from django.http import JsonResponse, HttpResponseForbidden
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img

# Create the demo news object
demo_news = News("Demo News",
                 "This is a demo news item for testing purposes.",
                 "https://example.com/demo-image.png")

@method_decorator(csrf_exempt, name='dispatch')
class NewsView(View):
    def get(self, request):
        # Check for the API key
        api_key = request.GET.get('api_key')
        if api_key != settings.API_KEY:
            return HttpResponseForbidden("Invalid API key")

        # Return the demo news item
        news_data = {
            'tit': demo_news.tit,
            'des': demo_news.des,
            'img': demo_news.img
        }
        return JsonResponse({'news': news_data})
