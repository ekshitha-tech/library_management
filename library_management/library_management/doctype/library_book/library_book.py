import frappe
from frappe.model.document import Document

class LibraryBook(Document):
    pass

# doc = frappe.get_doc("Library Book", "1sj1k74kc8")  # replace LB0001 with an actual book name in your system

# print("Before Reload:", doc.status)
# doc.reload()
# print("After Reload:", doc.status)

    
    
    
    
    # def before_save(self):
    #     old_doc = self.get_doc_before_save()
    #     if old_doc and old_doc.book_name != self.book_name:
    #         frappe.msgprint(f"Book name changed from {old_doc.book_name} → {self.book_name}")

# class LibraryBook(Document):
#     def before_save(self):
#         # Example: delete a specific book (make sure you have a book named "BOOK-0001")
#         if self.book_name == "DeleteTest":
#             frappe.msgprint("Deleting this test book...")
#             self.delete()






# import frappe
# from frappe.model.document import Document

# class LibraryBook(Document):
#     def after_insert(self):
#         # Prevent recursion
#         if self.book_name == "Auto Created Book":
#             return

#         # create a new book only once
#         new_book = frappe.new_doc("Library Book")
#         new_book.book_name = "Auto Created Book"
#         new_book.author = "System"
#         new_book.status = "Available"

#         new_book.insert(
#             ignore_permissions=True,
#             ignore_links=True,
#             ignore_if_duplicate=True,
#             ignore_mandatory=True
#         )

#         frappe.msgprint("✅ Auto Created Book inserted successfully!")
#     frappe.msgprint("✅ Auto Created Book inserted successfully!")

# class LibraryBook(Document):
#     def validate(self):
#         frappe.db.add_unique('Library Book', ['book_name'])
#         frappe.msgprint("🔒 Added unique constraint on book_name.")


# class LibraryBook(Document):
#     def validate(self):
#         desc = frappe.db.describe('Library Book')
#         frappe.msgprint(f"🔍 Table Description: {desc}")

# class LibraryBook(Document):
#     def validate(self):
#         frappe.db.multisql({
#             'mariadb': "UPDATE `tabLibrary Book` SET status='Checked' WHERE status='Available'",
#             'postgres': 'UPDATE "tabLibrary Book" SET status=\'Checked\' WHERE status=\'Available\''
#         })
#         frappe.msgprint("🛠️ Updated book status using multisql")


# class LibraryBook(Document):
#     def validate(self):
#         frappe.db.commit()
#         frappe.msgprint("💾 Transaction committed successfully.")



# class LibraryBook(Document):
#     def validate(self):
#         frappe.db.delete('Library Book', {'status': 'Old'})
#         frappe.msgprint("🗑️ Deleted all Library Books with status = 'Old'")

# class LibraryBook(Document):
#     def validate(self):
#         total_books = frappe.db.count('Library Book')
#         available_books = frappe.db.count('Library Book', {'status': 'Available'})
#         frappe.msgprint(f"📚 Total Books: {total_books}, Available: {available_books}")



















# class LibraryBook(Document):
#     def validate(self):
#         # Only check when book_name is "hu"
#         if self.book_name == "hu":
#             exists = frappe.db.exists('Library Book', {'book_name': 'hu'})
#             if exists:
#                 frappe.msgprint("✅ Book 'hu' exists in Library Book.")
#             else:
#                 frappe.msgprint("❌ Book 'hu' not found in Library Book.")
