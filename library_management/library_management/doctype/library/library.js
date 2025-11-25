// Copyright (c) 2025, shridevi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Library', {
//     library_name: function(frm) {
//         frappe.call({
//             method: "library_management.library_management.doctype.library.library.get_library_message",
//             type: "POST",   // <-- HERE is the POST type
//             args: {
//                 library_name: frm.doc.library_name
//             },
//             freeze: true,
//             freeze_message: "Fetching data from server...",

//             success: function(r) {
//                 if (r.message) {
//                     frappe.msgprint("Server Response: " + r.message);
//                 }
//             },

//             error: function(r) {
//                 frappe.msgprint("Error occurred while calling server!");
//             },

//             always: function(r) {
//                 console.log("Request completed.");
//             }
//         });
//     }
// });
