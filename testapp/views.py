from django.shortcuts import render, redirectfrom django.urls import reversefrom .forms import NewUserFormfrom django.contrib.auth import login, logout, authenticatefrom django.contrib import messagesfrom django.contrib.auth.forms import AuthenticationFormfrom .models import UserWeightModeldef register_request(request):    if request.method == "POST":        form = NewUserForm(request.POST)        if form.is_valid():            print("\n\n\n\n\nform2", form)            user = form.save()            login(request, user)            messages.success(request, "Registration successful.")            print("success")            return redirect(reverse('homepage'))        messages.error(request, "Unsuccessful registration. Invalid information.")    else:        form = NewUserForm()        print("\n\n\n\n\nform", form)        return render(request, "register.html", {"register_form": form})def homepage(request):    if request.method == "GET":        print("homepage")        # form = UserWeightForm()        # print("\n\n\n\n\nform", form)        return render(request, "homepage.html")    else:        # form = UserWeightForm(request.POST)        weight = request.POST['weight']        user_id = request.user        user_weight = UserWeightModel.objects.create(user_id=user_id, weight=weight)        messages.success(request, "Form Saved successful.")        return redirect("homepage")def login_request(request):    if request.method == 'POST':        # AuthenticationForm_can_also_be_used__        username = request.POST['username']        password = request.POST['password']        user = authenticate(request, username=username, password=password)        if user is not None:            form = login(request, user)            messages.success(request, f' welcome {username} !!')            return redirect(reverse('homepage'))        else:            messages.info(request, f'account done not exit plz sign in')    form = AuthenticationForm()    return render(request, 'login.html', {'form': form, 'title': 'log in'})def logout_view(request):    logout(request)    return redirect('login_request')def dashboard(request):    if request.method == "GET":        queryset = UserWeightModel.objects.filter(user_id=request.user.id).order_by('created_date')        print(queryset.values())        return render(request, "dashboard.html", {"queryset":queryset})