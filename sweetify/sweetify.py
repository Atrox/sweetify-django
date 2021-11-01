import json
import sys

from django.conf import settings

from .encoder import LazyEncoder

DEFAULT_OPTS = {
    'showConfirmButton': False,
    'timer': 2500,
    'allowOutsideClick': True,
    'confirmButtonText': 'OK',
}


def _flash_config(request, opts):
    request.session['sweetify'] = json.dumps(opts, cls=LazyEncoder)


def _flash_multiple_configs(request, jsonData):
    request.session['sweetify'] = jsonData


def _is_string(s):
    # if we use Python 3
    if sys.version_info[0] >= 3:
        return isinstance(s, str)
    # we use Python 2
    return isinstance(s, basestring)


def _treat_data(opts):

    button = opts.pop('button', None)
    if button:
        opts['showConfirmButton'] = True

        if _is_string(button):
            opts['confirmButtonText'] = button

    persistent_toast = opts.pop('persistent_toast', None)
    if persistent_toast:
        opts['showConfirmButton'] = True
        opts['timer'] = None
        if _is_string(persistent_toast):
            opts['confirmButtonText'] = persistent_toast    

    persistent = opts.pop('persistent', None)
    if persistent:
        opts['showConfirmButton'] = True
        opts['allowOutsideClick'] = False
        opts['timer'] = None

        if _is_string(persistent):
            opts['confirmButtonText'] = persistent

    # sweetalert changes
    if getattr(settings, 'SWEETIFY_SWEETALERT_LIBRARY', 'sweetalert2') == 'sweetalert':
        opts['icon'] = opts.pop('type', None)
        opts['closeOnClickOutside'] = opts.pop('allowOutsideClick', None)

        if opts.pop('showConfirmButton', False):
            opts['button'] = opts['confirmButtonText']
        else:
            opts['button'] = False
    return opts


def sweetalert(request, title, **kwargs):
    opts = DEFAULT_OPTS.copy()
    opts.update(kwargs)
    opts['title'] = title
    if opts.pop('is_toast', None):
        opts.pop('allowOutsideClick', None)
    opts = _treat_data(opts)
    _flash_config(request, opts)


def toast(request, title, icon, **kwargs):
    kwargs['icon'] = icon
    kwargs['toast'] = True
    kwargs['position'] ='top-end'
    kwargs['timerProgressBar'] = True
    kwargs['is_toast'] = True
    return sweetalert(request, title, **kwargs)


def info(request, title, **kwargs):
    kwargs['icon'] = 'info'
    return sweetalert(request, title, **kwargs)


def success(request, title, **kwargs):
    kwargs['icon'] = 'success'
    return sweetalert(request, title, **kwargs)


def error(request, title, **kwargs):
    kwargs['icon'] = 'error'
    return sweetalert(request, title, **kwargs)


def warning(request, title, **kwargs):
    kwargs['icon'] = 'warning'
    return sweetalert(request, title, **kwargs)


def multiple(request, *args):
    optsls = []
    for dictionary in args:
        opts = DEFAULT_OPTS.copy()
        opts.update(dictionary)
        opts = _treat_data(opts)
        optsls.append(json.dumps(opts, cls=LazyEncoder))
    _flash_multiple_configs(request, optsls)
