---
title: Pipedrive (v05-10-2016)
permalink: /integrations/saas/pipedrive/v05-10-2016
keywords: pipedrive, integration, schema, etl pipedrive, pipedrive etl, pipedrive schema
summary: "Connection instructions and schema details for Stitch's Pipedrive integration."
layout: singer
input: false
old-schema-template: true

key: "pipedrive-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "pipedrive"
display_name: "Pipedrive"

singer: false
status-url: "http://status.pipedrive.com/"

this-version: "05-10-2016"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"

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
## Activities
  - name: "activities"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the activities (calls, tasks, lunches, etc.) in your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Activity ID (<code>id</code>)
      - name: active_flag
      - name: add_time
      - name: assigned_to_user_id
      - name: company_id
      - name: created_by_user_id
      - name: deal_dropbox_bcc
      - name: deal_id
      - name: deal_title
      - name: done
      - name: due_date
      - name: due_time
      - name: duration
      - name: marked_as_done_time
      - name: note
      - name: org_id
      - name: org_id
      - name: owner_name
      - name: person_dropbox_bcc
      - name: person_id
      - name: person_name
      - name: reference_type
      - name: subject
      - name: type
      - name: update_time
      - name: user_id

## Activity Types
  - name: "activity_types"
    doc-link: https://developers.pipedrive.com/v1#methods-ActivityTypes
    description: "info about the various activity types in your Pipedrive account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Activity Type ID (<code>id</code>)
      - name: active_flag
      - name: add_time
      - name: icon_key
      - name: is_custom_flag
      - name: key_string
      - name: name
      - name: order_nr

## Currencies
  - name: "currencies"
    doc-link: https://developers.pipedrive.com/v1#methods-Currencies
    description: "info about the currencies listed in your Pipedrive account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Currency ID (<code>id</code>)
      - name: active_flag
      - name: code
      - name: decimal_points
      - name: is_custom_flag
      - name: name
      - name: symbol

## Deals
  - name: "deals"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the deals in your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Deal ID (<code>id</code>)
      - name: active
      - name: activites_count
      - name: add_time
      - name: cc_email
      - name: creator_user_id
      - name: currency
      - name: deleted
      - name: done_activities_count
      - name: expected_close_date
      - name: followers_count
      - name: formatted_value
      - name: formatted_weighted_value
      - name: last_activity_date
      - name: last_activity_id
      - name: next_activity_date
      - name: next_activity_duration
      - name: next_activity_id
      - name: next_activity_note
      - name: next_activity_subject
      - name: next_activity_time
      - name: next_activity_type
      - name: notes_count
      - name: org_hidden
      - name: org_id
      - name: org_name
      - name: owner_name
      - name: participants_count
      - name: person_hidden
      - name: person_id
      - name: person_name
      - name: pipeline_id
      - name: reference_activites_count
      - name: rotten_time
      - name: stage_id
      - name: stage_order_nr
      - name: status
      - name: title
      - name: undone_activites_count
      - name: update_time
      - name: user_id
      - name: value
      - name: visible_to
      - name: weighted_value

## Email Messages
  - name: "email_messages"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the email messages sent and received through your Pipedrive account. <strong>Your Pipedrive account must have the Mailbox feature enabled to replicate this data.</strong>"
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Email Message ID (<code>id</code>)
      - name: company_id
      - name: user_id
      - name: message_id
      - name: external_message_id
      - name: thread_id
      - name: mailbox
      - name: subject
      - name: summary
      - name: active
      - name: read
      - name: replied
      - name: sent
      - name: draft
      - name: has_body
      - name: include_body
      - name: read_time
      - name: language_code
      - name: reply_to_message_id
      - name: messages_to<code>*</code>
      - name: messages_from<code>*</code>
      - name: sent_error
      - name: attachment_count
      - name: draft_parameters
      - name: person_id
      - name: org_id
      - name: message_time
      - name: update_time
      - name: add_time

## Email Threads
  - name: "email_threads"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the email threads in your Pipedrive account. Individual emails are organized into threads."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Email Thread (<code>id</code>)
      - name: company_id
      - name: user_id
      - name: deal_id
      - name: first_message_subject
      - name: last_message_subject
      - name: total_messages
      - name: unread_messages
      - name: last_message_summary
      - name: first_message_time
      - name: last_message_time
      - name: replied
      - name: shared
      - name: last_message_attachment
      - name: last_message_cc
      - name: last_message_bcc
      - name: active
      - name: attachment
      - name: draft_messages
      - name: org_id
      - name: add_time
      - name: update_time
      - name: last_message_from<code>*</code>
      - name: last_message_to<code>*</code>
      - name: labels<code>*</code>

## Files
  - name: "files"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the files in your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: File ID (<code>id</code>)
      - name: name
      - name: type
      - name: active
      - name: inline
      - name: remote_location
      - name: remote_id
      - name: cid
      - name: s3_bucket
      - name: deal_name
      - name: person_name
      - name: org_name
      - name: product_name
      - name: url
      - name: description
      - name: add_time
      - name: update_time
      - name: user_id
      - name: person_id
      - name: org_id
      - name: product_id
      - name: email_message
      - name: activity
      - name: mail_message

## Filters
  - name: "filters"
    doc-link: https://developers.pipedrive.com/v1#methods-Filters
    description: "info about the filters that can be applied to Deals, Persons, Organizations, Products, and Activities in your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Filter ID (<code>id</code>)
      - name: active_flag
      - name: add_time
      - name: name
      - name: type
      - name: update_time
      - name: user_id
      - name: visible_to

## Notes
  - name: "notes"
    doc-link: https://developers.pipedrive.com/v1#methods-Recent
    description: "info about notes associated with deals."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Note ID (<code>id</code>)
      - name: active_flag
      - name: add_time
      - name: content
      - name: deal__title
      - name: deal_id
      - name: org_id
      - name: organization_name
      - name: pinned_to_deal_flag
      - name: pinned_to_organization_flag
      - name: pinned_to_person_flag
      - name: update_time
      - name: user__email
      - name: user__is_you
      - name: user__name
      - name: user_id

## Organizations
  - name: "organizations"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the organizations - or the companies you’re doing deals with - in your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Organization ID (<code>id</code>)
      - name: active_flag
      - name: activities_count
      - name: add_time
      - name: address
      - name: address_admin_area_level_1
      - name: address_admin_area_level_2
      - name: address_country
      - name: address_formatted_address
      - name: address_locality
      - name: address_postal_code
      - name: address_route
      - name: address_street_number
      - name: address_sublocality
      - name: address_subpremise
      - name: cc_email
      - name: company_id
      - name: done_activities_count
      - name: email_messages_count
      - name: first_char
      - name: followers_count
      - name: last_activity_date
      - name: last_activity_id
      - name: lost_deals_count
      - name: name
      - name: next_activity_date
      - name: next_activity_id
      - name: next_activity_time
      - name: notes_count
      - name: open_deals_count
      - name: owner_id
      - name: people_count
      - name: reference_activites_count
      - name: undone_activities_count
      - name: update_time
      - name: visible_to
      - name: won_deals_count

## Persons
  - name: "persons"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the ‘persons’ in your Pipedrive account. These are the customers you’re doing deals with."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Person ID (<code>id</code>)
      - name: active_flag
      - name: activities_count
      - name: add_time
      - name: cc_email
      - name: company_id
      - name: done_activities_count
      - name: email<code>*</code>
      - name: email_messages_count
      - name: first_char
      - name: followers_count
      - name: last_activity_date
      - name: last_activity_id
      - name: last_incoming_mail_time
      - name: last_name
      - name: lost_deals_count
      - name: name
      - name: next_activity_date
      - name: next_activity_id
      - name: next_activity_time
      - name: notes_count
      - name: open_deals_count
      - name: org_id
      - name: org_name
      - name: owner_id
      - name: participant_closed_deals_count
      - name: participant_open_deals_count
      - name: phone<code>*</code>
      - name: reference_activities_count
      - name: undone_activities_count
      - name: update_time
      - name: visible_to
      - name: won_deals_count

## Pipelines
  - name: "pipelines"
    doc-link: https://developers.pipedrive.com/v1#methods-Pipelines
    description: "info about the pipelines in your account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Pipeline ID (<code>id</code>)
      - name: active
      - name: add_time
      - name: name
      - name: order_nr
      - name: selected
      - name: url_title

## Products
  - name: "products"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "info about the products in your account. <strong>Products must be enabled in your account, or there’ll be no data for Stitch to replicate.</strong>"
    notes: |
      A set of the `prices__[currency]__[attribute]` columns will be created for every currency enabled in your account.

      If USD, for example:

      - `prices__usd__cost`
      -` prices__usd__currency`
      - `prices__usd__id`
      - `prices__usd__overhead_cost`
      - `prices__usd__price`
      - `prices__usd__product_id`

    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Product ID (<code>id</code>)
      - name: active
      - name: add_time
      - name: code
      - name: first_char
      - name: followers_count
      - name: name
      - name: owner_id
      - name: "prices__[currency]__cost"
      - name: "prices__[currency]__currency"
      - name: "prices__[currency]__id"
      - name: "prices__[currency]__overhead_cost"
      - name: "prices__[currency]__price"
      - name: "prices__[currency]__product_id"
      - name: selectable
      - name: tax
      - name: update_time
      - name: visible_to

## Stages
  - name: "stages"
    doc-link: https://developers.pipedrive.com/v1#methods-Stages
    description: "info about the stages in each of your pipelines."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Stage ID (<code>id</code>)
      - name: active_flag
      - name: add_time
      - name: deal_probability
      - name: name
      - name: order_nr
      - name: pipeline_id
      - name: pipeline_name
      - name: rotten_days
      - name: rotten_flag
      - name: update_time

## Users
  - name: "users"
    doc-link: https://developers.pipedrive.com/v1#methods-Recents
    description: "information about the internal users of your Pipedrive account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: User ID (<code>id</code>)
      - name: activated
      - name: active_flag
      - name: created
      - name: default_currency
      - name: email
      - name: is_admin
      - name: is_you
      - name: lang
      - name: last_login
      - name: locale
      - name: modified
      - name: name
      - name: phone
      - name: role_id
      - name: timezone_name


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Create a Stitch {{ integration.display_name }} user"
    anchor: "create-stitch-pipedrive-user"
    content: |
      To ensure Stitch can access and replicate all your data, the {{ integration.display_name }} credentials you use to connect to Stitch need **Admin permissions**. We recommend that you [create a separate {{ integration.display_name }} Admin user for Stitch](http://support.pipedrive.com/hc/en-us/articles/207319685-How-to-add-edit-remove-a-user){:target="new"}, but this isn’t mandatory to use the integration. Creating a user for us simply makes our activity easier to distinguish in logs and audits.

      If you don’t want to create a user for us, ensure that the credentials you use to connect to Stitch have Admin permissions. If the API token associated with a non-Admin user is used to set up the integration, Stitch may be unable to access and replicate all of your data.

      **Note**: Users in {{ integration.display_name }} are counted at the account level, not the company level. If you want to create a user for us and are concerned about the cost of your {{ integration.display_name }} subscription, don’t worry - you won’t be charged twice.

      {% capture multiple-companies %}
      If you want to connect more than one {{ integration.display_name }} company to Stitch, you’ll have to repeat the entire process in this guide for **each** company you want to add. Essentially, you’ll have to create a separate {{ integration.display_name }} integration for each company.

      Our {{ integration.display_name }} integration uses an API Token to authenticate. **{{ integration.display_name }} API tokens are unique not only at the user level, but the company level as well**. This means that a user’s API Token will vary from company to company, even if everything is housed in the same {{ integration.display_name }} account.
      {% endcapture %}

      {% include note.html first-line="**Connect multiple Pipedrive companies**" content=multiple-companies %}
  
  - title: "Retrieve your {{ integration.display_name }} API token"    
    anchor: "retrieve-api-token"
    content: |
      1. If you created a {{ integration.display_name }} user for Stitch, sign into {{ integration.display_name }} as the Stitch user.

         If you didn’t, sign into {{ integration.display_name }} as an Admin user.
      2. Click the **user menu** (where your avatar is) in the top right corner of the screen.
      3. Click **Settings**.
      4. In the settings menu, click **API**.
      5. The user’s API Token will display.

      Leave this page open for now - you'll need it to complete the setup in Stitch.
  
  - title: "add integration"
    content: |
      4. Paste the {{ integration.display_name }} API Token into the **API Token** field.
  
  - title: "historical sync"
  - title: "replication frequency"


# -------------------------- #
#       Schema Details       #
# -------------------------- #

schema-sections:
  - content: |
      Want to check out what your data looks like in {{ integration.display_name }}'s API? If you still have your API Token handy, you can enter it on {{ integration.display_name }}'s website to interact directly with the API and see your data in raw JSON format.

      In the **Attributes** section for each table is a link to {{ integration.display_name }}'s documentation for that endpoint. Use those links to interact with {{ integration.display_name }}'s API.
---
{% assign integration = page %}
{% include misc/data-files.html %}