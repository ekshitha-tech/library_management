// Copyright (c) 2025, shridevi and contributors
// For license information, please see license.txt

frappe.query_reports["Library Book Dropdown Report2"] = {
    onload: function(report) {
        report.page.set_title("Library Book Dropdown Report2");

        // Wait for the report to render
        frappe.after_ajax(() => {
            // Use event delegation to handle dropdown changes
            $(document).on("change", ".book-action", function() {
                const book_name = $(this).data("name");
                const selected_value = $(this).val();

                frappe.call({
                    method: "library_management.library_management.report.library_book_dropdown_report2.library_book_dropdown_report2.update_action",
                    args: {
                        docname: book_name,
                        action: selected_value
                    },
                    callback: function() {
                        frappe.show_alert({
                            message: __("Updated action for " + book_name + " to " + selected_value),
                            indicator: "green"
                        });
                    }
                });
            });
        });
    }
};
