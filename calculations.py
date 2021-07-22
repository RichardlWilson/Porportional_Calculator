
    

def calculation(info):
    '''
    Calculates the max height and max width from a pre determined measurment and 
    a maximum square footage.

    info is expected to be a list of list ex: [ [ value ] , [True or False]]
    '''

    print(info)

    current_height = float(info[0][0])
    current_height_feet = info[0][1]

    current_width = float(info[1][0])
    current_width_feet = info[1][1]

    max_height = float(info[2][0])
    max_height_feet = info[2][1]

    max_width = float(info[3][0])
    max_width_feet = info[3][1]

    max_sqft = float(info[4][0])
    max_sqft_feet = info[4][1]

    
    if max_height == 0:
        max_height = 100**100

    if max_width == 0:
        max_width= 100**100

    if current_height > current_width:
        width_percentage = current_width / current_height
        height_percentage = 1
    else:    
        height_percentage = current_height / current_width
        width_percentage = 1

    width = current_width
    height = current_height 

    while  (((width + width_percentage) * (height + height_percentage) / 144) <= max_sqft \
        and (height <= max_height) and (width <= max_width)):

        width += width_percentage
        height += height_percentage
   
    safe_sqft = width * height / 144

    return f'        Height: {round(height, 2)}\n         Width: {round(width, 2)}\nSquare Footage: {round(safe_sqft, 2)}'
