
import unittest
import pandas as pd

#path = 'Orginal_classes.csv'

class Testing(unittest.TestCase):
	def setUp(self):
	    self.path = 'Orginal_classes.csv'
	    self.student_return = pd.read_csv(self.path,header=None)
	    self.original_return = pd.read_csv('Orginal_classes.csv')
	    print(self.student_return.dtypes)	
#	    with open(self.path, 'r') as f:
#            	 student_return = f.readlines()
#	    with open('Orginal_classes.csv', 'r') as f:
#            	 original_return = f.readlines()
	    #self.student_return = self.path

	def test_return(self):
            self.assertEqual(self.student_return.shape, (138, 1), "Return value shape does not match expected value")
	
if __name__=='__main__':
    unittest.main()
