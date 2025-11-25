import frappe

def get_home_page(user):
    if "Librarian" in frappe.get_roles(user):
        return "/librarian-dashboard"
    elif "Member" in frappe.get_roles(user):
        return "/member-dashboard"
    else:
        return "/library-home"
