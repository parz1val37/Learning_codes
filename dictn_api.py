import requests

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5)  # wait max 5 seconds
        response.raise_for_status()
        
        data = response.json()
        meaning = data[0]["meanings"][0]   # just take first meaning
        part_of_speech = meaning["partOfSpeech"]
        definition = meaning["definitions"][0]["definition"]

        print(f"\n{word.capitalize()} ({part_of_speech}): {definition}")

    except requests.exceptions.Timeout:
        print("⏳ The request took too long. Try again later.")
    except requests.exceptions.RequestException:
        print(f"❌ Word '{word}' not found.")

# Example usage
word = input("Enter the word correctly to search its meaning: ")
get_meaning(word)