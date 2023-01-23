#%%
from typing import Optional
from datetime import datetime, timedelta

class Subscription:

    def __init__(self, is_active: bool, subscription_type: Optional[str] = None) -> None:
        self.is_active = is_active
        self.subscription_type = subscription_type
       
    def __str__(self) -> str:
        return f"Subscription(is_active={self.is_active}, subscription_type={self.subscription_type})"

    def __repr__(self) -> str:
        return f"Subscription({self.is_active!r}, {self.subscription_type!r})"

    def __bool__(self) -> bool:
        return self.is_active

    @property
    def status(self) -> bool:
        return self.is_active

    @property
    def type(self) -> Optional[str]:
        if self.is_active:
            return self.subscription_type

    @property
    def cost(self) -> float:
        if self.is_active:
            if self.subscription_type == "monthly":
                return 9.99
            elif self.subscription_type == "yearly":
                return 99.99
            else:
                return 0.0

    
    @property
    def expiration_date(self) -> Optional[datetime]:
        if self.is_active:
            if self.subscription_type == "monthly":
                return datetime.now() + timedelta(days=30)
            elif self.subscription_type == "yearly":
                return datetime.now() + timedelta(days=365)
        else:
            return None

    @expiration_date.setter
    def expiration_date(self, value: datetime) -> None:
        self._expiration_date = value

    def activate(self, subscription_type: str):
        if not self.is_active:
            if subscription_type in ["monthly", "yearly"]:
                self.is_active = True
                self.subscription_type = subscription_type
    
    def renew(self):
        if self.is_active:
            if self.subscription_type == "monthly":
                if self.expiration_date is not None:
                    self.expiration_date = datetime.now() + timedelta(days=30)
                else:
                    self.activate("monthly")
            elif self.subscription_type == "yearly":
                if self.expiration_date is not None:
                    self.expiration_date = datetime.now() + timedelta(days=365)
                else:
                    self.activate("yearly")

    def cancel(self):
        if self.is_active:
            self.is_active = False
            self.subscription_type = None
            self.expiration_date = None
    
    def change(self, subscription_type: str):
        if self.is_active and self.subscription_type:
            if subscription_type in ["monthly", "yearly"]:
                self.subscription_type = subscription_type
                if subscription_type == "monthly":
                    self.expiration_date = datetime.now() + timedelta(days=30)
                elif subscription_type == "yearly":
                    self.expiration_date = datetime.now() + timedelta(days=365)


    def is_expired(self) -> bool:
        if self.is_active:
            return datetime.now() > self.expiration_date
        else:
            return False
    
    def get_time_left(self, now: datetime = datetime.now()) -> Optional[timedelta]:
        if self.is_active:
            return self.expiration_date - now
        else:
            return None


subscription = Subscription(False)

# Check the subscription status
#print(f"Subscription active: {subscription.status}")

# Activate the subscription
subscription.activate("monthly")

# Check the subscription status and type
#print(f"Subscription active: {subscription.status}")
#print(f"Subscription type: {subscription.type}")

# Check the subscription cost and expiration date
#print(f"Subscription cost: {subscription.cost}")
#print(f"Subscription expiration date: {subscription.expiration_date}")

#print(f"Time left until expiration: {subscription.get_time_left()}")

# Change the subscription type
#subscription.change("yearly")

# Check the updated subscription type and expiration date
#print(f"Subscription type: {subscription.type}")
#print(f"Subscription expiration date: {subscription.expiration_date}")

# Renew the subscription
#subscription.renew()

# Check the updated expiration date
#print(f"Subscription expiration date: {subscription.expiration_date}")

# Cancel the subscription
#subscription.cancel()

# Check the subscription status and type
#print(f"Subscription active: {subscription.status}")
#print(f"Subscription type: {subscription.type}")

print(f"Subscription expiration date: {subscription.get_time_left()}")

# %%
