import pytest
from quadratic_solver import quadratic_solver

def test_solve_quadratic_1():
    # Test case 1: Real and distinct roots
    a, b, c = 1, -3, 2
    assert quadratic_solver.solve_quadratic(a, b, c) == (2.0, 1.0)

def test_solve_quadratic_2():
    # Test case 2: Real and equal roots
    a, b, c = 1, -2, 1
    assert quadratic_solver.solve_quadratic(a, b, c) == (1.0, 1.0)

def test_solve_quadratic_3():
    # Test case 3: Complex roots
    a, b, c = 1, 2, 5
    assert quadratic_solver.solve_quadratic(a, b, c) == (-1+2j, -1-2j)

def test_solve_quadratic_4():
    # Test case 4: Zero coefficient for 'a'
    with pytest.raises(ZeroDivisionError):
        quadratic_solver.solve_quadratic(0, 2, 3)

def test_solve_quadratic_5():
    # Test case 5: Negative discriminant
    a, b, c = 1, 2, 5   
    assert quadratic_solver.solve_quadratic(a, b, c) == (-1+2j, -1-2j)  

def test_solve_quadratic_6():
    # Test case 6: Positive discriminant
    a, b, c = 1, -3, 2  
    assert quadratic_solver.solve_quadratic(a, b, c) == (2.0, 1.0) 

def test_solve_quadratic_7():
    # Test case 7: Zero discriminant
    a, b, c = 1, -2, 1  
    # print("Inputs:", a, b, c, "Outputs:", quadratic_solver.solve_quadratic(a, b, c))
    assert quadratic_solver.solve_quadratic(a, b, c) == (1.0, 1.0)
    
def test_solve_quadratic_8():
    # Test case 8: Complex discriminant
    a, b, c = 1, 2, 5
    assert quadratic_solver.solve_quadratic(a, b, c) == (-1+2j, -1-2j)

def test_solve_quadratic_9():
    # Test case 9: Large coefficients
    a, b, c = 1000000, -3000000, 2000000
    assert quadratic_solver.solve_quadratic(a, b, c) == (2.0, 1.0)

def test_solve_quadratic_10():
    # Test case 10: Small coefficients
    a, b, c = 0.0001, -0.0003, 0.0002
    assert quadratic_solver.solve_quadratic(a, b, c) == (2.0, 1.0)
