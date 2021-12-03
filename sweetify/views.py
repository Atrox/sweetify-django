import sweetify


class SweetifySuccessMixin(object):
    """
    Adds a sweetalert success message on successful form submission.
    Drop-in replacement for django's SuccessMessageMixin.
    """

    success_message = ""
    sweetify_options = {}

    def form_valid(self, form):
        response = super(SweetifySuccessMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            sweetify.success(self.request, success_message, **self.get_sweetify_options())
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_sweetify_options(self):
        return self.sweetify_options
