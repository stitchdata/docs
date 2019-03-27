---
tap: "netsuite"
# version: "1.0"

name: "Employee"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Employee.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "IPAddressRule"
    type: "string"
    description: ""

  - name: "_class"
    type: "anything"
    description: ""

  - name: "accountNumber"
    type: "string"
    description: ""

  - name: "accruedTimeList"
    type: "anything"
    description: ""

  - name: "addressbookList"
    type: "anything"
    description: ""

  - name: "adpId"
    type: "string"
    description: ""

  - name: "altName"
    type: "string"
    description: ""

  - name: "approvalLimit"
    type: "number, string"
    description: ""

  - name: "approver"
    type: "anything"
    description: ""

  - name: "baseWage"
    type: "number, string"
    description: ""

  - name: "baseWageType"
    type: "anything"
    description: ""

  - name: "billPay"
    type: "boolean, string"
    description: ""

  - name: "billingClass"
    type: "anything"
    description: ""

  - name: "birthDate"
    type: "date-time"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "commissionPaymentPreference"
    type: "anything"
    description: ""

  - name: "companyContributionList"
    type: "anything"
    description: ""

  - name: "compensationCurrency"
    type: "anything"
    description: ""

  - name: "concurrentWebServicesUser"
    type: "boolean, string"
    description: ""

  - name: "currency"
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

  - name: "deductionList"
    type: "anything"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "department"
    type: "anything"
    description: ""

  - name: "directDeposit"
    type: "boolean, string"
    description: ""

  - name: "directDepositList"
    type: "anything"
    description: ""

  - name: "earningList"
    type: "anything"
    description: ""

  - name: "eligibleForCommission"
    type: "boolean, string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emergencyContactList"
    type: "anything"
    description: ""

  - name: "employeeStatus"
    type: "anything"
    description: ""

  - name: "employeeType"
    type: "anything"
    description: ""

  - name: "entityId"
    type: "string"
    description: ""

  - name: "ethnicity"
    type: "anything"
    description: ""

  - name: "expenseLimit"
    type: "number, string"
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

  - name: "gender"
    type: "anything"
    description: ""

  - name: "giveAccess"
    type: "boolean, string"
    description: ""

  - name: "globalSubscriptionStatus"
    type: "anything"
    description: ""

  - name: "hasOfflineAccess"
    type: "boolean, string"
    description: ""

  - name: "hcmPositionList"
    type: "anything"
    description: ""

  - name: "hireDate"
    type: "date-time"
    description: ""

  - name: "homePhone"
    type: "string"
    description: ""

  - name: "hrEducationList"
    type: "anything"
    description: ""

  - name: "image"
    type: "anything"
    description: ""

  - name: "inheritIPRules"
    type: "boolean, string"
    description: ""

  - name: "initials"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isJobResource"
    type: "boolean, string"
    description: ""

  - name: "isSalesRep"
    type: "boolean, string"
    description: ""

  - name: "isSupportRep"
    type: "boolean, string"
    description: ""

  - name: "job"
    type: "anything"
    description: ""

  - name: "jobDescription"
    type: "string"
    description: ""

  - name: "laborCost"
    type: "number, string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "lastPaidDate"
    type: "date-time"
    description: ""

  - name: "lastReviewDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "maritalStatus"
    type: "anything"
    description: ""

  - name: "middleName"
    type: "string"
    description: ""

  - name: "mobilePhone"
    type: "string"
    description: ""

  - name: "nextReviewDate"
    type: "date-time"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "officePhone"
    type: "string"
    description: ""

  - name: "password"
    type: "string"
    description: ""

  - name: "password2"
    type: "string"
    description: ""

  - name: "payFrequency"
    type: "anything"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "phoneticName"
    type: "string"
    description: ""

  - name: "purchaseOrderApprovalLimit"
    type: "number, string"
    description: ""

  - name: "purchaseOrderApprover"
    type: "anything"
    description: ""

  - name: "purchaseOrderLimit"
    type: "number, string"
    description: ""

  - name: "ratesList"
    type: "anything"
    description: ""

  - name: "releaseDate"
    type: "date-time"
    description: ""

  - name: "requirePwdChange"
    type: "boolean, string"
    description: ""

  - name: "rolesList"
    type: "anything"
    description: ""

  - name: "salesRole"
    type: "anything"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "sendEmail"
    type: "boolean, string"
    description: ""

  - name: "socialSecurityNumber"
    type: "string"
    description: ""

  - name: "startDateTimeOffCalc"
    type: "date-time"
    description: ""

  - name: "subscriptionsList"
    type: "anything"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""

  - name: "supervisor"
    type: "anything"
    description: ""

  - name: "template"
    type: "anything"
    description: ""

  - name: "terminationCategory"
    type: "anything"
    description: ""

  - name: "terminationDetails"
    type: "string"
    description: ""

  - name: "terminationReason"
    type: "anything"
    description: ""

  - name: "terminationRegretted"
    type: "anything"
    description: ""

  - name: "timeApprover"
    type: "anything"
    description: ""

  - name: "timeOffPlan"
    type: "anything"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "usePerquest"
    type: "boolean, string"
    description: ""

  - name: "useTimeData"
    type: "anything"
    description: ""

  - name: "workAssignment"
    type: "anything"
    description: ""

  - name: "workCalendar"
    type: "anything"
    description: ""

  - name: "workplace"
    type: "anything"
    description: ""
---
