a = 7
b = 2
c = 8

def triangle_area(side_1=a, side_2=b, side_3=c):
    return side_1 + side_2 + side_3

def triangle_perimeter(side_1=a, side_2=b, side_3=c):
    p = triangle_area(side_1, side_2, side_3) / 2
    return (p * (p - side_1) * (p - side_2) * (p - side_3)) ** 0.5


if __name__ == '__main__':
    print(__name__)
    print(triangle_area(3,4,5))
    print(triangle_perimeter())