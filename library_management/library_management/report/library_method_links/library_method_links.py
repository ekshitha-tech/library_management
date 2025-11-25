# Copyright (c) 2025, shridevi and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {"label": "Name", "fieldname": "name", "fieldtype": "Data", "width": 120},
        {"label": "Age", "fieldname": "age", "fieldtype": "Int", "width": 80},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 180},
        {"label": "Member", "fieldname": "member", "fieldtype": "Link", "options": "Library Member", "width": 180},
        {"label": "Reference Doctype", "fieldname": "reference_doctype", "fieldtype": "Data", "width": 150},
        {"label": "Reference Name", "fieldname": "reference_name", "fieldtype": "Dynamic Link", "options": "reference_doctype", "width": 200}
    ]

    data = frappe.get_all(
        "Library Methods",
        fields=["name", "age", "email", "member", "reference_doctype", "reference_name"]
    )

    return columns, data
