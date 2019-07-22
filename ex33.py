numbers = []


def fill_numbers(start, stop, step):
    i = start
    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


fill_numbers(0, 6, 1)
print("The numbers: ")

for num in numbers:
    print(num)
