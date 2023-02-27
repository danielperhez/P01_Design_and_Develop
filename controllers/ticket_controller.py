from random import randint

from schemas.card import Card
from schemas.ticket import Retirar
from schemas.user import User


class TicketController:

    @staticmethod
    def retirar(user: User, card: Card, amount: int) -> Retirar:
        retirar = Retirar(user=user.id,
                        card=card.id,
                        amount=amount)
        
        retirar.save()
        return retirar

    #@staticmethod
    #def scan_ticket(ticket: Ticket) -> None:
    #    if not ticket.status:
    #        raise ValueError("Can't make the transaction")

     #   ticket.status = False
      #  ticket.save()
