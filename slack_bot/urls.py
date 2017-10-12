from django.conf.urls import url

from cse_slack_bot import settings
from slack_bot import views
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^index', views.SlackResponseView.as_view(), name="slack-response"),
                url(r'^fill_db', views.DatabaseUpdateView.as_view(), name="db_extractor")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
