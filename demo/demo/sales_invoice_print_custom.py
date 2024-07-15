import frappe

def open_print_view(doc, method):
    print_url = f"/printview?doctype=Sales%20Invoice&name={doc.name}&format=Standard&no_letterhead=0"
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = print_url