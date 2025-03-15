import math

def display_menu():
    while True:
        print("Select an option (1-6):")
        print("1. Sum of prime numbers \n2. Length unit conversion \n3. Count consonants in a string \n4. Find min and max values \n5. Palindrome check \n6. Count word frequency \n0. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            def is_prime(n):
                if n < 2:
                    return False
                for j in range(2, int(n**0.5) + 1):
                    if n % j == 0:
                        return False
                return True
            
            def prime_sum_in_range(start, end):
                return sum(num for num in range(start, end + 1) if is_prime(num))
            
            start_range = int(input("Enter the start of the range: "))
            end_range = int(input("Enter the end of the range: "))
            print("Sum of prime numbers in range:", prime_sum_in_range(start_range, end_range))
        
        elif choice == 2:
            length = float(input("Enter the length value: "))
            unit_type = input("Enter conversion type (M/F): ")
            
            if unit_type.upper() == "M":
                converted_value = round(length * 3.28084, 2)
            elif unit_type.upper() == "F":
                converted_value = round(length / 3.28084, 2)
            else:
                converted_value = "Invalid conversion type"
                
            print(f"Converted length: {converted_value}")
        
        elif choice == 3:
            input_text = input("Enter a string of text: ")
            consonant_count_func = lambda text: sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")
            print("Total consonants:", consonant_count_func(input_text))
        
        elif choice == 4:
            def get_min_max():
                while True:
                    try:
                        num_count = int(input("How many numbers will you input? "))
                        if num_count > 0:
                            break
                        print("Please enter a number greater than 0.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                num_list = [float(input(f"Enter number {i + 1}: ")) for i in range(num_count)]
                return min(num_list), max(num_list)
            
            minimum, maximum = get_min_max()
            print(f"Minimum value: {minimum}, Maximum value: {maximum}")
        
        elif choice == 5:
            def is_palindrome_check(word):
                cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
                return cleaned_word == cleaned_word[::-1]
            
            phrase_input = input("Enter a word or phrase: ")
            print("Is it a palindrome?", is_palindrome_check(phrase_input))
        
        elif choice == 6:
            def word_frequency_from_file(file_path):
                target_words = ["the", "was", "and"]
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read().lower().split()
                        return {word: content.count(word) for word in target_words}
                except FileNotFoundError:
                    print("Error: File not found.")
                    return {}
            
            file_path_input = input("Enter the file path: ")
            print("Word frequencies:", word_frequency_from_file(file_path_input))
        
        elif choice == 0:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please choose a valid option.")

if __name__ == "__main__":
    display_menu()
