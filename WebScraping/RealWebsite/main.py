import bookstoscrape


def caller():
    url = input("Enter the URL of the website you want to scrape: ")
    """
    Note that we scrape only books.toscrape.com!
    """
    scraping = bookstoscrape.BooksToScrape(url)
    print("\nYou can choose one piece of functionality here:")
    print("1. Get the titles of all books on the webpage.")
    print("2. Get the warning on the webpage.")
    print("3. Get the images of all books on the webpage.")
    print("4. Get the genres of all books on the webpage.")

    number = int(input("Enter the number of the needed option: "))
    if number == 1:
        scraping.get_titles()
    elif number == 2:
        scraping.get_warning()
    elif number == 3:
        scraping.get_images()
    elif number == 4:
        scraping.get_genres()
    else:
        print("Oops, check your input!")


if __name__ == "__main__":
    caller()
