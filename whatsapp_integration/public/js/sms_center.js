frappe.ui.form.on("SMS Center", "send_whatsapp", function(frm) {

	frappe.call({
		method: "whatsapp_integration.api.send_whatsapp",
		args: {
			receiver_list: frm.doc.receiver_list,
			doctype: 'SMS Center',
			msg: frm.doc.message
		},
		callback: function(r, rt) {
			if (r.message) {
				frappe.msgprint(r.message);
			}
		}
	});
});