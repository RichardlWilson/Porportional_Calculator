
def convert_to_inches(nested_list):
        '''
        Converts all passed arguments to inches.
        Expects a nested list: [[float, bool]]*5 
        Returns a list: [float]*5
        '''
        check_empty = lambda entry: 0.0 if entry == '' else float(entry)

        converted_data = []

        for data in nested_list:

            if data[1]:
                converted_data.append(check_empty(data[0]) * 12)
            else:
                converted_data.append(check_empty(data[0]))

        return converted_data       


def add(current_height, current_width, height_scale, width_scale):
        '''
        Add to current Height & Width
        '''
        current_height += height_scale
        current_width += width_scale

        return current_height, current_width   


def subtract(current_height, current_width, height_scale, width_scale):
    '''
    Subtract from current Height & Width.
    '''
    current_height -= height_scale
    current_width -= width_scale

    return current_height, current_width


def scale(current_height, current_width):
    '''
    calculates the ratio of current height to current width.
    '''
    try:
        if current_height >= current_width:
            height_scale = current_width / current_height
            width_scale = 1.0
        else:
            width_scale = current_height / current_width
            height_scale = 1.0

        return height_scale, width_scale

    except ZeroDivisionError:
        return 0, 0      


def square_footage(current_height, current_width):
    '''
    calculates square footage of current height and width.
    '''
    return round(current_height * current_width /144, 2) 


def up_to_max_square_footage(current_height, current_width, height_scale,
    width_scale, max_sqft):
    '''
    Calculates up to max square footage.
    '''
    if max_sqft == 0:
        return current_height, current_width, square_footage(current_height,
            current_width)
    
    while ((square_footage(current_height, current_width) > max_sqft)):

        current_height, current_width = subtract(current_height, current_width,
            height_scale, width_scale)

    while ((square_footage(current_height + height_scale,
        current_width + width_scale) <= max_sqft)):

        current_height, current_width = add(current_height, current_width,
            height_scale, width_scale)
        
    return round(current_height, 2), round(current_width, 2), \
    round(square_footage(current_height, current_width), 2)


def up_to_max_height(current_height, current_width, height_scale, width_scale,
    max_height, max_width, max_sqft):
    '''
    calculates up to max height but not higher than max square footage unless
    max square footage == 0.
    '''
    if max_height == 0:
        return current_height, current_width, \
        square_footage(current_height, current_width)

    while ((current_height >= max_height)):
        current_height, current_width, = subtract(current_height, current_width,
            height_scale, width_scale)

    while ((max_sqft == 0) and (current_height < max_height)):
        current_height, current_width = add(current_height, current_width,
            height_scale, width_scale)    

    return current_height, current_width, \
    square_footage(current_height,current_width)


def up_to_max_width(current_height, current_width, height_scale, width_scale,
    max_height, max_width, max_sqft):
    '''
    calculates up to max width but not higher than max height or max square
    footage unless both max height and max square footage == 0.
    '''
    if max_width == 0:
        return current_height, current_width, \
        square_footage(current_height, current_width)

    while ((current_width >= max_width)):
        current_height, current_width, = subtract(current_height, current_width,
            height_scale, width_scale)

    while ((max_sqft == 0) and (current_width + width_scale <= max_width) \
        and ((current_height + height_scale <= max_height) or (max_height == 0))):
        current_height, current_width = add(current_height, current_width,
            height_scale, width_scale)    

    return current_height, current_width, \
    square_footage(current_height, current_width) 


def get_format(height, width, square_footage):
    '''
    formats arguments passed in.
    '''
    return f'{height}" | {round(height/12, 2)}\'\n' \
        + f'{width}" | {round(width/12, 2)}\'\n' \
        + f'{square_footage}\''


def calculate(data):
    '''
    Main calculation function.
    expecting list of 5 Float Values. LIST = [Current Height, Current Width,
    Max Height, Max Width, Max Square Footage]
    '''
    data = convert_to_inches(data)
    
    current_height = data[0]
    current_width = data[1]
    max_height = data[2]
    max_width = data[3]
    max_sqft = data[4] / 12
    current_sqft = square_footage(current_height, current_width)

    if (current_height == 0) and  (current_width != 0):
        return get_format(0.0, current_width, 0.0)

    elif (current_height != 0) and (current_width == 0):
        return get_format(current_height,0.0,0.0)
    
    height_scale, width_scale = scale(current_height, current_width)
    current_height, current_width, current_sqft = \
        up_to_max_square_footage(current_height, current_width, height_scale,
            width_scale, max_sqft)
    
    current_height, current_width, current_sqft = \
        up_to_max_height(current_height, current_width, height_scale,
            width_scale, max_height, max_width, max_sqft)
    
    current_height, current_width, current_sqft = \
        up_to_max_width(current_height, current_width, height_scale,
            width_scale,max_height, max_width, max_sqft)

    return get_format(round(current_height, 2), round(current_width, 2), \
    round(current_sqft, 2))

               

if __name__ == '__main__':
    test_data = ([[5, False],[5, False],[0, False],[12, True]]) + [[0, True]]
    print(calculate(test_data))