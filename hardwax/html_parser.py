from bs4 import BeautifulSoup
import pandas as pd

input_file = "hardwax/spiders/products.csv"

df = pd.read_csv(input_file, usecols=['html'])

def get_description(html):
    soup = BeautifulSoup(html, "html.parser")

    description_tag = soup.find("p", class_="qt")
    description = description_tag.get_text(strip=True) if description_tag else ""
    return description

df['descriptions'] = df['html'].apply(get_description)
df['descriptions'].to_csv('descriptions.csv')