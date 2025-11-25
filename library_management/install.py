import frappe

def after_install():
    sample_books = [
        {"book_name": "The Pragmatic Programmer", "author": "Andy Hunt"},
        {"book_name": "Clean Code", "author": "Robert C. Martin"},
        {"book_name": "Refactoring", "author": "Martin Fowler"},
        {"book_name": "Design Patterns", "author": "GoF"},
        {"book_name": "Effective Java", "author": "Joshua Bloch"}
    ]

    for book in sample_books:
        if not frappe.db.exists("Library Book", {"book_name": book["book_name"]}):
            doc = frappe.get_doc({
                "doctype": "Library Book",
                **book
            })
            doc.insert(ignore_permissions=True)

    frappe.db.commit()
    frappe.msgprint("📚 Sample Library Book records created successfully!")
