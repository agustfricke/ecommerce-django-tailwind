from .models import Category



def menu_categorys(request):
    categorys = Category.objects.all()
    return {'menu_categorys':categorys}