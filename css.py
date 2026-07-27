import requests
from bs4 import BeautifulSoup
import csv


base_url = "http://quotes.toscrape.com/page/{}/"


# CSV file create
with open("quotes_all_pages.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["Quote", "Author", "Tags"])


    # Pages 1 to 11
    for page in range(1, 11):

        print("Scraping Page:", page)

        url = base_url.format(page)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")


        # select() -> all quotes
        quotes = soup.select("div.quote")


        for quote in quotes:


            # select_one() -> single quote text
            text = quote.select_one("span.text").text


            # select_one() -> single author
            author = quote.select_one("small.author").text


            # select() -> multiple tags
            tags = quote.select("a.tag")


            # tags list ko text me convert karna
            tag_list = []

            for tag in tags:
                tag_list.append(tag.text)


            tags_text = ", ".join(tag_list)


            # Save row in CSV
            writer.writerow([
                text,
                author,
                tags_text
            ])


print("Scraping Completed!")