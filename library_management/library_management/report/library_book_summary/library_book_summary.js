frappe.query_reports["Library Book Report"] = {
    filters: [
        {
            fieldname: "author",
            label: __("Author"),
            fieldtype: "Data",
            reqd: 0
        },
        {
            fieldname: "status",
            label: __("status"),
            fieldtype: "Select",
            options: ["Available", "Issued"],
            
        }
    ]
}
