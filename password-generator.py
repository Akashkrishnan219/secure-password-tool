import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a password with custom options - guaranteed to include selected types"""
    characters = ""
    password_list = []
    
    # Build character set and ensure at least one of each selected type
    if use_uppercase:
        characters += string.ascii_uppercase
        password_list.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        characters += string.ascii_lowercase
        password_list.append(random.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password_list.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password_list.append(random.choice(string.punctuation))
    
    if not characters:
        print("Error: You must select at least one character type!")
        return None
    
    # Fill the rest of the password
    remaining_length = length - len(password_list)
    for i in range(remaining_length):
        password_list.append(random.choice(characters))
    
    # Shuffle so required chars aren't always at start
    random.shuffle(password_list)
    
    # Convert list to string
    password = ''.join(password_list)
    
    return password

def check_password_strength(password):
    """Check and return password strength"""
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Consider using at least 12 characters")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Add numbers")
    
    # Check for symbols
    if any(c in string.punctuation for c in password):
        strength += 1
    else:
        feedback.append("Add special characters")
    
    # Determine strength level
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

def get_yes_no(prompt):
    """Get yes/no answer from user"""
    while True:
        answer = input(prompt + " (y/n): ").lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please enter y or n")

def get_password_length():
    """Get desired password length from user"""
    while True:
        try:
            length = int(input("Enter password length (8-50): "))
            if 8 <= length <= 50:
                return length
            else:
                print("Please enter a number between 8 and 50")
        except ValueError:
            print("Please enter a valid number")

# Main program
if __name__ == "__main__":
    print("=== Password Generator ===\n")
    
    # Get user preferences
    length = get_password_length()
    use_uppercase = get_yes_no("Include uppercase letters?")
    use_lowercase = get_yes_no("Include lowercase letters?")
    use_digits = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols?")
    
    # Generate password
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    if password:
        print(f"\nYour password is: {password}")
        
        # Check strength
        strength, feedback = check_password_strength(password)
        print(f"Password Strength: {strength}")
        
        if feedback:
            print("\nTo improve your password:")
            for suggestion in feedback:
                print(f"  - {suggestion}")
