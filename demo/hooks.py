from . import __version__ as app_version

app_name = "demo"
app_title = "Demo"
app_publisher = "Gatura Njenga"
app_description = "Print Sales Invoice Upon Submission"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "gatura@bulkbox.co.ke"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demo/css/demo.css"
# app_include_js = "/assets/demo/js/demo.js"

# include js, css files in header of web template
# web_include_css = "/assets/demo/css/demo.css"
# web_include_js = "/assets/demo/js/demo.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demo/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "demo.install.before_install"
# after_install = "demo.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "demo.uninstall.before_uninstall"
# after_uninstall = "demo.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "demo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Sales Invoice": {
		"on_submit":"demo.demo.sales_invoice_print_custom.open_print_view"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"demo.tasks.all"
#	],
#	"daily": [
#		"demo.tasks.daily"
#	],
#	"hourly": [
#		"demo.tasks.hourly"
#	],
#	"weekly": [
#		"demo.tasks.weekly"
#	]
#	"monthly": [
#		"demo.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "demo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "demo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "demo.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["demo.utils.before_request"]
# after_request = ["demo.utils.after_request"]

# Job Events
# ----------
# before_job = ["demo.utils.before_job"]
# after_job = ["demo.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"demo.auth.validate"
# ]

