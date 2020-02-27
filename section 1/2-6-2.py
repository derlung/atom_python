from bs4 import BeautifulSoup
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

fp = open("D:/atom_python/section1/food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

print(soup)
