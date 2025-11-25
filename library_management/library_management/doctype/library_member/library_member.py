# Copyright (c) 2025, Shridevi and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
   pass


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''def db_update(self, *args, **kwargs):
        frappe.msgprint(f"⚙️ db_update: Saving {self.full_name} to the database.")
        result = super(LibraryMember, self).db_update(*args, **kwargs)
        return result

    def on_update(self):
        frappe.msgprint(f"✅ on_update: Finished saving {self.full_name}.")
'''
    
    
    
    
    
'''def on_change(self):
        frappe.msgprint(f"✏️ on_change triggered for: {self.full_name}")

        # Example: Detect if email was changed
        if self.has_value_changed("email"):
            frappe.msgprint(f"📧 Email updated to: {self.email}")

        # Example: Detect if age changed
        if self.has_value_changed("age"):
            frappe.msgprint(f"🎂 Age updated to: {self.age}")

        frappe.logger().info(f"[LibraryMember] on_change called for {self.full_name}")
'''
    
    
    
    
    
    
'''def on_update(self):
        frappe.msgprint(f"🔁 on_update triggered for: {self.full_name}")

        # Example: Auto-update full name if first or last name changed
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
            frappe.msgprint(f"🧩 Full Name updated to: {self.full_name}")

        # Example: Log info to the server console (developer view)
        frappe.logger().info(f"[LibraryMember] on_update called for {self.full_name}, age {self.age}")
'''   
    
'''def db_insert(self, *args, **kwargs):
        frappe.msgprint(f"🧩 db_insert called for: {self.full_name}")
        
        # Always call parent method with *args and **kwargs
        result = super(LibraryMember, self).db_insert(*args, **kwargs)
        
        frappe.logger().info(f"[LibraryMember] db_insert executed for {self.full_name}")
        return result'''   
    
'''def after_insert(self):
        # 1️⃣ Simple message to confirm creation
        frappe.msgprint(f"🎉 Library Member '{self.full_name}' has been successfully created!")

        # 2️⃣ Example: Send a small welcome note (optional)
        if self.email:
            frappe.msgprint(f"📧 Welcome email would be sent to: {self.email}")

        # 3️⃣ Optional: Log info to console (useful for backend testing)
        frappe.logger().info(f"New Library Member Created: {self.full_name}, Age: {self.age}")
'''
'''def before_save(self):
        # 1️⃣ Auto-update full name every time before saving
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        elif self.last_name:
            self.full_name = self.last_name

        # 2️⃣ Default member_status to Active
        if not self.get("member_status"):
            self.member_status = "Active"

        # 3️⃣ Mark is_adult = True if age >= 18
        if self.age and self.age >= 18:
            self.is_adult = 1
        else:
            self.is_adult = 0

        # 4️⃣ Block certain email domains
        if self.email and self.email.endswith("@test.com"):
            frappe.throw("Members cannot register with @test.com email addresses.")

        # 5️⃣ Show confirmation message
        frappe.msgprint(f"✅ Before Save executed — Member: {self.full_name}")'''
    
'''def before_validate(self):
        # Pre-validation cleanup (optional)
        if self.email:
            self.email = self.email.lower().strip()
        if self.first_name:
            self.first_name = self.first_name.strip()
        if self.last_name:
            self.last_name = self.last_name.strip()

    def validate(self):
        # 1️⃣ Email must contain '@'
        if not self.email or '@' not in self.email:
            frappe.throw("Please enter a valid email address.")

        # 2️⃣ Age check
        if self.age < 12:
            frappe.throw("Member must be at least 12 years old to register.")

        # 3️⃣ Require first & last name
        if not self.first_name or not self.last_name:
            frappe.throw("Both first name and last name are required.")

        # 4️⃣ Prevent duplicate full_name
        existing = frappe.db.exists(
            "Library Member",
            {
                "full_name": f"{self.first_name} {self.last_name}",
                "name": ["!=", self.name]  # exclude current doc during update
            }
        )
        if existing:
            frappe.throw(f"A Library Member named '{self.first_name} {self.last_name}' already exists.")

        # 5️⃣ Auto full name if missing
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}"

        # Optional: Show message for confirmation
        frappe.msgprint(f"✅ Validation passed for {self.full_name}")
'''       
'''def before_validate(self):
                if self.first_name:
                        self.first_name=self.first_name.strip()
                if self.last_name:
                        self.last_name=self.last_name.strip()
                if self.email:
                        self.email=self.email.lower().strip()
                if not self.age:
                        self.age=18
                frappe.msgprint("before_validate executed successfully")'''   
    
'''def before_insert(self):
        # 1️⃣ Convert email to lowercase
        if self.email:
            self.email = self.email.lower()

        # 2️⃣ Prevent duplicate email
        if frappe.db.exists("Library Member", {"email": self.email}):
            frappe.throw(f"A Library Member with email '{self.email}' already exists.")

        # 3️⃣ Auto full name
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        elif self.last_name:
            self.full_name = self.last_name

        # 4️⃣ Default age
        if not self.age:
            self.age = 18

        # 5️⃣ Restrict underage
        if self.age < 12:
            frappe.throw("Member must be at least 12 years old to register.")
'''