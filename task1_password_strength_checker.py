import string

password = input("Enter your password: ")

checks = {
    "At least 8 characters": len(password) >= 8,
    "Contains uppercase letter": any(ch.isupper() for ch in password),
    "Contains lowercase letter": any(ch.islower() for ch in password),
    "Contains a number": any(ch.isdigit() for ch in password),
    "Contains special character": any(ch in string.punctuation for ch in password)
}

score = sum(checks.values())

print("\nPassword Strength:", end=" ")
if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")

print("\nFeedback:")
for message, passed in checks.items():
    print(("✓ " if passed else "✗ ") + message)
