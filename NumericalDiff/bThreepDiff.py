import math

def backward_three_point_differentiation(f, x, h=1e-5):
    """
    Approximate the derivative of a function at a point using backward (regressive) three-point differentiation.

    :param f: The function for which to estimate the derivative.
    :param x: The point at which to estimate the derivative.
    :param h: The step size (default is 1e-5).
    :return: The estimated derivative.
    """
    derivative = (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2 * h)
    return derivative

if __name__ == "__main__":
    # Allow the user to input the function as a string
    function_str = input("Enter the function f(x) (e.g., 'math.exp(x) * math.cos(x)'): ")

    try:
        # Parse and evaluate the user-entered function
        def user_function(x):
            return eval(function_str)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    # Allow the user to input the interval bounds
    a = float(input("Enter the left bound of the interval: "))
    b = float(input("Enter the right bound of the interval: "))

    # Allow the user to input the step size
    step_size = float(input("Enter the step size: "))

    # Perform backward three-point differentiation and store intermediate results
    results = []
    x0 = a
    while x0 <= b:
        estimated_derivative = backward_three_point_differentiation(user_function, x0, step_size)
        results.append((x0, estimated_derivative))
        x0 += step_size

    # Print the table of derivatives within the interval
    print("\nDerivatives within the Interval (Backward Three-Point Differentiation):")
    print("    x     | Estimated Derivative")
    print("-" * 30)
    for x, derivative in results:
        print(f"{x:^10.4f} | {derivative:^20.6f}")
