from sign_config import *
import numpy as np
def check_mouse_in_box(mouse_x, mouse_y, boxes):
    for index in range(len(boxes)):
        _, x1, y1, x2, y2 = boxes[index]
        if  x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2 :
            return index
    return -1


def find_sign( img, class_id):

    # Инициализация переменной результата
    result_type = ""
    # Проверяем, есть ли модель для данного класса
    if names_signs_for_YOLO[class_id] in model_dict:
        model = model_dict[names_signs_for_YOLO[class_id]]

        number_result = np.argmax(model.predict_step(np.expand_dims(img, axis=0)))
        # Обработка особых случаев для класса "treugolnik"
        if names_signs_for_YOLO[class_id] == "treugolnik":
            result_type = name_signs_cnn["treugolnik"][number_result]
            if result_type in sub_models:
                sub_model = sub_models[result_type]
                number_result = np.argmax(sub_model.predict_step(np.expand_dims(img, axis=0)))
                result_type = name_sub_signs_cnn[result_type][number_result]
        else:
            result_type = name_signs_cnn[names_signs_for_YOLO[class_id]][number_result]
    else:
        # Возвращаем тип из YOLO, если модели не найдены
        result_type = type_signs_yolo[names_signs_for_YOLO[class_id]]

    # Если результат пустой, присваиваем "empty"
    if result_type == "":
        result_type = "empty"

    return result_type