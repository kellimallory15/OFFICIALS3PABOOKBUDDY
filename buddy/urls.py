from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', views.getUser, name='home'),
    path('api-auth', include('rest_framework.urls')),
    path('api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/books/', views.book_list, name='book-list'),
    path('api/books/<int:pk>/', views.getBook, name='book-detail'),
    path('api/authors/', views.author_list, name='author-list'),
    path('api/authors/<int:pk>/', views.getAuthor, name='author-detail'),
    path('api/reviews/', views.review_list, name='review-list'),
    path('api/reviews/<int:pk>/', views.getReview, name='review-detail'),
    path('api/book-buddies/', views.book_buddy_list, name='book-buddy-list'),
    path('api/book-buddies/<int:pk>/', views.getBookBuddy, name='book-buddy-detail'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/user/', views.getUser, name='user-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)