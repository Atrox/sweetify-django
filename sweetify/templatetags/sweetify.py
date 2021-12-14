from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def sweetify(context, nonce=None):
    opts = context.request.session.pop("sweetify", None)
    library = getattr(settings, "SWEETIFY_SWEETALERT_LIBRARY", "sweetalert2")

    if not opts:
        return ""

    if isinstance(opts, list):
        if library == "sweetalert":
            raise RuntimeError("multiple alerts are currently not supported in sweetalert")

        script = concatenate(opts)
    else:
        if library == "sweetalert2":
            script = "Swal.fire({})".format(opts)
        else:
            script = "swal({})".format(opts)

    if nonce:
        return mark_safe("""<script nonce='{}'>{}</script>""".format(nonce, script))
    else:
        return mark_safe("""<script>{}</script>""".format(script))


def concatenate(list):
    i = 0
    length = len(list)
    script = "Swal.fire({})"
    for opts in list:
        if i == 0:
            script = script.format(opts)
            i = i + 1
        elif i < length:
            script += ".then((result) => {{if (result.value) {{Swal.fire({}".format(opts)
            script += ")"
    for k in range(length - 1):
        script += "}})"
    return script
