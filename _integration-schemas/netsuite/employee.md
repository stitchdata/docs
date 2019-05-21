---
tap: "netsuite"
version: "1.0"

name: "Employee"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/employee.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Employee.json"
description: |
  The `{{ table.name }}` table contains info about the employees in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "employee"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "employee-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "IPAddressRule"
    type: "string"
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "accountNumber"
    type: "string"
    description: ""

  - name: "accruedTimeList"
    type: "varies"
    description: ""

  - name: "addressbookList"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "baseWage"
    type: "number, string"
    description: ""

  - name: "baseWageType"
    type: "varies"
    description: ""

  - name: "billPay"
    type: "boolean, string"
    description: ""

  - name: "billingClass"
    type: "varies"
    description: ""

  - name: "birthDate"
    type: "date-time"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "commissionPaymentPreference"
    type: "varies"
    description: ""

  - name: "companyContributionList"
    type: "varies"
    description: ""

  - name: "compensationCurrency"
    type: "varies"
    description: ""

  - name: "concurrentWebServicesUser"
    type: "boolean, string"
    description: ""

  - name: "currency"
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

  - name: "deductionList"
    type: "varies"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "directDeposit"
    type: "boolean, string"
    description: ""

  - name: "directDepositList"
    type: "varies"
    description: ""

  - name: "earningList"
    type: "varies"
    description: ""

  - name: "eligibleForCommission"
    type: "boolean, string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emergencyContactList"
    type: "varies"
    description: ""

  - name: "employeeStatus"
    type: "varies"
    description: ""

  - name: "employeeType"
    type: "varies"
    description: ""

  - name: "entityId"
    type: "string"
    description: ""

  - name: "ethnicity"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "giveAccess"
    type: "boolean, string"
    description: ""

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: ""

  - name: "hasOfflineAccess"
    type: "boolean, string"
    description: ""

  - name: "hcmPositionList"
    type: "varies"
    description: ""

  - name: "hireDate"
    type: "date-time"
    description: ""

  - name: "homePhone"
    type: "string"
    description: ""

  - name: "hrEducationList"
    type: "varies"
    description: ""

  - name: "image"
    type: "varies"
    description: ""

  - name: "inheritIPRules"
    type: "boolean, string"
    description: ""

  - name: "initials"
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
    type: "varies"
    description: ""

  - name: "jobDescription"
    type: "string"
    description: ""

  - name: "laborCost"
    type: "number, string"
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
    type: "varies"
    description: ""

  - name: "maritalStatus"
    type: "varies"
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
    type: "varies"
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
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "purchaseOrderLimit"
    type: "number, string"
    description: ""

  - name: "ratesList"
    type: "varies"
    description: ""

  - name: "releaseDate"
    type: "date-time"
    description: ""

  - name: "requirePwdChange"
    type: "boolean, string"
    description: ""

  - name: "rolesList"
    type: "varies"
    description: ""

  - name: "salesRole"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "supervisor"
    type: "varies"
    description: ""

  - name: "template"
    type: "varies"
    description: ""

  - name: "terminationCategory"
    type: "varies"
    description: ""

  - name: "terminationDetails"
    type: "string"
    description: ""

  - name: "terminationReason"
    type: "varies"
    description: ""

  - name: "terminationRegretted"
    type: "varies"
    description: ""

  - name: "timeApprover"
    type: "varies"
    description: ""

  - name: "timeOffPlan"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "usePerquest"
    type: "boolean, string"
    description: ""

  - name: "useTimeData"
    type: "varies"
    description: ""

  - name: "workAssignment"
    type: "varies"
    description: ""

  - name: "workCalendar"
    type: "varies"
    description: ""

  - name: "workplace"
    type: "varies"
    description: ""
---