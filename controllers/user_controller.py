from schemas.user import User


class UserController:

    @staticmethod
    def new_user(names: str, first_name : str,second_name:str,
                    phone_number: str, email: str,address: str,ExternNumber : int) -> User:
        user = User(names=names,first_name=first_name, second_name = second_name ,
                    phone_number=phone_number, email = email,address=address, ExternNumber = ExternNumber)
        user.save()
        return user