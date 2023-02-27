import datetime

from controllers.card_controller import CardController
from controllers.user_controller import UserController


movie1 = CardController.create_card(datetime(2023,2,27,0,22),card_Number="41523136989065",Account="12345678")
movie2 = CardController.create_card(datetime(2023,2,27,0,23),card_Number="41523136000000",Account="13346789")


user1 = UserController.new_user("Jesus Israel","Reyes","Valdez,",phone_number="3323-8405-20",email="reyes0valdez0@gmail,com",
                                address="Frida Kahlo",ExternNumber=108)
user2 = UserController.new_user("Alan Jose","Maldonado","Jimenez,",phone_number="3323-8432-21",email="alan12@gmail,com",
                                address="itesito",ExternNumber=420)