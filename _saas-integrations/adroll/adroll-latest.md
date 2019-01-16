---
title: AdRoll
permalink: /integrations/saas/adroll
keywords: adroll, integration, schema, etl adroll, adroll etl, adroll schema, ad roll
tags: [saas_integrations]
summary: "Connection instructions and schema details for Stitch's AdRoll integration."
format: 
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "adroll"
display_name: "AdRoll"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://status.adroll.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
historical: "1 year"
tier: "Free"
icon: /images/integrations/icons/adroll.svg

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Ad Groups
  - name: "adroll_ad_groups"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_adgroups
    description: "info about the adgroups contained within the campaigns of your AdRoll account."
    notes: 
    replication-method: "Full Table"
    primary-key: "eid"
    nested-structures: true
    attributes:
      - name: Adgroup ID (<code>eid</code>)
      - name: Ad info<code>*</code>
      - name: ad_optimization
      - name: campaign
      - name: created_date
      - name: flight_timezone
      - name: name
      - name: Segment info<code>*</code>
      - name: space_optimization
      - name: status
      - name: type
      - name: updated_date

## Ad Reports
  - name: "adroll_ad_reports"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-report-ad
    description: "ad-level reporting data."
    notes: "Each row in this table contains totals for the ad, by date."
    replication-method: "Key-based Incremental"
    primary-key: "eid"
    nested-structures: false
    attributes:
      - name: Ad ID (<code>eid</code>)
      - name: ad
      - name: ad_size
      - name: adjusted_click_through_ratio
      - name: adjusted_cpa
      - name: adjusted_cpa_usd
      - name: adjusted_ctc
      - name: adjusted_total_conversion_rate
      - name: adjusted_total_conversions
      - name: adjusted_view_through_ratio
      - name: adjusted_vtc
      - name: advertiser
      - name: click_cpa
      - name: click_cpa_usd
      - name: click_through_conversions
      - name: click_through_ratio
      - name: clicks
      - name: cost
      - name: cost_usd
      - name: cpa
      - name: cpa_usd
      - name: cpc
      - name: cpc_usd
      - name: cpm
      - name: cpm_usd
      - name: created_date
      - name: ctr
      - name: date
      - name: height
      - name: impressions
      - name: paid_impressions
      - name: prospects
      - name: status
      - name: total_conversion_rate
      - name: total_conversions
      - name: type
      - name: view_through_conversions
      - name: view_through_ratio
      - name: width

## Ads
  - name: "adroll_ads"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_ads
    description: "about the ads, or creatives, associated with the advertisables in your account."
    notes: 
    replication-method: "Full Table"
    primary-key: "eid"
    nested-structures: true
    attributes:
      - name: Ad ID (<code>eid</code>)
      - name: ad_format
      - name: ad_format_id
      - name: ad_format_name
      - name: Ad Group info<code>*</code>
      - name: advertisable
      - name: call_to_action
      - name: created_date
      - name: destination_url
      - name: has_edits
      - name: has_future_campaigns
      - name: has_pending_edits
      - name: height
      - name: inventory_type
      - name: is_active
      - name: is_fb_dynamic
      - name: is_outlined
      - name: name
      - name: original_ad
      - name: outline_color
      - name: src
      - name: status
      - name: type
      - name: updated_date
      - name: valid_clicktag
      - name: width

## Advertisables
  - name: "adroll_advertisables"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get
    description: "about the advertisables (typically the parent object for a brand) in your AdRoll account."
    notes: 
    replication-method: "Full Table"
    primary-key: "eid"
    nested-structures: false
    attributes:
      - name: Advertisable ID (<code>id</code>)
      - name: is_active
      - name: name
      - name: organization
      - name: status
      - name: url
      - name: product_name
      - name: click_through_conversion_window
      - name: view_through_conversion_window
      - name: created_date
      - name: updated_date
      - name: attached_users<code>*</code>
      - name: blacklisted_sites
      - name: enable_customer_multi_dur_segs
      - name: is_coop_approved
      - name: is_publisher
      - name: cm_networks
      - name: iab1_category_id
      - name: iab1_category_name
      - name: iab2_category_id
      - name: iab2_category_iname
      - name: zvelo_category_id
      - name: zvelo_category_name
      - name: approval_state
      - name: has_privacy_policy
      - name: ops
      - name: optimizer
      - name: saleser
      - name: liquidads

## Campaigns
  - name: "adroll_campaigns"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_campaigns
    description: "about the advertising campaigns in your account."
    notes: 
    replication-method: "Full Table"
    primary-key: "eid"
    nested-structures: true
    attributes:
      - name: Campaign ID (<code>eid</code>)
      - name: adgroups<code>*</code>
      - name: advertisable
      - name: budget
      - name: ui_budget_daily
      - name: created_date
      - name: cpc
      - name: cpm
      - name: end_date
      - name: is_active
      - name: is_facebook
      - name: is_fbx_newsfeed
      - name: is_retargeting
      - name: is_fb_wca
      - name: is_apple
      - name: max_cpm
      - name: name
      - name: promotion
      - name: pricing_strategies
      - name: start_date
      - name: status
      - name: updated_date
      - name: is_coop
      - name: is_pubgraph
      - name: spend_limit_until
      - name: created_date
      - name: updated_date

## Segments
  - name: "adroll_segments"
    doc-link: https://developers.adroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_segments
    description: "about segments, or the lists of users that visit your site."
    notes: 
    replication-method: "Full Table"
    primary-key: "eid"
    nested-structures: false
    attributes:
      - name: Segment ID (<code>eid</code>)
      - name: display_name
      - name: name
      - name: type
      - name: match_method
      - name: pattern
      - name: threshold
      - name: duration
      - name: conversion_value
      - name: group
      - name: mobile
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your AdRoll data to Stitch is a four-step process:

1. [Create an AdRoll user for Stitch](#create-adroll-user-for-stitch)
2. [Add AdRoll as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)

### Create an AdRoll User for Stitch {#create-adroll-user-for-stitch}

While you can use your own credentials to connect AdRoll to Stitch, we recommend creating a separate user for us. This will make it easier for you to manage users and audit events in your AdRoll account.

**We require a General User role** - which is the default - to be able to replicate your AdRoll data. Note that Stitch does not need billing access. If you need help creating an AdRoll user, you can find instructions here in AdRoll’s support docs.

{% include integrations/shared-setup/connection-setup.html %}
4. Enter the email address and username for the Stitch AdRoll user.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
