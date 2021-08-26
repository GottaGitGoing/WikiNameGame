import requests
import re

def FindPotentialLInks(web_url):
    r = requests.get(web_url)
    # r = requests.get("https://en.wikipedia.org/wiki/Max_Weber")
    # run a reg ex on the r.text string, this pattern works for now
    pattern = "href=\"/wiki/[A-Za-z0-9_]*"
    target_text = r.text
    # wiki_links = re.findall(pattern, target_text)
    # Here, we have a list of wikipedia links. Needs clean-up
    # for dead_link in wiki_links:
    #     dead_link = "https://en.wikipedia.org"

    # NOTE: attempting the iter path for cleaning up and turning "matches" into
    # links
    wiki_links_iter = re.finditer(pattern, target_text)
    unique_links_set = set()
    while True:
        try:
            current_href_object = next(wiki_links_iter)
            current_href_string = current_href_object.group(0)
            if current_href_string is not None \
                    and current_href_string not in unique_links_set:
                unique_links_set.add("https://en.wikipedia.org"
                                     +current_href_string[6:])

        except StopIteration:
            break

    return unique_links_set

starting_link = "https://en.wikipedia.org/wiki/Max_Weber"
print(FindPotentialLInks(starting_link))



