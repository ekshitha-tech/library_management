import frappe
def execute(filters=None):
    columns = [
        {"label": "Book Name", "fieldname": "book_name", "fieldtype": "Data", "width": 200},
        {"label": "Author", "fieldname": "author", "fieldtype": "Data", "width": 200},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 200},
        {"label": "Action", "fieldname": "action", "fieldtype": "HTML", "width": 150},
    ]
    data = []
    for book in frappe.get_all("Library Book", fields=["name", "book_name", "author", "email"]):
        data.append({
            "book_name": book.book_name,
            "author": book.author,
            "email": book.email,
            "action": f"""
                <select class='book-action' data-name='{book.name}'>
                    <option value="">Select</option>
                    <option value="Available">Available</option>
                    <option value="Issued">Issued</option>
                    <option value="Lost">Lost</option>
                </select>
            """
        })
    return columns, data
@frappe.whitelist()
def update_action(docname, action):
    frappe.db.set_value("Library Book", docname, "status", action)
    frappe.db.commit()
