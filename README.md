# Automated_Research

AutoScholar AI is a modular research assistant built using the **Agentic AI approach**. It automates the process of finding, summarizing, categorizing, and critiquing academic papers using a multi-agent system powered by transformers, semantic clustering, and LLM-based techniques

##  Features

-  Search academic papers via arXiv API  
-  Summarize abstracts using Hugging Face Transformers  
-  Categorize using semantic embeddings and KMeans  
-  Generate markdown research reports  
-  Critique report structure and content
## Prerequisites
- Python 3.8 and higher
- Required libraries
- Internet Connection

##  Project Structure
```
auto_scholar_ai/
├── main.py
├── agents/
│ ├── researcher.py
│ ├── summarizer.py
│ ├── categorizer.py
│ ├── writer.py
│ └── critic.py
├── tools/
│ ├── arxiv_api.py
│ ├── text_processing.py
│ └── web_search.py
├── data/
│ ├── papers/
│ └── output/
├── requirements.txt
└── README.md
```

##  Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the project
   ``` bash
   python main.py
   ```
## Output
The output of the corresponding topic's research papers are summarized and hence stored in the corresponding output folder as a .md file

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers.


