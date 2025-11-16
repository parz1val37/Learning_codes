from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def password_strength(password):
  result = zxcvbn(password)
  score = result['score']  # 'Score' - (0 to 4)

  if score==3:
    response = "Strong enough passsword: score of 3"
  elif score == 4:
    response = "Very strong password: score of 4"
  else:
    feedback = result.get('feedback')
    warning = feedback.get('warning')
    suggestions = feedback.get('suggestions')
    response = f"Weak password: score of {score}\nWarning: {warning}\nSuggestions: {suggestions[0]}"
  return response

def hash_password(password):
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(password.encode(), salt)
  return hashed

def verify_password(password_attempt, hashed):
  if bcrypt.checkpw(password_attempt.encode(), hashed):
    return "Password is correct. Access granted!"
  return "Incorrect password. Access denied!"

if __name__ == "__main__":
  while True:
    password1 = getpass("Enter a password to check strength: ")
    print(password_strength(password1))
    if password_strength(password1).startswith("Weak"):
      print("Choose a stronger password.")
    else:
      break
  hashed_password = hash_password(password1)
  print("Hashed password: ", hashed_password)
  attempt = getpass("Re-enter the password to verify: ")
  print(verify_password(attempt, hashed_password))