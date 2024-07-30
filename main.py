import PyPDF2
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, Toplevel, Text, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, LEFT, Y, BOTH, END
import os

def keyword_search(pdf_file, search_term):
    """
    """
    # read document
    doc = PyPDF2.PdfReader(pdf_file)
    # find number of pages
    pages = len(doc.pages)
    #print(f"Number of Pages: {pages}")

    # Look for search term in file
    # append to list as tuple (all occurence, pages)
    list_pages = []

    for page in range(pages):
        # get specific text from page
        current_page = doc.pages[page]
        text = current_page.extract_text(page)
        #print(page, text)
        
        #find all matches for search term
        if re.findall(search_term, text):
            # number of occurances on a specific page
            occurance_page = len(re.findall(search_term, text))
            list_pages.append((occurance_page, page+1))
        
    # result
    return list_pages

def open_file_dialog():
    pass

def open_folder_dialog():
    pass

def get_keywords_from_user():
    pass

# assign file
file_name = "FL_School District Matching Grants Program.pdf"
print(keyword_search(file_name, "grant"))

# app = tk.Tk()
# app.title("PDF Keyword Search")

# open_button = tk.Button(app, text="Open PDF", command=open_file_dialog)
# open_button.pack(pady=10)

# open_folder_button = tk.Button(app, text="Open Folder", command=open_folder_dialog)
# open_folder_button.pack(pady=10)

# result_label = tk.Label(app, text="", justify="left")
# result_label.pack(pady=20)

# app.mainloop()