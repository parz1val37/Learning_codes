import wikipedia
import webbrowser

topic = input("Enter a topic to search: ")

try:
    # Get summary
    summary = wikipedia.summary(topic, sentences=4)
    print("\nResult:\n")
    print(summary)

    # Ask if user wants full page
    choice = input("\nDo you want to open the full Wikipedia page? (yes/no): ").lower()
    if choice == "yes":
        page = wikipedia.page(topic)
        webbrowser.open(page.url)

except wikipedia.exceptions.DisambiguationError as e:
    print("Your search was too broad.")
    # print(e.options)
except wikipedia.exceptions.PageError:
    print("No page found for that topic.")