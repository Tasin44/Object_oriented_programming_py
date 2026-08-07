
"""
#================================================================================
  TOPIC 19: OBSERVER PATTERN
#================================================================================

  WHAT IS IT?
  -----------
  The Observer pattern defines a one-to-many dependency between objects. 
  When one object (the Subject) changes its state, all its dependents (the 
  Observers) are automatically notified and updated.

  REAL-WORLD ANALOGY:
  -------------------
  Think of a YouTube Channel and Subscribers.
  - Subject: The YouTube Channel.
  - Observers: The Subscribers.
  When the Channel uploads a new video, it doesn't manually find every person. 
  Instead, it broadcasts a notification to all its subscribers.

  WHEN TO USE IT:
  ---------------
  - Event handling systems.
  - UI frameworks (button clicks notify listeners).
  - Real-time data feeds (e.g., stock market tickers).

#================================================================================
"""

# ============================================================
# Step 1: Create the Subject (The Publisher)
# ============================================================

class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = [] # List to hold all observers
        self.latest_video = None

    def subscribe(self, observer):
        if observer not in self.subscribers:
            self.subscribers.append(observer)
            print(f"  [+] {observer.name} subscribed to {self.name}.")

    def unsubscribe(self, observer):
        if observer in self.subscribers:
            self.subscribers.remove(observer)
            print(f"  [-] {observer.name} unsubscribed from {self.name}.")

    def upload_video(self, video_title):
        self.latest_video = video_title
        print(f"\n[{self.name}] Uploaded new video: '{self.latest_video}'")
        # Notify all observers about the new state!
        self.notify_all()

    def notify_all(self):
        for subscriber in self.subscribers:
            # Call the 'update' method on every observer
            subscriber.update(self.name, self.latest_video)


# ============================================================
# Step 2: Create the Observers (The Subscribers)
# ============================================================
from abc import ABC, abstractmethod

class SubscriberInterface(ABC):
    @abstractmethod
    def update(self, channel_name, video_title):
        pass


class User(SubscriberInterface):
    def __init__(self, name):
        self.name = name

    def update(self, channel_name, video_title):
        # This is the callback method that gets executed when the Subject notifies us.
        print(f"    🔔 Notification for {self.name}: {channel_name} uploaded '{video_title}'!")


print("=== Observer Pattern ===")

# Create Subject
tech_channel = YouTubeChannel("TechWithTasin")

# Create Observers
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

# Subscribe them
tech_channel.subscribe(user1)
tech_channel.subscribe(user2)
tech_channel.subscribe(user3)

# Trigger an event! All 3 users will be notified automatically.
tech_channel.upload_video("Python OOP Masterclass")

# Bob decides to unsubscribe
tech_channel.unsubscribe(user2)

# Trigger another event! Only Alice and Charlie get notified.
tech_channel.upload_video("Understanding Design Patterns")

"""
SUMMARY:
---------
- The Subject maintains a list of Observers.
- The Subject provides methods to subscribe/unsubscribe.
- When the Subject changes state, it loops through its list and calls the `update()` method on all Observers.
- Promotes decoupling: The Subject doesn't need to know *who* the observers are, as long as they implement `update()`.
"""
