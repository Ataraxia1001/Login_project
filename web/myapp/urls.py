from django.urls import path, include
from .views.home_views import home
from .views.about_views import about
from .views.progress_views import progressing
from .views.visualization_views import visualization
from .views.recommend_views import recommend, recommend_02, recommend_03 
from .views.progress_write_views import progress_view
from .views.register_login import login_view, register, logout_view
from django.conf import settings
from django.conf.urls.static import static
from django_plotly_dash.views import add_to_session
from django.views.generic import TemplateView
from .views.visualization_views import map
from .views.visualization_views import map_01, map_02, map_03, map_04
from .views.visualization_views import gangnam_sankey


#  앱의 URL 패턴을 정의하는 파일, URL 요청을 뷰 함수와 연결하는 역할을 함

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('progress/', progressing, name='progress'),
    path('progress/write', progress_view, name='progress_write'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('visualization/', visualization, name='visualization'),
    path('recommend/', recommend, name='recommend'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('map/', map, name='map'),
    path('map_01/', map_01, name='map_01'),
    path('map_02/', map_02, name='map_02'),
    path('map_03/', map_03, name='map_03'),    
    path('map_04/', map_04, name='map_04'),    
    path('sankey_01/', gangnam_sankey, name='sankey_01'),
    path('recommend_02/', recommend_02, name='recommend_02'),
    path('recommend_03/', recommend_03, name='recommend_03'),
    

    # path('BusStations/_dash-update-component', add_to_session, name='session_state'),
    # path('BusStations/', TemplateView.as_view(template_name='BusStations.html'), name="BusStations"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)