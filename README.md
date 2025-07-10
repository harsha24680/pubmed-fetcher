# PubMed Fetcher CLI Tool

This command-line Python tool fetches research papers from PubMed based on a user-specified query and identifies papers with at least one author affiliated with a pharmaceutical or biotech company. The filtered results are exported as a CSV file.

## 📦 Features

- Fetches papers using PubMed's full query syntax
- Identifies non-academic authors using heuristic rules
- Outputs:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Authors
  - Company Affiliations
  - Corresponding Author Email
- Supports CLI options for custom queries, debug mode, and file output

### 🛠 Installation

1. **Clone the repository:**

git clone https://github.com/harsha24680/pubmed-fetcher
cd pubmed-fetcher
2. **Install dependencies using Poetry:**
poetry install
#### 🚀 Usage
**Run the tool using the get-papers-list command via Poetry:**
poetry run get-papers-list "cancer immunotherapy" --for-file results.csv
Options
-h, --help — Show usage information

-d, --debug — Enable debug logging

--for-file <filename> — Save output to CSV (prints to console if omitted)
##### 🧠 How Non-Academic Authors Are Detected
The tool uses simple heuristics to detect non-academic authors:

Affiliation string does not contain academic keywords like:
university, institute, college, school, department, hospital, research center

Affiliation does contain corporate indicators like:
pharma, biotech, inc, ltd, corp, gmbh, etc.

Email domains also help identify affiliation type
###### 🧱 Project Structure
pubmed-fetcher/
├── pubmed_fetcher/
│   ├── __init__.py              # Package initializer
│   ├── fetcher.py               # Core logic to fetch and process PubMed data
│   ├── main.py                  # Entrypoint functions for CLI
│   ├── utils.py                 # Helper functions and filters
│
├── get-papers-list.py          # CLI script (renamed from cli.py)
├── results.csv                 # Example output file
├── README.md                   # This file
├── poetry.lock                 # Poetry lock file
├── pyproject.toml              # Project config & script binding
###### 💡 Tools & Libraries Used
Typer — CLI framework

BioPython — For interacting with PubMed/Entrez API

pandas — For CSV data processing

Poetry — Dependency management and packaging

Git — Version control

OpenAI GPT — Used for development assistance and suggestions
###### ✨ Bonus (Optional)
To publish your package on Test PyPI:
 poetry build
 poetry publish -r test-pypi
Configure your token if needed:
 poetry config pypi-token.test-pypi <your-token>
###### 👨‍💻 Author
Nithin Harsha Nidigonda

GitHub: @harsha24680

LinkedIn: https://www.linkedin.com/in/nithin-harsha-nidigonda-6ab41726a

