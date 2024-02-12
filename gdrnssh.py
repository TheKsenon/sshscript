import sys

with open("logs.txt", "a") as file:
    while True:        
        text = input()
        file.write(text + "\n")
        file.flush(
