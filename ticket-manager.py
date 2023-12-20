import requests
import base64
from urllib.parse import quote
from datetime import datetime, timedelta

# User's API key and specific domain for authentication
api_key = "YOUR API KEY"
domain = "domain.freshdesk.com"
headers = {
    "Authorization": f"Basic {base64.b64encode(f'{api_key}:X'.encode('utf-8')).decode('utf-8')}",
    "Content-Type": "application/json"
}

# Function to fetch tickets with a search query
def search_tickets(query):
    url = f"https://{domain}/api/v2/search/tickets?query={query}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tickets = response.json()
        return tickets.get("results", [])
    else:
        print(f"Failed to search tickets. Status code: {response.status_code}")
        print(f"Error message: {response.text}")
        return []

# Function to filter tickets not updated in the last three weeks
def filter_old_tickets(tickets):
    three_weeks_ago = datetime.now() - timedelta(weeks=3)
    return [ticket for ticket in tickets if datetime.strptime(ticket['updated_at'], '%Y-%m-%dT%H:%M:%SZ') < three_weeks_ago]

# Function to add a private note to a ticket
def add_private_note(ticket_id, note):
    url = f"https://{domain}/api/v2/tickets/{ticket_id}/notes"
    data = {
        "body": note,
        "private": True
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Private note added to Ticket ID: {ticket_id}")
    else:
        print(f"Failed to add note to Ticket ID: {ticket_id}. Status code: {response.status_code}")

# Function to close a ticket
def close_ticket(ticket_id):
    url = f"https://{domain}/api/v2/tickets/{ticket_id}"
    data = {
        "status": 5  # Status code for 'Closed'
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Ticket ID: {ticket_id} closed")
    else:
        print(f"Failed to close Ticket ID: {ticket_id}. Status code: {response.status_code}")

# Main process
query = '"status:3 AND agent_id:"YOUR AGENT ID""'
encoded_query = quote(query)
tickets = search_tickets(encoded_query)
old_tickets = filter_old_tickets(tickets)

for ticket in old_tickets:
    ticket_id = ticket['id']
    add_private_note(ticket_id, "No response for 3 weeks or more. Closing out.")
    close_ticket(ticket_id)
