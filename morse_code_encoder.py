def check_input(input: str) ->bool:
  for char in input:
    if char.isalnum() or char ==" ":
      continue
    return False
  return True

def encode_to_morse(string: str) ->str:
  string = string.lower()
  encoded_list = []
  letter_to_morse: dict = {
  'a' : "•–", "b": "–•••", "c": "–•–•", "d": "–••",
  "e": "•", "f": "••–•", "g": "–•", "h": "••••",
  "i": "••", "j": "•–", "k": "–•–", "l": "•–••",
  "m": "–", "n": "–•", "o": "–", "p": "•–•",
  "q": "–•–", "r": "•–•", "s": "•••", "t": "–",
  "u": "••–", "v": "•••–", "w": "•–", "x": "–••–",
  "y": "–•–", "z": "–••",
  '1': "•––––", '2': "••–––", '3': "•••––", '4': "••••–",
  '5': "•••••", '6': "–••••", '7': "––•••", '8': "–––••",
  '9': "––––•", '0': "–––––", " ": " "
  }
  for char in string:
    encoded_list += letter_to_morse[char] + " "
  return "".join(encoded_list)

if __name__=="__main__":
  while True:
    intro = "Disclaimer: Morse code only supports (a–z, A–Z and 0–9)\n"
    option1 = "1: Encode your message to morse code."
    option2 = "2: Exit"

    print(f'{option1}\n{option2}')
    choice = int(input("Enter your choice[1 0r 2]: "))
    if choice==2:
      print("Have a nice day :)")
      break
    
    print(intro)
    message = input("Enter your message to encode: ")
    output = check_input(message)
    if output:
      print(f"\nYour message in morse code is: {encode_to_morse(message)}\n")
    else:
      print("\nError: Invalid character in your message\nTry Again!\n")