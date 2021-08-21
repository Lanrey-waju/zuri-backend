from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Message_me
from django.contrib import messages

# Create your views here.
def contact_me(request):
    if request.method == "POST":
        form = Message_me(request.POST)
        if form.is_valid:
            form.save()
            messages.success(
                request, "Thanks for contacting me. I'll attend to it shortly."
            )
            return redirect("home-page")
        # else:
        #     form = Message_me()
        #     return render(request, "resume_app/index.html", {"form": form})
    form = Message_me()
    context = {
        "form": form,
    }
    return render(request, "resume_app/index.html", context)


# def go_to_zuri(request):
#     return HttpResponseRedirect(request, "www.internship.zuri.team")
