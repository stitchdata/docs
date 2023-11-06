---
tap: "netsuite"
version: "2"
name: Employee
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Employee.html
description: |
  The `{{ table.name }}` table contains info about the employees in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "employee"

replication-method: "Key-based Incremental"
attributes:
- name: timeApprover
  type: varies
  description: ""
- name: rolesList
  type: varies
  description: ""
- name: companyContributionList
  type: varies
  description: ""
- name: middleName
  type: string
  description: ""
- name: password2
  type: string
  description: ""
- name: initials
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: eligibleForCommission
  type: boolean, string
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
- name: ratesList
  type: varies
  description: ""
- name: bonusTargetType
  type: string
  description: ""
- name: isJobResource
  type: boolean, string
  description: ""
- name: usePerquest
  type: boolean, string
  description: ""
- name: employeeStatus
  type: varies
  description: ""
- name: hrEducationList
  type: varies
  description: ""
- name: addressbookList
  type: varies
  description: ""
- name: accountNumber
  type: string
  description: ""
- name: defaultAddress
  type: string
  description: ""
- name: compensationCurrency
  type: varies
  description: ""
- name: subscriptionsList
  type: varies
  description: ""
- name: deductionList
  type: varies
  description: ""
- name: terminationDetails
  type: string
  description: ""
- name: nextReviewDate
  type: string
  description: ""
- name: password
  type: string
  description: ""
- name: phone
  type: string
  description: ""
- name: purchaseOrderLimit
  type: string, number
  description: ""
- name: purchaseOrderApprovalLimit
  type: string, number
  description: ""
- name: hcmPositionList
  type: varies
  description: ""
- name: approvalLimit
  type: string, number
  description: ""
- name: bonusTargetPayFrequency
  type: string
  description: ""
- name: isSalesRep
  type: boolean, string
  description: ""
- name: earningList
  type: varies
  description: ""
- name: commissionPaymentPreference
  type: varies
  description: ""
- name: terminationReason
  type: varies
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
- name: adpId
  type: string
  description: ""
- name: mobilePhone
  type: string
  description: ""
- name: birthDate
  type: string
  description: ""
- name: terminationRegretted
  type: varies
  description: ""
- name: concurrentWebServicesUser
  type: boolean, string
  description: ""
- name: firstName
  type: string
  description: ""
- name: salutation
  type: string
  description: ""
- name: releaseDate
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: isSupportRep
  type: boolean, string
  description: ""
- name: ethnicity
  type: varies
  description: ""
- name: template
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: socialSecurityNumber
  type: string
  description: ""
- name: isJobManager
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: bonusTargetComment
  type: string
  description: ""
- name: workAssignment
  type: varies
  description: ""
- name: bonusTarget
  type: string, number
  description: ""
- name: baseWageType
  type: varies
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: requirePwdChange
  type: boolean, string
  description: ""
- name: directDeposit
  type: boolean, string
  description: ""
- name: useTimeData
  type: varies
  description: ""
- name: homePhone
  type: string
  description: ""
- name: supervisor
  type: varies
  description: ""
- name: approver
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: targetUtilization
  type: string, number
  description: ""
- name: accruedTimeList
  type: varies
  description: ""
- name: billingClass
  type: varies
  description: ""
- name: purchaseOrderApprover
  type: varies
  description: ""
- name: giveAccess
  type: boolean, string
  description: ""
- name: baseWage
  type: string, number
  description: ""
- name: externalId
  type: string
  description: ""
- name: jobDescription
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: billPay
  type: boolean, string
  description: ""
- name: lastName
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: lastReviewDate
  type: string
  description: ""
- name: altName
  type: string
  description: ""
- name: hireDate
  type: string
  description: ""
- name: image
  type: varies
  description: ""
- name: terminationCategory
  type: varies
  description: ""
- name: gender
  type: varies
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: workCalendar
  type: varies
  description: ""
- name: employeeType
  type: varies
  description: ""
- name: hasOfflineAccess
  type: boolean, string
  description: ""
- name: IPAddressRule
  type: string
  description: ""
- name: inheritIPRules
  type: boolean, string
  description: ""
- name: maritalStatus
  type: varies
  description: ""
- name: officePhone
  type: string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: laborCost
  type: string, number
  description: ""
- name: timeOffPlan
  type: varies
  description: ""
- name: salesRole
  type: varies
  description: ""
- name: defaultAcctCorpCardExp
  type: string
  description: ""
- name: entityId
  type: string
  description: ""
- name: emergencyContactList
  type: varies
  description: ""
- name: workplace
  type: varies
  description: ""
- name: startDateTimeOffCalc
  type: string
  description: ""
- name: expenseLimit
  type: string, number
  description: ""
- name: directDepositList
  type: varies
  description: ""
- name: lastPaidDate
  type: string
  description: ""
- name: defaultExpenseReportCurrency
  type: string
  description: ""
- name: job
  type: varies
  description: ""
- name: payFrequency
  type: varies
  description: ""
---