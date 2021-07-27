#unit test for porportion tool

import unittest
#import gui
import calculations as cal

class Test_Cal(unittest.TestCase):

    def test_feet_to_inches(self):
    	info = [[12,1],[12,1],[12,1],[12,1],[12,1]]
    	calculation = cal.Calculation(info)

    	result = calculation.convert_to_inches()
    	self.assertEqual(result, [12*12 for num in range(5)])
    	print('Inches to Feet: PASSED')


    def test_inches_to_inches(self):
    	info = [[12,0],[12,0],[12,0],[12,0],[12,1]]
    	calculation = cal.Calculation(info)

    	result = calculation.convert_to_inches()
    	self.assertEqual(result, [12 for num in range(4)] + [12*12])
    	print('Inches to Inches: PASSED')


    def test_for_zeros(self):
    	info = [[12,0],[12,0],[12,0],[12,0],[12,1]]
    	calculation = cal.Calculation(info)

    	result = calculation.check_zeros()
    	self.assertEqual(result, False)
    	print('Check for Zeros: OK')


    def test_scale_percentages(self):
    	info = [[12,0],[24,0],[12,0],[12,0],[12,1]]
    	calculation = cal.Calculation(info)

    	result = calculation.scale_ratio()
    	self.assertEqual(result, (0.5,1))
    	print('Scale Percentages: PASSED')


if __name__ == '__main__':
	unittest.main()