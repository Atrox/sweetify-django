# Sweetify - SweetAlert for Django

[![Build Status](https://img.shields.io/travis/Atrox/sweetify-django.svg?style=flat-square)](https://travis-ci.org/Atrox/sweetify-django)
[![Latest Version](https://img.shields.io/pypi/v/sweetify.svg?style=flat-square)](https://pypi.python.org/pypi/sweetify)
[![Coverage Status](https://img.shields.io/coveralls/Atrox/sweetify-django.svg?style=flat-square)](https://coveralls.io/r/Atrox/sweetify-django)

**Sweetify** allows you to use [SweetAlert](http://t4t5.github.io/sweetalert/) or [SweetAlert2](https://github.com/limonte/sweetalert2) for your temporary messages.
_See the examples below, to see how to use this library_

## Installation
**Note: This package does not provide the client-side files of SweetAlert. You have to provide them yourself.**

Install the latest version with `pip`:

```bash
pip install --upgrade sweetify
```

Then you have to add `sweetify` to your django apps:
```python
INSTALLED_APPS = [
    ...
    'sweetify'
]
```

Next up you have to specify, in your settings, which library you are using (SweetAlert or SweetAlert2):
```python
# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'
```

Next add the following lines to the bottom of your layout/base template:
```html
...

{% load sweetify %}
{% sweetify %}

</body>
</html>
```

## Usage
You can now easily create alerts in your views with any of the following methods provided by **Sweetify**:
```python
import sweetify

# Base method with no type specified
sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')

# Additional methods with the type already defined
sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
sweetify.success(self.request, 'You successfully changed your password')
sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
sweetify.warning(self.request, 'This is a warning... I guess')
```

## Example Usage
```python
import sweetify

def test_view(request):
    sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    return redirect('/')
```

## Replacement for SuccessMessageMixin
Sweetify includes a drop-in replacement for `SuccessMessageMixin`.
Just replace the Django mixin with Sweetify's `SweetifySuccessMixin` and you are good to go.

```python
from sweetify.views import SweetifySuccessMixin

class TestUpdateView(SweetifySuccessMixin, UpdateView):
    model = TestModel
    fields = ['text']
    success_message = 'TestModel successfully updated!'
```

## Options
**By default, all alerts will dismiss after a sensible default number of seconds.**

Default options set by **Sweetify**:
```python
sweetify.DEFAULT_OPTS = {
    'showConfirmButton': False,
    'timer': 2500,
    'allowOutsideClick': True,
    'confirmButtonText': 'OK',
}
```

The following special options provided by **Sweetify** are available:
```python
# Shows the alert with a button, but will still close automatically
sweetify.sweetalert(self.request, 'Title', button=True)
sweetify.sweetalert(self.request, 'Title', button='Awesome!') # Custom text for the button

# Shows the alert with a button and only closes if the button is pressed
sweetify.sweetalert(self.request, 'Title', persistent=True)
sweetify.sweetalert(self.request, 'Title', persistent='Awesome!') # Custom text for the button
```

You also can use any other available option that [SweetAlert accepts](http://t4t5.github.io/sweetalert/):
```python
sweetify.info(self.request, 'Sweet!', text='Here is a custom image', imageUrl='images/thumbs-up.jpg', timer=5000)
```



## Development
Use the `Makefile`to execute common tasks:

- Install dependencies
```shell
$ make install
```

- Run all tests
```shell
$ make test
```

## Contributing
Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/atrox/sweetify-django/issues)
- Fix bugs and [submit pull requests](https://github.com/atrox/sweetify-django/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features
