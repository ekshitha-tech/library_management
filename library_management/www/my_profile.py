import frappe

def get_context(context):
    # Do not cache this page
    context.no_cache = True

    # Set page title
    context.title = "My Profile Pagessssssssssss4"

  

    # Show the website sidebar
    context.show_sidebar = True

    # Add custom breadcrumbs
    context.add_breadcrumbs = [
        {"label": "Home", "route": "/"},
        {"label": "My Profile", "route": "/my_profile"}
    ]

    # Add Next and Previous links (you can make them any URLs)
    context.add_next_prev_links = {
        "next": {"label": "Go to Dashboard", "route": "/dashboard"},
        "prev": {"label": "Back to Library", "route": "/library"}
    }

    # Example profile data
    context.profile = {
        "name": "Shridevi Shrishail Madiwalar",
        "email": "shridevi@example.com",
        "role": "Library Member",
        "about": "I’m learning how to build Frappe web pages and explore portal features."
    }

    return context
