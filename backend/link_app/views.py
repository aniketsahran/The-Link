from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from . import models


def auth(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['pass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'link_app/login.html', {'message': 'Invalid credentials.'})
        elif 'register' in request.POST:
            username = request.POST['username']
            name = request.POST['name']
            roll = request.POST['roll']
            password1 = request.POST['pass1']
            password2 = request.POST['pass2']
            if password1 == password2:
                if models.CustomUser.objects.filter(username=username).exists():
                    return render(request, 'link_app/login.html', {'message': 'Email already registered.'})

                user = models.CustomUser.objects.create_user(
                    username=username, password=password1, roll_no=roll, first_name=name, is_student=True)
                user.save()
                # print(request.POST)
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'link_app/login.html', {'message': 'Passwords do not match.'})
    return render(request, 'link_app/login.html')


@login_required
def auth_logout(request):
    logout(request)
    return redirect('auth')


@login_required
def home(request):
    return render(request, 'link_app/home.html')


@login_required
def add_resource(request):
    if request.method == 'POST':
        print(request.POST)
        sub = request.POST['sub']
        year = request.POST['year']
        cat = request.POST['type']
        files = request.FILES.getlist('file')
        for i in files:
            models.Resource.objects.create(
                subject_code=sub, year=year, category=cat, material=i)
        return render(request, 'link_app/add_resource.html', {'message': 'Upload Successful!'})
    return render(request, 'link_app/add_resource.html')


@login_required
def resource(request):
    objects = models.Resource.objects.filter(isApproved=True)
    context = {'objects': objects}
    return render(request, 'link_app/resource.html', context)


@login_required
@permission_required("models.CustomUser.is_staff")
def admin_resource(request):
    if request.method == 'POST':
        if 'approve' in request.POST:
            models.Resource.objects.filter(
                id=request.POST['approve']).update(isApproved=True)
        if 'reject' in request.POST:
            models.Resource.objects.filter(
                id=request.POST['reject']).update(isApproved=False)
    approved_objects = models.Resource.objects.filter(isApproved=True)
    pending_objects = models.Resource.objects.filter(isApproved=False)
    context = {'approved_objects': approved_objects,
               'pending_objects': pending_objects}
    return render(request, 'link_app/admin_resource.html', context)


@login_required
def qr(request):
    return render(request, 'link_app/qr.html')


@login_required
def doubt(request):
    context = {}
    if request.user.is_teacher:
        objects = models.Doubt.objects.filter(faculty=request.user)
        context = {'doubts': objects}
    elif request.user.is_student:
        objects = models.Doubt.objects.filter(asked_by=request.user)
        context = {'doubts': objects}
    return render(request, 'link_app/doubt.html', context)


@login_required
def doubt_add(request):
    if request.method == 'POST':
        sub = request.POST['sub']
        fcode = request.POST['fcode']
        doubt = request.POST['doubt']
        files = request.FILES.getlist('file')
        try:
            faculty = models.CustomUser.objects.get(faculty_code=fcode)
        except:
            return render(request, 'link_app/doubt_add.html', {'error': 'Invalid Faculty Code.'})
        for i in files:
            models.Doubt.objects.create(
                asked_by=request.user, subject_code=sub, faculty=faculty, doubt=doubt, file=i)
        return render(request, 'link_app/doubt_add.html', {'message': 'Doubt added successfully!'})
    return render(request, 'link_app/doubt_add.html')


@login_required
def doubt_view(request, pk):
    doubt = models.Doubt.objects.get(id=pk)
    context = {'doubt': doubt}
    if request.user.is_teacher:
        if request.method == 'POST':
            solution = request.POST['solution']
            files = request.FILES.getlist('file')
            for i in files:
                models.Solution.objects.create(solution=solution, file=i, doubt=doubt)
            return render(request, 'link_app/doubt_view.html', {'message': 'Solution added successfully!'})
    elif request.user.is_student:
        try:
            solution = models.Solution.objects.filter(doubt=doubt)
            context['solution'] = solution
        except models.Solution.DoesNotExist:
            solution = None
        if solution is None or solution.count() == 0:
            context['error'] = 'Not Answered Yet.'
            return render(request, 'link_app/doubt_view.html', context)         
    return render(request, 'link_app/doubt_view.html', context)


@login_required
def notification(request):
    notifications = models.Notification.objects.all()
    return render(request, 'link_app/notification_view.html', {'notifications': notifications})


@login_required
@permission_required("models.CustomUser.is_teacher")
def notification_add(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        desc = request.POST['desc']
        file = request.FILES.getlist('file')
        for i in file:
            models.Notification.objects.create(
                title=title, description=desc, uploaded_by=request.user, file=i)
        return render(request, 'link_app/notification_add.html', {'message': 'Notification added successfully!'})
    return render(request, 'link_app/notification_add.html')


@login_required
def contact(request):
    return render(request, 'link_app/contact.html')
