from random import randint

from schemas.card import Card
from schemas.ticket import Retirar
from schemas.user import User


class TicketController:

    @staticmethod
    def transaction(amount_to_get: int, initial_amount = int) -> Retirar:
        retirar = Retirar(amount_to_get=amount_to_get, initial_amount=initial_amount)

    #def transaction(user: User, card: Card, amount: int) -> Ticket:
    #    amount = amount
    #    ticket = Ticket(user=user.id,
    #                    card=card.id,
    #                    proxy=f"{card.id}-{randint(10000, 99999)}",
    #                    amount = amount,
    #                    status=True)
        retirar.save()
        return retirar

    #@staticmethod
    #def scan_ticket(ticket: Ticket) -> None:
    #    if not ticket.status:
    #        raise ValueError("Can't make the transaction")

     #   ticket.status = False
      #  ticket.save()
