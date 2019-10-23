---
title: Pardot
permalink: /integrations/saas/pardot
keywords: pardot, pardot data, etl pardot, pardot etl, pardot schema
summary: "Connection instructions and schema details for Stitch's Pardot integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

key: "pardot-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "pardot"
display_name: "Pardot"

singer: false
status-url: "http://trust.pardot.com/"

this-version: "15-10-2015"

api: |
  [{{ integration.display_name }} API](http://developer.pardot.com/#official-pardot-api-documentation){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "28 days"
frequency: "30 minutes"
tier: "Standard"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Lists
  - name: "pardotlists"
    doc-link: http://developer.pardot.com/kb/object-field-references/#list
    description: "info about the lists in your Pardot account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: List ID (<code>id</code>)
      - name: name
      - name: is_public
      - name: is_dynamic
      - name: title
      - name: description
      - name: is_crm_visible
      - name: created_at
      - name: updated_at

## List Memberships
  - name: "pardotlistmemberships"
    doc-link: http://developer.pardot.com/kb/object-field-references/#list-membership
    description: "list membership info."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: List Membership ID (<code>id</code>)
      - name: list_id
      - name: prospect_id
      - name: opted_out
      - name: created_at
      - name: updated_at

## Opportunities
  - name: "pardotopportunity"
    doc-link: http://developer.pardot.com/kb/api-version-3/object-field-references/#opportunity
    description: "info about the opportunities in your Pardot account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Opportunity ID (<code>id</code>)
      - name: campaign_id
      - name: name
      - name: value
      - name: probability
      - name: type
      - name: stage
      - name: status
      - name: closed_at
      - name: created_at
      - name: updated_at

## Prospects
  - name: "pardotprospect"
    doc-link: http://developer.pardot.com/kb/object-field-references/#prospect
    description: "info about your prosepcts and the attributes associated with them."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Prospect ID (<code>id</code>)
      - name: campaign_id
      - name: salutation
      - name: first_name
      - name: last_name
      - name: email
      - name: password
      - name: company
      - name: prospect_account_id
      - name: website
      - name: job_title
      - name: department
      - name: country
      - name: address_one
      - name: address_two
      - name: city
      - name: state
      - name: territory
      - name: zip
      - name: phone
      - name: fax
      - name: source
      - name: annual_revenue
      - name: employee
      - name: industry
      - name: years_in_business
      - name: comments
      - name: notes
      - name: score
      - name: grade
      - name: last_activity_at
      - name: recent_interaction
      - name: crm_lead_fid
      - name: crm_contact_fid
      - name: crm_owner_fid
      - name: crm_account_fid
      - name: crm_last_sync
      - name: crm_url
      - name: is_do_not_email
      - name: is_do_not_call
      - name: opted_out
      - name: is_reviewed
      - name: is_starred
      - name: created_at
      - name: updated_at

## Tags
  - name: "pardottags"
    doc-link: http://developer.pardot.com/kb/object-field-references/#tag
    description: "info about the tags in your Pardot account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Tag ID (<code>id</code>)
      - name: name
      - name: created_at
      - name: updated_at

## Tag Objects
  - name: "pardottagobjects"
    doc-link: http://developer.pardot.com/kb/object-field-references/#tag-object
    description: "info about the tag objects in your Pardot account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Tag Object ID (<code>id</code>)
      - name: tag_id
      - name: type
      - name: object_id
      - name: created_at

## Visitors
  - name: "pardotvisitor"
    doc-link: http://developer.pardot.com/kb/object-field-references/#visitor
    description: "info about the visitors who visit your Pardot website."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Visitor ID (<code>id</code>)
      - name: page_view_counts
      - name: ip_address
      - name: hostname
      - name: campaign_parameter
      - name: medium_parameter
      - name: source_parameter
      - name: content_parameter
      - name: term_parameter
      - name: created_at
      - name: updated_at

## Visits
  - name: "pardotvisits"
    doc-link: 
    description: "info about visits made to your Pardot website."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Visit ID (<code>id</code>)
      - name: visitor_id
      - name: prospect_id
      - name: visitor_page_view_count
      - name: first_visitor_page_view_at
      - name: last_visitor_page_view_at
      - name: duration_in_seconds
      - name: campaign_parameter
      - name: medium_parameter
      - name: source_parameter
      - name: content_parameter
      - name: term_parameter
      - name: created_at
      - name: updated_at

## Visitor Activity
  - name: "pardotvisitoractivity"
    doc-link: http://developer.pardot.com/kb/object-field-references/#visitor-activity
    description: "info about the activities user engage - for example: open, custom URL click, video view, and so on - in during visits to your Pardot website."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Visitor Activity ID (<code>id</code>)
      - name: visitor_id
      - name: prospect_id
      - name: type
      - name: type_name
      - name: details
      - name: email_id
      - name: form_id
      - name: form_handler_id
      - name: site_search_query_id
      - name: landing_page_id
      - name: paid_search_id_id
      - name: multivariate_test_variation_id
      - name: visitor_page_view_id
      - name: file_id
      - name: campaign
      - name: created_at
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Pardot data to Stitch is a three-step process:

1. [Retrieve your Pardot API User Key](#retrieve-pardot-api-user-key)
2. [Whitelist Stitch's IP Addresses](#whitelist-stitch-ips)`*`
2. [Add Pardot as a Stitch data source](#add-stitch-data-source)
3. [Define the Replication Frequency](#define-rep-frequency)

`*` This step is necessary only if IP-based security is enabled for your Pardot account.

### Retrieve Your Pardot API User Key {#retrieve-pardot-api-user-key}

1. Sign into your Pardot account.
2. Hover over the **User** menu - it's where your email address is displayed, in the upper right-hand corner of the screen.
3. In the dropdown menu that displays, click the **Settings** option. Your user information will display.
4. Locate the **API User Key** field.

Leave this page open for now - you'll need it to complete the setup in Stitch.

### Whitelist Stitch's IP Addresses {#whitelist-stitch-ips}

{% include note.html type="single-line" content="If your Pardot account doesn't have IP-based security enabled, skip this step." %}

If your Pardot account allows access from certain IP addresses, you'll need to whitelist the Stitch's IP addresses for the connection to be successful.

**Note**: Admin permissions in Pardot are required to add and manage whitelisted IP addresses. [Refer to Pardot's documentation for more info](https://help.salesforce.com/articleView?id=pardot_admin_ip_manage_whitelisted.htm&type=5).

Whitelist all of the following IP addresses in Pardot:

{% for ip-address in ip-addresses %}
- {{ ip-address.ip }}
{% endfor %}

{% include integrations/shared-setup/connection-setup.html %}
4. In the **Pardot User Key** field, paste your API User Key.

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
