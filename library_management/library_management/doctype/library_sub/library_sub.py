# Copyright (c) 2025, shridevi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibrarySub(Document):
    def before_submit(self):
        frappe.msgprint("Before Submit: Verifying data before submission.")

