#%%
# generate_html.py
from subscription import Subscription

def generate_html():
    # Import the Python code you want to execute
   
    # Create a new subscription object
    subscription = Subscription(False)

    # Generate the HTML output
    html = "<h1>Subscription Page</h1>"
    html += "<p>Status: " + subscription.status + "</p>"
    html += "<p>Type: " + subscription.type + "</p>"
    html += "<p>Cost: " + subscription.cost + "</p>"
    html += "<p>Expiration Date: " + subscription.expiration_date + "</p>"

    return html

ht = generate_html()
# %%
