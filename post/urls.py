from django.urls import path
from .models import Article
from .views import all_post, post_details  # Import the views

urlpatterns = [
    path('', all_post, name="all_post"),
    path('post/<int:id>/', post_details, name="post_detail"),  # Corrected the view name
    # Other URL patterns...
]
# ]
# urlpatterns = [
#     path('', include('post.urls')),
#     path('admin'/, admin.site.urls),
# ]

def all_post(request):
    posts = Post.objects.all()
    return render(request, 'post/all_post.html', {'posts': posts})


def post_details(request, id):
    post = get_object_or_404(article, id=id)

    return render(request, 'post/post_details.html')
