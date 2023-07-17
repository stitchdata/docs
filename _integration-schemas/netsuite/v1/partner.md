---
tap: "netsuite"
version: "1"

name: "Partner"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/partner.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Partner.json"
description: |
  The `{{ table.name }}` table contains info about the partners in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "partner"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "partner-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "accessRole"
    type: "varies"
    description: ""

  - name: "addressbookList"
    type: "varies"
    description: ""

  - name: "altEmail"
    type: "string"
    description: ""

  - name: "altName"
    type: "string"
    description: ""

  - name: "bcn"
    type: "string"
    description: ""

  - name: "categoryList"
    type: "varies"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "companyName"
    type: "string"
    description: ""

  - name: "contactRolesList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dateCreated"
    type: "date-time"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "eligibleForCommission"
    type: "boolean, string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailPreference"
    type: "varies"
    description: ""

  - name: "entityId"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "giveAccess"
    type: "boolean, string"
    description: ""

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: ""

  - name: "homePhone"
    type: "string"
    description: ""

  - name: "image"
    type: "varies"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isPerson"
    type: "boolean, string"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "loginAs"
    type: "string"
    description: ""

  - name: "middleName"
    type: "string"
    description: ""

  - name: "mobilePhone"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "partnerCode"
    type: "string"
    description: ""

  - name: "password"
    type: "string"
    description: ""

  - name: "password2"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "phoneticName"
    type: "string"
    description: ""

  - name: "printOnCheckAs"
    type: "string"
    description: ""

  - name: "promoCodeList"
    type: "varies"
    description: ""

  - name: "referringUrl"
    type: "string"
    description: ""

  - name: "requirePwdChange"
    type: "boolean, string"
    description: ""

  - name: "roleList"
    type: "varies"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "sendEmail"
    type: "boolean, string"
    description: ""

  - name: "subPartnerLogin"
    type: "boolean, string"
    description: ""

  - name: "subscriptionsList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "taxFractionUnit"
    type: "varies"
    description: ""

  - name: "taxIdNum"
    type: "string"
    description: ""

  - name: "taxRounding"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "vatRegNumber"
    type: "string"
    description: ""
---