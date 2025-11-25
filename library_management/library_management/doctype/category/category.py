import frappe
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class Category(NestedSet):
    pass


@frappe.whitelist()
def show_children(name):
    doc = frappe.get_doc("Category", name)
    children = [child.name for child in doc.get_children()]
    return children


@frappe.whitelist()
def show_parent(name):
    doc = frappe.get_doc("Category", name)
    parent = doc.get_parent()
    return parent.name if parent else None
