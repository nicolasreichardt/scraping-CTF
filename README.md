## Overview

This repository contains a Python script developed to uncover hidden flags as part of a Capture The Flag (CTF) competition in the context of the Hertie Workshop on "Python Bots and Scrapers." A total of 63 flags were discovered, and the first three levels have been successfully completed.

## Requirements

- Python 3.7+
- Required Python packages listed in `requirements.txt`
- Functioning Selenium: correct version Chrome and ChromeDriver, ChromeDriver accessible from your system's PATH


## How to run the script

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/scraping-ctf.git
   cd scraping-ctf
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script:
    ```bash
    python CTF_script.py
    ```

## Project Structure

```
scraping-ctf/
├── CTF_script.py          # Main script for CTF challenge
├── README.md              # This file
└── requirements.txt       # Python dependencies
```
