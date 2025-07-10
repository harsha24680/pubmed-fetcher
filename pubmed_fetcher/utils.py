import pandas as pd
import xml.etree.ElementTree as ET
from typing import List

def parse_xml(xml_data: str) -> List[dict]:
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "Publication Date": article.findtext(".//PubDate/Year") or "N/A",
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": ""
        }

        for author in article.findall(".//Author"):
            affiliation = author.findtext("AffiliationInfo/Affiliation")
            lastname = author.findtext("LastName", default="Unknown")

            if affiliation:
                affil_lower = affiliation.lower()
                if any(keyword in affil_lower for keyword in [
                    "inc", "ltd", "biotech", "pharma", "corp", "solutions", "therapeutics"
                ]):
                    paper["Non-academic Author(s)"].append(lastname)
                    paper["Company Affiliation(s)"].append(affiliation)

                if "@" in affiliation and not paper["Corresponding Author Email"]:
                    paper["Corresponding Author Email"] = affiliation

        papers.append(paper)

    print(f"Total papers parsed: {len(papers)}")
    return papers

def filter_non_academic_papers(papers: List[dict]) -> List[dict]:
    filtered = [p for p in papers if p["Non-academic Author(s)"]]
    print(f"Papers after filtering non-academic: {len(filtered)}")
    return filtered

def save_to_csv(papers: List[dict], filename: str):
    if not papers:
        print("No papers to save.")
        return
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Saved {len(papers)} papers to {filename}")

