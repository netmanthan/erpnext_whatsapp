# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
from frappe.core.doctype.sms_settings.sms_settings import validate_receiver_nos


class WhatsappSettings(Document):
    def validate(self):
        validate_receiver_nos([self.wp_number])
