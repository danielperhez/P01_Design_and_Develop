from controllers.user_controller import UserController

from schemas.user import User


def test_create_user():
    # Arrange
    user = UserController.new_user(names="John Doe",first_name="reyes",second_name="valdez",
                                   phone_number="123-123-1234",email="loco@gmail.com", address="iteso",ExternNumber=10)

    # Act
    created_user = User.select().where(User.id == user.id).get()

    # Assert
    assert user.id == created_user.id
    assert user.names == created_user.names
    assert user.first_name == created_user.first_name
    assert user.second_name == created_user.second_name
    assert user.phone_number == created_user.phone_number
    assert user.email == created_user.email
    assert user.address == created_user.address
    assert user.ExternNumber == created_user.ExternNumber
    # Delete test instances
    created_user.delete_instance()
