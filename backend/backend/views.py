import jwt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

JWT_SECRET_KEY = "0cf9440fb9cac02a2af17ba1a40c54acd41cbe0ff959101cdc76f94b07c000e4"

@csrf_exempt
def test(request):
    token = request.GET.get('token')
    
    
    # Convert the token to bytes before passing it to jwt.decode
    token_bytes = token.encode('utf-8')  # Assuming the token is a string
    
    try:
        decod = jwt.decode(token_bytes, JWT_SECRET_KEY, algorithms=['HS256'])
        print(decod)
        return HttpResponse("Hello, world. You're at the polls index.")
    except jwt.ExpiredSignatureError:
        return HttpResponse("JWT token has expired", status=401)  # Unauthorized
    except jwt.DecodeError:
        return HttpResponse("JWT token decode error", status=401)  # Unauthorized
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=401)  # Unauthorized
