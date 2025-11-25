frappe.ui.form.on("ToDo", {
    refresh: function(frm) {
        frm.trigger("my_custom_code");
    },
    my_custom_code: function(frm){
        frappe.msgprint("🧩 Custom JS Triggered for: " + frm.doc.name);
        console.log("Custom code executed for ToDo:", frm.doc.name);
    }
});
