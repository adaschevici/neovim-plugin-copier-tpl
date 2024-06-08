from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        new_context = {}
        new_context["say"] = "hello " + context["name"]
        return new_context
