'''
Created on 31 Aug 2021

@author: jenny
'''
import unittest
from main.notation import PPawn
from main.notation import PBishop
from main.notation import PKing
from main.notation import PKnight
from main.notation import PQueen
from main.notation import PRook

class Test(unittest.TestCase):


    def testPawn(self):
        myPawn = PPawn()
        
        isAllow = myPawn.validate_movement(1, 1,1, 3)
        assert isAllow == True 
        
        isAllow = myPawn.validate_movement(1, 1,1, 3)
        assert isAllow == False 
        
        isAllow = myPawn.validate_movement(2, 1,2, 2)
        assert isAllow == True 
        
    def testBishop(self):
        
        myBishop = PBishop()
        
        isAllow = myBishop.validate_movement(2, 4, 3, 3)
        assert isAllow == True 
        
        return 
    
    def testKing(self):
        myKing = PKing()
        
        isAllow = myKing.validate_movement(1, 1, 2, 2)
        assert isAllow == True 
        
        return 
    
    def testQueen(self):
        
        myQueen = PQueen()
        
        isAllow = myQueen.validate_movement(1, 1, 2, 2)
        assert isAllow == True 
        
        
        isAllow = myQueen.validate_movement(3, 2, 1, 4)
        assert isAllow == True 

        isAllow = myQueen.validate_movement(3, 2, 3, 4)
        assert isAllow == False         
        return 
    
    def testRook(self):
        
        myRook = PRook()
        isAllow = myRook.validate_movement(1, 1, 1, 4)
        assert isAllow == True 
        
        return 
    
    def testKight(self):
        myKight = PKnight()
        isAllow = myKight.validate_movement(3, 2, 2, 4)
        assert isAllow == True 
        
        return

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPawn']
    unittest.main()