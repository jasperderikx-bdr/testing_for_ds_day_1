# o	Exercise: wordt de code na een assert uitgevoerd?

from src.hanoi import show_solution


def test_hoi():
    show_solution(4)
    assert False


from src.hanoi_graph import hanoi_graph


def test_hoi2():
    g3 = hanoi_graph(2)
    print("\n")
    print(g3)
    print("\n\n")
    g3 = hanoi_graph(3)
    print("\n")
    print(g3)
    assert False
