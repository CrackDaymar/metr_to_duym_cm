
Inch = {'1/8': {'min': 0.0625, 'max': 0.1875}, '1/4': {'min': 0.1875000000001, 'max': 0.3125}, '3/8': {'min': 0.3125000000001, 'max': 0.4375},
        '1/2': {'min': 0.4375000000001, 'max': 0.5625}, '5/8': {'min': 0.5625000000001, 'max': 0.6875}, '3/4': {'min': 0.68750000000001, 'max': 0.8125},
        '7/8':{'min': 0.81250000000001, 'max': 0.9375}}


def take_translate(input_data: float = 0):
    FEAT = 0
    FEAT_data = input_data/25.4
    while FEAT_data >= 12:
        FEAT += 1
        FEAT_data -= 12
    inch = FEAT_data
    INCH = 0
    while inch >= 1:
        INCH += 1
        inch -= 1
    if inch >= 0.9375:
        INCH += 1
    add_inch = inch
    ADD_INCH = 0
    for word in Inch.items():
        if word[1]['min'] <= add_inch <= word[1]['max']:
            ADD_INCH = word[0]
    return FEAT, INCH, ADD_INCH


def out_info_COLLAR(input_data: float = 0, min: bool = True):
    FEAT, INCH, ADD_INCH = take_translate(input_data)
    INCH += FEAT*12
    if ADD_INCH != 0:
        str_out_min = str(INCH+1) + '"'
        str_out_max = str(INCH) + '"'
    else:
        str_out_min = str(INCH) + '"'
        str_out_max = str(INCH) + '"'
    if min == True:
        return str_out_min
    else:
        return str_out_max


def out_info_LEASH(input_data: float = 0, min: bool = True):
    FEAT, INCH, ADD_INCH = take_translate(input_data)
    str_out = ''
    if min is False:
        if FEAT != 0:
            str_out += str(FEAT) + "'"
        if INCH != 0:
            str_out += str(INCH) + '"'
    else:
        if ADD_INCH == 0:
            if FEAT != 0:
                str_out += str(FEAT) + "'"
            if INCH != 0:
                str_out += str(INCH) + '"'
        else:
            inch = int(INCH) + 1
            if inch == 12:
                FEAT += 1
                str_out += str(FEAT) + "'"
                return str_out
            else:
                str_out = str(FEAT) + "' " + str(inch) + '"'
    return str_out


def out_info_INCH(input_data: float = 0):
    FEAT, INCH, ADD_INCH = take_translate(input_data)
    str_out = ''
    if FEAT != 0:
        str_out += str(FEAT) + "'"
    if INCH != 0:
        str_out += str(INCH)
    if ADD_INCH != 0:
        str_out += " " + ADD_INCH + '"'
    else:
        str_out += '"'
    if INCH == 0 and ADD_INCH == 0:
        str_out += str(FEAT) + "'"
    return str_out

def out_info_FEAT_INCH(input_data: float = 0):
    FEAT, INCH, ADD_INCH = take_translate(input_data)
    str_out = ''
    INCH += FEAT*12
    if INCH != 0:
        str_out += str(INCH)
    if ADD_INCH != 0:
        str_out += " " + ADD_INCH + '"'
    else:
        str_out += '"'
    return str_out


def out_info_FEAT_INCH_max(input_data: float = 0):
    FEAT, INCH, ADD_INCH = take_translate(input_data)
    str_out = ''

    if ADD_INCH == 0:
        if FEAT != 0:
            str_out += str(FEAT) + "'"
        if INCH != 0:
            str_out += str(INCH) + '"'
    else:
        inch = int(INCH) + 1
        if inch == 12:
            FEAT += 1
            str_out += str(FEAT) + "'"
            return str_out
        elif FEAT!= 0:
            str_out = str(FEAT) + "' " + str(inch) + '"'
        else:
            str_out = str(inch) + '"'
    return str_out


def last_func(input_data: str, cm: bool = True):
    i = 0
    while True:
        split = False
        for w in str(input_data):
            if w == '-':
                split = True
        if split is True:
            input_data_1, input_data_2 = input_data.split('-')
            if cm is True:
                input_data_1 = float(input_data_1) * 10
                input_data_2 = float(input_data_2) * 10
        elif input_data == 0:
            break
        else:
            if cm is True:
                input_data = float(input_data) * 10
            str_ = f"Полное значение: {out_info_INCH(float(input_data))}" \
                   f"\nЗначение только в дюймах {out_info_FEAT_INCH(float(input_data))}" \
                   f"\nЗначение для ошейников {out_info_COLLAR(float(input_data), True)}" \
                   f"\nОкруглённые в большую сторону {out_info_FEAT_INCH_max(float(input_data))}"
            return str_

        str_ = f"Полное значение в имперской системе, такое: {out_info_INCH(float(input_data_1))} - {out_info_INCH(float(input_data_2))}" \
              f"\nДля ошейников значение будет выглядеть так: {out_info_COLLAR(float(input_data_1), True)} - {out_info_COLLAR(float(input_data_2), False)}" \
              f"\nДля поводков, значение будет выглядеть так: {out_info_LEASH(float(input_data_1), True)} - {out_info_LEASH(float(input_data_2), False)}"
        return str_

