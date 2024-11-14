from ..models import Modules
from django import template

register = template.Library()

@register.filter(name='event_has_module')
def event_has_module(value,event_id) -> bool:
    
    if(isinstance(value,Modules)):
        return value.event_has_module(event_id)
    
    return False