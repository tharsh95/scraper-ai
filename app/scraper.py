import requests
from bs4 import BeautifulSoup

def scrape_website(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Unable to access website")

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.get_text()

    industry = extract_industry(content)
    company_size = extract_company_size(content)
    location = extract_location(content)

    return {
        "industry": industry,
        "company_size": company_size,
        "location": location
    }

def extract_industry(content: str):
    # Simplistic pattern matching
    if "technology" in content.lower():
        return "Technology"
    return "Unknown"

def extract_company_size(content: str):
    if "small" in content.lower():
        return "Small"
    if "medium" in content.lower():
        return "Medium"
    if "large" in content.lower():
        return "Large"
    return "Unknown"

def extract_location(content: str):
    # Add more sophisticated extraction logic if needed
    return "Location not specified"
