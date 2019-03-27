---
tap: "netsuite"
# version: "1.0"

name: "Partner"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Partner.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "anything"
    description: ""

  - name: "accessRole"
    type: "anything"
    description: ""

  - name: "addressbookList"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "companyName"
    type: "string"
    description: ""

  - name: "contactRolesList"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "dateCreated"
    type: "date-time"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "department"
    type: "anything"
    description: ""

  - name: "eligibleForCommission"
    type: "boolean, string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailPreference"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "homePhone"
    type: "string"
    description: ""

  - name: "image"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isPerson"
    type: "boolean, string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "location"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "parent"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "referringUrl"
    type: "string"
    description: ""

  - name: "requirePwdChange"
    type: "boolean, string"
    description: ""

  - name: "roleList"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""

  - name: "taxFractionUnit"
    type: "anything"
    description: ""

  - name: "taxIdNum"
    type: "string"
    description: ""

  - name: "taxRounding"
    type: "anything"
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
