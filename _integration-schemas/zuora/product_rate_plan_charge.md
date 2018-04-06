---
tap: "zuora"
version: 1.0 

name: "productRatePlanCharge"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Product-Rate-Plan-Charges
description: |
  The `productRatePlanCharge` table contains info about product rate plan charges, which are a charge model or set of fees associated with a product rate plan.

replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the product rate plan charge."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the product rate plan charge was last updated."

  - name: "accountingCode"
    type: "string"
    description: "The accounting code for the charge."

  - name: "applyDiscountTo"
    type: "string"
    description: |
      The type of charges to apply a specific discount to. Possible values are:

      - `ONETIME (1)`
      - `RECURRING (2)`
      - `ONETIMERECURRING (3)`
      - `USAGE (4)`
      - `ONETIMEUSAGE (5)`
      - `RECURRINGUSAGE (6)`
      - `ONETIMERECURRINGUSAGE (7)`

  - name: "billCycleDay"
    type: "integer"
    description: "The bill cycle day (BCD) for the charge, which determines which day of the month the customer is billed. For example: A value of `1` indicates that the customer is billed on the first day of the month."

  - name: "billCycleType"
    type: "string"
    description: |
      Indicates how to determine the billing day for the charge. Possible values are:

      - `DefaultFromCustomer`
      - `SpecificDayOfMonth:`
      - `SubscriptionStartDay`
      - `ChargeTriggerDay`
      - `SpecificDayOfWeek`

  - name: "billingPeriod"
    type: "string"
    description: |
      The billing period for the charge. The start day of the billing period is called the bill cycle day (BCD). Possible values are:

      - `Month`
      - `Quarter`
      - `Annual`
      - `Semi-Annual`
      - `Specific Months`
      - `Subscription Term`
      - `Week`
      - `Specific Weeks`

  - name: "billingPeriodAlignment"
    type: "string"
    description: |
      Indicates how charges within the same subscription should be aligned if multiple charges begin on different dates. Possible values are:

      - `AlignToCharge`
      - `AlignToSubscriptionStart`
      - `AlignToTermStart`

  - name: "billingTiming"
    type: "string"
    description: |
      The billing timing for the charge. Possible values are:

      - `In Advance`
      - `In Arrears`

  - name: "chargeModel"
    type: "string"
    description: |
      Determines how to calculate charges. Possible values are:

      - `Discount-Fixed Amount`
      - `Discount-Percentage`
      - `Flat Fee Pricing`
      - `Per Unit Pricing`
      - `Overage Pricing`
      - `Tiered Pricing`
      - `Tiered with Overage Pricing`
      - `Volume Pricing`

  - name: "chargeType"
    type: "string"
    description: |
      The type of charge. Possible values are:

      - `OneTime`
      - `Recurring`
      - `Usage`

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the product rate plan charge."

  - name: "createdDate"
    type: "date-time"
    description: "The date the product rate plan charge was created."

  - name: "defaultQuantity"
    type: "decimal"
    description: "The default quantity of units."

  - name: "deferredRevenueAccount"
    type: "string"
    description: "The name of the deferred revenue account for this charge."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "description"
    type: "string"
    description: "The description of the charge."

  - name: "discountClass"
    type: "string"
    description: "The class that the discount belongs to. A discount class defines the order in which discount product rate plan charges are applied."

  - name: "discountLevel"
    type: "string"
    description: |
      Indicates what the discount applies to. Possible values are:

      - `rateplan`
      - `subscription`
      - `account`

  - name: "endDateCondition"
    type: "string"
    description: |
      Defines when the charge ends after the charge trigger date. Possible values are:

      - `SubscriptionEnd` - The charge ends on the subscription end date after a specified period, based on the trigger date of the charge.
      - `FixedPeriod` - The charge ends after a specified period, based on the trigger date of the charge.

  - name: "includedUnits"
    type: "decimal"
    description: "Indicates the number of units in the base set of units."

  - name: "listPriceBase"
    type: "string"
    description: |
      The list price base for the product rate plan charge. Possible values are:

      - `Per Month`
      - `Per Billing Period`
      - `Per Week`

  - name: "maxQuantity"
    type: "decimal"
    description: "Indicates the maximum number of units for this charge."

  - name: "minQuantity"
    type: "decimal"
    description: "Indicates the minimum number of units for this charge."

  - name: "name"
    type: "string"
    description: "The name of the product rate plan charge."

  - name: "numberOfPeriod"
    type: "integer"
    description: "Specifies the number of periods to use when calculating charges in an overage smoothing charge model."

  - name: "overCalculationOption"
    type: "string"
    description: |
      Determines when to calculate overage charges. Possible values are:

      - `endOfSmoothingPeriod`
      - `perBillingPeriod`

  - name: "overageUnusedUnitsCreditOption"
    type: "string"
    description: |
      Determines whether the customer will credited with unused units of usage. Possible values are:

      - `NoCredit`
      - `CreditBySpecificRate`

  - name: "priceChangeOption"
    type: "string"
    description: |
      Indicates whether an automatic price change is applied when a termed subscription is renewed. Possible values are:

      - `NoChange`
      - `SpecificPercentageValue`
      - `UseLatestProductCatalogPricing`

  - name: "priceIncreaseOption"
    type: "string"
    description: |
      Indicates if an automatic price increase when a termed subscription is renewed. Possible values are:

      - `FromTenantPercentageValue`
      - `SpecificPercentageValue`

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with this product rate plan charge."
    foreign-key: true
    ## foreign-keys:
    ##   - table-name: "productRatePlan"
    ##     attribute: "Id"

  - name: "recognizedRevenueAccount"
    type: "string"
    description: "The name of the recognized revenue account for this charge."

  - name: "revRecCode"
    type: "string"
    description: "Associates the product rate plan charge with a specific revenue recognition code."

  - name: "revRecTriggerCondition"
    type: "string"
    description: |
      Indicates when revenue recognition begins. Possible values are:

      - `contractEffectiveDate`
      - `serviceActivationDate`
      - `customerAcceptanceDate`

  - name: "revenueRecognitionRuleName"
    type: "string"
    description: |
      Indicates when the revenue for this charge is recognized. Possible values are:

      - `Recognize upon invoicing`
      - `Recognize daily over time`

  - name: "smoothingModel"
    type: "string"
    description: |
      The smoothing model for an overage smoothing model. Possible values are:

      - `RollingWindow`
      - `Rollover`

  - name: "specificBillingPeriod"
    type: "integer"
    description: "The number of months or weeks for the charges billing period."

  - name: "taxCode"
    type: "string"
    description: "The tax code for taxation rules."

  - name: "taxMode"
    type: "string"
    description: |
      Defines taxation for the charge. Possible values are:

      - `TaxExclusive`
      - `TaxInclusive`

  - name: "taxable"
    type: "boolean"
    description: "If `true`, the charge is taxable."

  - name: "triggerEvent"
    type: "string"
    description: |
      Indicates when the customer should begin to be billed. Possible values are:

      - `ContractEffective` - The date when the subscription's contract goes into effect and the charge is ready to be billed.
      - `ServiceActivation` - The date when the services or products for a subscription have been activated and the customers have access.
      - `CustomerAcceptance` - The date the customer accepts the services or products for a subscription.

  - name: "uom"
    type: "string"
    description: "The units to measure usage."

  - name: "upToPeriods"
    type: "integer"
    description: "The length of the period during which the charge is active."

  - name: "upToPeriodsType"
    type: "string"
    description: |
      The period type used to define when the charge ends. Possible values are:

      - `Billing Periods`
      - `Days`
      - `Weeks`
      - `Months`
      - `Years`

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the product rate plan change."

  - name: "useDiscountSpecificAccountingCode"
    type: "boolean"
    description: "If `true`, a new accounting code for new discount charges will be used."

  - name: "useTenantDefaultForPriceChange"
    type: "boolean"
    description: "If true, the tenant-level percentage uplift value for an automatic price change to a termed subscription renewal will be applied."

  - name: "weeklyBillCycleDay"
    type: "string"
    description: "The day of the week that is used as the bill cycle day (BCD) for the charge."

---