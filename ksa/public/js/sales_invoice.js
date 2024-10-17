frappe.ui.form.on("Sales Invoice", {
  on_submit(frm) {
    if (frm.doc.ksa_einv_qr) {
      let image_url = frm.doc.ksa_einv_qr; // Assuming 'ksa_einv_qr' holds the URL of the image
      let html = `<img src="${image_url}" style="max-width: 150px; max-height: 150px;">`;
      frm.set_df_property("custom_qr_image", "options", html); // Setting the image in the HTML field
    }
  },
});
