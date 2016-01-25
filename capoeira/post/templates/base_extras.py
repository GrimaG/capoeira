from django import template
register = template.Library()

@register.inclusion_tag('post/base.html')
def show_menu(menu):
    menu = Menu.objects.all()
    return {'menu': menu}
