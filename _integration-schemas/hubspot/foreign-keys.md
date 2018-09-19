---
tap-reference: "hubspot"

version: "2.0"

foreign-keys:
  - id: "campaign-id"
    attribute: "leadNurturingCampaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "email_events"
        join-on: "emailCampaignId"
      - table: "forms"
        join-on: "leadNurturingCampaignId"

  - id: "contact-id"
    attribute: "canonical-vid"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
      - table: "contacts_by_company"
        join-on: "contact-id"

  - id: "company-id"
    attribute: "company-id"
    table: "companies"
    all-foreign-keys:
      - table: "companies"
        join-on: "companyId"
      - table: "contacts_by_company"
      - table: "deals"
        subtable: "associations__associatedCompanyIds"
        join-on: "value"
      - table: "engagements"
        subtable: "associations__companyIds"
        join-on: "value"

  - id: "contact-list-id"
    attribute: "listId"
    table: "contact_lists"
    all-foreign-keys:
      - table: "contact_lists"
      - table: "contacts"
        subtable: "list-memberships"
        join-on: "internal-list-id"
      - table: "engagements"
        subtable: "associations__contactIds"
        join-on: "value"

  - id: "deal-id"
    attribute: "dealId"
    table: "deals"
    all-foreign-keys:
      - table: "deals"
      - table: "deals"
        subtable: "associations__associatedDealIds"
        join-on: "value"
      - table: "engagements"
        subtable: "associations__dealIds"
        join-on: "value"

  - id: "deal-pipeline-id"
    attribute: "pipelineId"
    table: "deal_pipelines"
    all-foreign-keys:
      - table: "deal_pipelines"

  - id: "email-event-id"
    attribute: "emailEventId"
    table: "email_events"
    all-foreign-keys:
      - table: "email_events"

  - id: "engagement-id"
    attribute: "engagementId"
    table: "engagements"
    all-foreign-keys:
      - table: "engagements"

  - id: "form-id"
    attribute: "form-id"
    table: "forms"
    all-foreign-keys:
      - table: "forms"
      - table: "contacts"
        subtable: "form-submissions"
        join-on: "form-id"

  - id: "owner-id"
    attribute: "ownerId"
    table: "owners"
    all-foreign-keys:
      - table: "engagements"
      - table: "owners"
      - table: "owners"
        subtable: "remoteList"

  - id: "portal-id"
    attribute: "portalId"
    table: ""
    all-foreign-keys:
      - table: "companies"
      - table: "contact_lists"
      - table: "contacts"
        join-on: "portal-id"
      - table: "contacts"
        subtable: "form-submissions"
        join-on: "portal-id"
      - table: "deals"
      - table: "email_events"
      - table: "engagements"
      - table: "forms"
      - table: "owners"
      - table: "owners"
        subtable: "remoteList"
      - table: "subscription_changes"
      - table: "subscription_changes"
        subtable: "changes"
---