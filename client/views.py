from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic import View
from django.utils.translation import gettext_lazy as _


class ClientRegistrationForm(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yxatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.seccess(request, _("Siz muvaffaqiyatli ro'yxatdan o'tingiz!"))
            return redirect('main:index')

        return render(request, 'layouts/form.html', {
            'form': form
        })
