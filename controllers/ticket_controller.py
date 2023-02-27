from random import randint

#from schemas.card import Card
#from schemas.ticket import Ticket
#from schemas.user import User

from schemas.card import Card


class TicketController:

    @staticmethod
    def buy_ticket(user: User, card: Card) -> Ticket:
        # TODO: Validate movie date, and stuff like that
        ticket = Ticket(user=user.id,
                        card=card.id,
                        proxy=f"{card.id}-{randint(10000, 99999)}",
                        status=True)
        ticket.save()
        return ticket

    @staticmethod
    def scan_ticket(ticket: Ticket) -> None:
        if not ticket.status:
            raise ValueError("Your ticket is expired.")

        ticket.status = False
        ticket.save()
