# Copyright (c) 2025, shridevi and contributors
# For license information, please see license.txt

# import frappe

import frappe
def execute(filters=None):
    columns = [
        {"label": "Student", "fieldname": "student", "fieldtype": "Data", "width": 200},
        {"label": "Positive Percentage", "fieldname": "positive_percentage", "fieldtype": "Float", "width": 150},
        {"label": "Negative Percentage", "fieldname": "negative_percentage", "fieldtype": "Float", "width": 150},
    ]
    data = []
    results = frappe.get_all("School result", fields=["student", "percentage"])
    for r in results:
        row = {
            "student": r.student,
            "positive_percentage": r.percentage if r.percentage >= 0 else None,
            "negative_percentage": r.percentage if r.percentage < 0 else None,
        }
        data.append(row)
    return columns, data
