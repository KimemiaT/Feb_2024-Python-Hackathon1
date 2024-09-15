def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    # Create an empty list to store the Fibonacci sequence
    fib_sequence = []

    # Check if n is less than or equal to 0
    if n <= 0:
        # If so, return an empty sequence
        return fib_sequence
    # Check if n is equal to 1
    elif n == 1:
        # If so, return a sequence containing only 0
        fib_sequence.append(0)
        return fib_sequence
    else:
        # If n is greater than 1, start with the first two terms 0 and 1
        fib_sequence.extend([0, 1])
        a, b = 0, 1
        # Generate subsequent terms and add them to the sequence
        for _ in range(2, n):
            c = a + b
            fib_sequence.append(c)
            # Update the values of a and b for the next iteration
            a, b = b, c
        # Return the generated Fibonacci sequence
        return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
