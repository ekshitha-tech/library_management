// Copyright (c) 2025, shridevi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Category", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Category', {
    refresh(frm) {
        // Add a custom button to show children
        frm.add_custom_button('Show Children', () => {
            frappe.call({
                method: "library_management.library_management.doctype.category.category.show_children",
                args: { name: frm.doc.name },
                callback(r) {
                    if (r.message && r.message.length > 0) {
                        frappe.msgprint("Children: " + r.message.join(", "));
                    } else {
                        frappe.msgprint("No children found");
                    }
                }
            });
        });

        // Add a custom button to show parent
        frm.add_custom_button('Show Parent', () => {
            frappe.call({
                method: "library_management.library_management.doctype.category.category.show_parent",
                args: { name: frm.doc.name },
                callback(r) {
                    frappe.msgprint("Parent: " + (r.message || "No parent"));
                }
            });
        });
    }
});
