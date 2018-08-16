---
title: NetSuite
permalink: /integrations/saas/netsuite
tags: [saas_integrations]
keywords: netsuite, integration, schema, etl netsuite, netsuite etl, netsuite schema
summary: "Connection instructions and schema details for Stitch's NetSuite integration."
format: ## controls formatting options in template
  schema-list: false
  table-desc: true
  list: table

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "netsuite"
display_name: "NetSuite"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.netsuite.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"
icon: /images/integrations/icons/netsuite.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Account
  - name: "netsuite_account"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/account.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Accounting Period
  - name: "netsuite_accounting_period"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/accountingperiod.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## App Definition
  - name: "netsuite_app_definition"
    doc-link: 
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## App Package
  - name: "netsuite_app_package"
    doc-link: 
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Billing Schedule
  - name: "netsuite_billing_schedule"
    doc-link: 
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Bin
  - name: "netsuite_bin"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/bin.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Budget
  - name: "netsuite_budget"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/budgetsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Calendar Event
  - name: "netsuite_calendar_event"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/calendareventsearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false 

## Campaign
  - name: "netsuite_campaign"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/campaign.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false 

## Charge
  - name: "netsuite_charge"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/charge.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Classification
  - name: "netsuite_classification"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/classificationsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Contact
  - name: "netsuite_contact"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/contact.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Contact Category
  - name: "netsuite_contact_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/contactcategorysearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Contact Role
  - name: "netsuite_contact_role"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/contactrolesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Coupon Code
  - name: "netsuite_coupon_code"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/couponcode.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Currency Rate
  - name: "netsuite_currency_rate"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/currencyratesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Custom List
  - name: "netsuite_custom_list"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customlistsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Customer
  - name: "netsuite_customer"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customersearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Customer Category
  - name: "netsuite_customer_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/customercategory.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Customer Message
  - name: "netsuite_customer_message"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customermessagesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Customer Status
  - name: "netsuite_customer_status"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customerstatussearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Custom Records
  - name: "netsuite_custom_records"
    doc-link: 
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Deleted Records
  - name: "netsuite_deleted"
    doc-link: 
    notes: See <a href="#using-netsuite-deleted">Deleted Records</a> for info on using this table.
    replication-method: "Key-based Incremental"
    primary-key: "internalid:_type"
    abstract: true

## Department
  - name: "netsuite_department"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/department.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Employee
  - name: "netsuite_employee"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/employeesearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Entity Group
  - name: "netsuite_entity_group"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/entitygroup.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Expense Category
  - name: "netsuite_expense_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/expensecategory.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## File
  - name: "netsuite_file"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/filesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Folder
  - name: "netsuite_folder"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/folder.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Gift Certificate
  - name: "netsuite_gift_certificate"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/giftcertificate.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Global Account Mapping
  - name: "netsuite_global_account_mapping"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/globalaccountmapping.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Inventory Number
  - name: "netsuite_inventory_number"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/inventorynumber.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Issue
  - name: "netsuite_issue"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/issue.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Item
  - name: "netsuite_item"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/item.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Item Account Mapping
  - name: "netsuite_item_account_mapping"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/itemaccountmapping.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Item Demand Plan
  - name: "netsuite_item_demand_plan"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/itemdemandplan.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Item Revision
  - name: "netsuite_item_revision"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/itemrevision.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid:_type"
    abstract: true

## Item Supply Plan
  - name: "netsuite_item_supply_plan"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/itemsupplyplan.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Job
  - name: "netsuite_job"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/jobsearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Job Status
  - name: "netsuite_job_status"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/jobstatussearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Job Type
  - name: "netsuite_job_type"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/jobtypesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Location
  - name: "netsuite_location"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/location.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Manufacturing Cost Template
  - name: "netsuite_manufacturing_cost_template"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/manufacturingcosttemplate.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Manufacturing Operation Task
  - name: "netsuite_manufacturing_operation_task"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/manufacturingoperationtask.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Manufacturing Routing
  - name: "netsuite_manufacturing_routing"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/manufacturingrouting.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Message
  - name: "netsuite_message"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/message.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Nexus
  - name: "netsuite_nexus"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/nexus.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Note
  - name: "netsuite_note"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/note.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Note Type
  - name: "netsuite_note_type"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/notetypesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Opportunity
  - name: "netsuite_opportunity"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/opportunity.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Originating Lead
  - name: "netsuite_originating_lead"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/originatingleadsearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid:type"
    abstract: true

## Other Name Category
  - name: "netsuite_other_name_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/othernamecategorysearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Partner
  - name: "netsuite_partner"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/partner.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Partner Category
  - name: "netsuite_partner_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/partnercategorysearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Payment Method
  - name: "netsuite_payment_method"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/paymentmethodsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Payroll Item
  - name: "netsuite_payroll_item"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/payrollitem.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Phone Call
  - name: "netsuite_phone_call"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/phonecall.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Price Level
  - name: "netsuite_price_level"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/pricelevel.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Pricing Group
  - name: "netsuite_pricing_group"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/pricinggroupsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Project Task
  - name: "netsuite_project_task"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/projecttask.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Promotion Code
  - name: "netsuite_promotion_code"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/promotioncodesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Resource Allocation
  - name: "netsuite_resource_allocation"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/resourceallocation.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Rev Rec Schedule
  - name: "netsuite_rev_rec_schedule"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/revrecschedule.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Rev Rec Template
  - name: "netsuite_rev_rec_template"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/revrectemplate.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Sales Role
  - name: "netsuite_sales_role"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/salesrolesearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Site Category
  - name: "netsuite_site_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/sitecategorysearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Solution
  - name: "netsuite_solution"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/solution.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Subsidiary
  - name: "netsuite_subsidiary"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/subsidiary.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Support Case
  - name: "netsuite_support_case"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/supportcasesearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Task
  - name: "netsuite_task"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/task.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Term
  - name: "netsuite_term"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/term.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Time Bill
  - name: "netsuite_time_bill"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/timebillsearchbasic.html?mode=package
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Time Entry
  - name: "netsuite_time_entry"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/timeentry.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Time Sheet
  - name: "netsuite_time_sheet"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/timesheet.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Topic
  - name: "netsuite_topic"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/topic.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Transaction
  - name: "netsuite_transaction"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/transaction.html
    notes: See <a href="#transaction-types">Supported Transaction Types</a> for a list of the transaction types Stitch will replicate.
    replication-method: "Key-based Incremental"
    primary-key: "internalid:_type"
    abstract: true

## Units Type
  - name: "netsuite_units_type"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/unitstype.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Vendor
  - name: "netsuite_vendor"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/vendor.html
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "internalid"
    abstract: false

## Vendor Category
  - name: "netsuite_vendor_category"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/vendorcategory.html
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

## Win Loss Reason
  - name: "netsuite_win_loss_reason"
    doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/winlossreasonsearchbasic.html?mode=package
    notes: 
    replication-method: "Full Table"
    primary-key: "internalid"
    abstract: false

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your NetSuite data to Stitch is a six-step process:

1. [Locate your NetSuite Account ID](#locate-netsuite-account-id)
2. [Create a Stitch NetSuite Admin user](#create-netsuite-admin-user)
3. [Retrieve the Stitch NetSuite user's Role ID](#retrieve-netsuite-role-id)
4. [Add NetSuite as a Stitch data source](#add-stitch-data-source)
5. [Define the Historical Sync](#define-historical-sync)
6. [Define the Replication Frequency](#define-rep-frequency)
7. [Set tables to replicate](#syncing-data)

### Prerequisites

**You must have Administrator permissions in NetSuite.** This is required to complete parts of the setup.

### Locate your NetSuite Account ID {#locate-netsuite-account-id}

{% include layout/inline_image.html type="right" file="integrations/netsuite-account-id.png" alt="NetSuite account ID in Web Services Preferences" max-width="250px" %}
1. Sign into your NetSuite account.
2. Click the **Setup** option in the top navigation menu, then **Integration > Web Services Preferences**.
3. In the **Primary Information**, locate the **Account ID** field as shown in the image on the right.

**Note**: If your Account ID contains a suffix - `1234567_SB2`, for example - it should be included when entering the ID into Stitch.

### Create a Stitch NetSuite Admin user {#create-netsuite-admin-user}

To connect NetSuite to Stitch, we recommend that you create a Stitch-specific Admin user for us. We suggest this approach for a few reasons:

1. This will ensure that Stitch is easily distinguishable in any logs or audits.
2. NetSuite's API has some limitations that could make it difficult or impossible for Stitch to replicate data. For example: a single NetSuite user is only allowed to have **one** open API session at a time. If there's another connection elsewhere, Stitch will run into problems replicating data.

After you've created the Admin user, move onto the next step.

### Retrieve the Stitch NetSuite user's Role ID {#retrieve-netsuite-role-id}

All Roles in NetSuite have a **Name** - for example, Accountant - and **Role ID**, or **Internal ID** number. Stitch requires the Role ID to successfully create a NetSuite integration.

#### Locate the Role ID

Role IDs can be found on the **Manage Roles** page in NetSuite. From your dashboard, click **Setup > Users/Roles > Manage Roles**.

Locate the Role of the user in the Roles list. The ID is located in a column called **Internal ID**:

![The Internal ID column contains the user's Role ID.]({{ site.baseurl }}/images/integrations/netsuite-locate-role-id.png)

If you don't see the Internal ID column in the list, you may need to add it:

1. Click the **Edit View** button.
2. Click the drop-down menu and select **Internal ID**.
3. Click **Add**.
4. Click **Save**.

After you add the column to the Roles list, locate the ID for the user.

{% include integrations/shared-setup/connection-setup.html %}
4. Enter the email address and password associated with the Stitch NetSuite user.
5. Enter the **Role ID** - the numerical ID, not the name of the role - associated with the user entered above.

   **Note**: If this field is left blank, Stitch will use NetSuite's default role ID for Admin roles, which is 3. If you receive an error when trying to save the integration, enter a 3 in this field and try saving again.
6. In the **Account ID** field, enter your NetSuite account ID. If your Account ID contains a suffix - `1234567_SB2`, for example - it should also be entered into this field.
6. Select the **Account Type** - Production or Sandbox.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/saas/setup/saas-syncing.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}


## Deleted Records {#using-netsuite-deleted}
Stitch's NetSuite integration includes a table called `netsuite_deleted`; this table contains a row for **every deleted record that supports deletes**. Accounting for deleted records is especially important if you’re performing any sort of aggregate function - for example, totaling invoices or balancing your books.

For this reason, **we strongly recommend you set this table to sync when selecting tables to replicate**.

### netsuite_deleted Table Schema {#netsuite-deleted-table-schema}
The attributes of the `netsuite_deleted` table include:

- **type**: This indicates the **type** of record. For example: invoice.
- **name**: This is the name of the record. For example: Invoice #INV197
- **deletedDate:** The date the record was deleted.
- **customRecord:** This indicates if the record was a custom record.
- **internalId:** This is the numerical ID of the record.

**Custom records will look a little different than other records.** In this case, you'll see the following:

- **type**: This column will contain a **numerical ID**.
- **name** & **internalid**: The `internalid` of the record will display in **both** columns.
- **customRecord**: This column will contain a `true` value.

For example: the first two records in this table are "normal" records, while the third is a custom record:

| type         | internalId | name             | customRecord | deletedDate                   |
|--------------+------------+------------------+--------------+-------------------------------|
| invoice      | 124831     | Invoice #INV197  | false        | 2016-08-02T09:33:07.000-07:00 |
| journalEntry | 111366     | Journal #JV13526 | false        | 2016-08-04T12:01:22.000-07:00 |
| 19           | 128        | 128              | true         | 2016-07-21T12:05:26.000-07:00 |

### Accounting for Deleted Records {#accounting-record-deletes}

To account for deleted records, you can use a `LEFT JOIN` to tie deleted records back to the appropriate table. For example, the following SQL query would return all invoice records that exist in both the `netsuite_transaction` table and `netsuite_deleted` table:

{% highlight sql %}
SELECT * 
FROM netsuite_transactions tran 
LEFT JOIN netsuite_deleted del ON tran.internalId = del.internalId 
AND tran.type = ‘invoice’ 
AND del.type = ‘invoice’
{% endhighlight %}

If you're using a data warehouse that is **case-insensitive** (like Redshift), some queries may result in errors. If this occurs, try using `LOWER` to resolve the issue:

{% highlight sql %}
SELECT * 
FROM netsuite_transactions tran 
LEFT JOIN netsuite_deleted del 
ON tran.internalId = del.internalId 
AND LOWER(tran.type) = LOWER(del.type)
{% endhighlight %}

**To filter out deleted records from other data,** you can run a query like this one:

{% highlight sql %}
SELECT * 
FROM netsuite_transactions tran 
LEFT JOIN netsuite_deleted del ON tran.internalId = del.internalId 
AND LOWER(tran.type) = LOWER(del.type) 
WHERE del.deletedDate is null;
{% endhighlight %}

---

## Supported Transaction Types {#transaction-types}
Because NetSuite includes so much under transactions, it may be a little difficult to know what to expect in the `netsuite_transaction` table. To give you a better idea, here’s a full list of what our integration will pull into this table:

<table>
<tbody>
<tr>
<td valign="top">AssemblyBuild</td>
<td valign="top">CustomerPayment</td>
<td valign="top">ItemFulfillment</td>
<td valign="top">VendorBill</td>
</tr>
<tr>
<td valign="top">AssemblyUnBuild</td>
<td valign="top">CustomerRefund</td>
<td valign="top">ItemReceipt</td>
<td valign="top">VendorCredit</td>
</tr>
<tr>
<td valign="top">BinTransfer</td>
<td valign="top">Deposit</td>
<td valign="top">Journal</td>
<td valign="top">VendorPayment</td>
</tr>
<tr>
<td valign="top">BinWorksheet</td>
<td valign="top">DepositApplication</td>
<td valign="top">Opportunity</td>
<td valign="top">VendorReturnAuthorization</td>
</tr>
<tr>
<td valign="top">CashRefund</td>
<td valign="top">Estimate</td>
<td valign="top">PaycheckJournal</td>
<td valign="top">WorkOrder</td>
</tr>
<tr>
<td valign="top">CashSale</td>
<td valign="top">ExpenseReport</td>
<td valign="top">PurchaseOrder</td>
<td valign="top">WorkOrderClose</td>
</tr>
<tr>
<td valign="top">Check</td>
<td valign="top">InventoryAdjustment</td>
<td valign="top">Requisition</td>
<td valign="top">WorkOrderCompletion</td>
</tr>
<tr>
<td valign="top">CreditMemo</td>
<td valign="top">InventoryCostRevaluation</td>
<td valign="top">ReturnAuthorization</td>
<td valign="top">WorkOrderIssue</td>
</tr>
<tr>
<td valign="top">Custom</td>
<td valign="top">InventoryTransfer</td>
<td valign="top">SalesOrder</td>
<td valign="top"> </td>
</tr>
<tr>
<td valign="top">CustomerDeposit</td>
<td valign="top">Invoice</td>
<td valign="top">TransferOrder</td>
<td valign="top"> </td>
</tr>
</tbody>
</table>

---
