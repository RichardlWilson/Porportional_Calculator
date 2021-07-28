
    

class Calculation:
    '''
    Calculates the max height and max width from a pre determined measurment and 
    a maximum square footage.

    info is expected to be a list of list.

    str_info = [[str(value), int(0 or 1)],[str(value), int(0 or 1)],
                [str(value), int(0 or 1)],[str(value), int(0 or 1)],
                [str(value), int(0 or 1)]]
    '''

    def __init__(self, str_info):

        class Entry:
            def __init__(self, number, bool_value):
                self.number = number
                self.bool_value = bool_value
                self.scale_increase = 0

            def __str__(self):
                return str(self.number)

            def __float__(self):
                return self.number

            def __bool__(self):
                return self.bool_value
   

        check_empty = lambda entry: 0 if entry == '' else float(entry)

        self. current_height =  Entry(check_empty(str_info[0][0]),
            bool(str_info[0][1]))

        self.current_width = Entry(check_empty(str_info[1][0]),
            bool(str_info[1][1]))

        self.max_height = Entry(check_empty(str_info[2][0]),
            bool(str_info[2][1]))

        self.max_width = Entry(check_empty(str_info[3][0]),
            bool(str_info[3][1]))

        self.max_sqft = Entry(check_empty(str_info[4][0]), True)

        self.entry_list = [self.current_height, self.current_width,
            self.max_height, self.max_width, self.max_sqft]


    def convert_to_inches(self):
        '''
        Converts all passed arguments to inches. 
        '''
        #return converted_entries

        for entry in self.entry_list:
            if entry.bool_value:
                entry.number *= 12
                    
        return [num.number for num in self.entry_list]


    def check_zeros(self):
        '''
        Checks is max_height, max_width or max_sqft equal zero. If so, then
        change them to an un reachable limit.
        '''
        if self.current_width.number == 0 or self.current_height.number == 0:
            return True

        # if (self.max_height == 0) and (self.max_width == 0) and
        #   (self.max_sqft == 0):
        #     print('all max zeros Now', self.max_height, self.max_width,
        #    self.max_sqft)
        #     return True

        if not self.max_height.number:
            self.max_height.number = 2000000

        if not self.max_width.number:
            self.max_width.number = 2000000

        if not self.max_sqft.number:
            self.max_sqft.number = 2000000

        return False


    def scale_ratio(self):
        '''
        Get ratio between current_height and current_width.
        '''
        if self.current_height.number > self.current_width.number:
            self.current_height.scale_increase = 1
            self.current_width.scale_increase = self.current_width.number\
             / self.current_height.number
        else:
            self.current_height.scale_increase = self.current_height.number \
            / self.current_width.number
            self.current_width.scale_increase = 1

        return self.current_height.scale_increase, self.current_width.scale_increase


    def cal_entries(self):

        if self.max_height.number == 2000000 and self.max_width.number == 2000000 \
            and self.max_sqft.number == 2000000:

            return f'{round(self.current_height.number, 2)}" | '\
                + f'{round(self.current_height.number / 12, 2)}\'\n' \
                + f'{round(self.current_width.number, 2)}" | '\
                + f'{round(self.current_width.number / 12, 2)}\'\n' \
                + f'{round(self.current_height.number * self.current_width.number / 144 , 2)}\''
        

        while (((self.current_height.number + self.current_height.scale_increase) \
            * (self.current_width.number + self.current_width.scale_increase) \
             / 144 <= self.max_sqft.number / 12) \
            and (self.current_height.number + self.current_height.scale_increase \
                <= self.max_height.number) \
            and (self.current_width.number + self.current_width.scale_increase \
                <= self.max_width.number)):

            self.current_height.number += self.current_height.scale_increase
            self.current_width.number += self.current_width.scale_increase

            print(self.current_height, self.current_width,
                self.current_height.scale_increase,
                self.current_width.scale_increase,
                self.max_sqft)

        safe_sqft = (self.current_height.number * self.current_width.number / 144)

        return f'{round(self.current_height.number, 2)}" | '\
            + f'{round(self.current_height.number / 12, 2)}\'\n' \
            + f'{round(self.current_width.number, 2)}" | '\
            + f'{round(self.current_width.number / 12, 2)}\'\n' \
            + f'{round(safe_sqft, 2)}\''


    def compute(self):
        self.convert_to_inches()
        zeros = self.check_zeros()

        if zeros:
            return 'Error:\nCurrent Height Empty or\nCurrent Width Empty'
        else:    
            self.scale_ratio()

            return self.cal_entries()          

