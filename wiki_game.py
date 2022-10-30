import wikipedia as w

try:
    page = w.page(w.random())
except w.exceptions.DisambiguationError as DE:
    page = w.page(DE.options[0])
print(f"The current page is: {page.title}\n")

guess_count = 0
while page.title != "University of Zurich":
    print(f"The current page is: {page.title}\n")
    for i, link in enumerate(page.links):
        print(f"{i}: {link}")
    print(f"The current page is: {page.title}\n")
    number = int(input("choose your link: "))
    
    try:
        page = w.page(page.links[number], auto_suggest=False)
    except w.exceptions.DisambiguationError as DE:
        print("Disambiguation error. Options:\n")
        for i, option in enumerate(DE.options):
            print(f"{i}: {option}")
        number = int(input("Your choice: "))
        page=w.page(DE.options[number], auto_suggest=False)
    
    guess_count += 1
        # except:
            # number = int(input("something went wrong, try another one: "))
        
print(f"You Won!!\nYou needed {guess_count} attepts")