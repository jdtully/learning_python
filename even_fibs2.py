def fibonacci_sequence(n):
    numbers = [0,1]
    while numbers[-1] < n:
        numbers.append(numbers [-1] + numbers [-2])
    return numbers
def sum_of_evens(n):
    sequence = fibonacci_sequence(n)
    sequence = [n for n in sequence if n %2 == 0]
    print(sequence)
    return sum(sequence)
print(sum_of_evens(4000000))