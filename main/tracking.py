def check_mouse_in_box(mouse_x, mouse_y, boxes):
    for _, x1, y1, x2, y2 in boxes:
        if  x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2 :return True
    return False