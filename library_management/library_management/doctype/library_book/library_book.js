// Copyright (c) 2025, shridevi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Book", {
// 	refresh(frm) {

// 	},
// });
// additional validation on Task dates

// frappe.ui.form.on('Library Book', {
//     validate: function(frm) {
//         let today = frappe.datetime.get_today();

//         if (frm.doc.form_date && frm.doc.form_date < today) {
//             frappe.msgprint(__('You cannot select a past date in Form Date.'));
//             frappe.throw(__('Please select today or a future date.'));
//         }
//     }
// });
// frappe.ui.form.on('Library Book', {
//     onload_post_render(frm) {
//         frappe.msgprint('✅ The form is fully loaded and rendered!');
//         console.log("Form UI is ready for:", frm.doc.name);
//     }
// });


//frappe.ui.form.on('Library Book', {
    //refresh: function(frm) {
        // Fetch the 'email' from Library Member into 'member_email'
    //    cur_frm.add_fetch('member', 'email', 'member_email');
    //}
//});
//frappe.ui.form.on('Library Book', {
  //  refresh: function(frm) {
        // Make the IBSN field read-only after saving
    //    frm.set_df_property('ibsn', 'read_only', !frm.is_new());
    //}
//});
//frappe.ui.form.on('Library Book', {
    // Runs every time the form loads or refreshes
   // refresh(frm) {
     //   frappe.msgprint(__('Welcome to Library Book Form!'));
    //},

    // Runs before saving the document
    //validate(frm) {
      //  if (frm.doc.available_copies < 1) {
        //    frappe.throw(__('Cannot save — no available copies!'));
        //}
    //}
//});
// frappe.ui.form.on('Library Book', {
//    setup(frm) {
//        frappe.msgprint(__('Setup event triggered — runs only once when form is loaded first time!'));
//        frm.set_query('library_client', () => {
//            return {
//                filters: {
//                    active_member: 1  // show only active clients
//                }
//             };
//         });
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frappe.msgprint('📘 The form has been refreshed!');
//         console.log("Form refreshed for:", frm.doc.name);
//     }
// });


// frappe.ui.form.on('Library Book', {
//     before_load(frm) {
//         console.log("Before Load triggered");
//         frappe.msgprint(__('before_load event triggered — this runs before the form is displayed'));

//         // Example: pre-set a default author (just for testing)
//         if (!frm.doc.author) {
//             frm.doc.author = "Unknown Author";
//             console.log("Author field temporarily set before form loads");
//         }
//     }
// });

// 
// frappe.ui.form.on('Library Book', {
//     before_save(frm) {
//         frappe.msgprint(__('⚙️ before_save event triggered — preparing data to save'));
//         if (frm.doc.available_copies > 0) {
//             frm.set_value('status', 'Available');
//         } else {
//             frm.set_value('status', 'Out of Stock');
//         }
//         if (!frm.doc.form_date) {
//             frm.set_value('form_date', frappe.datetime.get_today());
//         }
//         console.log("⚙️ Before Save executed — data adjusted before saving");
//     },
//     after_save(frm) {
//         frappe.msgprint(__('💾 after_save event triggered — document saved successfully!'));
//         console.log("💾 After Save event executed for Library Book");
//     }
// });
// frappe.ui.form.on('Library Book', {
//     before_submit(frm) {
//         frappe.msgprint(__('📋 before_submit event triggered — preparing to submit Library Book'));
//         if (frm.doc.available_copies < 1) {
//             frappe.throw(__('Cannot submit — no available copies left.'));
//         }
//         frm.set_value('status', 'Submitted');

//         console.log("✅ before_submit event executed for Library Book");
//     },
//     on_submit(frm) {
//         frappe.msgprint(__('🚀 on_submit event triggered — Library Book has been submitted successfully!'));
//         console.log("🚀 on_submit event executed for Library Book");
//     }
// });

// frappe.ui.form.on('Library Book', {
//     before_cancel(frm) {
//         frappe.msgprint(__('⚠️ before_cancel event triggered — checking before cancellation'));
//         if (frm.doc.status === 'Issued') {
//             frappe.throw(__('Cannot cancel — this book is currently issued!'));
//         }

//         console.log("⚠️ Before Cancel event executed for Library Book");
//     },
//     after_cancel(frm) {
//         frappe.msgprint(__('❌ after_cancel event triggered — Library Book has been cancelled successfully!'));
//         frm.set_value('status', 'Cancelled');
//         console.log("❌ After Cancel event executed for Library Book");
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frappe.msgprint(__('📘 refresh event triggered — setting field values using frm.set_value'));
//         frm.set_value('book_name', 'The Great Gatsby');
//         frm.set_value('author', 'F. Scott Fitzgerald');
//         frm.set_value('form_date', frappe.datetime.get_today())
//             .then(() => {
//                 frappe.msgprint(__('📅 Form Date set to today!'));
//             });
//         console.log("✅ frm.set_value executed for Library Book — book_name, author, and form_date updated");
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frappe.msgprint(__('💾 refresh event triggered — now saving the form automatically'));

//         // Trigger save programmatically
//         frm.save().then(() => {
//             frappe.msgprint(__('🎉 Form saved successfully!'));
//             console.log("💾 frm.save() executed for Library Book");
//         });
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Check if the logged-in user has the 'Librarian' role
//         if (frappe.user_roles.includes('Librarian')) {
//             frm.enable_save();
//             frappe.msgprint(__('✅ You have the Librarian role — Save button enabled.'));
//         } else {
//             frm.disable_save();
//             frappe.msgprint(__('🚫 You are not a Librarian — Save button disabled.'));
//         }
//         console.log("Save button status updated based on user role");
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add a button to manually refresh the form
//         frm.add_custom_button(__('Refresh Form'), function() {
//             frappe.msgprint(__('🔄 Fetching latest data from server...'));

//             // Refresh the form
//             frm.refresh();

//             frappe.msgprint(__('✅ Form refreshed successfully!'));
//         });
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frappe.msgprint(__('🔄 Auto-saving form...'));
//         frm.save().then(() => {
//             frappe.msgprint(__('✅ Form saved successfully!'));
//         });
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Disable Save button when form loads
//         frm.disable_save();
//         frappe.msgprint(__('🚫 Save button disabled!'));

//         // Re-enable it after 5 seconds (for testing)
//         setTimeout(() => {
//             frm.enable_save();
//             frappe.msgprint(__('✅ Save button enabled again!'));
//         }, 5000);
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Open the Email dialog automatically when the form loads
//         // You can remove this automatic call if you only want to trigger it manually
//         frappe.msgprint(__('Opening email dialog...'));
//         frm.email_doc(`Hello, this is about the book "${frm.doc.book_name}" by ${frm.doc.author}.`);
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add a button to reload the document
//         frm.add_custom_button(__('🔄 Reload Document'), function() {
//             frappe.msgprint(__('Fetching latest document from server...'));
            
//             // Reload document
//             frm.reload_doc().then(() => {
//                 frappe.msgprint(__('✅ Document reloaded successfully!'));
//                 console.log("Form reloaded with latest data.");
//             });
//         });
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frappe.msgprint(__('Updating author name...'));

//         // Set a new value for the author field
//         frm.set_value('author', 'Unknown Author');

//         // Refresh only the author field (not the whole form)
//         frm.refresh_field('author');

//         frappe.msgprint(__('✅ Author field refreshed successfully!'));
//     }
// });

// frappe.ui.form.on('Library Book', {
//     book_name(frm) {
//         if (frm.is_dirty()) {
//             frappe.show_alert('📝 You changed the Book Name. Remember to save!');
//         }
//     }
// });
// frappe.ui.form.on('Library Book', {
//     onload(frm) {
//         frm.doc.browser_data = navigator.appVersion;
//         frm.dirty();

//         frappe.msgprint("✅ Form marked dirty and will be saved in a second!");

//         // Wait a bit before saving (so message stays visible)
//         setTimeout(() => {
//             frm.save();
//         }, 1000);
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         if (frm.is_new()) {
//             frappe.msgprint("🆕 This is a new unsaved Library Book form!");
//         } else {
//             frappe.msgprint("📘 This Library Book record is already saved!");
//         }
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         if (!frm.doc.author) {
//             frm.set_intro('✏️ Please enter the Author name before saving.', 'orange');
//         } else {
//             frm.set_intro('✅ Author name is set. You can continue editing.', 'green');
//         }
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frm.add_custom_button('Show Book Info', () => {
//             frappe.msgprint(`📘 Book Name: ${frm.doc.book_name || "Not set"}<br>✍️ Author: ${frm.doc.author || "Not set"}`);
//         });
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add buttons under a group called 'Set Status'
//         frm.add_custom_button('Available', () => {
//             frm.set_value('status', 'Available');
//             frappe.msgprint('📗 Status set to Available');
//         }, 'Set Status');

//         frm.add_custom_button('Issued', () => {
//             frm.set_value('status', 'Issued');
//             frappe.msgprint('📕 Status set to Issued');
//         }, 'Set Status');

//         frm.add_custom_button('Lost', () => {
//             frm.set_value('status', 'Lost');
//             frappe.msgprint('❌ Status set to Lost');
//         }, 'Set Status');

//         // Change the button types/colors immediately
//         frm.change_custom_button_type('Available', 'primary', 'Set Status'); // blue
//         frm.change_custom_button_type('Issued', 'warning', 'Set Status');    // orange/yellow
//         frm.change_custom_button_type('Lost', 'danger', 'Set Status');       // red
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add a button first
//         frm.add_custom_button('Show Info', () => {
//             frappe.msgprint(`Book: ${frm.doc.book_name || "Not set"}`);
//         });

//         // Remove it immediately (just for testing)
//         frm.remove_custom_button('Show Info');
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add some custom buttons first
//         frm.add_custom_button('Available', () => frm.set_value('status', 'Available'), 'Set Status');
//         frm.add_custom_button('Issued', () => frm.set_value('status', 'Issued'), 'Set Status');
//         frm.add_custom_button('Lost', () => frm.set_value('status', 'Lost'), 'Set Status');

//         frappe.msgprint("Custom buttons added!");

//         // Clear all custom buttons
//         frm.clear_custom_buttons();

//         frappe.msgprint("All custom buttons removed!");
//     }
// });


// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frm.set_df_property('status', 'options', ['Open', 'Closed']);
//         frm.set_df_property('book_name', 'reqd', 1);
//         frm.set_df_property('status', 'read_only', 1);
//         frappe.msgprint("Fields properties updated dynamically!");
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         let is_allowed = frappe.user_roles.includes('System Manager');

//         // Enable or disable fields based on the role
//         frm.toggle_enable(['status', 'author'], is_allowed);

//         // Delay the message slightly so it appears
//         if (!is_allowed) {
//             setTimeout(() => {
//                 frappe.msgprint('🔒 Status and Author fields are read-only for your role.');
//             }, 300); // 300ms delay
//         }
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Make author mandatory only if status is not Draft
//         let make_author_required = frm.doc.status !== 'Draft';
//         frm.toggle_reqd('author', make_author_required);

//         // Optional: show a message when it becomes required
//         if (make_author_required) {
//             frappe.msgprint('✍️ Author field is now mandatory because status is not Draft.');
//         }
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         let show_date = frm.doc.status === 'Issued';
//         frm.toggle_display('form_date', show_date);

//         if (!show_date) {
//             frappe.msgprint('🛈 form_date field is hidden because status is not Issued.');
//         }
//     }
// });
// frappe.ui.form.on('Library Book', {
//     setup(frm) {
//         frm.set_query('member', function() {
//             return {
//                 filters: {
//                     status: 'Active'  // This 'status' is from Library Client
//                 }
//             };
//         });
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // add new child row to Transaction table
//         let row = frm.add_child('transaction', {
//             member: 'Siri',
//             book_name: frm.doc.name,
//             form_date: frappe.datetime.nowdate()
//         });
//         frm.refresh_field('transaction');
//         frappe.msgprint('✅ New transaction added!');
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frm.call({
//             method: 'get_author_name',   // method name from your Python class
//             doc: frm.doc,                // pass current document context
//             callback: function(r) {
//                 if (r.message) {
//                     frappe.msgprint(`📚 The author name is: ${r.message}`);
//                 }
//             }
//         });
//     }
// });

// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frm.trigger('set_mandatory_fields');
//     },
//     set_mandatory_fields(frm) {
//         let is_available = frm.doc.status === 'Available';
//         frm.toggle_reqd('author', is_available);

//         frappe.msgprint('✅ Author field is ' + (is_available ? 'mandatory' : 'not mandatory'));
//     }
// });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         // Add a button to test selected rows
//         frm.add_custom_button('Show Selected Rows', () => {
//             let selected = frm.get_selected();

//             // If no rows are selected
//             if (!selected.transactions || selected.transactions.length === 0) {
//                 frappe.msgprint('⚠️ No rows selected in Transactions table.');
//                 return;
//             }

//             // Show selected rows in a popup
//             frappe.msgprint(`✅ Selected Rows: ${JSON.stringify(selected.transactions)}`);

//             // Also log in browser console for clarity
//             console.log("Selected rows:", selected);
//         });
//     }
// });

// frappe.ui.form.on('Library Transaction2', {
//     onload(frm) {
//         // Prevent linked Library Book and Library Client from getting cancelled
//         frm.ignore_doctypes_on_cancel_all = ['Library Book', 'Library Client'];

//         frappe.msgprint('🛑 Will ignore Library Book and Library Client during Cancel All.');
//     }
// });



// frappe.ui.form.on('Library Book', {
//     timeline_refresh(frm) {
//         console.log("🕒 timeline_refresh: Timeline refreshed for this document");
//         frappe.msgprint("📜 Timeline has been refreshed!");
//     }
// });



// frappe.ui.form.on('Library Book', {
//     transaction_on_form_rendered(frm, cdt, cdn) {
//         let row = frappe.get_doc(cdt, cdn);
//         frappe.msgprint(`🧾 You opened a Transaction row for Member: ${row.member || 'Unknown Member'}`);
//     }
// });


// frappe.ui.form.on('Library Book', {
//     member(frm) {
//         frappe.msgprint(`👤 Member changed to: ${frm.doc.member}`);
//     }
// });



//Dialogue API
// frappe.ui.form.on('Library Book', {
//     refresh: function(frm) {

//         // 1️⃣ frappe.ui.Dialog
//         let d = new frappe.ui.Dialog({
//             title: 'Enter details',
//             fields: [
//                 { label: 'First Name', fieldname: 'first_name', fieldtype: 'Data' },
//                 { label: 'Last Name', fieldname: 'last_name', fieldtype: 'Data' },
//                 { label: 'Age', fieldname: 'age', fieldtype: 'Int' }
//             ],
//             primary_action_label: 'Submit',
//             primary_action(values) {
//                 frappe.msgprint(__('You entered: ' + values.first_name + ' ' + values.last_name + ', Age: ' + values.age));
//                 d.hide();
//             }
//         });

//         // Show the dialog on refresh
//         d.show();


//         // 2️⃣ frappe.msgprint
//         frappe.msgprint({
//             title: __('Notification'),
//             indicator: 'green',
//             message: __('Document loaded successfully!')
//         });

//         // 3️⃣ frappe.throw
//         // Uncomment to test — this will stop execution
//         // frappe.throw(__('This is a test error message'));

//         // 4️⃣ frappe.prompt (multiple fields)
//         frappe.prompt([
//             { label: 'Favorite Book', fieldname: 'book', fieldtype: 'Data' },
//             { label: 'Library Card No', fieldname: 'card_no', fieldtype: 'Int' },
//         ], (values) => {
//             frappe.msgprint(`Book: ${values.book}, Card: ${values.card_no}`);
//         });

//         // 5️⃣ frappe.confirm
//         frappe.confirm('Do you want to see a thank-you message?',
//             () => frappe.msgprint('✅ Thank you for confirming!'),
//             () => frappe.msgprint('❌ You cancelled it.')
//         );

//         // 6️⃣ frappe.warn
//         frappe.warn('Proceed?', 'This will not be saved.',
//             () => frappe.msgprint('You chose to continue.'),
//             'Continue',
//             true
//         );

//         // 7️⃣ frappe.show_alert
//         frappe.show_alert({ message: 'Library Book Form Loaded', indicator: 'green' }, 5);

//         // 8️⃣ frappe.show_progress
//         frappe.show_progress('Loading Books', 70, 100, 'Almost done!');

//         // 9️⃣ frappe.new_doc
//         // Creates a new Library Client document with a prefilled name
//         frappe.new_doc('Library Client', { first_name: 'Auto Created Client' });

//         // 🔟 frappe.ui.form.MultiSelectDialog
//         new frappe.ui.form.MultiSelectDialog({
//             doctype: "Library Book",
//             target: frm,
//             setters: { author: null },
//             add_filters_group: 1,
//             date_field: "modified",
//             get_query() {
//                 return { filters: { docstatus: ['!=', 2] } };
//             },
//             action(selections) {
//                 frappe.msgprint('Selected: ' + selections.join(', '));
//             }
//         });

//         // 11️⃣ Table / Grid in a Dialog
//         const dialog = new frappe.ui.Dialog({
//             title: __("Log Activity"),
//             fields: [
//                 {
//                     fieldname: "logs",
//                     fieldtype: "Table",
//                     label: __("Logs"),
//                     in_place_edit: true,
//                     fields: [
//                         { fieldname: "log_type", label: __("Log Type"), fieldtype: "Select", options: "IN\nOUT", in_list_view: 1, reqd: 1 },
//                         { fieldname: "time", label: __("Time"), fieldtype: "Time", in_list_view: 1, reqd: 1 }
//                     ],
//                     on_add_row: (idx) => {
//                         let data_id = idx - 1;
//                         let logs = dialog.fields_dict.logs;
//                         let log_type = (data_id % 2) == 0 ? "IN" : "OUT";
//                         logs.df.data[data_id].log_type = log_type;
//                         logs.grid.refresh();
//                     },
//                 },
//             ],
//             primary_action_label: __("Save Logs"),
//             primary_action(values) {
//                 frappe.msgprint('Logs saved successfully!');
//                 dialog.hide();
//             }
//         });
//         dialog.show();
//     }
// });

// let d = new frappe.ui.Dialog({
//     title: 'Enter details',
//     fields: [
//         { label: 'First Name', fieldname: 'first_name', fieldtype: 'Data' },
//         { label: 'Last Name', fieldname: 'last_name', fieldtype: 'Data' },
//         { label: 'Age', fieldname: 'age', fieldtype: 'Int' }
//     ],
//     primary_action_label: 'Submit',
//     primary_action(values) {
//         console.log(values);
//         d.hide();
//     }
// });
// d.show();

//frappe.msgprint(__('Document updated successfully'));


//frappe.throw(__('This is an Error Message'));
// frappe.prompt([
//     { label: 'First Name', fieldname: 'first_name', fieldtype: 'Data' },
//     { label: 'Last Name', fieldname: 'last_name', fieldtype: 'Data' }
// ], (values) => {
//     console.log(values.first_name, values.last_name);
// });


// frappe.confirm('Are you sure you want to proceed?',
////     () => frappe.msgprint('Yes selected'),
//     () => frappe.msgprint('No selected')
// );
// frappe.warn(
//     'Are you sure you want to proceed?',
//     'There are unsaved changes on this page',
//     () => frappe.msgprint('Continued'),
//     'Continue',
//     true
// );
// frappe.show_alert({
//     message: __('Saved successfully'),
//     indicator: 'green'
// }, 3);

//frappe.show_progress('Loading..', 70, 100, 'Please wait');
// frappe.new_doc('Library Book', { title: 'Atomic Habits' }, doc => {
//     doc.publisher = 'James Clear Publications';
//     frappe.msgprint('Book form initialized!');
// });

// new frappe.ui.form.MultiSelectDialog({
//     doctype: "Library Book",
//     target: cur_frm,
//     setters: { author: null },
//     add_filters_group: 1,
//     date_field: "modified",
//     get_query() {
//         return { filters: { docstatus: ['!=', 2] } };
//     },
//     action(selections) {
//         frappe.msgprint('Selected: ' + selections.join(', '));
//     }
// });

// const dialog = new frappe.ui.Dialog({
//     title: __("Create Logs"),
//     fields: [
//         {
//             fieldname: "logs",
//             fieldtype: "Table",
//             label: __("Logs"),
//             in_place_edit: true,
//             fields: [
//                 { fieldname: "log_type", label: "Log Type", fieldtype: "Select", options: "IN\nOUT", in_list_view: 1, reqd: 1 },
//                 { fieldname: "time", label: "Time", fieldtype: "Time", in_list_view: 1, reqd: 1 }
//             ],
//             on_add_row: (idx) => {
//                 let logs = dialog.fields_dict.logs;
//                 logs.df.data[idx - 1].log_type = (idx % 2 === 0) ? "IN" : "OUT";
//                 logs.grid.refresh();
//             },
//         },
//     ],
//     primary_action_label: __("Create"),
//     primary_action(values) {
//         console.log(values);
//     }
// });
// dialog.show();


// frappe.db.get_doc('Library Book', '3dtqb0s4a4')
//     .then(doc => {
//         console.log(doc);
//         frappe.msgprint(`Book Title: ${doc.title}`);
//     });

// frappe.db.get_list('Library Book', {
//     fields: ['author'],
//     filters: { status: 'Available' }
// }).then(records => {
//     console.log(records);
// });
// frappe.db.get_value('Library Book', 'mi5v3pha0d', ['author'])
//     .then(r => {
//         frappe.msgprint(`Book: ${r.message.book_name} by ${r.message.author}`);
//     });
// frappe.db.get_single_value('Library Settings', 'default_library_branch')
//     .then(value => {
//         frappe.msgprint(`Default Branch: ${value}`);
//     });
// frappe.db.set_value('Library Book', '1sj1k74kc8', 'status', 'Issued')
//     .then(r => {
//         frappe.msgprint('Book status updated!');
//     });
// frappe.db.insert({
//     doctype: 'Library Book',
//     book_name: 'The Alchemist',
//     author: 'Paulo Coelho',
//     status: 'Available'
// }).then(doc => {
//     frappe.msgprint(`New Book Added: ${doc.name}`);
// });
// frappe.db.count('Library Book', { status: 'Available' })
//     .then(count => {
//         frappe.msgprint(`Available Books: ${count}`);
//     });
// frappe.db.delete_doc('Library Book', 'vsbs12kv5n')
//     .then(() => {
//         frappe.msgprint('Book deleted successfully!');
//     });

// frappe.db.exists('Library Book', 'mi5v3pha0d')
//     .then(exists => {
//         frappe.msgprint(exists ? 'Book exists ✅' : 'Book not found ❌');
//     });
// frappe.ui.form.on('Library Book', {
//     refresh(frm) {
//         frm.add_custom_button('Show Book Name', () => {
//             frm.call({
//                 method: 'show_book_name',  // just method name, not full path
//                 doc: frm.doc               // ensures call is made as Document method
//             });
//         });
//     }
// });

