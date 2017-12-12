---
title: MailChimp
permalink: /integrations/saas/mailchimp
tags: [saas_integrations]
keywords: mailchimp, integration, schema, etl mailchimp, mailchimp etl, mailchimp schema
summary: "Connection instructions, replication info, and schema details for Stitch's MailChimp integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mailchimp"
display_name: "MailChimp"
singer: false
author: "Stitch"
status: "Closed Beta"
historical: "1 year"
frequency: "24 hours"
tier: "Free"
status-url: "https://status.mailchimp.com/"
icon: /images/integrations/icons/mailchimp.svg
whitelist:
  tables: "No"
  columns: "No"

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## MailChimp's API doesn't allow us to query by a date,
## so as of now all tables replicate fully.
## Additionally, much of MailChimp's data is heavily nested.

## Details are in the Replication section, below.

replication-notes: true

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Campaigns
  - name: "mailchimp_campaigns"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/
    description: "info about the campaign settings and content in your account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Campaign ID (<code>id</code>)
      - name: archive_url
      - name: content_type
      - name: create_time
      - name: delivery_status__enabled
      - name: emails_sent
      - name: links <code>*</code>
      - name: long_archive_url
      - name: recipients__list_id
      - name: recipients__list_name
      - name: recipients__recipient_count
      - name: recipients__segment_text
      - name: report_summary__click_rate
      - name: report_summary__clicks
      - name: report_summary__ecommerce__total_orders
      - name: report_summary__ecommerce__total_revenue
      - name: report_summary__ecommerce__total_spent
      - name: report_summary__open_rate
      - name: report_summary__opens
      - name: report_summary__subscriber_clicks
      - name: report_summary__unique_opens
      - name: send_time
      - name: settings__authenticate
      - name: settings__auto_footer
      - name: settings__auto_tweet
      - name: settings__drag_and_drop
      - name: settings__fb_comments
      - name: settings__from_name
      - name: settings__inline_css
      - name: settings__reply_to
      - name: settings__subject_line
      - name: settings__template_id
      - name: settings__timewarp
      - name: settings__title
      - name: settings__to_name
      - name: settings__use_conversation
      - name: status
      - name: tracking__clicktale
      - name: tracking__ecomm360
      - name: tracking__goal_tracking
      - name: tracking__google_analytics
      - name: tracking__html_clicks
      - name: tracking__opens
      - name: tracking__text_clicks
      - name: type

## Email Activity
  - name: "mailchimp_email_activity"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/reports/email-activity/
    description: "info about member activity for a specific campaign."
    notes: |
      ### Email Activity & Row Counts
      This table (and its subtables, if the above applies) can contain large numbers of rows due to how MailChimp creates records for email activities. A single email address can have many actions associated with a single campaign, each of which can be its own row.
    replication-method: "Full Table"
    primary-key: "campaign_id:email_id"
    nested-structures: true
    attributes:
      - name: campaign_id
      - name: email_id
      - name: email_address
      - name: list_id
      - name: links<code>*</code>
      - name: activity<code>*</code>

## Lists
  - name: "mailchimp_lists"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/#create-post_lists
    description: "info about the subscriber lists in your MailChimp account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: List ID (<code>id</code>)
      - name: beamer_address
      - name: campaign_defaults__from_email
      - name: campaign_defaults__from_name
      - name: campaign_defaults__language
      - name: campaign_defaults__subject
      - name: contact__address1
      - name: contact__address2
      - name: contact__city
      - name: contact__company
      - name: contact__country
      - name: contact__phone
      - name: contact__state
      - name: contact__zip
      - name: date_created
      - name: email_type_option
      - name: links<code>*</code>
      - name: list_rating
      - name: name
      - name: notify_on_subscribe
      - name: notify_on_unsubscribe
      - name: permission_reminder
      - name: stats__avg_sub_rate
      - name: stats__avg_unsub_rate
      - name: stats__campaign_count
      - name: stats__campaign_last_sent
      - name: stats__cleaned_count
      - name: stats__cleaned_count_since_send
      - name: stats__click_rate
      - name: stats__last_sub_date
      - name: stats__last_unsub_date
      - name: stats__member_count
      - name: stats__member_count_since_send
      - name: stats__merge_field_count
      - name: stats__open_rate
      - name: stats__target_sub_rate
      - name: stats__unsubscribe_count
      - name: stats__unsubscribe_count_since_send
      - name: subscribe_url_long
      - name: subscribe_url_short
      - name: use_archive_bar
      - name: visibility

## Members
  - name: "mailchimp_members"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/
    description: "info about the members of your MailChimp campaigns."
    notes: 
    replication-method: "Full Table"
    primary-key: "member_id:list_id"
    nested-structures: true
    attributes:
      - name: member_id
      - name: list_id
      - name: email_address
      - name: email_client
      - name: email_type
      - name: ip_opt
      - name: ip_signup
      - name: language
      - name: last_changed
      - name: links<code>*</code>
      - name: list_id
      - name: location__country_code
      - name: location__dstoff
      - name: location__gmtoff
      - name: location__latitude
      - name: location__longitude
      - name: location__timezone
      - name: member_rating
      - name: merge_fields__fname
      - name: merge_fields__lname
      - name: merge_fields__mmerge3
      - name: stats__avg_click_rate
      - name: stats__avg_open_rate
      - name: status
      - name: timestamp_opt
      - name: unique_email_id
      - name: vip

## Sent To
  - name: "mailchimp_sent_to"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/reports/sent-to/#read-get_reports_campaign_id_sent_to
    description: "info about campaign recipients."
    notes: 
    replication-method: "Full Table"
    primary-key: "campaign_id:email_id"
    nested-structures: true
    attributes:
      - name: campaign_id
      - name: email_id
      - name: absplit_group
      - name: email_address
      - name: gmt_offset
      - name: last_open
      - name: links<code>*</code>
      - name: merge_fields__fname
      - name: merge_fields__lname
      - name: merge_fields__mmerge3
      - name: open_count
      - name: status
      - name: vip

## Unsubscribes
  - name: "mailchimp_unsubscribes"
    doc-link: http://developer.mailchimp.com/documentation/mailchimp/reference/reports/unsubscribed/#read-get_reports_campaign_id_unsubscribed
    description: "info about those who have unsubscribed from your email campaigns."
    notes: 
    replication-method: "Full Table"
    primary-key: "campaign_id:email_id"
    nested-structures: true
    attributes:
      - name: campaign_id
      - name: email_id
      - name: absplit_group
      - name: email_address
      - name: gmt_offset
      - name: last_open
      - name: links<code>*</code>
      - name: merge_fields__fname
      - name: merge_fields__lname
      - name: merge_fields__mmerge3
      - name: open_count
      - name: reason
      - name: status
      - name: timestamp
      - name: vip

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your MailChimp data to Stitch is a four-step process:

1. [Add MailChimp as a Stitch data source](#add-stitch-data-source)
2. [Define the Historical Sync](#define-historical-sync)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorize Stitch to access MailChimp](#authorize-stitch)

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorizing Stitch to Access MailChimp {#authorize-stitch}

Lastly, you'll be directed to MailChimp's website to complete the setup.

1. Enter the credentials of the MailChimp account you want to connect to Stitch.
2. Click **Login**.
3. After the authorization process successfully completes, you'll be redirected back to Stitch.
4. Click {{ app.buttons.finish-int-setup }}.


{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}

{% contentfor replication-notes %}
Because the MailChimp endpoints included in our integration don't currently allow querying by a date, **all tables use Full Table Replication**. 

The majority of tables also contain nested structures. If you're using a data warehouse that doesn't natively support nested structures, Stitch will de-nest these rows and create subtables, leading to a higher number of replicated rows than what's in MailChimp.

### Email Activity Record Creation
The [`mailchimp_email_activity`](#mailchimp_email_activity) table and its subtables can contain large numbers of rows due to how MailChimp creates records for email activities. A single email address can have many actions associated with a single campaign, each of which can be its own row.
{% endcontentfor %}