import frappe
from frappe.model.document import Document

class LibraryMethods(Document):
    def validate(self):
        """Call custom validation function during save"""
        # Instead of rollback here, call our separate function
        check_age_and_rollback(self.age, self.name)


@frappe.whitelist()
def check_age_and_rollback(age, name):
    """Custom rollback function"""
    if int(age) < 0:
        # Rollback any DB changes (manual rollback)
        frappe.db.rollback()
        frappe.throw(f"❌ Invalid age for record {name}. Transaction rolled back.")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def on_update(self):
        """Update last Library ORM record's details"""
        try:
            # Get the last record of Library ORM
            last_doc = frappe.get_last_doc("Library ORM")
            
            # Update age and number using frappe.db.set_value
            frappe.db.set_value("Library ORM", last_doc.name, {
                "age": 40,
                "number": "9876543210"
            })

            frappe.msgprint(f"✅ Updated record {last_doc.name} successfully!")

            # Confirm update
            updated_doc = frappe.get_doc("Library ORM", last_doc.name)
            frappe.msgprint(f"📋 Updated:\nAge: {updated_doc.age}\nNumber: {updated_doc.number}")

        except frappe.DoesNotExistError:
            frappe.msgprint("❌ No Library ORM records found to update.")
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def on_update(self):
        """Set and Get custom default values"""

        # Set a custom default
        frappe.db.set_default("number", "100")

        # Now retrieve it
        number= frappe.db.get_default("number")

        frappe.msgprint(f"🏙️ Default Library number is: {number}")'''

    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def on_update(self):
        """Fetch a specific field value using frappe.db.get_value"""
        frappe.msgprint("✅ Fetching a field value using frappe.db.get_value...")

        # Example 1: Get a single field value
        email = frappe.db.get_value("Library Methods", {"name1": "geeta"}, "email")
        frappe.msgprint(f"📧 Email of geeta: {email}")

        # Example 2: Get multiple field values
        values = frappe.db.get_value(
            "Library Methods",
            {"name1": "geeta"},
            ["age", "number"],
            as_dict=True
        )

        if values:
            frappe.msgprint(f"👤 Age: {values.age}, 📞 Number: {values.number}")
        else:
            frappe.msgprint("⚠️ No record found for name1 = geeta")'''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def on_update(self):
        """Runs each time you click Save"""
        frappe.msgprint("✅ Running custom SQL query...")

        # Safe SQL query using parameters
        records = frappe.db.sql(
            """
            SELECT name, name1, age, email, address, number
            FROM `tabLibrary Methods`
            WHERE age > %s
            """,
            values=(5,),  # Only show records where age > 5
            as_dict=True
        )

        # Print in backend console
        print("SQL Query Result:", records)

        # Build a UI message
        if records:
            message = "📋 Records (age > 5):"
            for rec in records:
                message += (
                    f"\n• Name: {rec.name1}, Age: {rec.age}, "
                    f"Email: {rec.email}, Number: {rec.number}"
                )
        else:
            message = "⚠️ No records found with age > 5."

        frappe.msgprint(message)
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def on_update(self):
        """Runs every time a record is saved or updated"""
        frappe.msgprint("✅ on_update triggered — fetching all Library Methods records...")

        # Fetch all records, ignoring user permissions
        all_records = frappe.db.get_all(
            "Library Methods",
            fields=["name", "name1", "age", "email", "address", "number"]
        )

        # Print in backend console (for debugging)
        print("All Library Methods Records:", all_records)

        # Build a formatted message for the UI
        message = "📋 All Library Methods Records:\n"
        for rec in all_records:
            message += (
                f"\n• Name: {rec.name1}, Age: {rec.age}, "
                f"Email: {rec.email}, Address: {rec.address}, Number: {rec.number}"
            )

        # Show results in Frappe UI
        frappe.msgprint(message)
        '''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def after_insert(self):
        """Runs after a new record is created"""
        frappe.msgprint("✅ after_insert triggered — record created successfully!")

        # Get list of all Library Methods records
        records = frappe.db.get_list(
            "Library Methods",
            fields=["name", "name1", "age", "email", "address", "number"],  # specify fields to fetch
            limit=5  # limit to avoid too many results
        )

        # Print the results to see in system console/logs
        print("Fetched Records:", records)

        # Display the results nicely in UI using msgprint
        message = "📋 Showing first few Library Methods records:\n"
        for rec in records:
            message += f"\n• {rec.name1} ({rec.age}) — {rec.email}"
        frappe.msgprint(message)
'''
