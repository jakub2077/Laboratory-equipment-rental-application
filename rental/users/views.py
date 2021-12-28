from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    roles = list(request.user.groups.values_list('name',flat=True))
    role = roles.pop() if roles else 'Not assigned'
    data = {
        'role': role,
    }
    return render(request, 'users/profile.html', data)