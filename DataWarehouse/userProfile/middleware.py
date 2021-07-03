from django.utils import timezone
import pytz
from .models import UserProfile
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

MAX_REQUEST_URL = 500


def get_request_path(string):
    return str(string).split("'")[-2]


class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and 'jsi18n' not in request.path:
            userProfile, created = UserProfile.objects.get_or_create(user_id=request.user.id)
            userProfile.last_request_time = timezone.now()
            last_last_text = userProfile.last_request_text.split('\n')

            if len(last_last_text) > MAX_REQUEST_URL:
                last_last_text = last_last_text[-MAX_REQUEST_URL:]
            url_path = get_request_path(request.build_absolute_uri)
            req_time = timezone.now().strftime("%Y/%M/%d %H:%m:%S")
            line = f'{req_time} {request.method} {url_path}'
            last_last_text.append(line)
            userProfile.last_request_text = '\n'.join(last_last_text)
            userProfile.save()
