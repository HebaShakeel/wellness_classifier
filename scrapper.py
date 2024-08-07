import requests
from bs4 import BeautifulSoup
import csv

def fetch_stories(url, pages, category):
    stories = []
    for page_num in range(1, pages + 1):
        page = requests.get(url.format(page_num))
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Save HTML content as XML file for each page
        with open(f'{category}_page_{page_num}.xml', 'w', encoding='utf-8') as xml_file:
            xml_file.write(soup.prettify())
        
        stories.extend([(story.text, category) for story in soup.find_all(class_='body-text')])
    return stories

anxiety_url = "https://forums.beyondblue.org.au/t5/anxiety/bd-p/c1-sc2-b1/page/{}"
depression_url = "https://forums.beyondblue.org.au/t5/depression/bd-p/c1-sc2-b2/page/{}"
ptsd_url = "https://forums.beyondblue.org.au/t5/ptsd-and-trauma/bd-p/c1-sc2-b3/page/{}"
suicidal_url = "https://forums.beyondblue.org.au/t5/suicidal-thoughts-and-self-harm/bd-p/c1-sc2-b4/page/{}"
relationship_url = "https://forums.beyondblue.org.au/t5/relationship-and-family-issues/bd-p/c1-sc3-b3/page/{}"
treatments_url = "https://forums.beyondblue.org.au/t5/treatments-health-professionals/bd-p/c1-sc3-b2/page/{}"
support_url = "https://forums.beyondblue.org.au/t5/supporting-family-and-friends/bd-p/c1-sc3-b4/page/{}"
grief_url = "https://forums.beyondblue.org.au/t5/grief-and-loss/bd-p/c1-sc4-b4/page/{}"

anxiety_stories = fetch_stories(anxiety_url, 40, 'ANXIETY')
depression_stories = fetch_stories(depression_url, 40, 'DEPRESSION')
ptsd_stories = fetch_stories(ptsd_url, 40, 'PTSD and TRAUMA')
suicidal_stories = fetch_stories(suicidal_url, 40, 'SUICIDAL THOUGHTS AND SELF HARM')
relationship_stories = fetch_stories(relationship_url, 40, 'RELATIONSHIP AND FAMILY ISSUES')
treatments_stories = fetch_stories(treatments_url, 40, 'TREATMENTS AND THERAPY')
support_stories = fetch_stories(support_url, 40, 'SUPPORTING FAMILY AND FRIENDS')
grief_stories = fetch_stories(grief_url, 40, 'GRIEF AND LOSS')

# Save stories to CSV file
with open('forum.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Stories', 'Category'])
    for story, category in anxiety_stories + depression_stories + ptsd_stories + suicidal_stories + relationship_stories + treatments_stories + support_stories + grief_stories:
        writer.writerow([story, category])

print("YOUR REQUEST IS FULFILLED")
