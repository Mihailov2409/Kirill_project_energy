

def calculator(ves, speed, km):
    if speed == "4km|h":
        kal = km * 1.125
        kal = kal * ves
        return kal
    elif speed == "6km|h":
        kal = km * 0.916
        kal = kal * ves
        return kal
    elif speed == "8km|h":
        kal = km * 1.25
        kal = kal * ves
        return kal