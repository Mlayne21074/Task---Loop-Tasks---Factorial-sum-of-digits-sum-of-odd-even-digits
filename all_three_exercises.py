# All three Python exercises in one program

print("Choose an exercise:")
print("1. Calculate factorial (N!)")
print("2. Sum all numbers from 1 to N")
print("3. Calculate the sum of odd and even numbers from 1 to N")

choice = input("Enter 1, 2, or 3: ")
n = int(input("Enter N: "))

if choice == "1":
    if n < 0:
        print("Answer: Unspecified")
    else:
        factorial = 1
        for number in range(1, n + 1):
            factorial *= number
        print("Answer:", factorial)

elif choice == "2":
    if n < 1:
        print("Answer: Unspecified")
    else:
        total = 0
        for number in range(1, n + 1):
            total += number
        print("Answer:", total)

elif choice == "3":
    if n < 1:
        print("Answer: Unspecified")
    else:
        odd_sum = 0
        even_sum = 0

        for number in range(1, n + 1):
            if number % 2 == 0:
                even_sum += number
            else:
                odd_sum += number

        print(f"Answer: Sum of Odd = {odd_sum}, Sum of Even = {even_sum}")

else:
    print("Invalid choice. Please run the program again and choose 1, 2, or 3.")
