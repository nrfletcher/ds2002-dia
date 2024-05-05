# DS2002 Data Ingestion and Analysis
* Author: Riley Fletcher
* Focus: API Requests
* Date: 5/5/2024

## Benchmarks
The goal of this project is as follows:
* Make an API request once a minute for exactly 1 hour.
* Persist retrieved data into a database (SQLite was chosen for this project).
* Use data analysis techniques to describe patterns in the data.
* Explain the patterns in the data over time.

## Instructions
If you would like to build this project from scratch, perform the following (note that a SQLite3 installation is expected):
1. Run "pip install -r requirements.txt" to get necessary Python libraries
```python
pip install -r requirements.txt
```
2. Create a ".env" file in the root of the project
```bash
touch .env
```
3. Inside, have a line with the format "API_URL={insert URL here}" where the URL is the API URL provided in the project writeup
```bash
echo "API_URL={URL of API}" >> .env
```
4. Run "python api_requester.py" which will hit the API once a minute for an hour
```python
python api_requester.py
```
5. Run "python db_query.py" to query results into a file data.json (this will be already be populated in the repo)
```python
python db_query.py
```
6. Run the code blocks in the "notebook.ipynb" file to see visualizations based off the collected API data (this is also already prepopulated in the repo by default).

## Data Trends
In "notebook.ipynb" there is a graph visualization of both factor over time as well as pi over time.
<br>
<br>
There appears to be two trends present in the data:
1. Factor value over time consistently rises until it hits (at least in this case) 2000000 before resetting back to 0 and going again.
2. Pi appears to be consistent at 3.14 until roughly the same time as factor starts to 0 again it jumps 4.0, goes back to 3.14 (with a bit of noise) and stays constant again.
3. Presumably, these trends will continue repeatedly. Whether or not it will always be 4.0 and 2000000 is impossible to tell with multiple tests, but we can extrapolate at least these two trends exist in the collected data.
4. It would certainly appear there is a correlation between factor and pi, but it is interesting that while factor increases consistently, pi stays at 3.14 until the same time factor resets to 0. For this reason, I do not believe their is a mathematical function behind these numbers, but it is possible. I am not aware of a function that would leave pi constant but have factor increase, but it is certainly a possibility that there is a function capable of this.