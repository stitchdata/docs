---
tap: netsuite
version: "2"
name: Job
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Job.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Job
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: projectedEndDateBaseline
  type: string
  description: ""
- name: actualTime
  type: varies
  description: ""
- name: percentTimeComplete
  type: string, number
  description: ""
- name: category
  type: varies
  description: ""
- name: estimatedLaborCostBaseline
  type: string, number
  description: ""
- name: emailPreference
  type: varies
  description: ""
- name: fxRate
  type: string, number
  description: ""
- name: billingSchedule
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
- name: jobResourcesList
  type: varies
  description: ""
- name: createChargeRule
  type: boolean, string
  description: ""
- name: isProductiveTime
  type: boolean, string
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
- name: parent
  type: varies
  description: ""
- name: estimatedCost
  type: string, number
  description: ""
- name: projectManager
  type: string
  description: ""
- name: creditCardsList
  type: varies
  description: ""
- name: phone
  type: string
  description: ""
- name: estimatedTimeOverride
  type: varies
  description: ""
- name: altPhone
  type: string
  description: ""
- name: schedulingMethod
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: percentCompleteOverrideList
  type: varies
  description: ""
- name: jobPrice
  type: string, number
  description: ""
- name: isExemptTime
  type: boolean, string
  description: ""
- name: startDate
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: calculatedStartDate
  type: string
  description: ""
- name: revRecForecastRule
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: usePercentCompleteOverride
  type: boolean, string
  description: ""
- name: isUtilizedTime
  type: boolean, string
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: allowTime
  type: boolean, string
  description: ""
- name: plannedWork
  type: string
  description: ""
- name: currency
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: openingBalance
  type: string, number
  description: ""
- name: jobBillingType
  type: varies
  description: ""
- name: lastBaselineDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: milestonesList
  type: varies
  description: ""
- name: language
  type: varies
  description: ""
- name: estimateRevRecTemplate
  type: varies
  description: ""
- name: percentComplete
  type: string, number
  description: ""
- name: customForm
  type: varies
  description: ""
- name: limitTimeToAssignees
  type: boolean, string
  description: ""
- name: billPay
  type: boolean, string
  description: ""
- name: estimatedGrossProfitPercent
  type: string, number
  description: ""
- name: sourceServiceItemFromRateCard
  type: boolean, string
  description: ""
- name: billingRateCard
  type: string
  description: ""
- name: applyProjectExpenseTypeToAll
  type: boolean, string
  description: ""
- name: projectExpenseType
  type: varies
  description: ""
- name: projectedEndDate
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: scheduledEndDate
  type: string
  description: ""
- name: altName
  type: string
  description: ""
- name: plannedWorkBaseline
  type: string
  description: ""
- name: openingBalanceDate
  type: string
  description: ""
- name: jobItem
  type: varies
  description: ""
- name: plStatementList
  type: varies
  description: ""
- name: calculatedEndDateBaseline
  type: string
  description: ""
- name: estimatedLaborCost
  type: string, number
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: timeApproval
  type: string
  description: ""
- name: startDateBaseline
  type: string
  description: ""
- name: materializeTime
  type: boolean, string
  description: ""
- name: companyName
  type: string
  description: ""
- name: calculatedEndDate
  type: string
  description: ""
- name: includeCrmTasksInTotals
  type: boolean, string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: allocatePayrollExpenses
  type: boolean, string
  description: ""
- name: timeRemaining
  type: varies
  description: ""
- name: estimatedTime
  type: varies
  description: ""
- name: jobType
  type: varies
  description: ""
- name: entityId
  type: string
  description: ""
- name: workplace
  type: varies
  description: ""
- name: estimatedLaborRevenue
  type: string, number
  description: ""
- name: allowAllResourcesForTasks
  type: boolean, string
  description: ""
- name: entityStatus
  type: varies
  description: ""
- name: allowExpenses
  type: boolean, string
  description: ""
- name: estimatedGrossProfit
  type: string, number
  description: ""
- name: openingBalanceAccount
  type: varies
  description: ""
- name: estimatedRevenue
  type: string, number
  description: ""
