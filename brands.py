#%%
import urllib.request
from bs4 import BeautifulSoup

# Set up the base URL and the brand names you want to get clothes from
base_url = "https://www.asos.com/men/"
brands = ["adidas", "Nike", "Topman"]

# Set up an empty list to store the clothes
clothes = []

# Loop through the brands and make a request to the store's website for each brand
for brand in brands:
  url = "{}/{}".format(base_url, brand)
  try:
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")

    # Parse the HTML to find the clothes for the current brand
    for item in soup.findAll("div", class_="item"):
      name = item.find("h3").text
      price = item.find("span", class_="price").text
      clothes.append((name, price))
  except Exception as e:
    print(f"An error occurred while trying to get clothes for the brand {brand}: {e}")

# Print the list of clothes
print(clothes[0])


# %%
