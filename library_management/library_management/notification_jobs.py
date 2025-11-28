# import frappe

# def send_email_every_10_minutes():
#     # Here we enqueue a background email job
#     frappe.enqueue(
#         "library_management.library_management.notification_jobs.send_email_job",
#         queue="default"
#     )

# def send_email_job():
#     # This is the actual email sending background job
#     frappe.sendmail(
#         recipients=["test@example.com"],
#         subject="Scheduler Email Test",
#         message="This email is sent every 10 minutes from Library Management scheduler."
#     )
import frappe
from frappe.utils.pdf import get_pdf


def send_email_every_10_minutes():
    frappe.enqueue(
        "library_management.library_management.notification_jobs.send_email_job",
        queue="default"
    )


def send_email_job():

    # -------------------------------
    # 1️⃣ Report PDF (School Result Color Report)
    # -------------------------------
    report_pdf = frappe.get_print(
        doctype="Report",
        name="School Result Color Report"
    )

    # -------------------------------
    # 2️⃣ Print Format PDF (Purchase Order)
    # -------------------------------
    print_pdf = frappe.get_print(
        doctype="Purchase Order",
        name="PUR-ORD-2025-00005",
        print_format="jinja  practice"
    )

    # -------------------------------
    # 3️⃣ Email + Attachments
    # -------------------------------
    attachments = [
        {"fname": "School Result Color Report.pdf", "fcontent": report_pdf},
        {"fname": "Purchase Order.pdf", "fcontent": print_pdf},
    ]

    frappe.sendmail(
        recipients=["test@example.com"],
        subject="Scheduler Email Test",
        message="Attached School Report and Purchase Order Print Format.",
        attachments=attachments
    )
