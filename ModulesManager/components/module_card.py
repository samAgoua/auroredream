from django_unicorn.components import UnicornView
from ..models import UserModule, Modules, EventModule
from Event.models import Evenement as Event


class ModuleCardView(UnicornView):
    modules : list = []
    event = None

    def mount(self):
        self.event = self.component_kwargs.get("event", None)
        self.modules = Modules.objects.all()
    

    def add_event_module(self, module_id):
        module = Modules.objects.get(id=module_id)
        event_module = EventModule(event=self.event, module=module)
        event_module.save()
    
    def remove_event_module(self, module_id):
        module = Modules.objects.get(id=module_id)
        event_module = EventModule.objects.get(event=self.event, module=module)
        event_module.delete()
