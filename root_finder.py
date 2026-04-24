class RootFinder:
    def __init__(self, func, tolerance=1e-7, max_iterations=1000):
        self.func = func  # The mathematical function
        self.tolerance = tolerance  # Error tolerance
        self.max_iterations = max_iterations  # Maximum iterations allowed

    @staticmethod
    def dichotomy(func, a, b, tolerance=1e-7, max_iterations=1000):
        if func(a) * func(b) >= 0:
            raise ValueError('The function must have different signs at the interval endpoints.')
        iterations = 0
        while (b - a) / 2 > tolerance and iterations < max_iterations:
            midpoint = (a + b) / 2
            if func(midpoint) == 0:
                return midpoint  # Found exact root
            elif func(a) * func(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            iterations += 1
        return (a + b) / 2  # Return midpoint as the best root found

    @staticmethod
    def newton_raphson(func, derivative, initial_guess, tolerance=1e-7, max_iterations=1000):
        x = initial_guess
        for _ in range(max_iterations):
            fx = func(x)
            if abs(fx) < tolerance:
                return x  # Found root
            dfx = derivative(x)
            if dfx == 0:
                raise ValueError('Derivative is zero. No solution found.')
            x -= fx / dfx  # Update guess
        raise ValueError('Max iterations exceeded. No root found.')

    @staticmethod
    def validate_interval(func, a, b):
        # Check continuity and monotonicity in the interval [a, b]
        # This is a basic validation, more checks can be implemented as required
        delta = 1e-5  # A small number to calculate differences
        for x in [a + i * delta for i in range(int((b-a)/delta) + 1)]:
            if not (a <= x <= b):  # Check if x is within the interval
                raise ValueError('Function is not valid in the specified interval.')  
            # Add checks for continuity and monotonicity if required...

# Usage examples:
if __name__ == '__main__':
    import math

    # Define a function and its derivative for Newton-Raphson
    def f(x):
        return math.exp(x) - x**2  # Example function
    def df(x):
        return math.exp(x) - 2*x  # Derivative of the function

    root_finder = RootFinder(f)
    print('Root by Dicotomy:', root_finder.dichotomy(f, 0, 2))  # Example call
    print('Root by Newton-Raphson:', root_finder.newton_raphson(f, df, initial_guess=1))  # Example call
