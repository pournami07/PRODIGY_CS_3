import re

def password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Criteria for password strength
    length_criteria = 10
    uppercase_criteria = False
    lowercase_criteria = False
    digit_criteria = False
    special_character_criteria = False

    # Check length
    if len(password) >= length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least {} characters long.".format(length_criteria))

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        uppercase_criteria = True
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        lowercase_criteria = True
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
        digit_criteria = True
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
        special_character_criteria = True
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback based on score
    if score == 5:
        feedback.append("Password is strong.")
    elif score >= 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")

    return score, feedback

# Example usage
password = input("Enter your password: ")
score, feedback = password_strength(password)
print("Strength Score:", score)
print("Feedback:")
for message in feedback:
    print("-", message)
