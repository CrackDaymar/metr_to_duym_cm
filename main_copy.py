FEAT_0_9 = {'0': {'min': 0, 'max': 303.29999}, '1': {'min': 303.3, 'max': 608.0999}, '2': {'min': 608.1, 'max': 912.899},
        '3': {'min': 912.9, 'max': 1217.699}, '4': {'min': 1217.7, 'max': 1522.499}, '5': {'min': 1522.5, 'max': 1827.199},
        '6': {'min': 1827.2, 'max': 2132}, '7': {'min': 2132.000001, 'max': 2436.759999}, '8': {'min': 2436.76, 'max': 2741.55999},
        '9': {'min': 2741.56, 'max': 3046.8}}
Inch = {'1/8': {'min': 0.0625, 'max': 0.1875}, '1/4': {'min': 0.18751, 'max': 0.3125}, '3/8': {'min': 0.31251, 'max': 0.4375},
        '1/2': {'min': 0.43751, 'max': 0.5625}, '5/8': {'min': 0.56251, 'max': 0.6875}, '3/4': {'min': 0.68751, 'max': 0.8125},
        '7/8':{'min': 0.81251, 'max': 0.9375}}
FEAT_10_69 = {'0': {'min': 0, 'max': 303.29999}, '1': {'min': 303.3, 'max': 608.0999}, '2': {'min': 608.1, 'max': 912.899},
        '3': {'min': 912.9, 'max': 1217.699}, '4': {'min': 1217.7, 'max': 1522.499}, '5': {'min': 1522.5, 'max': 1827.199},
        '6': {'min': 1827.2, 'max': 2132}, '7': {'min': 2132.000001, 'max': 2436.759999}, '8': {'min': 2436.76, 'max': 2741.55999},
        '9': {'min': 2741.56, 'max': 3046.8}}
simbol = '"'


def translate(input_data: float = 0):
    if (input_data / 25.4 - input_data // 25.4) > 0.9375:
        output_data = float((input_data // 25.4) + 1)
    else:
        output_data = float(input_data // 25.4)
    n = 0
    while True:
        if FEAT_0_9[str(n)]['min'] <= input_data <= FEAT_0_9[str(n)]['max']:
            FEAT = n
            break
        n = n + 1
    add_inch = None
    for word in Inch.items():
        if word[1]['min'] <= (input_data / 25.4 - input_data // 25.4) <= word[1]['max']:
            add_inch = word[0]
    if n == 0:
        if add_inch is None and output_data is None:
            print(f"В дюймах размер будет выглядеть так: 0{simbol}")
            string_output = '0'+str(simbol)
            return string_output
        elif add_inch is None and output_data is not None:
            if output_data == 0:
                print(f"Значение в дюймах = 0")
                string_output = '0'
                return string_output
            else:
                print(f"В дюймах размер будет выглядеть так: {int(output_data)}{simbol}")
                string_output = str(int(output_data))+simbol
                return string_output
        elif add_inch is not None and output_data is None:
            print(f"В дюймах размер будет выглядеть так: {add_inch}{simbol}")
            string_output = str(add_inch) + simbol
            return string_output
        else:
            if output_data == 0:
                print(f"В дюймах размер будет выглядеть так: {add_inch}{simbol}")
                string_output = str(add_inch) + simbol
                return string_output
            else:
                print(f"В дюймах размер будет выглядеть так: {int(output_data)} {add_inch}{simbol}")
                string_output = str(int(output_data))+' '+str(add_inch) + simbol
                return string_output
    if output_data is None and add_inch is None:
        print(f"В дюймах размер будет выглядеть так: {int(FEAT)}'")
        string_output = str(FEAT) +"'"
        return string_output
    elif output_data is not None and add_inch is None:
        if output_data == 0:
            print(f"В дюймах размер будет выглядеть так: {int(FEAT)}'{simbol}")
            string_output = str(FEAT) + "'"
            return string_output
        else:
            print(f"В дюймах размер будет выглядеть так: {int(FEAT)}'{int(output_data)}{simbol}")
            string_output = str(FEAT) + "'" + str(int(output_data))+simbol
            return string_output
    elif output_data is None and add_inch is not None:
        print((f"В дюймах размер будет выглядеть так: {int(FEAT)}'{add_inch}{simbol}"))
        string_output = str(FEAT) + "'" + str(add_inch) + simbol
        return string_output
    else:
        if output_data == 0:
            print((f"В дюймах размер будет выглядеть так: {int(FEAT)}' {add_inch}{simbol}"))
            string_output = str(FEAT) + "'" + str(add_inch) + simbol
            return string_output
        else:
            print((f"В дюймах размер будет выглядеть так: {int(FEAT)}'{int(output_data)} {add_inch}{simbol}"))
            string_output = str(FEAT) + "'" + str(int(output_data))+' '+ str(add_inch) + simbol
            return string_output


def output_data(str1: str = None, str2: str = None):
    try:
        if str1.find('/') == (-1):
            first = str1.find(' ')
            str1 = str1[:first]+'"'
        else:
            first = str1.find("'")
            str1 = str1[first+1:]
    except:
        pass
    print(str1)
    try:
        if str2.find('/') == (-1):
            first = str2.find(' ')
            str2 = str2[:first]+'"'
        else:
            first = str2.find("'")
            str2 = str2[first+1:]
    except:
        pass
    print(str2)
    if str2 is not None:
        return str1+'-'+str2
    else:
        return str1


def last_func_cm(input_data: str):
    i = 0
    while True:
        split = False
        for w in input_data:
            if w == '-':
                split = True
        if split is True:
            input_data_1, input_data_2 = input_data.split('-')
            str1 = translate(float(input_data_1)*10)
            str2 = translate(float(input_data_2)*10)
            return output_data(str1, str2)
        if input_data == 0:
            break
        str = translate(float(input_data)*10)
        return output_data(str)

def last_func_mm(input_data: str):
    i = 0
    while True:
        split = False
        for w in input_data:
            if w == '-':
                split = True
        if split is True:
            input_data_1, input_data_2 = input_data.split('-')
            str1 = translate(float(input_data_1))
            str2 = translate(float(input_data_2))
            return output_data(str1, str2)
        if input_data == 0:
            break
        str = translate(float(input_data))
        return output_data(str)

