#Bildirim sınıfları 

from datetime import datetime

# Base Class
class Notification:
    def __init__(self, message):
        #Attiribute'lar 
        self.message = message 
        self.created_at = datetime.now()

    def send(self):
        # Base method (override edilecek)
        print("Genel bildirim gönderildi.")

    def __str__(self):
         #Bildirim mesajını döndürür 
        return f"[{self.created_at}] {self.message}"

    def __len__(self):
        return len(self.message)


# Email Notification
class EmailNotification(Notification):
    def send(self):
        print(f"Email gönderildi: {self.message}")


# SMS Notification
class SMSNotification(Notification):
    def send(self):
        print(f"SMS gönderildi: {self.message}")


# Push Notification
class PushNotification(Notification):
    def send(self):
        print(f"Push bildirimi gönderildi: {self.message}")
