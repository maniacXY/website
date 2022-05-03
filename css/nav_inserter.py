from cgitb import html
import os

html_files = [file for file in os.listdir("../") if file.endswith(".html")]

with open("../templates/navbar.html", "r") as nav:
    navbar = nav.read()

for file in html_files:
    with open(file, "r") as change:
        edit = change.read()
    fused = edit.replace("<NAVBAR>", navbar)
    with open(file, "w") as w:
        w.write(fused)
    