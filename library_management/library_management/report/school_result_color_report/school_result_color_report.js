// Copyright (c) 2025, shridevi and contributors
// For license information, please see license.txt
frappe.query_reports["School Result Color Report"] = {
    onload: function(report) {
        report.page.set_title("School Result Color Report");
    },
    formatter: function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);
        if (column.fieldname === "positive_percentage" && data.positive_percentage !== undefined && data.positive_percentage !== null) {
            value = `<span style="color:green; font-weight:bold;">${data.positive_percentage}</span>`;
        }

        if (column.fieldname === "negative_percentage" && data.negative_percentage !== undefined && data.negative_percentage !== null) {
            value = `<span style="color:red; font-weight:bold;">${data.negative_percentage}</span>`;
        }
        return value;
    }
};


