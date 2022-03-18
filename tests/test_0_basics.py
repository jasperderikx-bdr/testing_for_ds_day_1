# o	Exercise: wordt de code na een assert uitgevoerd?

from src.basics import show_solution


def test_hoi():
    show_solution(4)
    assert False


from src.graph import hanoi_graph

# hoeveel standen zijn er.
#Volgens de legende 64 schijven en dan klaar. stel ze begonnen in jaar 0. 1 schijf per seconde. Schrijf een test die passed zolang we nog minstens 100 jaar te leven hebben.
# in hoeveel stappen kan je de puzzel oplossen?

def test_hoi2():
    g3 = hanoi_graph(2)
    print("\n")
    print(g3)
    print("\n\n")
    g3 = hanoi_graph(3)
    print("\n")
    print(g3)
    assert False

from src.basics import show_solution

def test3():
    show_solution(4)
    assert False
