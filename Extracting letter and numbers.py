Mixed = input("Enter mixed letters and numbers: ")

def extract_from(x):
    if len(Mixed)==0:
        print("Nothing Entered")
    else:
        try:
            letters = [letter for letter in x if letter.isalpha()]
            if len(letters)!=0:
                print(f"List of all the letters is: {letters}")

            numbers = [number for number in x if number.isdigit()]
            if len(numbers)!=0:
                print(f"List of all the numbers is: {numbers}")
            
            others = [other for other in x if other.isdigit()==False and other.isalpha()==False]
            if len(others)!=0:
                print(f"Other Special characters is: {others}")
        except Exception as e:
            print(f"ERROR: {e}")

extract_from(Mixed)
print("\n-----*---*-----\n")
#----- Further it can be modified to give unique letters, numbers or special characters or to give how many numbers, letters and special characters are present ----
#--------- EXAMPLE  ----
def count_char(x):
    if len(x)==0:
        return
    else:
        try:
            letters = [letter for letter in x if letter.isalpha()]
            if len(letters)!=0:
                print(f"No of unique letters: {len(set(letters))}")

            numbers = [number for number in x if number.isdigit()]
            if len(numbers)!=0:
                print(f"No of unique digits: {len(set(numbers))}")
            
            others = [other for other in x if other.isdigit()==False and other.isalpha()==False]
            if len(others)!=0:
                print(f"No of unique Special character: {len(set(others))}")
        except Exception as e:
            print(f"ERROR: {e}")

count_char(Mixed)