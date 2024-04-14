import requests
from bs4 import BeautifulSoup


url = 'https://in.bookmyshow.com/buytickets/prasads-multiplex-hyderabad/cinema-hyd-PRHN-MT/20231221'  

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

events = soup.find_all('div', class_='event-info') 

# Extract details from each event
for event in events:
    event_title = event.find('h2', class_='event-title').text.strip()
    event_date = event.find('span', class_='event-date').text.strip()
    ticket_info = event.find('div', class_='ticket-info').text.strip()

    # Print or store the extracted information
    print(f"Event Title: {event_title}")
    print(f"Event Date: {event_date}")
    print(f"Ticket Info: {ticket_info}")
    print("-----------------------------------")
