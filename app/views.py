from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket
from django.http import HttpResponseRedirect
from django.views import View
from app.forms import NewTicketForm

# Create your views here.


class Home(View):
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "home.html", {"movies": movie})


class NewTicket(View):
    def get(self, request, id):
        purchase = Movie.objects.get(id=id)
        forms = NewTicketForm.objects.all()
        return render(request, "new_ticket.html", {"movie": purchase}, {"form": forms})

    def getting(self, request, id):
        purchase = Movie.object.get(id=id)
        if request.method == "POST":
            form = NewTicketForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect("/thanks/")
        else:
            form = NewTicketForm()

        return render(request, "new_ticket.html", {"movie": purchase}, {"form": form})

    def post(self, request, id):
        showtime = Showing.objects.get(showtime)
        purchase = Ticket.object.get(id=id)
        Ticket.objects.create(name=purchase, showing_id=showtime)
        return render(
            request, "new_ticket.html", {"movie": purchase}, {"form": showtime}
        )


class TicketDetail(View):
    def post(self, request):
        ticket = Ticket.objects.all()
        return render(request, "ticket_detail.html", {"ticket": ticket})
