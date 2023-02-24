import csv
import Course
import BSTNode
import API_Functions
from tkinter import *
from tkinter import ttk
import json
from urllib.request import urlopen
import re

def main(): 
    API_Functions.Subject_CSV_Fill("PSYC")

if __name__ == "__main__": 
    main()