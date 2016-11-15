from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins
from django.contrib import messages

from .forms import FeedbackForm
from .models import Feedback


class FeedbackView(CreateView):
    model = Feedback  # to avoid ImproperlyConfigured error
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')
    exclude = ['create_date']
    template_name = 'feedbacks/feedback.html'  # template_name = 'feedback.html'

    def form_valid(self, form):
        data = form.cleaned_data
        text = 'Message from {0},\n {1}'.format(data['name'], data['message'])
        mail_admins(data['subject'], text, fail_silently=True)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Leave a feedback"
        return context
