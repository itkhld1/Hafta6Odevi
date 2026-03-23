import os

AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

def connect():
    # Do not print secrets
    print("Connecting")
