# from __future__ import unicode_literals
# import frappe

# def execute(filters=None):
#     filters = filters or {}
#     columns = [
#         {"label": "Book Name", "fieldname": "book_name", "fieldtype": "Data", "width": 180},
#         {"label": "Author", "fieldname": "author", "fieldtype": "Data", "width": 150},
#         {"label": "Available", "fieldname": "available", "fieldtype": "Data", "width": 100},
#         {"label": "Form Date", "fieldname": "form_date", "fieldtype": "Date", "width": 120},
#         {"label": "Member Email", "fieldname": "member_email", "fieldtype": "Data", "width": 220},
#         {"label": "IBSN", "fieldname": "ibsn", "fieldtype": "Data", "width": 120},
#         {"label": "Available Copies", "fieldname": "available_copies", "fieldtype": "Int", "width": 150},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
#     ]
#     # --- Prepare filter conditions ---
#     conditions = {}
#     if filters.get("author"):
#         conditions["author"] = filters["author"]
#     if filters.get("status") and filters["status"] != "All":
#         conditions["status"] = filters["status"]
#     # --- Fetch data ---
#     data = frappe.db.get_all(
#         "Library Book",
#         fields=[
#             "book_name",
#             "author",
#             "available",
#             "form_date",
#             "member_email",
#             "ibsn",
#             "available_copies",
#             "status"
#         ],
#         filters=conditions,
#         order_by="book_name asc"
#     )
#     # --- Optional chart (books by status) ---
#     status_summary = frappe.db.get_all(
#         "Library Book",
#         fields=["status", "count(name) as total"],
#         group_by="status"
#     )

#     chart = {
#         "data": {
#             "labels": [row["status"] for row in status_summary],
#             "datasets": [{"name": "Books", "values": [row["total"] for row in status_summary]}]
#         },
#         "type": "bar"
#     }
#     # --- Optional summary (totals) ---
#     total_books = len(data)
#     available_books = sum(1 for d in data if d.get("available") == "Yes")

#     report_summary = [
#         {"value": total_books, "label": "Total Books", "indicator": "Blue", "datatype": "Int"},
#         {"value": available_books, "label": "Available Books", "indicator": "Green", "datatype": "Int"}
#     ]
#     return columns, data, None, chart, report_summary
import frappe
from frappe import _

def execute(filters=None):
    # ✅ Restrict access to specific roles
    allowed_roles = ["Librarian"]  # you can customize these

    # Check if current user has any of the allowed roles
    if not any(frappe.has_role(role) for role in allowed_roles):
        frappe.throw(_("You are not permitted to view this report."))

    # --- Normal report code below ---
    columns = [
        {"fieldname": "book_name", "label": "Book Name", "fieldtype": "Data"},
        {"fieldname": "author", "label": "Author", "fieldtype": "Data"},
        {"fieldname": "available_copies", "label": "Available Copies", "fieldtype": "Int"},
    ]

    data = frappe.get_all(
        "Library Book",
        fields=["book_name", "author", "available_copies"]
    )

    return columns, data
