import requests
from bs4 import BeautifulSoup
import csv

def fetch_stories(url, pages):
    stories = []
    for page_num in range(1, pages + 1):
        page = requests.get(url.format(page_num))
        soup = BeautifulSoup(page.content, 'html.parser')
        stories.extend([story.text for story in soup.find_all(class_='body-text')])
    return stories

anxiety_url = "https://forums.beyondblue.org.au/t5/anxiety/bd-p/c1-sc2-b1/page/{}"
depression_url = "https://forums.beyondblue.org.au/t5/depression/bd-p/c1-sc2-b2/page/{}"

anxiety_stories = fetch_stories(anxiety_url, 10)
depression_stories = fetch_stories(depression_url, 10)

with open('forum.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stories'])
    for story in anxiety_stories + depression_stories:
        writer.writerow([story])

print("Comments from 10 pages have been written to forum.csv")
