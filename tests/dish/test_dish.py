from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish1 = Dish("lasanha presunto", 25.90)
    dish2 = Dish("lasanha berinjela", 27.00)

    assert dish1.name == "lasanha presunto"
    assert dish1.price == 25.90

    assert dish1.get_restrictions() == set()

    #  __repr__
    assert repr(dish1) == "Dish('lasanha presunto', R$25.90)"

    # __eq__
    assert dish1 == dish1
    assert dish1 != dish2

    # __hash__
    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)

    # __error__
    with pytest.raises(ValueError):
        Dish('lasanha presunto', -10.00)
    with pytest.raises(TypeError):
        Dish('lasanha presunto', 'abc')

    dish1.add_ingredient_dependency(Ingredient("tomate"), 100)
    assert dish1.get_ingredients() == {Ingredient('tomate')}
