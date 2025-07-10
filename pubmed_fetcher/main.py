from pubmed_fetcher.fetcher import fetch_papers
from pubmed_fetcher.utils import filter_non_academic_papers, save_to_csv

def run(query: str, filename: str = "", debug: bool = False):
    print("Run function invoked ✅")
    papers = fetch_papers(query)

    if debug:
        print(f"\nFetched {len(papers)} papers:")
        for p in papers:
            print(p)

    filtered = filter_non_academic_papers(papers)

    if debug:
        print(f"\nFiltered {len(filtered)} non-academic papers:")
        for p in filtered:
            print(p)

    if filename:
        save_to_csv(filtered, filename)
    else:
        print("\nFinal Output:")
        for paper in filtered:
            print(paper)
