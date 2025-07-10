import requests
from typing import List
from pubmed_fetcher.utils import parse_xml

def fetch_papers(query: str) -> List[dict]:
    # Step 1: Search for PubMed IDs using esearch
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": 20,
        "retmode": "json"
    }
    response = requests.get(search_url, params=search_params)
    response.raise_for_status()
    id_list = response.json().get("esearchresult", {}).get("idlist", [])

    if not id_list:
        print("No PubMed IDs found.")
        return []

    # Step 2: Fetch paper details using efetch
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    fetch_response = requests.get(fetch_url, params=fetch_params)
    fetch_response.raise_for_status()

    print("Fetched XML data successfully.")
    return parse_xml(fetch_response.text)
