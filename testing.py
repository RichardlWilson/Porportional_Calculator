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
        self.square_footage = 0.83
        self.height_scale = 1.2
        self.width_scale = 1
        self.max_height = 0
        self.max_width = 0
        self.max_sqft = 2

    def test_convert_to_inches(self):
    	result = cal.convert_to_inches(self.info_feet)
    	self.assertEqual(result, [12*12 for num in range(5)])

    def test_scale(self):
        result = cal.scale(self.current_height, self.current_width)
        self.assertEqual(result, (1.2, 1) )  


    def test_add(self):
        result = cal.add(self.current_height, self.current_width, self.height_scale,
            self.width_scale)
        self.assertEqual(result,(13.2 ,11.0))



    def test_subtract(self):
        result = cal.subtract(self.current_height, self.current_width, self.height_scale,
            self.width_scale)
        self.assertEqual(result,(10.8 ,9.0))


    def test_square_footage(self):
        result = cal.square_footage(self.current_height, self.current_width)
        self.assertEqual(result, (0.83))
        


    def test_up_to_max_square_footage(self):
        low_max_sqft = 0.5
        high_max_sqft = 100
        
        #low
        result = cal.up_to_max_square_footage(self.current_height, self.current_width,
        self.height_scale, self.width_scale, low_max_sqft)

        self.assertEqual(result, (8.40,7.0,0.41))
        
        #high
        result = cal.up_to_max_square_footage(self.current_height, self.current_width,
        self.height_scale, self.width_scale, high_max_sqft)

        self.assertEqual(result, (130.8,109.0,99.01))


    def test_up_to_max_height(self):
        low_max_height = 6
        high_max_height = 200
        
        #low
        result = cal.up_to_max_height(self.current_height, self.current_width, self.height_scale, self.width_scale,
        low_max_height, self.max_width, 0)

        self.assertEqual(result, (4.80,4.0,0.13))
        
        #high
        result = cal.up_to_max_height(self.current_height, self.current_width, self.height_scale, self.width_scale,
        high_max_height, self.max_width, 0)

        self.assertEqual(result, (199.20,166,229.63))
        


    def test_up_to_max_width(self):
        #low
        self.max_width = 6
        result = cal.up_to_max_width(self.current_height, self.current_width, self.height_scale, self.width_scale,
        self.max_height, self.max_width, 0)

        self.assertEqual(result,(7.2,6,0.3))
        
        #high
        self.max_width = 200
        result = cal.up_to_max_width(self.current_height, self.current_width, self.height_scale, self.width_scale,
        self.max_height, self.max_width, 0)

        self.assertEqual(result, (240,200,333.33))


    def test_get_format(self):
        result = cal.get_format(self.current_height, self.current_width, self.square_footage)
        self.assertEqual(result, '12.0" | 1.0\'\n10.0" | 0.83\'\n0.83\'')


    def test_calculate_sqft(self):
        '''
        Test to check square footage calculation using only current height and current width.
        '''
        #inches = False | feet = True
        #[[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]

        #square footage only, inches selected
        result = cal.calculate([[12, False],[10, False],[0, False],[0, False], [0, True]])

        self.assertEqual(result, '12.0" | 1.0\'\n10.0" | 0.83\'\n0.83\'' )

        #square footage only, feet selected
        result = cal.calculate([[12, True],[10, True],[0, False],[0, False], [0, True]])

        self.assertEqual(result, '144.0" | 12.0\'\n120.0" | 10.0\'\n120.0\'' )

    
    def test_calculate_max_sqft_limiter_low(self):
        '''
        Test to check if calculations are correct once the max square foot limit is reached.
        Max Square Footage set to 0.5 ft.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max square footage low limit, inches selected
        result = cal.calculate([[12, False],[10, False],[0, False],[0, False], [0.5, True]])

        self.assertEqual(result, '8.4" | 0.7\'\n7.0" | 0.58\'\n0.41\'' )

        #max square footage low limit, feet selected
        result = cal.calculate([[12, True],[10, True],[0, False],[0, False], [0.5, True]])

        self.assertEqual(result, '8.4" | 0.7\'\n7.0" | 0.58\'\n0.41\'' )

    
    def test_calculate_max_sqft_limiter_high(self):
        '''
        Test to check if calculations are correct once the max square foot limit is reached.
        Max Square footage set to 200 ft.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max square footage high limit, inches selected
        result = cal.calculate([[12, False],[10, False],[0, False],[0, False], [200, True]])

        self.assertEqual(result, '184.8" | 15.4\'\n154.0" | 12.83\'\n197.58\'' )

        #max square footage high limit, feet selected
        result = cal.calculate([[12, True],[10, True],[0, False],[0, False], [200, True]])

        self.assertEqual(result, '184.8" | 15.4\'\n154.0" | 12.83\'\n197.58\'' )

    
    def test_calculate_max_height_limiter_low(self):
        '''
        Test to check if calculations are correct once the max height limit is reached.
        Max Height is set to 3 in.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max height low limit, current height and width with inches selected
        result = cal.calculate([[12, False],[10, False],[3, False],[0, False], [0, True]])

        self.assertEqual(result, '2.4" | 0.2\'\n2.0" | 0.17\'\n0.03\'' )

        #max height low limit, current height and width with feet selected
        result = cal.calculate([[12, True],[10, True],[3, False],[0, False], [0, True]])

        self.assertEqual(result, '2.4" | 0.2\'\n2.0" | 0.17\'\n0.03\'' )

    
    def test_calculate_max_height_limiter_high(self):
        '''
        Test to check if calculations are correct once the max height limit is reached.
        Max Height is set to 200 in.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max height high limit, current height and width with inches selected
        result = cal.calculate([[12, False],[10, False],[200, False],[0, False], [0, True]])

        self.assertEqual(result, '199.2" | 16.6\'\n166.0" | 13.83\'\n229.58\'' )

        #max height high limit, current height and width with feet selected
        result = cal.calculate([[12, True],[10, True],[200, False],[0, False], [0, True]])

        self.assertEqual(result, '199.2" | 16.6\'\n166.0" | 13.83\'\n229.58\'' )

    
    def test_calculate_max_width_limiter_low(self):
        '''
        Test to check if calculations are correct once the max width limit is reached.
        Max Height is set to 3 in.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max width low limit, current height and width with inches selected
        result = cal.calculate([[12, False],[10, False],[0, False],[3, False], [0, True]])

        self.assertEqual(result, '3.6" | 0.3\'\n3.0" | 0.25\'\n0.07\'' )

        #max width low limit, current height and width with feet selected
        result = cal.calculate([[12, True],[10, True],[0, False],[3, False], [0, True]])

        self.assertEqual(result, '3.6" | 0.3\'\n3.0" | 0.25\'\n0.07\'' )

    
    def test_calculate_max_width_limiter_high(self):
        '''
        Test to check if calculations are correct once the max width limit is reached.
        Max Height is set to 200 in.

        inches = False | feet = True
        [[Current_height], [Current_width], [Max_height], [Max_width], [Max_Square_footage]]
        '''

        #max width high limit, current height and width with inches selected
        result = cal.calculate([[12, False],[10, False],[0, False],[200, False], [0, True]])

        self.assertEqual(result, '240.0" | 20.0\'\n200.0" | 16.67\'\n333.4\'' )

        #max width high limit, current height and width with feet selected
        result = cal.calculate([[12, True],[10, True],[0, False],[200, False], [0, True]])

        self.assertEqual(result, '240.0" | 20.0\'\n200.0" | 16.67\'\n333.4\'' )



if __name__ == '__main__':
	unittest.main()