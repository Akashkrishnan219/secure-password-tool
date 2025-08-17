# secure-password-tool
A secure, customizable password generator with built-in strength analysis written in Python.
✨ Features

Customizable Options: Choose to include/exclude uppercase, lowercase, digits, and symbols
Guaranteed Inclusion: Ensures at least one character from each selected type
Strength Analysis: Real-time password strength checker with improvement suggestions
User-Friendly: Interactive command-line interface with input validation
Flexible Length: Generate passwords from 8 to 50 characters

🚀 How to Use

Clone the repository:
bashgit clone https://github.com/Akashkrishnan219/password-generator.git
cd password-generator

Run the generator:
bashpython password_generator.py

Follow the prompts:

Choose your desired password length (8-50 characters)
Select which character types to include
Get your generated password with strength analysis



📋 Example Output
=== Password Generator ===

Enter password length (8-50): 16
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Your password is: K9$mP2#vL8@nQ4!r
Password Strength: Strong
🛡️ Security Features

Cryptographically Secure: Uses Python's random module for password generation
No Storage: Passwords are not saved or logged anywhere
Strength Validation: Checks against common security requirements:

Minimum length recommendations
Character variety requirements
Provides specific improvement suggestions



🔧 Requirements

Python 3.6 or higher
No external dependencies (uses only standard library)

📝 Code Structure

generate_password(): Core password generation with guaranteed character inclusion
check_password_strength(): Analyzes password strength and provides feedback
get_yes_no(): Input validation for user preferences
get_password_length(): Length input with validation

🤝 Contributing
Feel free to fork this project and submit pull requests for any improvements!
📄 License
This project is open source and available under the MIT License.
