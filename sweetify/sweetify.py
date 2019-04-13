import json
import sys

from .encoder import LazyEncoder

DEFAULT_OPTS = {
    'showConfirmButton': False,
    'timer': 2500,
    'allowOutsideClick': True,
    'confirmButtonText': 'OK',
}


def _flash_config(request, opts):
    request.session['sweetify'] = json.dumps(opts, cls=LazyEncoder)


def _is_string(s):
    # if we use Python 3
    if sys.version_info[0] >= 3:
        return isinstance(s, str)
    # we use Python 2
    return isinstance(s, basestring)


def sweetalert(request, title, **kwargs):
    opts = DEFAULT_OPTS.copy()
    opts.update(kwargs)

    opts['title'] = title

    button = opts.pop('button', None)
    if button:
        opts['showConfirmButton'] = True

        if _is_string(button):
            opts['confirmButtonText'] = button

    persistent = opts.pop('persistent', None)
    if persistent:
        opts['showConfirmButton'] = True
        opts['allowOutsideClick'] = False
        opts['timer'] = None

        if _is_string(persistent):
            opts['confirmButtonText'] = persistent

    _flash_config(request, opts)


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
