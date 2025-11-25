# Copyright (c) 2025, shridevi and Contributors
# See license.txt

# import frappe
#import frappe

# def test_get_list():
#     books = frappe.db.get_list('Library Book',
#         fields=['book_name', 'author'],
#         filters={'status': 'Available'}
#     )

#     if not books:
#         frappe.msgprint("No available books.")
#         return

#     msg = "<h3>Available Books:</h3>"
#     for b in books:
#         msg += f"📘 {b['book_name']} — {b['author']}<br>"

#     frappe.msgprint(msg)


# Run: bench --site your-site execute library_management.library_management.doctype.library_book.test_get_list.test_get_list
