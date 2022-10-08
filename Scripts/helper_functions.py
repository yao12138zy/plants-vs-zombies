def inside_rect(left_top_point,size,exam_point):
    if exam_point[0] >= left_top_point[0] and exam_point[0] <= left_top_point[0] + size[0] \
        and exam_point[1] >= left_top_point[1] and exam_point[1] <= left_top_point[1] + size[1]:
        return True
    else:
        return False

def get_key_from_value(dict,value):
    for key in dict:
        if dict[key] == value:
            return key


