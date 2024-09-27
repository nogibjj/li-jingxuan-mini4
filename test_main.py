from main import add


def test_add():
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    print("correct")


if __name__ == "__main__":
    test_add()
