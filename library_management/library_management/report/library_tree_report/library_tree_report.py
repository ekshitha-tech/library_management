# Copyright (c) 2025, shridevi and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {"label": "Name", "fieldname": "name", "fieldtype": "Data", "width": 300},
        {"label": "Type", "fieldname": "type", "fieldtype": "Data", "width": 120},
        {"label": "Parent", "fieldname": "parent", "fieldtype": "Data", "width": 200},
    ]

    data = []

    # ---- LEVEL 0: Library ----
    libraries = frappe.get_all("Library", fields=["name"])
    for lib in libraries:
        data.append({
            "name": lib.name,
            "type": "Library",
            "parent": "",
            "indent": 0
        })

        # ---- LEVEL 1: Section ----
        sections = frappe.get_all("Library Section", fields=["name"], filters={"library": lib.name})
        for section in sections:
            data.append({
                "name": section.name,
                "type": "Section",
                "parent": lib.name,
                "indent": 1
            })

            # ---- LEVEL 2: Shelf ----
            shelves = frappe.get_all("Library Shelf", fields=["name"], filters={"section": section.name})
            for shelf in shelves:
                data.append({
                    "name": shelf.name,
                    "type": "Shelf",
                    "parent": section.name,
                    "indent": 2
                })

                # ---- LEVEL 3: Book ----
                books = frappe.get_all("Library Book", fields=["book_name"], filters={"shelf": shelf.name})
                for book in books:
                    data.append({
                        "name": book.book_name,
                        "type": "Book",
                        "parent": shelf.name,
                        "indent": 3
                    })

    return columns, data
