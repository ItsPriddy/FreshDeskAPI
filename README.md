# Freshdesk Ticket Manager

This is a Python script to help manage tickets in Freshdesk by:

- Searching for tickets based on custom query 
- Filtering tickets that have not been updated in the past 3 weeks
- Adding a private note to the filtered tickets
- Closing out the filtered tickets

## Usage

The script requires the following:

- Freshdesk API key
- Freshdesk domain 
- Python 3
- requests module

Configure your API key, domain, and query to search for tickets in the script.

To run the script:

```
python ticket-manager.py
```

## What it Does

1. Authenticates with the Freshdesk API using the provided API key 
2. Searches for open tickets assigned to a particular agent, based on the query
3. Filters the tickets to find those not updated in the past 3 weeks
4. For each filtered ticket:
   - Adds a private note indicating no response for over 2 weeks and the ticket will be closed
   - Closes the ticket by setting the status to closed

So in summary, it allows automatically closing out tickets that have gone stale.

## Customization

The main sections to customize are:

- API credentials
- Organization's domain
- Search query 
- Filter criteria 
- Private note text

This allows adapting it to your specific Freshdesk ticket workflow.
