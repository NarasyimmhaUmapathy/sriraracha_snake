#Discipline of TDD (test driven development)

'''
1. Write a test
2. Run the test and make sure it fails
3. Write just enough code to make the test pass
4. Run the test again and make sure it passes
5. Clean up
6. Run the tests again (regression testing)
7. Back to step 1

calculate test coverage with pytest --cov


'''



from spicy_snake import move, VALID_DIRECTIONS
import pytest,random

# tests that snake is moving in all directions
# test random positions

@pytest.mark.parametrize("position,direction,expected",[((5,5),"left",(4,5)),

((5,5),"right",(6,5)), 
((5,0),"left",(4,0)),
((5,5),"up",(5,6)),
((5,5),"down",(5,4)),
((3,3),"right",(4,3))
])

 #declarators iterates functions on the go with parameters, usage for quick testing
def test_move(position,direction,expected):
    #checks if snake moves in all 4 directions
    assert move(position,direction) == expected

def test_move_invalid():
    position = move(3,5)
    with pytest.raises(Exception):
        move(position,"dummy")


def test_move_fraction():
    position = move(3.445,5)
    with pytest.raises(Exception):
        move(position,"left")

def test_move_random():
    for i in range(100):
        x = random.randint(1,10)
        y = random.randint(1,10)
        position = x,y
        new_position = move(position,"left")
        assert new_position == (x-1,y)
        

#todo check for boundaries of playing field