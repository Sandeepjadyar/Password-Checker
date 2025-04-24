import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 0

    if not length_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not digit_error:
        score += 1
    if not special_char_error:
        score += 1

    # Feedback based on score
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")
    print("\n--- Feedback ---")
    if length_error:
        print("❌ Password should be at least 8 characters long.")
    if uppercase_error:
        print("❌ Add at least one uppercase letter.")
    if lowercase_error:
        print("❌ Add at least one lowercase letter.")
    if digit_error:
        print("❌ Include at least one number.")
    if special_char_error:
        print("❌ Use at least one special character (!@#$ etc.)")
    if strength == "Strong":
        print("✅ Great job! Your password is strong.")

# Main function
def main():
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter your password: ")
    check_password_strength(user_password)

if __name__ == "__main__":
    main()
