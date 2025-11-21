import pytest
import tp0.arithmetique as art

def test_valeur_absolue():
    assert art.valeur_absolue(5) == 5
    assert art.valeur_absolue(-2) == 2
    assert art.valeur_absolue(-0) == 0

@pytest.mark.parametrize("arg,expected",[(7,True),(8,False),(6,False),(3,True),(10,False)])
def test_parite(arg, expected):
    assert art.parite(arg) == expected

@pytest.fixture
def quarante_deux()-> int:
    return 42

@pytest.mark.parametrize("argument,expexted",[(i,0) for i in range(1,10)])
def test_prod_mod(quarante_deux: int, argument, expexted):
    m=quarante_deux
    n = m*5
    assert art.prod_mod(n,argument,m) == expexted

@pytest.mark.parametrize("mul42",[i * 42 for i in range(1,10)])
@pytest.mark.parametrize("div42",[0,1,2,3,6,7,21,42])
def test_diviseur(mul42, div42):
    if div42 == 0:
        with pytest.raises(ZeroDivisionError):
            art.diviseur(mul42, div42)
    else:
        assert art.diviseur(mul42, div42) == True