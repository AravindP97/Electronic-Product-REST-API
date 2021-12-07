def verify_user(request):
     token = request.COOKIES.get('authorization')
     if not token:
          return None
     else:
          return True
