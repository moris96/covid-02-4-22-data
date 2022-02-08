import requests
import json

API_KEY = "{API key here}"
PROJECT_TOKEN = "{project token here}"
RUN_TOKEN = "{run token here}"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
        self.data = json.loads(response.text)
        return response

    def get_total_cases(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

    def get_total_recovered(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Recovered:":
                return content['value']

    def get_country_data(self, country):
        data = self.data['country']
        for content in data:
            if content['name'].lower() == country.lower():
                return content

    def get_list_of_countries(self):
        countries = []
        for country in self.data['country']:
            countries.append(country['name'].lower())
            return countries

    def update_data(self):
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)
        return response


data = Data(API_KEY, PROJECT_TOKEN)
print("Total Cases:", data.get_total_cases())
print("Total Deaths:", data.get_total_deaths())
print("Total recoveries:", data.get_total_recovered())

print(data.get_country_data('usa'))


# pandas stuff
import pandas as pd
df = pd.DataFrame.from_dict(data.get_data())
print(df.shape)
print(df.head())

