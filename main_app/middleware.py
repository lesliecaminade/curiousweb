from django.contrib.sessions.models import Session

class OnlyOneUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(request.session.keys())
        # for key in request.session.keys():
        #     print(request.session[key])

        #print(dir(request.session))
        print(request.session._session_key)

        if request.user.is_authenticated:
            cur_session_key = request.user.session_key
            if cur_session_key and cur_session_key != request.session._session_key:
                # Default handling... kick the old session...
                try:
                    s = Session.objects.get(session_key=cur_session_key)
                    s.delete()
                except:
                    pass
            if not cur_session_key or cur_session_key != request.session._session_key:
                p = request.user
                p.session_key = request.session._session_key
                p.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
