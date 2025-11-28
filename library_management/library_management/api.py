# import frappe

# @frappe.whitelist()
# def hello():
#     return "Hello ekshi!"
# @frappe.whitelist()
# def get_book(name):#one record
#     doc = frappe.get_doc("Library Book", name)
#     return doc
# @frappe.whitelist()
# def update_book(name=None, book_name=None, author=None, **kwargs):#update
#     if not name:
#         return "Name is required"

#     doc = frappe.get_doc("Library Book", name)

#     if book_name:
#         doc.book_name = book_name

#     if author:
#         doc.author = author

#     doc.save()
#     return doc


# @frappe.whitelist()
# def create_book():# post
#     doc = frappe.new_doc("Library Book")
#     doc.book_name = "jungle book"
#     doc.author = "hari"
#     doc.save()
#     return doc

# @frappe.whitelist()
# def delete_book(name):
#     frappe.delete_doc("Library Book", name, force=1)
#     return {"message": f"Book {name} deleted successfully"}
import frappe

@frappe.whitelist()
def get_user_customers():
    # 1. Get logged-in user
    user = frappe.session.user

    # If user is Guest
    if not user or user == "Guest":
        return {
            "message": {
                "status": "failed",
                "message": "User not logged in",
                "data": {"customer": []}
            },
            "filters_applied": {"user": user}
        }

    # 2. Fetch user email from User document
    email = frappe.db.get_value("User", user, "email")

    # 3. Fetch Contacts linked to that email
    contact_rows = frappe.get_all(
        "Contact Email",
        filters={"email_id": email},
        fields=["parent"]
    )
    contacts = [c.parent for c in contact_rows]

    if not contacts:
        return {
            "message": {
                "status": "success",
                "message": "User is linked with 0 customers",
                "data": {"customer": []}
            },
            "filters_applied": {"user": user}
        }

    # 4. Fetch linked Customers using Dynamic Link
    customer_links = frappe.get_all(
        "Dynamic Link",
        filters={
            "parent": ["in", contacts],
            "link_doctype": "Customer"
        },
        fields=["link_name"]
    )

    customers = sorted(list({c.link_name for c in customer_links}))

    # 5. Final response
    return {
        "message": {
            "status": "success",
            "message": f"User is linked with {len(customers)} customers",
            "data": {
                "customer": customers
            }
        },
        "filters_applied": {
            "user": user   # logged-in User ID
        }
    }
