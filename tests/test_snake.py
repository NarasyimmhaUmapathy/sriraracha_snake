#Discipline of TDD (test driven development)

'''
1. Write a test
2. Run the test and make sure it fails
3. Write just enough code to make the test pass
4. Run the test again and make sure it passes
5. Clean up
6. Run the tests again (regression testing)
7. Back to step 1


'''

from spicy_snake import move
import pytest

# tests that snake is moving in all directions
# test random positions
def test_move_left():
    position = (5,5) #x,y
    new_position = move(position,"left")
    assert  new_position == (4,5)

def test_move_right():
    position = (5,5) #x,y
    new_position = move(position,"right")
    assert  new_position == (6,5)

def test_move_down():
    position = (5,5) #x,y
    new_position = move(position,"down")
    assert  new_position == (5,4)

def test_move_fraction():
    #code is not supp to work
    position = (3.444,5)
    with pytest.raises(Exception):
        
        move(position,"down")
