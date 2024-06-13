# This program about Secant method, with "Rename" refactoring
# This program does not consider the case where there is a root at the point of x0

def secant_method(f, x0, x1, tolerance=1e-6, max_iteration=50):
    p = None
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x0", "x1", "p"))
    for i in range(max_iteration):
        if f(x1) - f(x0) == 0:
            print("Derivative is zero at x0, method cannot continue.")
            return                                         # Returns NONE if already at point p0 there is a 0 derivative

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < tolerance:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, p))
        x0 = x1
        x1 = p
    return p


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x + 2
    x0 = 80         # First initial guess point
    x1 = 100        # Second initial guess point
    tolerance = 1e-6
    max_iteration = 20
    roots = secant_method(f, x0, x1, tolerance, max_iteration)
    print(f"\n The equation f(x) has an approximate root at x =", roots)
