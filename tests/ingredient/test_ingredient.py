from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1*
def test_ingredient():
    ingredient1 = Ingredient('queijo mussarela')
    assert ingredient1.name == 'queijo mussarela'
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
        }

    #  __repr__
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"

    #  __eq__
    ingredient2 = Ingredient('queijo mussarela')
    ingredient3 = Ingredient('presunto')
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # __hash__
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
