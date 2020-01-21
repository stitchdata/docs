---
tap-reference: "salesforce"

version: "1"

foreign-keys:
  - id: "account-id"
    attribute: "accountId"
    table: "account"
    all-foreign-keys:
      - table: "account"
        join-on: "id"
      - table: "contact"
      - table: "lead"
        join-on: "convertedAccountId"
      - table: "opportunity"
      - table: "user"

  - id: "contact-id"
    attribute: "contactId"
    table: "contact"
    all-foreign-keys:
      - table: "contact"
        join-on: "id"
      - table: "lead"
        join-on: "convertedContactId"
      - table: "user"

  - id: "lead-id"
    attribute: "leadId"
    table: "lead"
    all-foreign-keys:
      - table: "lead"
        join-on: "id"

  - id: "opportunity-id"
    attribute: "opportunityId"
    table: "opportunity"
    all-foreign-keys:
      - table: "lead"
        join-on: "convertedOpportunityId"
      - table: "opportunity"
        join-on: "id"

  - id: "user-id"
    attribute: "ownerId"
    table: "user"
    all-foreign-keys:
      - table: "account"
      - table: "contact"
      - table: "lead"
      - table: "opportunity"
      - table: "user"
        join-on: "id"
      - table: "user"
        join-on: "delegatedApproverId"
      - table: "user"
        join-on: "managerId"

  - id: "user-role-id"
    attribute: "userRoleId"
    table: "users"
    all-foreign-keys:
      - table: "user"
--- 