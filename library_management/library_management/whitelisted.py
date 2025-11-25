import frappe

@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    """
    Custom implementation of frappe.client.get_count
    """
    frappe.msgprint(f"📊 Custom get_count called for DocType: {doctype}")

    # call the original function manually if you want
    original_count = frappe.db.count(doctype, filters)

    # return your modified response
    return {
        "custom_message": f"This is your overridden count for {doctype}",
        "count": original_count
    }
