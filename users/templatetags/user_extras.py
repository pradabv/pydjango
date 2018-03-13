from django import template

register = template.Library()

@register.filter(name='is_room_occupied')
def is_room_occupied(arg):
    if arg > 5:
        return True
    else:
        return False