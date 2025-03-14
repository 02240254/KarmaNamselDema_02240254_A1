def main():
    while True:
        # Display the menu
        print("Select a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word counter")
        print("0. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            prime_sum_calculator()
        elif choice == '2':
            length_converter()
        elif choice == '3':
            consonant_counter()
        elif choice == '4':
            min_max_finder()
        elif choice == '5':
            palindrome_checker()
        elif choice == '6':
            word_counter()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        # Ask if user wants to try another function
        again = input("Would you like to try another function? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program. Goodbye!")
            break

def prime_sum_calculator():
    # Get input range from the user
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    # Helper function to check if a number is prime
    def is_prime(n):
        if n < 2:            # 0 and 1 are not prime numbers
            return False
        for i in range(2, int(n ** 0.5) + 1):     # Check divisibility up to square root of n
            if n % i == 0:
                return False
        return True

    # Calculate the sum of prime numbers
    prime_sum = sum(num for num in range(start, end + 1) if is_prime(num))
    print(f"The sum of prime numbers between {start} and {end} is {prime_sum}")

def length_converter():
    try:
        value = float(input("Enter the length value: "))
        direction = input("Enter direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
        if direction == 'M':
            converted = round(value * 3.28084, 2)
            print(f"{value} meters is {converted} feet")
        elif direction == 'F':
            converted = round(value / 3.28084, 2)
            print(f"{value} feet is {converted} meters")
        else:
            print("Invalid direction. Use 'M' or 'F'.")
    except ValueError:
        print("Please enter a valid numeric value.")

def consonant_counter():
    # Get a string from the user
    text = input("Enter a text string: ")

    # Count consonants
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in text if char in consonants)
    print(f"The number of consonants in the string is {count}")

def min_max_finder():
    try:
        # Get a list of numbers from the user
        numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

        # Find minimum and maximum values
        if numbers:
            print(f"Smallest: {min(numbers)}, Largest: {max(numbers)}")
        else:
            print("No numbers were entered.")
    except ValueError:
        print("Please enter valid integers.")

def palindrome_checker():
    # Get a string from the user
    text = input("Enter a text string: ").lower().replace(" ", "")     # Convert to lowercase and remove spaces

    # Check if the string is a palindrome
    print(text == text[::-1])

def word_counter():
    try:
        # Ask the user to provide a local text file path
        file_path = input("Enter the path to the text file: ")

        # Read content from the file
        with open(file_path, 'r') as file:
            text = file.read().lower()

        # Count occurrences of specific words
        words_to_count = ["the", "was", "and"]
        counts = {word: text.split().count(word) for word in words_to_count}

        # Display results
        for word, count in counts.items():
            print(f"{word}: {count}")
    except Exception as e:
        print(f"Error reading the file: {e}")

if __name__ == "__main__":
    main()
