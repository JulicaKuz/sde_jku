import pytest

from pytestcar.Car import Car


# class TestCarClass:
#
#     def test_brake(self):
#         car = Car(50)
#         car.brake()
#         assert car.speed == 45

@pytest.fixture
def my_car():
    return Car(50)


def test_brake(my_car):
    my_car.brake()
    assert my_car.speed == 45


def test_car_accelerate(my_car):
    my_car.acclerate()
    assert my_car.speed == 55
