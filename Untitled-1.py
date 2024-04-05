import tkinter as tk
from tkinter import messagebox
import csv
import os
class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("400x600")
        self.master.config(bg='#32a88d')
    
        
    #def library_management_screen(self):
        self.title_book_label = tk.Label(self.master, text="title Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.title_book_label.grid(row=1, column=0, padx=10, pady=10)
        self.title_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.title_book_entry.grid(row=1, column=1, padx=10, pady=10)

        self.author_book_label = tk.Label(self.master, text="authore Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.author_book_label.grid(row=2, column=0, padx=10, pady=10)
        self.author_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.author_book_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.genre_book_label = tk.Label(self.master, text="genre Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.genre_book_label.grid(row=3, column=0, padx=10, pady=10)
        self.genre_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.genre_book_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.pub_book_label = tk.Label(self.master, text="pub Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.pub_book_label.grid(row=4, column=0, padx=10, pady=10)
        self.pub_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.pub_book_entry.grid(row=4, column=1, padx=10, pady=10)

        self.search_book_label = tk.Label(self.master, text="search Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.search_book_label.grid(row=5, column=0, padx=10, pady=10)
        self.search_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.search_book_entry.grid(row=5, column=1, padx=10, pady=10)

        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Helvetica", 16), bg='#32a88d', fg='white')
        self.remove_book_label.grid(row=6, column=0, padx=10, pady=10)
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.grid(row=6, column=1, padx=10, pady=10)
        # Buttons

        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.grid(row=7, column=0, padx=10, pady=10)



        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Helvetica", 12))
        self.remove_book_button.grid(row=7, column=1, padx=10, pady=10)


        self.search_books_button = tk.Button(self.master, text="search Books", command=self.search_book, font=("Helvetica", 12))
        self.search_books_button.grid(row=8, column=0, padx=10, pady=10)

       
        self.view_books_button = tk.Button(self.master, text="view Books", command=self. view_books, font=("Helvetica", 12))
        self.view_books_button.grid(row=8, column=1, padx=10, pady=10)

    def add_book(self):
        self.title = self.title_book_entry .get()
        self.author = self.author_book_entry.get()
        self.genre = self.genre_book_entry .get()
        self.pub = self.pub_book_entry .get()
        if  self.title== "" and self.author == ""and self.genre==""and self.pub=="":
            messagebox.showerror("Error", "Please fill all the fields!")
        else:
            with open("library.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([self.title, self.author, self.genre,self.pub])
            messagebox.showinfo("Success", "Book added successfully!")
            self.title_book_entry .delete(0, END)
            self.author_book_entry.delete(0, END)
            self.genre_book_entry.delete(0, END)
            self.pub_book_entry.delete(0, END)

    def search_book(self):
         self.search_value = self.search_book_entry.get()
         with open("library.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if self.search_value  in row:
                        messagebox.showinfo("Book Details", f"title: {row[0]}\nauthor: {row[1]}\genre: {row[2]}")
                        self.search_book_entry .delete(0, tk.END)
                        return
                messagebox.showerror("Error", "Book not found!")
                self.search_book_entry .delete(0, END)

        

    def remove_book(self):
       self.remove_book_value = self.remove_book_entry.get() 
       with open("library.csv", "r") as file:
                reader = csv.reader(file)
                for i in reader:
                  if self.remove_book_value in i:
                    messagebox.showinfo("Success", "Book removed successfully")
                    self.remove_book_entry.delete(0, tk.END)
                    return
                messagebox.showerror("Error", "Book not found")
                self.remove_book_entry.delete(0, tk.END)

    def view_books(self):
        if os.path.exists("library.csv"):
            with open("library.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        else:
            print("The CSV file does not exist.")           
                



       
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()                      



