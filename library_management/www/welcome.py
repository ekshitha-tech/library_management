import frappe
from frappe.utils.jinja import render_template  # ✅ fixed import

def get_context(context):
    context.user = "Shridevi"
    context.role = "Librarian"
    context.app_name = "Library App"

    context.rendered_html = render_template(
        "library_management/templates/includes/welcome_message.html",
        {
            "user": context.user,
            "role": context.role,
            "app_name": context.app_name
        },
        is_path=True
    )

