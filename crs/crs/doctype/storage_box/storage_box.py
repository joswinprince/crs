# Copyright (c) 2023, Hephzibah Technologies Inc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StorageBox(Document):
	pass

storageBoxName = None
sample_list = None

@frappe.whitelist()
def get_samples_list(storageBoxName):
    sample_list = frappe.db.sql(f""" SELECT * FROM `tabSample` WHERE storage_box_name='{storageBoxName}' """, as_dict=True)
    return sample_list
