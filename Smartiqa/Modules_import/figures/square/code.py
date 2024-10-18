a = 15

def square_area(side_=a):
    return side_ ** 2

def square_perimeter(side_=a):
    return side_ * 4


if __name__ == '__main__':
    print(__name__)
    print(square_area())
    print(square_perimeter())