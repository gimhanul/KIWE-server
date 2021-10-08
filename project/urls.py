"""project URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as user
from kiword import views as kiword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.index, name='index'),
    path('join/', user.join, name='join'),
    path('login/', user.userlogin, name='login'),
    path('kiwe/', user.kiwe, name='kiwe'),
    path('friends/', user.friends, name='friends'),
    path('memory/', kiword.memory, name='memory'),
    path('setting/', user.setting, name='setting'),
    path('q/<int:question_id>/', kiword.q, name='q'),
    path('keyword/', kiword.kiword, name='keyword'),
]
