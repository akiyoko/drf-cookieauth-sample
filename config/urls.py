from django.contrib import admin
from django.urls import path, include  # 修正
from django.views.generic import TemplateView  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # 追加
    path('api-auth/', include('rest_framework.urls')),                         # 追加
    path('api/v1/', include('apiv1.urls')),                                    # 追加
]
