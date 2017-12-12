---
title: Desk
permalink: /integrations/saas/desk
tags: [saas_integrations]
keywords: desk, desk data, desk schema, etl desk, desk etl
summary: "Connection instructions and schema details for Stitch's Desk integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "desk"
display_name: "Desk"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://statusgator.com/status/deskcom"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/desk.svg
whitelist:
  tables: false
  columns: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Cases
  - name: "cases"
    doc-link: http://dev.desk.com/API/cases/#fields
    description: "about the support cases in your Desk account."
    notes: "In addition to the fields listed below, our Desk integration will also include any custom fields."
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Case ID (<code>id</code>)
      - name: external_id
      - name: blurb
      - name: subject
      - name: priority
      - name: description
      - name: status
      - name: type
      - name: labels<code>*</code>
      - name: locked_until
      - name: changed_at
      - name: active_at
      - name: language
      - name: suppress_rules
      - name: received_at
      - name: first_opened_at
      - name: last_opened_at
      - name: first_resolved_at
      - name: resolved_at
      - name: created_at
      - name: updated_at

## Customers
  - name: "customers"
    doc-link: http://dev.desk.com/API/customers/#fields
    description: "about the end-users in your Desk account."
    notes: "In addition to the fields listed below, our Desk integration will also include any custom fields."
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Customer ID (<code>id</code>)
      - name: first_name
      - name: last_name
      - name: company
      - name: title
      - name: avatar
      - name: uid
      - name: background
      - name: language
      - name: locked_until
      - name: created_at
      - name: updated_at
      - name: emails<code>*</code>
      - name: phone numbers<code>*</code>
      - name: addresses<code>*</code>
      - name: access_private_portal
      - name: access_company_cases

## Replies
  - name: "replies"
    doc-link: http://dev.desk.com/API/replies/#fields
    description: "the individual replies in cases."
    notes: |
      Depending on the configuration of your Desk account, you may see more fields in this table than what's listed here. For example: Tweet fields. 
    replication-method: "Incremental"
    primary-key: "case_id:reply_id"
    nested-structures: false
    attributes:
      - name: Case ID
      - name: Reply ID
      - name: subject
      - name: body
      - name: direction (in vs. out)
      - name: status
      - name: to
      - name: from
      - name: cc
      - name: bcc
      - name: client_type
      - name: suppress_rules
      - name: sent_by
      - name: sent_at
      - name: created_at
      - name: updated_at

## Users
  - name: "users"
    doc-link: http://dev.desk.com/API/users/#fields
    description: "about the internal users of your Desk account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: User ID (<code>id</code>)
      - name: name
      - name: public_name
      - name: email
      - name: email_verified
      - name: avatar
      - name: level
      - name: current_login_at
      - name: last_login_at
      - name: created_at
      - name: updated_at

## User Groups
  - name: "user_groups"
    doc-link: http://dev.desk.com/API/users/
    description: "the groups your internal users belong to."
    notes: 
    replication-method: "Full Table"
    primary-key: "user_id:id"
    nested-structures: false
    attributes:
      - name: Group ID (<code>id</code>)
      - name: User ID (<code>user_id</code>)
      - name: Group Name
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Desk data to Stitch is a six-step process:

1. [Add Stitch as an app in your Desk account](#add-stitch-app-to-desk)
2. [Retrieve your Desk Key and Secret](#retrieve-desk-key-secret)
3. [Retrieve your Desk Token and Token Secret](#retrieve-desk-token-secret)
4. [Add Desk as a Stitch data source](#add-stitch-data-source)
5. [Define the Historical Sync](#define-historical-sync)
6. [Define the Replication Frequency](#define-rep-frequency)

### Adding Stitch as an App in Your Desk Account {#add-stitch-app-to-desk}

1. Sign into your Desk account.
2. Navigate to the **Admin panel** by clicking the link in the upper left section of the Agent interface.
3. In the Admin panel, click the **Settings** option in the menu at the top of the window. 
4. When the Settings page displays, click the **API** option in the menu that appears on the left side of the window.
5. Click the **+Add API Application** button.
6. After clicking the button, a window will display. This is where the initial parameters for the API application are set. Complete the fields as follows:
  - **Name:** Stitch
  - **Website URL:** http://www.stitchdata.com
  - **Callback URL:** http://www.stitchdata.com
  - **Support URL:** http://docs.stitchdata.com
7. When finished, click the **Add** button.

### Retrieving Your Desk Key & Secret {#retrieve-desk-key-secret}

1. After the URL parameters have been successfully submitted, a screen detailing the parameters, Key, and Secret will display.
2. Copy the **Key and Secret** into a text file - you'll need easy access to them to complete the setup.

### Retrieving Your Desk Token & Token Secret {#retrieve-desk-token-secret}
1. Click the **Your Access Token** link on the right side of the **API Application** page. A window containing your Token and Token Secret will display.
2. Copy the **Token and Token Secret** into the text file that contains your Key and Secret. Be careful not to mix up the Secret and Token Secret or you'll encounter errors when saving the integration in Stitch.

{% include integrations/shared-setup/connection-setup.html %}
4. In the **Site URL** field, enter your Desk.com website address. For example: `https://stitch.desk.com`
5. Enter your **Key, Secret, Token, and Token Secret** into their respective fields.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}