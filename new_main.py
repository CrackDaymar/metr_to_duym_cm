FEAT_0_9 = {'0': {'min': 0, 'max': 303.29999}, '1': {'min': 303.3, 'max': 608.0999}, '2': {'min': 608.1, 'max': 912.899},
        '3': {'min': 912.9, 'max': 1217.699}, '4': {'min': 1217.7, 'max': 1522.499}, '5': {'min': 1522.5, 'max': 1827.199},
        '6': {'min': 1827.2, 'max': 2132}, '7': {'min': 2132.000001, 'max': 2436.759999}, '8': {'min': 2436.76, 'max': 2741.55999},
        '9': {'min': 2741.56, 'max': 3046.8}}
Inch = {'1/8': {'min': 0.0625, 'max': 0.1875}, '1/4': {'min': 0.18751, 'max': 0.3125}, '3/8': {'min': 0.31251, 'max': 0.4375},
        '1/2': {'min': 0.43751, 'max': 0.5625}, '5/8': {'min': 0.56251, 'max': 0.6875}, '3/4': {'min': 0.68751, 'max': 0.8125},
        '7/8':{'min': 0.81251, 'max': 0.9375}}

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
        n += 1
    add_inch = None
    for word in Inch.items():
        if word[1]['min'] <= (input_data / 25.4 - input_data // 25.4) <= word[1]['max']:
            add_inch = word[0]
    if output_data is None:
        output_str = str(FEAT) + "'" + ('' if add_inch is None else str(add_inch) + '"')
    else:
        output_str = str(FEAT) + "'" + str(int(output_data)) + ('' if add_inch is None else ' ' + str(add_inch) + '"')
    return output_str

def output_data(str1: str = None, str2: str = None):
    if str2 is not None:
        return str1 + '-' + str2
    else:
        return str1

def last_func_cm(input_data: str):
    input_data = input_data.split('-')
    output_str = ''
    for data in input_data:
        if data != '':
            output_str += translate(float(data) * 10) + '-'
    output_str = output_str[:-1] if output_str.endswith('-') else output_str
    return output_data(output_str)

def last_func_mm(input_data: str):
    input_data = input_data.split('-')
    output_str = ''
    for data in input_data:
        if data != '':
            output_str += translate(float(data)) + '-'
    output_str = output_str[:-1] if output_str.endswith('-') else output_str
    return output_data(output_str)


print(last_func_mm('10-222'))