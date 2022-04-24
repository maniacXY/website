import os
from bs4 import BeautifulSoup

with open("templates/navbar.html", "r") as f:
    navbar = f.read()

files = [file for file in os.listdir(".") if file.endswith(".html")]

print(files[3])