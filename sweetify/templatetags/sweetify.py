from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def sweetify(context):
	opts = context.request.session.pop('sweetify', None)

	if not opts:
		return ''
	if isinstance(opts, list):
		if getattr(settings, 'SWEETIFY_SWEETALERT_LIBRARY', 'sweetalert2') == 'sweetalert':
			#TODO Add sweetalert 1 compatibility with multiple alerts.
			return''
		script = concatenate(opts)
	else:
		if getattr(settings, 'SWEETIFY_SWEETALERT_LIBRARY', 'sweetalert2') == 'sweetalert2':
			script = 'Swal.fire({})'.format(opts)
		else:
			script = 'swal({})'.format(opts)
	return mark_safe("""<script>{}</script>""".format(script))

def concatenate(list):
	i = 0
	length = len(list)
	script = 'Swal.fire({})'
	for opts in list:
		if i == 0:
			script = script.format(opts)
			i = i + 1
		elif i < length:
			script += '.then((result) => {{if (result.value) {{Swal.fire({}'.format(opts)	
			script += ')'
	for k in range(length - 1):
		script += '}})'
	return script
