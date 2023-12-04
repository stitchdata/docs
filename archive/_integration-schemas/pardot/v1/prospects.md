---
tap: "pardot"
version: "1"
key: "prospect"

name: "prospects"
doc-link: "http://developer.pardot.com/kb/object-field-references/#prospect"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/prospects.json"
description: |
  The `{{ table.name }}` table contains info about the prospects in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Query prospects"
  doc-link: "http://developer.pardot.com/kb/api-version-3/prospects/#supported-operations_1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The prospect ID."
    foreign-key-id: "prospect-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the prospect was updated."

  - name: "address_one"
    type: "string"
    description: "The first line of the prospect's address."

  - name: "address_two"
    type: "string"
    description: "The second line of the prospect's address."

  - name: "annual_revenue"
    type: "string"
    description: "The prospect's annual revenue."

  - name: "campaign_id"
    type: "integer"
    description: "The ID of the campaign associated with the prospect."
    foreign-key-id: "campaign-id"

  - name: "city"
    type: "string"
    description: "The city of the prospect's address."

  - name: "comments"
    type: "string"
    description: "Comments about the prospect."

  - name: "company"
    type: "string"
    description: "The prospect's company."

  - name: "country"
    type: "string"
    description: "The country of the prospect's address."

  - name: "created_at"
    type: "date-time"
    description: "The time the prospect was created."

  - name: "crm_account_fid"
    type: "string"
    description: "The prospect's account ID in a supported CRM system."

  - name: "crm_contact_fid"
    type: "string"
    description: "The prospect's contact ID in a supported CRM system."

  - name: "crm_last_sync"
    type: "date-time"
    description: "The last time the prospect was synced with a supported CRM system."

  - name: "crm_lead_fid"
    type: "string"
    description: "The prospect's lead ID in a supported CRM system."

  - name: "crm_owner_fid"
    type: "string"
    description: "The prospect's owner ID in a supported CRM system."

  - name: "crm_url"
    type: "string"
    description: "The URL to view the prospect within the CRM system."

  - name: "department"
    type: "string"
    description: "The department of the prospect."

  - name: "email"
    type: "string"
    description: "The prospect's email address."

  - name: "employees"
    type: "string"
    description: "The prospect's number of employees."

  - name: "fax"
    type: "string"
    description: "The prospect's fax number."

  - name: "first_name"
    type: "string"
    description: "The first name of the prospect."

  - name: "grade"
    type: "string"
    description: "The prospect's letter grade."

  - name: "industry"
    type: "string"
    description: "The prospect's industry."

  - name: "is_do_not_call"
    type: "boolean"
    description: "If `1`, the prospect prefers to not be called."

  - name: "is_do_not_email"
    type: "boolean"
    description: "If `1`, the prospect prefers to not be emailed."

  - name: "is_reviewed"
    type: "boolean"
    description: "If `1`, the prospect has been reviewed."

  - name: "is_starred"
    type: "boolean"
    description: "If `1`, the prospect has been starred."

  - name: "job_title"
    type: "string"
    description: "The prospect's job title."

  - name: "last_activity_at"
    type: "date-time"
    description: "The time of the prospect's last activity."

  - name: "last_name"
    type: "string"
    description: "The prospect's last name."

  - name: "notes"
    type: "string"
    description: "Notes about the prospect."

  - name: "opted_out"
    type: "boolean"
    description: "If `1`, the prospect has opted out of marketing communications."

  - name: "password"
    type: "string"
    description: "The prospect's password."

  - name: "phone"
    type: "string"
    description: "The prospect's phone number."

  - name: "prospect_account_id"
    type: "integer"
    description: "The prospect's account ID."

  - name: "recent_interaction"
    type: "string"
    description: "The prospect's most recent interaction with {{ integration.display_name }}."

  - name: "salutation"
    type: "string"
    description: "The prospect's salutation."

  - name: "score"
    type: "integer"
    description: "The prospect's score."

  - name: "source"
    type: "string"
    description: "The source of the prospect."

  - name: "state"
    type: "string"
    description: "The US state of the prospect's address."

  - name: "territory"
    type: "string"
    description: "The territory of the prospect's address."

  - name: "website"
    type: "string"
    description: "The prospect's website."

  - name: "years_in_business"
    type: "string"
    description: "The prospect's number of years in business."

  - name: "zip"
    type: "string"
    description: "The prospect's postal code."
---