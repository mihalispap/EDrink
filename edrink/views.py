# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from edrink.forms import EditProfileForm


def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None,
                           initial={'pk': user.pk, 'username': user.username, 'avatar': user.avatar})
    if request.method == 'POST':
        if form.is_valid():
            user.avatar = request.FILES['avatar']
            user.save()
            return HttpResponseRedirect('%s' % (reverse('admin:index')))

    context = {
        "form": form
    }

    return render(request, "admin/edit_profile.html", context)
