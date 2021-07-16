# #square foot calculation

def get_info():
    '''
    captures the initial measurment & max sqft.
    '''
    max_sqft = float(input('Enter max Sqft: '))
    height_constraint = float(input('Enter Max Height: '))
    width_constraint = float(input('Enter Max Width: '))
    init_height = float(input('Enter Height: '))
    init_width = float(input('Enter Width: '))
    

    return max_sqft, height_constraint, width_constraint, init_height, init_width

def calculation(info):
    '''
    Calculates the max height and max width from a pre determined measurment and 
    a maximum square footage.
    '''
    max_sqft, height_constraint, width_constraint, init_height, init_width = info

    if height_constraint == 0:
        height_constraint = 100**100
    if width_constraint == 0:
        width_constraint == 100**100    
    

    if init_height > init_width:
        width_percentage = init_width / init_height
        height_percentage = 1
    else:    
        height_percentage = init_height / init_width
        width_percentage = 1

    width = init_width
    height = init_height    

    while  (((width + width_percentage) * (height + height_percentage) / 144) <= max_sqft) \
        and (height <= height_constraint) and (width <= width_constraint):
        
        print('Check point')
        width += width_percentage
        height += height_percentage
    
    safe_sqft = width * height / 144
    return f'New Sqft: {safe_sqft}, {height} x {width}'

print(calculation(get_info()))    












# def get_info():
#     sqft_largest = float(input('Enter SqFt: '))

#     height = float(input('Enter Height: '))

#     width = float(input('Enter Width: '))
    
#     return sqft_largest, height, width


# def calculate(info):

#     sqft_largest, height, width = info
    
#     sqft_check = height * width / 144

#     while not sqft_check >= sqft_largest:

#         sqft_check = ((height + 1) * (width + 1)) / 144

#         if sqft_check > sqft_largest:
#             break

#         else:
#             height += 1
#             width += 1  
    
#     return f'max sqft:{height*width/144} , {height} x {width}'


# print(calculate(get_info()))       



