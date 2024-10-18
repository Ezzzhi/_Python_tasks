from math import pi

default_radius = 5

def circle_perimeter(radius = default_radius):
    return radius * 2 * pi

def circle_area(radius = default_radius):
    return radius ** 2 * pi

# Отладка: запустится здесь, но не запустится при импорте
if __name__ == '__main__':
    print(__name__)
    print(circle_area())
    print(circle_perimeter())