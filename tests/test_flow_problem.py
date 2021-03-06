from graph import Graph


def test_maximum_flow():
    """ [2] ----- [5]
       /    +   /  | +
    [1]      [4]   |  [7]
       +    /   +  | /
        [3] ----- [6]
    """
    edges = [
        (1, 2, 18),
        (1, 3, 10),
        (2, 4, 7),
        (2, 5, 6),
        (3, 4, 2),
        (3, 6, 8),
        (4, 5, 10),
        (4, 6, 10),
        (5, 6, 16),
        (5, 7, 9),
        (6, 7, 18)
    ]
    g = Graph(from_list=edges)

    flow, g2 = g.maximum_flow(1, 7)
    assert flow == 23, flow


def test_maximum_flow01():
    edges = [
        (1, 2, 1)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=2)
    assert flow == 1, flow


def test_maximum_flow02():
    edges = [
        (1, 2, 10),
        (2, 3, 1),  # bottleneck.
        (3, 4, 10)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=4)
    assert flow == 1, flow


def test_maximum_flow03():
    edges = [
        (1, 2, 10),
        (1, 3, 10),
        (2, 4, 1),  # bottleneck 1
        (3, 5, 1),  # bottleneck 2
        (4, 6, 10),
        (5, 6, 10)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=6)
    assert flow == 2, flow


def test_maximum_flow04():
    edges = [
        (1, 2, 10),
        (1, 3, 10),
        (2, 4, 1),  # bottleneck 1
        (2, 5, 1),  # bottleneck 2
        (3, 5, 1),  # bottleneck 3
        (3, 4, 1),  # bottleneck 4
        (4, 6, 10),
        (5, 6, 10)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=6)
    assert flow == 4, flow


def test_maximum_flow05():
    edges = [
        (1, 2, 10),
        (1, 3, 1),
        (2, 3, 1)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=3)
    assert flow == 2, flow


def test_maximum_flow06():
    edges = [
        (1, 2, 1),
        (1, 3, 1),
        (2, 4, 1),
        (3, 4, 1),
        (4, 5, 2),
        (5, 6, 1),
        (5, 7, 1),
        (6, 8, 1),
        (7, 8, 1)
    ]
    g = Graph(from_list=edges)
    flow, g2 = g.maximum_flow(start=1, end=8)
    assert flow == 2, flow
    assert set(g2.edges()) == set(edges)

