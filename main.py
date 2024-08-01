import PyPDF2
import fitz
import pymupdf
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, Toplevel, Text, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, LEFT, Y, BOTH, END
import os
import csv

def keyword_search(pdf_file, search_term):
    """
    Search for a keyword in a PDF file and return the list of occurrences and their respective pages.
    
    Input:
        pdf_file (str): Path to the PDF file.
        search_term (str): Keyword to search for.

    Output:
        list: A list of list with the PDF file, number of occurrences, and page number.
    """
    print(f"Reading Document...")

    # Open document
    doc = fitz.open(pdf_file)
    search_term = search_term.lower()

    list_pages = []

    for page_num in range(len(doc)):
        # Get specific text from page
        page = doc.load_page(page_num)
        text = page.get_text("text")
        text = text.lower()
        
        # Find all matches for search term
        occurrences = re.findall(re.escape(search_term), text)
        if occurrences:
            # Number of occurrences on a specific page
            occurrence_count = len(occurrences)
            list_pages.append([pdf_file, occurrence_count, page_num + 1])
            print(f"Found '{search_term}' on page {page_num + 1}, {occurrence_count} times")
        
    # Result
    return list_pages

def open_file_dialog():
    """
    Opens file via upload

    inputs:
    None

    output:
    output.csv in app

    """
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        keyword = simpledialog.askstring("Input", "Enter the keyword to search for:")
        if keyword:
            results = keyword_search(file_path, keyword)
            if results:
                result_text = "\n".join([f"File: {row[0]}, Occurrences: {row[1]}, Page: {row[2]}" for row in results])
            else:
                result_text = "Keyword not found"
            result_label.config(text=result_text)

def open_folder_dialog():
    pass

def get_keywords_from_user():
    pass

def output_to_csv(list):
    headers = ['file_path', 'number_of_occurances', 'page_number']

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in list:
            writer.writerow(row)

    return "CSV file created successfully"

# assign file
#file_name = "/Users/samaguiar/Desktop/Burbio Code/pdf_search/638640_SWEETWATER UNION HIGH_12-31-23_PURCHASE ORDERS.PDF"
#print(keyword_search(file_name, "vendor"))

#output = output_to_csv(keyword_search(file_name, "vendor"))

app = tk.Tk()
app.title("PDF Keyword Search")

open_button = tk.Button(app, text="Open PDF", command=open_file_dialog)
open_button.pack(pady=10)

# open_folder_button = tk.Button(app, text="Open Folder", command=open_folder_dialog)
# open_folder_button.pack(pady=10)

result_label = tk.Label(app, text="", justify="left")
result_label.pack(pady=20)

app.mainloop()