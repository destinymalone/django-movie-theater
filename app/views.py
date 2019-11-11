from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket
from app.forms import NewTicketForm
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "home.html", {"movies": movie})


class PurchaseTicket(View):
    def get(self, request, id):
        purchase = Movie.objects.get(id=id)
        forms = NewTicketForm.objects.all()
        return render(request, "new_ticket.html", {"movie": purchase}, {"form": forms})

    def post(self, request, id):
        showtime = Showing.objects.get(showtime)
        purchase = NewTicketForm.objects.get(id=id)
        if request.method == POST:
            Ticket.objects.create(
                name=purchase, showing_id=showtime
            )
        else:
            print("Invalid")

        return render(request, "new_ticket.html", {"movie": }, {"form": })


class TicketDetail(View):
    def post(self, request):
        ticket = Ticket.objects.all()
        return render(request, "ticket_detail.html", {"ticket": ticket})
