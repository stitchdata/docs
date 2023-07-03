---
tap: "netsuite"
version: "2"
name: Partner
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Partner.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Partner
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: contactRolesList
  type: varies
  description: ""
- name: middleName
  type: string
  description: ""
- name: partnerCode
  type: string
  description: ""
- name: emailPreference
  type: varies
  description: ""
- name: password2
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: eligibleForCommission
  type: boolean, string
  description: ""
- name: taxFractionUnit
  type: varies
  description: ""
- name: fax
  type: string
  description: ""
- name: email
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: isPerson
  type: boolean, string
  description: ""
- name: vatRegNumber
  type: string
  description: ""
- name: referringUrl
  type: string
  description: ""
- name: addressbookList
  type: varies
  description: ""
- name: defaultAddress
  type: string
  description: ""
- name: parent
  type: varies
  description: ""
- name: subscriptionsList
  type: varies
  description: ""
- name: password
  type: string
  description: ""
- name: phone
  type: string
  description: ""
- name: sendEmail
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: categoryList
  type: varies
  description: ""
- name: accessRole
  type: varies
  description: ""
- name: mobilePhone
  type: string
  description: ""
- name: promoCodeList
  type: varies
  description: ""
- name: firstName
  type: string
  description: ""
- name: loginAs
  type: string
  description: ""
- name: salutation
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: subsidiary
  type: varies
  description: ""
- name: taxRegistrationList
  type: varies
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: defaultTaxReg
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: requirePwdChange
  type: boolean, string
  description: ""
- name: homePhone
  type: string
  description: ""
- name: subPartnerLogin
  type: boolean, string
  description: ""
- name: giveAccess
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: lastName
  type: string
  description: ""
- name: printOnCheckAs
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: taxRounding
  type: varies
  description: ""
- name: altName
  type: string
  description: ""
- name: altEmail
  type: string
  description: ""
- name: image
  type: varies
  description: ""
- name: roleList
  type: varies
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: companyName
  type: string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: entityId
  type: string
  description: ""
- name: taxIdNum
  type: string
  description: ""
- name: bcn
  type: string
  description: ""
---