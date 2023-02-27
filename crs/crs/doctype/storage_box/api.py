# Copyright (c) 2023, Hephzibah Technologies Inc and contributors
# For license information, please see license.txt

import frappe

@frappe.whitelist()
def get_samples_list(storageBoxName):
    frappe.msgprint(f'after_insert : {storageBoxName}')
    sample_list = frappe.db.sql(f""" SELECT * FROM `tabSample` WHERE storage_box_name='{storageBoxName}' """, as_dict=True)
    return frappe.response['message'] = sample_list 
