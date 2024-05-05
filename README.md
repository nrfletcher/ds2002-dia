# DS2002 Data Ingestion and Analysis
* Author: Riley Fletcher
* Focus: API Requests
* Date: 5/5/2024

## API Requests
The first part of this project involves making requests to an API provided in the writeup.
<br>
This URL is stored inside of a .dotenv file which exists only locally.
<br>
<br>
In order to pull and test this code locally, you must do the following:
1. Import python-dotenv (as well as requests and json if not already installed)
2. Create a '.dotenv' file in the root of the project
3. Inside, have a line with the format "API_URL={insert URL here}" where the URL is the API URL provided in the writeup.

## Benchmarks
The goal of this project is as follows:
* Make an API request once a minute for exactly 1 hour.
* Persist retrieved data into a database (SQLite was chosen for this project).
* Use data analysis techniques to describe patterns in the data.
* Explain the patterns in the data over time.

# Instructions
Follow these steps, from scratch, to test this project:
1. pip install -r requirements.txt
2. You can do "python data_visualizer.py >> data.json" to query results into a file data.json