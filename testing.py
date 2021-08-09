#unit test for porportion tool

import unittest
#import gui
import calculations as cal

class Test_Cal(unittest.TestCase):

    def setUp(self):
        self.str_info = [['12',0],['12',0],['12',0],['12',0],['12',0]]
        self.info_feet = [[12,1],[12,1],[12,1],[12,1],[12,1]]
        self.info_inch = [[12,0],[12,0],[12,0],[12,0],[12,0]] 

        self.current_height = 12.0
        self.current_width = 10.0
        self.height_scale = 1.0
        self.width_scale = 0.83
        self.max_sqft = 2

    def test_convert_to_inches(self):

    	result = cal.convert_to_inches(self.info_feet)

    	self.assertEqual(result, [12*12 for num in range(5)])
    	print('PASSED, convert_to_inches()')


    def test_add(self):
        result = cal.add(self.current_height, self.current_width, self.height_scale,
            self.width_scale)

        self.assertEqual(result,(13.0 ,10.83))

        print('PASSED, add()')


    def test_subtract(self):
        result = cal.subtract(self.current_height, self.current_width, self.height_scale,
            self.width_scale)

        self.assertEqual(result,(11.0 ,9.17))

        print('PASSED, subtract()')


    def scale(self):
        pass
        result = cal.scale(self.current_height, self.current_width)


    def square_footage(current_height, current_width):
        pass


    def up_to_max_square_footage(current_height, current_width,
        height_scale, width_scale, max_sqft):
        pass


    def up_to_max_height(current_height, current_width, height_scale, width_scale,
        max_height, max_width, max_sqft):
        pass


    def up_to_max_width(current_height, current_width, height_scale, width_scale,
        max_height, max_width, max_sqft):
        pass


    def get_format(height, width, square_footage):
        pass


    def calculate(info):
        pass


if __name__ == '__main__':
	unittest.main()