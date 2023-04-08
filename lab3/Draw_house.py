def main():
    x, y = 300, 400
    width, heigth = 200, 300

    draw_house(x, y, width, heigth)


def draw_house(x, y, width, heigth):
    """
    Нарисовать домик ширины wigth и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: габаритная ширина
    :param heigth: габаритная высота
    :return: None
    """
    print('Типа рисую домик...', x, y, width, heigth)
    foundation_height = 0.05 * heigth
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height)
    draw_house_roof()




main()
