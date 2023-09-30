def three_point_difference(x, y, index):
    """
    Approximate the derivative of a set of data points using three-point difference formula.

    :param x: List of x-values.
    :param y: List of corresponding y-values.
    :param index: Index of the point at which to estimate the derivative.
    :return: The estimated derivative at the specified point.
    """
    n = len(x)
    
    if index < 1 or index >= n - 1:
        raise ValueError("Index must be within the range of 1 to n-2 for three-point difference.")
    
    h = x[1] - x[0]  # Assuming evenly spaced x-values
    
    derivative = (y[index + 1] - y[index - 1]) / (2 * h)
    
    return derivative

if __name__ == "__main__":
    # Allow the user to input the x and y data points
    x_values = input("Enter x-values separated by spaces: ").split()
    y_values = input("Enter y-values separated by spaces: ").split()
    
    x_values = [float(x) for x in x_values]
    y_values = [float(y) for y in y_values]
    
    # Allow the user to input the index at which to estimate the derivative
    index = int(input("Enter the index at which to estimate the derivative: "))
    
    try:
        estimated_derivative = three_point_difference(x_values, y_values, index)
        print(f"Estimated derivative at x = {x_values[index]}: {estimated_derivative}")
    except ValueError as e:
        print(e)
