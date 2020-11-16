# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from edrink.forms import EditProfileForm
from edrink.models import User, Room


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


def assign_rooms(request):
    users = User.objects.all().order_by('?')
    rooms = [room for room in Room.objects.all().order_by('capacity')]
    for user in users:
        if len(rooms) == 0:
            break
        user.assigned_in_room = rooms[0]
        rooms[0].capacity -= 1
        if rooms[0].capacity == 0:
            rooms.pop(0)
        user.save()
    return HttpResponseRedirect('%s' % (reverse('admin:index')))
