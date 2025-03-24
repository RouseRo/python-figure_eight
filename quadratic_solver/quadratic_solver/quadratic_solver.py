import cmath

def round_complex_number(c: complex, decimal_places: int) -> complex:
    """
    Rounds the real and imaginary parts of a complex number to a specified number of decimal places.

    Parameters:
    c (complex): The complex number to be rounded.
    decimal_places (int): The number of decimal places to round to.

    Returns:
    complex: The rounded complex number.
    """
    real_part = round(c.real, decimal_places)
    imaginary_part = round(c.imag, decimal_places)
    return complex(real_part, imaginary_part)

def solve_quadratic(a:float, b:float, c:float)-> tuple[complex, complex]:
    """
    Solves the quadratic equation ax^2 + bx + c = 0 and returns the two solutions.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    tuple: A tuple containing the two solutions (x1, x2)
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two solutions using the quadratic formula
    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    # rounded_real_part_x1 = round(x1.real, 5)
    # rounded_complex_x1 = complex(rounded_real_part_x1, round(x1.imag, 5))

    # rounded_real_part_x2 = round(x2.real, 5)
    # rounded_complex_x2 = complex(rounded_real_part_x2, round(x2.imag, 5))

    return (round_complex_number(x1,5), round_complex_number(x2,5))

def main():
    # Example usage
    a = 1
    b = -3
    c = 2
    solutions = solve_quadratic(a, b, c)
    print(f"The solutions are: {solutions[0]} and {solutions[1]}")

if __name__ == "__main__":  
    main()
