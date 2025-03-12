import streamlit as st 
import json


# library data save and load 
def load_libary():
    try: 
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_libary():
    with open("library.json", "w") as file:
        json.dump(library,file, indent=4)

# initializing library 
library = load_libary()

st.title("Personal Library Manager")
menu = st.sidebar.radio("Select An Option", ["View Library", "Add Book", "Remove Book", "Find Book", "Save & Exit"])

if menu == "View Library":
    st.sidebar.title("Your Library")
    if library:
      st.table(library)
    else:
        st.write("Your Library is empty. Add your fav books")

# Adding Books 
elif menu == "Add Book":
    st.sidebar.title("Add Your Latest Fav Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input('Year', min_value=2020, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark As Read")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        st.success("New Book Add Successfully")
        st.rerun() # the will reset the page

# rmove book
elif menu == "Remove Book":
    st.sidebar.title("Remove Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a Book to remove", book_titles)
        if st.button("Remove Book"):
           library = [book for book in library if book["title"] != selected_book]
           save_libary()
           st.success("Book Removed successfully")
           st.rerun()
        else:
           st.warning("There are no books in the library")


# Find Book
elif menu =='Find Book':
    st.sidebar.title("Find The Book You Are Looking")
    find_term = st.text_input("Enter title or author name")

    if st.button("Search"):
        results = [book for book in library if find_term.lower() in book["title"].lower() or find_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No Book Found")

# Save & Exit

elif menu == "Save & Exit":
    save_libary()
    st.success("Library Saved successfully")

