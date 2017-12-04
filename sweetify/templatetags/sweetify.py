from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def sweetify(context):
    opts = context.request.session.pop('sweetify', None)
    if not opts:
        return ''

    return mark_safe("""
<script>
swal({})
</script>
""".format(opts))
