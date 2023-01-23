#%%


# Import the Subscription class
from subscription import Subscription

# Create a new subscription
subscription = Subscription(False)

# Check the subscription status
print(f"Subscription active: {subscription.status}")

# Activate the subscription
subscription.activate("monthly")

# Check the subscription status and type
print(f"Subscription active: {subscription.status}")
print(f"Subscription type: {subscription.type}")

# Check the subscription cost and expiration date
print(f"Subscription cost: {subscription.cost}")
print(f"Subscription expiration date: {subscription.expiration_date}")

# Check the time left until the subscription expires
print(f"Time left until expiration: {subscription.get_time_left()}")

# Change the subscription type
#subscription.change("yearly")

# Check the updated subscription type and expiration date
print(f"Subscription type: {subscription.type}")
print(f"Subscription expiration date: {subscription.expiration_date}")

# Renew the subscription
subscription.renew()

# Check the updated expiration date
print(f"Subscription expiration date: {subscription.expiration_date}")

# Cancel the subscription
#subscription.cancel()

# Check the subscription status and type
print(f"Subscription active: {subscription.status}")
print(f"Subscription type: {subscription.type}")

# %%
