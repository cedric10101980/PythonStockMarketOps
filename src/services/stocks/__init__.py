import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json


def fetch_and_store_mutual_fund_data():
    url = "https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/large-cap-fund.html"
    response = requests.get(url)

    # with open('response_content.html', 'w', encoding='utf-8') as file:
    #    file.write(response.content.decode('utf-8'))

    soup = BeautifulSoup(response.content, 'html.parser')

    with open('parsed_soup.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # Find the table with id 'dataTableId'
    table = soup.find('table', id='dataTableId')
    if table:
        headers = [header.text for header in table.find_all('th')]
        rows = []
        for row in table.find_all('tr')[1:]:
            rows.append([cell.text for cell in row.find_all('td')])

        # Convert to DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # Save to CSV
        csv_file_path = 'mutual_fund_data.csv'
        df.to_csv(csv_file_path, index=False)

        # Store in vector database (assuming a function `store_csv_in_vector_db` exists)
        store_csv_in_vector_db(csv_file_path)

        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')
        return json.loads(json_data)
    else:
        error_message = {"error": "No table found with id 'dataTableId'"}
        return error_message

def store_csv_in_vector_db(csv_file_path):
    # Implement the logic to store CSV data in a vector database
    pass