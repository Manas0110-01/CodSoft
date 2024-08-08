import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x500")

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack(pady=5)

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(root)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack(pady=5)

        self.address_entry = tk.Entry(root)
        self.address_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(root)
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.contacts_listbox = tk.Listbox(root, width=40)
        self.contacts_listbox.pack(pady=5)

        self.update_button = tk.Button(root, text="Update", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.display_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = self.search_entry.get()
        found = False
        for name, details in self.contacts.items():
            if search_term in name or search_term in details["phone"]:
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.contacts_listbox.get(selected_index)
            name = name.split(" - ")[0]
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address

            self.display_contacts()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.contacts_listbox.get(selected_index)
            name = name.split(" - ")[0]
            del self.contacts[name]
            self.display_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()