from django.contrib import admin
from django.urls import path
from yt.views import HomeView, NewVideo, CommentView, LoginView, RegisterView, VideoView, VideoFileView, LogoutView, CreateChannelView, ChannelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('video/<int:id>', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view()),
    path('createchannel', CreateChannelView.as_view()),
    path('<user>/channel', ChannelView.as_view())
]
