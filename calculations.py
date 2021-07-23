
    

def calculation(str_info):
    '''
    Calculates the max height and max width from a pre determined measurment and 
    a maximum square footage.

    info is expected to be a list of list ex: [ [ value ] , [True or False]]
    '''
    print(str_info)

    def convert_to_inches(info):
        '''
        Converts all passed arguments to inches.
        '''
        converted_info = []

        for x in info[:4]:
            if x[0] =='':
                converted_info.append(0)
            elif x[1]:
                converted_info.append(float(x[0])*12)
            else:
                converted_info.append(float(x[0]))

        if info[4][0]=='':
            converted_info.append(100**100)
        else:
            converted_info.append(float(info[4][0]) *12)

        print(f'converted info {converted_info}')               

        return converted_info


    def percentage(current_height, current_width):
        '''
        check ratio between current_height & current_width.
        '''
        if current_height > current_width:
            width_percentage = current_width / current_height
            height_percentage = 1
        else:    
            height_percentage = current_height / current_width
            width_percentage = 1

        print(f'Height Precentage: {height_percentage} / Width Percentage: {width_percentage}')

        return height_percentage, width_percentage 


    def cal_h_w_sqft(current_height, current_width,height_percentage,
        width_percentage, max_height, max_width, max_sqft):
        '''
        Calculate largest height and width until an argument returns True.
        '''
        print(f'max_height:{max_height} / current_height: {current_height} / max_sqft: {max_sqft}')

        width = current_width
        height = current_height 

        while  (((width + width_percentage) * (height + height_percentage) <= max_sqft * 12) \
            and (height + height_percentage  <= max_height) and (width + width_percentage <= max_width)):

            print('Check point', width, height)

            width += width_percentage
            height += height_percentage
        
        safe_sqft = width * height / 144

        return f'{round(height, 2)}" | {round(height / 12, 2)}\'\n' \
            + f'{round(width, 2)}" | {round(width / 12, 2)}\'\n{round(safe_sqft, 2)}\''      


    info = (convert_to_inches(str_info))  

    current_height, current_width, max_height, max_width, max_sqft = info

    if current_width == 0 or current_height ==0:
        return 'Error:\nCurrent Height Empty or\nCurrent Width Empty'

    else:    
        height_percentage, width_percentage = percentage(current_height, current_height)

        #check if max_height, max_width and max_sqft = 0.
        if max_height == 0:
            max_height = 100**100

        if max_width == 0:
            max_width= 100**100

        if max_sqft ==0:
            max_sqft_feet = 100**100
       
        return cal_h_w_sqft(current_height, current_width,height_percentage,
            width_percentage, max_height, max_width, max_sqft)    

