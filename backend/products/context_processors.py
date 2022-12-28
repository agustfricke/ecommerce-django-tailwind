from .models import Category
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

def menu_categorys(request):
    categorys = Category.objects.all()
    return {'menu_categorys':categorys}