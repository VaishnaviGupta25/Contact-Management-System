import json
import os
import re
import logging

logging.basicConfig(
    filename="contacts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ContactManager:
    def __init__(self, file_name="contacts.json"):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def validate_name(self, name):
        return name.strip() != ""

    def validate_phone(self, phone):
        return re.fullmatch(r"\d{10}", phone) is not None

    def validate_email(self, email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def phone_exists(self, phone):
        for c in self.contacts:
            if c["phone"] == phone and not c["is_deleted"]:
                return True
        return False

    def add_contact(self):
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone (10 digits): ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address (optional): ").strip()

        if not self.validate_name(name):
            print("❌ Name cannot be empty.")
            return

        if not self.validate_phone(phone):
            print("❌ Phone must be 10 digits.")
            return

        if self.phone_exists(phone):
            print("❌ Phone number already exists.")
            return

        if not self.validate_email(email):
            print("❌ Invalid email format.")
            return

        new_id = max([c["id"] for c in self.contacts], default=0) + 1

        contact = {
            "id": new_id,
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "is_deleted": False
        }

        self.contacts.append(contact)
        self.save_contacts()
        logging.info(f"Contact added: {name}")

        print("✅ Contact added successfully.")

    def view_contacts(self):
        print("\n---- Contact List ----")
        found = False

        for c in self.contacts:
            if not c["is_deleted"]:
                found = True
                print(
                    f"ID: {c['id']} | Name: {c['name']} | "
                    f"Phone: {c['phone']} | Email: {c['email']} | "
                    f"Address: {c['address']}"
                )

        if not found:
            print("No contacts available.")

    def search_contact(self):
        key = input("Search by Name or Phone: ").lower()

        found = False
        for c in self.contacts:
            if not c["is_deleted"] and (
                key in c["name"].lower() or key in c["phone"]
            ):
                print(
                    f"ID: {c['id']} | Name: {c['name']} | "
                    f"Phone: {c['phone']} | Email: {c['email']}"
                )
                found = True

        if not found:
            print("Contact not found.")

    def update_contact(self):
        phone = input("Enter phone of contact to update: ")

        for c in self.contacts:
            if c["phone"] == phone and not c["is_deleted"]:
                new_name = input("New Name: ").strip()
                new_phone = input("New Phone: ").strip()
                new_email = input("New Email: ").strip()

                if new_name and self.validate_name(new_name):
                    c["name"] = new_name

                if new_phone and self.validate_phone(new_phone):
                    if not self.phone_exists(new_phone):
                        c["phone"] = new_phone
                    else:
                        print("Phone already exists.")

                if new_email and self.validate_email(new_email):
                    c["email"] = new_email

                self.save_contacts()
                logging.info(f"Contact updated: {phone}")
                print("✅ Contact updated.")
                return

        print("Contact not found.")

    def delete_contact(self):
        phone = input("Enter phone to delete: ")

        for c in self.contacts:
            if c["phone"] == phone and not c["is_deleted"]:
                c["is_deleted"] = True
                self.save_contacts()
                logging.info(f"Contact deleted: {phone}")
                print("✅ Contact deleted (soft delete).")
                return

        print("Contact not found.")

    def menu(self):
        while True:
            print("\n===== Contact Management System =====")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
