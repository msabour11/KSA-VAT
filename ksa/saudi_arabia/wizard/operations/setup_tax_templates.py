import json
import os

from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data, simple_to_detailed

def setup_templates(doc,method=None):
    if doc.country == 'Saudi Arabia':
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ksa_template.json")
        with open(file_path, "r") as json_file:
            template = simple_to_detailed(json.load(json_file))
            from_detailed_data(doc.name,template)


##############3

# import os
# import json
# import frappe


# def setup_templates(doc, method=None):
#     if doc.country == "Saudi Arabia":
#         try:
#             # Resolve file path
#             file_path = os.path.join(
#                 os.path.dirname(__file__), "..", "data", "ksa_template.json"
#             )
#             frappe.logger().info(f"Loading KSA template from: {file_path}")

#             # Load JSON data
#             with open(file_path, "r") as json_file:
#                 json_data = json.load(json_file)
#                 frappe.logger().info(f"JSON data loaded: {json_data}")

#                 # Convert simple data to detailed structure
#                 template = simple_to_detailed(json_data)
#                 frappe.logger().info(f"Converted template: {template}")

#                 # Create templates
#                 from_detailed_data(doc.name, template)
#                 frappe.logger().info("Templates setup successfully.")

#         except frappe.exceptions.ValidationError as e:
#             frappe.throw(f"Failed to load the tax template: {str(e)}")
#         except FileNotFoundError:
#             frappe.throw(f"Tax template file not found at path: {file_path}")
#         except json.JSONDecodeError:
#             frappe.throw(
#                 "Failed to parse JSON file. Ensure the file is in valid JSON format."
#             )
#         except Exception as e:
#             frappe.throw(f"An unexpected error occurred: {str(e)}")


################3


# import json
# import os
# import frappe
# from erpnext.setup.setup_wizard.operations.taxes_setup import (
#     from_detailed_data,
#     simple_to_detailed,
# )


# def create_tax_account(account_name, tax_rate):
#     """Create a tax account if it doesn't already exist."""
#     existing_account = frappe.get_all("Account", filters={"account_name": account_name})
#     if not existing_account:
#         # Create new account
#         account = frappe.get_doc(
#             {
#                 "doctype": "Account",
#                 "account_name": account_name,
#                 "account_type": "Tax",
#                 "is_group": 1,
#                 "tax_rate": tax_rate,
#             }
#         )
#         account.insert()
#         frappe.db.commit()  # Commit to save the new account
#         frappe.msgprint(f"Created account: {account_name}")


# def setup_templates(doc, method=None):
#     if doc.country == "Saudi Arabia":
#         # Define the path to the template file
#         file_path = os.path.join(
#             os.path.dirname(__file__), "..", "data", "ksa_template.json"
#         )

#         # Verify the file exists
#         if not os.path.isfile(file_path):
#             frappe.throw(f"Template file not found at {file_path}")

#         try:
#             # Load JSON data
#             with open(file_path, "r") as json_file:
#                 template_data = json.load(json_file)

#             # Validate and create tax accounts
#             for tax_key, tax_info in template_data.items():
#                 create_tax_account(tax_info["account_name"], tax_info["tax_rate"])

#             # Convert simple template to detailed format (if applicable)
#             detailed_template = simple_to_detailed(template_data)

#             # Validate detailed_template structure
#             if not detailed_template or not isinstance(detailed_template, list):
#                 frappe.throw("Template data is invalid or missing necessary structure.")

#             # Call from_detailed_data
#             from_detailed_data(doc.name, detailed_template)

#         except json.JSONDecodeError as e:
#             frappe.throw(f"JSON decode error: {str(e)}")
#         except Exception as e:
#             frappe.throw(f"Failed to load the tax template: {str(e)}")


# import json
# import os
# import frappe
# from erpnext.setup.setup_wizard.operations.taxes_setup import (
#     from_detailed_data,
#     simple_to_detailed,
# )


# def setup_templates(doc, method=None):
#     if doc.country == "Saudi Arabia":
#         # Define the path to the template file
#         file_path = os.path.join(
#             os.path.dirname(__file__), "..", "data", "ksa_template.json"
#         )

#         # Verify the file exists
#         if not os.path.isfile(file_path):
#             frappe.throw(f"Template file not found at {file_path}")

#         try:
#             # Load JSON data
#             with open(file_path, "r") as json_file:
#                 template_data = json.load(json_file)

#             # Convert simple template to detailed format
#             detailed_template = simple_to_detailed(template_data)

#             # Validate detailed_template structure before passing it to from_detailed_data
#             if not detailed_template or not isinstance(detailed_template, list):
#                 frappe.throw("Template data is invalid or missing necessary structure.")

#             # Run from_detailed_data with a try-except to capture detailed issues
#             try:
#                 from_detailed_data(doc.name, detailed_template)
#             except IndexError as e:
#                 frappe.throw(f"Error in processing tax group setup: {str(e)}")
#             except Exception as e:
#                 frappe.throw(f"An unexpected error occurred: {str(e)}")

#         except json.JSONDecodeError as e:
#             frappe.throw(f"JSON decode error: {str(e)}")
#         except Exception as e:
#             frappe.throw(f"Failed to load the tax template: {str(e)}")
