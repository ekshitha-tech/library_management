import frappe
from frappe.model.document import Document

class LibraryORM(Document):
    def validate(self):
        """Validate runs before saving the record"""
        if not self.email or "@" not in self.email:
            frappe.throw("Please enter a valid email address.")

    def on_update(self):
        """on_update runs every time the record is saved"""
        frappe.msgprint("Record has been updated. Now fetching another Library ORM record...")

        # Use the 'name' field of the current document to fetch another record
        record_name = self.name  # this will use the name of the current record

        if not record_name:
            frappe.msgprint("❌ This record does not have a name!")
            return

        try:
            # Fetch the record based on the name
            existing_doc = frappe.get_doc("Library ORM", record_name)
            frappe.msgprint(f"✅ Found record: {existing_doc.name}")
            frappe.msgprint(f"Name: {existing_doc.name}, Email: {existing_doc.email}")
            frappe.msgprint(f"Address: {existing_doc.address}")  # Display address
            frappe.msgprint(f"Number: {existing_doc.number}")  # Display number
        except frappe.DoesNotExistError:
            frappe.msgprint(f"❌ No record found with name {record_name}")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def after_insert(self):
        """This method runs after a new record is added"""

        # Get meta info of this DocType
        meta = frappe.get_meta("Library ORM")

        frappe.msgprint("✅ Meta Information:")
        frappe.msgprint(f"Doctype: {meta.name}")
        frappe.msgprint(f"Module: {meta.module}")
        frappe.msgprint(f"Total Fields: {len(meta.fields)}")
        frappe.msgprint(f"Has field 'email'? {'Yes' if meta.has_field('email') else 'No'}")

        # Print field details
        field_list = [f"{f.fieldname} ({f.fieldtype})" for f in meta.fields]
        frappe.msgprint("<br>".join(field_list))
'''


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''def on_submit(self):
        """Rename a Library ORM record when this document is submitted"""
        
        old_name = "ahj2fveij4"   # must exist in your Library ORM records
        new_name = "LIB-0020"   # the new name you want
        
        try:
            renamed_doc = frappe.rename_doc("Library ORM", old_name, new_name)
            frappe.db.commit()
            frappe.msgprint(f"✅ Successfully renamed record from {old_name} ➡️ {new_name}")
        except frappe.DoesNotExistError:
            frappe.msgprint(f"❌ Record '{old_name}' not found.")
        except frappe.ValidationError as e:
            frappe.msgprint(f"⚠️ Validation error: {str(e)}")
        except Exception as e:
            frappe.msgprint(f"⚠️ Unexpected error: {str(e)}")'''
            
            
            
            
            
            
            
            
            
'''def on_submit(self):
        """This method runs when you submit a Library ORM document"""

        # The record name to delete (replace with one that actually exists)
        record_to_delete = "l18u97ohc4"

        try:
            frappe.delete_doc("Library ORM", record_to_delete, ignore_permissions=True)
            frappe.db.commit()
            frappe.msgprint(f"🗑️ Successfully deleted record: {record_to_delete}")
        except frappe.DoesNotExistError:
            frappe.msgprint(f"❌ Record {record_to_delete} not found.")
        except Exception as e:
            frappe.msgprint(f"⚠️ Error while deleting record: {str(e)}")
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''def after_insert(self):
        """Run only when the document is freshly created by user"""
        # Skip creating new doc if this one was created by controller
        if getattr(self.flags, "from_controller", False):
            return

        # Create a new record using frappe.new_doc()
        new_doc = frappe.new_doc("Library ORM")
        new_doc.name1 = "Divya2"
        new_doc.age = 23
        new_doc.email = "divya@example.com"
        new_doc.address = "Bengaluru"
        new_doc.number = "9876543212"

        # Mark this one as system-created (so it doesn't loop)
        new_doc.flags.from_controller = True
        new_doc.insert(ignore_permissions=True)
        

        frappe.db.commit()
        frappe.msgprint(f"✅ Created new record using frappe.new_doc(): {new_doc.name}")
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''def after_insert(self):
        """Runs after inserting a new record"""
        frappe.msgprint("✅ Record inserted. Now fetching a cached document...")

        try:
            # Fetch a specific record using cache
            cached_doc = frappe.get_cached_doc("Library ORM", self.name)

            frappe.msgprint("📦 Cached document fetched successfully!")
            frappe.msgprint(f"Name: {cached_doc.name1}")
            frappe.msgprint(f"Age: {cached_doc.age}")
            frappe.msgprint(f"Email: {cached_doc.email}")
            frappe.msgprint(f"Address: {cached_doc.address}")
            frappe.msgprint(f"Number: {cached_doc.number}")

        except frappe.DoesNotExistError:
            frappe.msgprint("❌ No record found in cache for this name.")
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

'''def before_insert(self):
        """Runs after a new record is inserted"""

        frappe.msgprint("✅ Record inserted. Now fetching the last Library ORM record with filters...")

        try:
            # Fetch the last record where age = 25
            last_doc = frappe.get_last_doc(
                "Library ORM",
                filters={"age": 25}  # You can change this to any condition
            )

            frappe.msgprint(f"🎯 Last record found where age = 25:")
            frappe.msgprint(f"Name: {last_doc.name1}")
            frappe.msgprint(f"Age: {last_doc.age}")
            frappe.msgprint(f"Email: {last_doc.email}")
            frappe.msgprint(f"Address: {last_doc.address}")
            frappe.msgprint(f"Number: {last_doc.number}")

        except frappe.DoesNotExistError:
            frappe.msgprint("❌ No record found matching the filter.")'''


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''def after_insert(self):
        """This method runs automatically after a new record is inserted"""

        frappe.msgprint("🚀 after_insert triggered! Fetching the last Library ORM record...")

        try:
            # Fetch the last created Library ORM record
            last_doc = frappe.get_last_doc("Library ORM")

            # Show details in popup messages
            frappe.msgprint(f"✅ Last Record Name: {last_doc.name}")
            frappe.msgprint(f"Name1: {last_doc.name1}")
            frappe.msgprint(f"Age: {last_doc.age}")
            frappe.msgprint(f"Email: {last_doc.email}")
            frappe.msgprint(f"Address: {last_doc.address}")
            frappe.msgprint(f"Number: {last_doc.number}")

        except Exception as e:
            frappe.msgprint(f"❌ Error while fetching last record: {str(e)}")
'''
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''def before_submit(self):
        """This method runs after a new record is inserted"""

        # Now let's create another record in the same DocType using frappe.get_doc(dict)
        new_doc = frappe.get_doc({
            "doctype": "Library ORM",
            "name1": "Geeta",
            "age": 25,
            "email": "geeta@example.com",
            "address": "Hubballi",
            "number": "9876543210"
        })

        new_doc.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.msgprint(f"✅ New record inserted: {new_doc.name}")
'''





































































































































































































'''def validate(self):
        """Validate runs before saving the record"""
        if not self.email or "@" not in self.email:
            frappe.throw("Please enter a valid email address.")

    def on_update(self):
        """on_update runs every time the record is saved"""
        frappe.msgprint("Record has been created or updated")

        # Use the 'name' field of the current document to fetch another record
        record_name = self.name  # this will use the name of the current record

        if not record_name:
            frappe.msgprint("❌ This record does not have a name!")
            return

        try:
            # Fetch the record based on the name
            existing_doc = frappe.get_doc("Library ORM", record_name)
            frappe.msgprint(f"✅ Found record: {existing_doc}")
            frappe.msgprint(f"Name: {existing_doc.name}, Email: {existing_doc.email}")
            frappe.msgprint(f"Address: {existing_doc.address}")  # Display address
            frappe.msgprint(f"Number: {existing_doc.number}")  # Display number
        except frappe.DoesNotExistError:
            frappe.msgprint(f"❌ No record found with name {record_name}")'''
