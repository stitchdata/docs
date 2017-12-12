---
title: HubSpot - DEPRECATED VERSION; REPLACED BY SINGER
permalink: /integrations/saas/hubspot
tags: [saas_integrations]
keywords: hubspot, integration, schema, etl hubspot, hubspot etl

name: "HubSpot"
author: "Stitch"
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
status-url: "https://status.hubspot.com/"
icon: /images/integrations/icons/hubspot.svg
whitelist:
  tables: "No"
  columns: "No"

format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

tables:
## Campaigns
  - name: "hubspot_campaigns"
    doc-link: http://developers.hubspot.com/docs/methods/email/get_campaign_data
    description: "the campaigns in your HubSpot account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Campaign ID (<code>id</code>)
      - name: portalid
      - name: name
      - name: numincluded
      - name: numqueued
      - name: subtype
      - name: subject
      - name: type

## Campaign Lists
  - name: "hubspot_campaign_lists"
    doc-link: http://developers.hubspot.com/docs/methods/email/get_campaigns
    description: "campaigns with recent activity."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Campaign List ID (<code>id</code>)
      - name: portalid
      - name: appid
      - name: appname
      - name: lastupdatedtime

## Companies
  - name: "hubspot_companies"
    doc-link: http://developers.hubspot.com/docs/methods/companies/get_company
    description: "companies your contacts belong to."
    notes:
    replication-method: "Incremental"
    primary-key: "companyid"
    nested-structures: true
    attributes:
      - name: Company ID (<code>companyid</code>)
      - name: portalid
      - name: isdeleted
      - name: description
      - name: timestamp
      - name: source
      - name: sourceid
      - name: Version info <code>*</code>
      - name: name
      - name: createddate

## Contacts
  - name: "hubspot_contacts"
    doc-link: http://developers.hubspot.com/docs/methods/contacts/get_contacts
    description: "individual contacts in HubSpot."
    notes: *nested
    replication-method: "Incremental"
    primary-key: "vid"
    nested-structures: true
    attributes:
      - name: Contact ID (<code>vid</code>)
      - name: portalid
      - name: firstname
      - name: lastname
      - name: Identity Profile info<code>*</code>
      - name: profile-id
      - name: profile-token
      - name: profile-url
      - name: canonical-vid
      - name: is-contact
      - name: addedat
      - name: Form Submission info<code>*</code>

## Contact Lists
  - name: "hubspot_contact_lists"
    doc-link: http://developers.hubspot.com/docs/methods/lists/get_lists
    description: "the contact lists in your HubSpot account."
    notes:
    replication-method: "Full Table"
    primary-key: "listid"
    nested-structures: true
    attributes:
      - name: Contact List ID(<code>listid</code>)
      - name: authorid
      - name: createdat
      - name: deleteable
      - name: dynamic
      - name: internallistid
      - name: listid
      - name: listtype
      - name: metadata__error
      - name: metadata__lastprocessingstatechangeat
      - name: metadata__lastsizechangeat
      - name: metadata__processing
      - name: metadata__size
      - name: name
      - name: portalid
      - name: Filter info
      - name: updatedat

## Deals
  - name: "hubspot_deals"
    doc-link: http://developers.hubspot.com/docs/methods/deals/get_deals_modified
    description: "all the deals in a HubSpot portal."
    notes:
    replication-method: "Full Table"
    primary-key: "dealid"
    nested-structures: false
    attributes:
      - name: Deal ID (<code>dealid</code>)
      - name: portalid
      - name: dealname
      - name: associatedcompanyids
      - name: associateddealids
      - name: email_address
      - name: hs_lastmodifieddate
      - name: num_associated_contacts
      - name: dealstage
      - name: hs_createdate
      - name: createdate
      - name: source
      - name: contact_number
      - name: imports

## Email Events
  - name: "hubspot_email_events"
    doc-link: http://developers.hubspot.com/docs/methods/email/get_events
    description: "email events and how recipients interact with content."
    notes:
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes: 
      - name: Email Event ID (<code>id</code>)
      - name: appid
      - name: created
      - name: emailcampaignid
      - name: hmid
      - name: portalid
      - name: portalsubscriptionstatus
      - name: recipient
      - name: type
      - name: unsubscribefromany

## Forms
  - name: "hubspot_forms"
    doc-link: http://developers.hubspot.com/docs/methods/forms/v2/get_forms
    description: "your HubSpot website forms."
    notes:
    replication-method: "Incremental"
    primary-key: "guid"
    nested-structures: true
    attributes: 
      - name: Form ID (<code>guid</code>)
      - name: action
      - name: campaignguid
      - name: captchaenabled
      - name: cloneable
      - name: createdat
      - name: cssclass
      - name: deletable
      - name: editable
      - name: followupid
      - name: "Form Field Groups: Groups, Fields, Options, Selected Options<code>*</code>"
      - name: formtype
      - name: ignorecurrentvalues
      - name: inlinemessage
      - name: leadnurturingcampaignid
      - name: method
      - name: migratedfrom
      - name: name
      - name: notifyrecipients
      - name: performablehtml
      - name: portalid
      - name: redirect
      - name: socialloginenabled
      - name: Social Login Types<code>*</code>
      - name: submittext
      - name: tmsid
      - name: updatedat
      - name: visible

## Keywords
  - name: "hubspot_keywords"
    doc-link: http://developers.hubspot.com/docs/methods/keywords/get_keywords
    description: "your HubSpot portal keywords."
    notes:
    replication-method: "Incremental"
    primary-key: "keyword_guid"
    nested-structures: false
    attributes:
      - name: Keyword ID (<code>keyword_guid</code>)
      - name: contacts
      - name: country
      - name: created_at
      - name: keyword
      - name: leads

## Owners
  - name: "hubspot_owners"
    doc-link: http://developers.hubspot.com/docs/methods/owners/get_owners
    description: "the owners that exist in your HubSpot portal."
    notes:
    replication-method: "Incremental"
    primary-key: "ownerid"
    nested-structures: true
    attributes:
      - name: Owner ID (<code>ownerid</code>)
      - name: createdat
      - name: email
      - name: firstname
      - name: lastname
      - name: portalid
      - name: type
      - name: updatedat

## Subscription Changes
  - name: "hubspot_subscription_changes"
    doc-link: http://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline
    description: "changes made to subscriptions."
    notes:
    replication-method: "Incremental"
    primary-key: "recipient:timestamp"
    nested-structures: true
    attributes:
      - name: portalid
      - name: recipient
      - name: timestamp
      - name: Change Event info<code>*</code>

## Workflows
  - name: "hubspot_workflows"
    doc-link: http://developers.hubspot.com/docs/methods/workflows/v3/get_workflows
    description: "the workflows in your HubSpot portal."
    notes:
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Workflow ID (<code>id</code>)
      - name: contactlisids__active
      - name: contactlistids__enrolled
      - name: enabled
      - name: insertedat
      - name: name
      - name: originalauthoruserid
      - name: type
      - name: updatedat
---

{% contentfor setup %}
Connecting your HubSpot data to Stitch is a four-step process:

1. [Locate your HubSpot portal ID](#locate-hubspot-portal-id)
2. [Add HubSpot as a Stitch data source](#add-stitch-data-source)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorize Stitch to access HubSpot](#grant-stitch-authorization)

### Prerequisites
**You'll need Admin permissions to complete the setup.** This will ensure that Stitch is able to access and replicate all the data in your HubSpot account.

### Locating Your HubSpot Portal ID {#locate-hubspot-portal-id}
A portal ID is a unique identifier HubSpot uses to differentiate accounts, or ‘portals.’ You can find your ID by looking in the top-right corner when you're signed into your HubSpot account:

![Locating your HubSpot portal ID.]({{ site.baseurl }}/images/integrations/hubspot-portal-id.png)

After you've located your portal ID, you can move onto connecting HubSpot to Stitch.

{% include custom/integrations/setup/connection-setup.html %}
4. In the **HubSpot Portal ID** field, enter the portal ID of the account you want to connect to Stitch.

{% include custom/integrations/setup/replication-frequency.html %}

### Authorizing Stitch to Access HubSpot {#grant-stitch-authorization}

1. Next, you'll be prompted to sign into your HubSpot account if you aren't already.
2. A screen asking for authorization to HubSpot will display after you sign in. **Note that we will only ever read your data**. Stitch will never modify or delete any data in your HubSpot account. 
3. Click **Authorize.**
4. After the authorization process is successfully completed, you'll be directed back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.
{% endcontentfor %}