from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket
from django.http import HttpResponseRedirect
from django.views import View
from app.forms import NewTicketForm
from datetime import datetime

# Create your views here.


class Home(View):
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "home.html", {"movies": movie})


class NewTicket(View):
    def get(self, request, id):
        purchase = Movie.objects.get(id=id)
        forms = NewTicketForm()
        return render(request, "new_ticket.html", {"movie": purchase, "form": forms})

    def post(self, request, id):
        form = NewTicketForm(request.POST)
        if form.is_valid():
            t = Ticket.objects.create(
                name=form.cleaned_data["name"],
                showing_id=form.cleaned_data["showing_id"],
                purchased_at=datetime.now(),
            )
            return redirect("ticket_detail", t.id)
        else:
            form = NewTicketForm()
            return render(request, "new_ticket.html", {"movie": purchase, "form": form})


class TicketDetail(View):
    def get(self, request, id):
        ticket = Ticket.objects.get(id=id)
        return render(request, "ticket_detail.html", {"ticket": ticket})
