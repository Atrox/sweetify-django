from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def sweetify(context):
    opts = context.request.session.pop('sweetify', None)
    if not opts:
        return ''

    if getattr(settings, 'SWEETIFY_SWEETALERT_LIBRARY', 'sweetalert2') == 'sweetalert2':
        script = 'Swal.fire({})'.format(opts)
    else:
        script = 'swal({})'.format(opts)

    return mark_safe("""
<script>
{}
</script>
""".format(script))
