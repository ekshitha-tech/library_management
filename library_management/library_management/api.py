import frappe

@frappe.whitelist()
def hello():
    return "Hello ekshi!"
@frappe.whitelist()
def get_book(name):#one record
    doc = frappe.get_doc("Library Book", name)
    return doc
@frappe.whitelist()
def update_book(name=None, book_name=None, author=None, **kwargs):#update
    if not name:
        return "Name is required"

    doc = frappe.get_doc("Library Book", name)

    if book_name:
        doc.book_name = book_name

    if author:
        doc.author = author

    doc.save()
    return doc


@frappe.whitelist()
def create_book():# post
    doc = frappe.new_doc("Library Book")
    doc.book_name = "jungle book"
    doc.author = "hari"
    doc.save()
    return doc

@frappe.whitelist()
def delete_book(name):
    frappe.delete_doc("Library Book", name, force=1)
    return {"message": f"Book {name} deleted successfully"}
