from ThePaginator.models import Post
from django.views.generic.list_detail import object_list

def index(request):
    post = Post.objects.all().order_by('-timestamp')
    return object_list(request, template_name='home.html', queryset=post, paginate_by=5)
