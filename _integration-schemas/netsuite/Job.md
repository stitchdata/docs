---
tap: "netsuite"
version: "1.0"

name: "Job"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/job.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Job.json"
description: |
  The `{{ table.name }}` table contains info about the projects in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "job"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "job-id"

  - name: "accountNumber"
    type: "string"
    description: ""

  - name: "actualTime"
    type: "varies"
    description: ""

  - name: "addressbookList"
    type: "varies"
    description: ""

  - name: "allocatePayrollExpenses"
    type: "boolean, string"
    description: ""

  - name: "allowAllResourcesForTasks"
    type: "boolean, string"
    description: ""

  - name: "allowExpenses"
    type: "boolean, string"
    description: ""

  - name: "allowTime"
    type: "boolean, string"
    description: ""

  - name: "altName"
    type: "string"
    description: ""

  - name: "altPhone"
    type: "string"
    description: ""

  - name: "applyProjectExpenseTypeToAll"
    type: "boolean, string"
    description: ""

  - name: "billPay"
    type: "boolean, string"
    description: ""

  - name: "billingSchedule"
    type: "varies"
    description: ""

  - name: "calculatedEndDate"
    type: "date-time"
    description: ""

  - name: "calculatedEndDateBaseline"
    type: "date-time"
    description: ""

  - name: "category"
    type: "varies"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "companyName"
    type: "string"
    description: ""

  - name: "creditCardsList"
    type: "varies"
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

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailPreference"
    type: "varies"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "entityId"
    type: "string"
    description: ""

  - name: "entityStatus"
    type: "varies"
    description: ""

  - name: "estimateRevRecTemplate"
    type: "varies"
    description: ""

  - name: "estimatedCost"
    type: "number, string"
    description: ""

  - name: "estimatedGrossProfit"
    type: "number, string"
    description: ""

  - name: "estimatedGrossProfitPercent"
    type: "number, string"
    description: ""

  - name: "estimatedLaborCost"
    type: "number, string"
    description: ""

  - name: "estimatedLaborCostBaseline"
    type: "number, string"
    description: ""

  - name: "estimatedLaborRevenue"
    type: "number, string"
    description: ""

  - name: "estimatedRevenue"
    type: "number, string"
    description: ""

  - name: "estimatedTime"
    type: "varies"
    description: ""

  - name: "estimatedTimeOverride"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "fxRate"
    type: "number, string"
    description: ""

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: ""

  - name: "includeCrmTasksInTotals"
    type: "boolean, string"
    description: ""

  - name: "isExemptTime"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isProductiveTime"
    type: "boolean, string"
    description: ""

  - name: "isUtilizedTime"
    type: "boolean, string"
    description: ""

  - name: "jobBillingType"
    type: "varies"
    description: ""

  - name: "jobItem"
    type: "varies"
    description: ""

  - name: "jobPrice"
    type: "number, string"
    description: ""

  - name: "jobResourcesList"
    type: "varies"
    description: ""

  - name: "jobType"
    type: "varies"
    description: ""

  - name: "language"
    type: "varies"
    description: ""

  - name: "lastBaselineDate"
    type: "date-time"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "limitTimeToAssignees"
    type: "boolean, string"
    description: ""

  - name: "materializeTime"
    type: "boolean, string"
    description: ""

  - name: "milestonesList"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "openingBalance"
    type: "number, string"
    description: ""

  - name: "openingBalanceAccount"
    type: "varies"
    description: ""

  - name: "openingBalanceDate"
    type: "date-time"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "percentComplete"
    type: "number, string"
    description: ""

  - name: "percentCompleteOverrideList"
    type: "varies"
    description: ""

  - name: "percentTimeComplete"
    type: "number, string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "phoneticName"
    type: "string"
    description: ""

  - name: "plStatementList"
    type: "varies"
    description: ""

  - name: "projectExpenseType"
    type: "varies"
    description: ""

  - name: "projectedEndDate"
    type: "date-time"
    description: ""

  - name: "projectedEndDateBaseline"
    type: "date-time"
    description: ""

  - name: "revRecForecastRule"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "startDateBaseline"
    type: "date-time"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "timeRemaining"
    type: "varies"
    description: ""

  - name: "usePercentCompleteOverride"
    type: "boolean, string"
    description: ""

  - name: "workplace"
    type: "varies"
    description: ""
---