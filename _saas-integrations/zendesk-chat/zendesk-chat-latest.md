---
title: Zendesk Chat (Zopim)
permalink: /integrations/saas/zendesk-chat
keywords: zopim, integration, schema, etl zopim, zopim etl, zopim schema, zendesk chat, zendesk
summary: "Connection instructions and schema details for Stitch's Zendesk Chat integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zendesk-chat"
display_name: "Zendesk Chat"

singer: false
status-url: "https://status.zendesk.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Closed Beta"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"

table-selection: false
column-selection: false

anchor-scheduling: false
cron-scheduling: false

extraction-logs: false
loading-reports: true

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Account
  - name: "zopim_account"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/accounts
    description: "info about your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "account_key"
    nested-structures: false
    attributes:
      - name: Widget Key (<code>account_key</code>)
      - name: create_date
      - name: status
      - name: plan
      - name: billing

## Agents
  - name: "zopim_agents"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/agents
    description: "info about the agents in your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Agent ID (<code>id</code>)
      - name: first_name
      - name: last_name
      - name: display_name
      - name: create_date
      - name: email
      - name: role
      - name: enabled
      - name: departments<code>*</code>

## Banned IPs
  - name: "zopim_banned_ips"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/bans#get-banned-ip-addresses
    description: "info about the IPs banned from your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Banned IP ID (<code>id</code>)
      - name: ip_address
      - name: reason
      - name: type

## Banned Visitors
  - name: "zopim_banned_visitors"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/bans#get-ban
    description: "info about the visitors banned from your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Ban ID (<code>id</code>)
      - name: ip_address
      - name: visitor_id
      - name: visitor_name
      - name: reason
      - name: type

## Chats
  - name: "zopim_chats"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/chats
    description: "info about the chats in your Zopim account."
    notes: |
     ### Chat Types & Null Values
     Depending on the type of chat - support versus offline - some records may have `NULL` values. Offline chats will only have some of the attributes listed below populated.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Chat ID (<code>id</code>)
      - name: visitor
      - name: type
      - name: started_by
      - name: session
      - name: timestamp
      - name: count
      - name: duration
      - name: department_id
      - name: department_name
      - name: response_time
      - name: agent_names<code>*</code>
      - name: agent_ids<code>*</code>
      - name: triggered
      - name: triggered_response
      - name: unread
      - name: missed
      - name: history
      - name: tags<code>*</code>
      - name: rating
      - name: comment
      - name: webpath<code>*</code>
      - name: zendesk_ticket_id

## Departments
  - name: "zopim_departments"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/departments
    description: "info about the departments in your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Department ID (<code>id</code>)
      - name: name
      - name: description
      - name: enabled
      - name: members<code>*</code>
      - name: settings

## Shortcuts
  - name: "zopim_shortcuts"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/shortcuts
    description: "info about the shortcuts in your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "name"
    nested-structures: true
    attributes:
      - name: Shortcut Name (<code>name</code>)
      - name: options
      - name: message
      - name: tags<code>*</code>

## Triggers
  - name: "zopim_triggers"
    doc-link: https://developer.zendesk.com/rest_api/docs/chat/triggers
    description: "info about the triggers in your Zopim account."
    notes: 
    replication-method: "Full Table"
    primary-key: "name"
    nested-structures: false
    attributes:
      - name: Trigger Name (<code>name</code>)
      - name: enabled
      - name: description

---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your {{ integration.display_name }} (formerly known as Zopim) data to Stitch is a four-step process:

1. [Add {{ integration.display_name }} as a Stitch data source](#add-stitch-data-source)
2. [Define the Historical Sync](#define-historical-sync)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorize Stitch to access Zopim](#authorize-stitch)

### Prerequisites {#prerequisites}

1. **Owner permissions in {{ integration.display_name }}**. The user who authorizes the integration must have [Owner permissions in {{ integration.display_name }}](https://chat.zendesk.com/hc/en-us/articles/212679597-Understanding-and-managing-roles-in-Zendesk-Chat){:target="_blank"}. Otherwise, Stitch will encounter authentication issues and be unable to replicate data.

2. **An Advanced or Premium {{ integration.display_name }} account.** Zendesk only allows customers on their Advanced or Paid {{ integration.display_name }} plans to utilize the Rest API, which is what Stitch uses to connect to your {{ integration.display_name }} account and replicate data.

   If your {{ integration.display_name }} account is on Lite or Basic, you will need to upgrade your {{ integration.display_name }} plan. [More info on {{ integration.display_name }} plans can be found on Zendesk's website](https://www.zendesk.com/chat/compare/#compare){:target="_blank"}.  

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorizing Stitch to Access {{ integration.display_name }} {#authorize-stitch}

Lastly, you'll be directed to Zendesk's website to complete the setup.

1. Enter your {{ integration.display_name }} credentials and click **Login**.
2. Complete the authorization process.
4. After the authorization process successfully completes, you'll be redirected back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}