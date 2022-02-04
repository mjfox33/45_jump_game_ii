import code_45_jump_game_ii as c

def test_example_1():
    s = c.Solution()
    assert s.jump([2,3,1,1,4]) == 2

def test_example_2():
    s = c.Solution()
    assert s.jump([2,3,0,1,4]) == 2

def test_failed_69():
    s = c.Solution()
    assert s.jump([1,2,3]) == 2