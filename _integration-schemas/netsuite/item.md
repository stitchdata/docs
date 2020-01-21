---
tap: "netsuite"
version: "1"

name: "Item"
doc-link: ""
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Item.json"
description: |
  The `{{ table.name }}` table contains info about items.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "item-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "_type"
    type: "string"
    description: ""

  - name: "account"
    type: "varies"
    description: ""

  - name: "accountingBookDetailList"
    type: "varies"
    description: ""

  - name: "alternateDemandSourceItem"
    type: "varies"
    description: ""

  - name: "amortizationPeriod"
    type: "integer, string"
    description: ""

  - name: "amortizationTemplate"
    type: "varies"
    description: ""

  - name: "assetAccount"
    type: "varies"
    description: ""

  - name: "authCodesList"
    type: "varies"
    description: ""

  - name: "autoLeadTime"
    type: "boolean, string"
    description: ""

  - name: "autoPreferredStockLevel"
    type: "boolean, string"
    description: ""

  - name: "autoReorderPoint"
    type: "boolean, string"
    description: ""

  - name: "availableToPartners"
    type: "boolean, string"
    description: ""

  - name: "averageCost"
    type: "number, string"
    description: ""

  - name: "backwardConsumptionDays"
    type: "integer, string"
    description: ""

  - name: "billExchRateVarianceAcct"
    type: "varies"
    description: ""

  - name: "billOfMaterialsList"
    type: "varies"
    description: ""

  - name: "billPriceVarianceAcct"
    type: "varies"
    description: ""

  - name: "billQtyVarianceAcct"
    type: "varies"
    description: ""

  - name: "billingRatesMatrix"
    type: "varies"
    description: ""

  - name: "billingSchedule"
    type: "varies"
    description: ""

  - name: "binNumberList"
    type: "varies"
    description: ""

  - name: "buildEntireAssembly"
    type: "boolean, string"
    description: ""

  - name: "buildTime"
    type: "integer, string"
    description: ""

  - name: "cogsAccount"
    type: "varies"
    description: ""

  - name: "contingentRevenueHandling"
    type: "boolean, string"
    description: ""

  - name: "copyDescription"
    type: "boolean, string"
    description: ""

  - name: "cost"
    type: "number, string"
    description: ""

  - name: "costCategory"
    type: "varies"
    description: ""

  - name: "costEstimate"
    type: "number, string"
    description: ""

  - name: "costEstimateType"
    type: "varies"
    description: ""

  - name: "costEstimateUnits"
    type: "string"
    description: ""

  - name: "costUnits"
    type: "string"
    description: ""

  - name: "costingMethod"
    type: "varies"
    description: ""

  - name: "costingMethodDisplay"
    type: "string"
    description: ""

  - name: "countryOfManufacture"
    type: "varies"
    description: ""

  - name: "createJob"
    type: "boolean, string"
    description: ""

  - name: "createRevenuePlansOn"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dateConvertedToInv"
    type: "date-time"
    description: ""

  - name: "daysBeforeExpiration"
    type: "integer, string"
    description: ""

  - name: "defaultItemShipMethod"
    type: "varies"
    description: ""

  - name: "defaultReturnCost"
    type: "number, string"
    description: ""

  - name: "defaultRevision"
    type: "string"
    description: ""

  - name: "deferRevRec"
    type: "boolean, string"
    description: ""

  - name: "deferralAccount"
    type: "varies"
    description: ""

  - name: "deferredRevenueAccount"
    type: "varies"
    description: ""

  - name: "demandModifier"
    type: "number, string"
    description: ""

  - name: "demandSource"
    type: "varies"
    description: ""

  - name: "demandTimeFence"
    type: "integer, string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "directRevenuePosting"
    type: "boolean, string"
    description: ""

  - name: "displayName"
    type: "string"
    description: ""

  - name: "distributionCategory"
    type: "varies"
    description: ""

  - name: "distributionNetwork"
    type: "varies"
    description: ""

  - name: "dontShowPrice"
    type: "boolean, string"
    description: ""

  - name: "dropshipExpenseAccount"
    type: "varies"
    description: ""

  - name: "effectiveBomControl"
    type: "varies"
    description: ""

  - name: "enforceMinQtyInternally"
    type: "boolean, string"
    description: ""

  - name: "excludeFromSitemap"
    type: "boolean, string"
    description: ""

  - name: "expenseAccount"
    type: "varies"
    description: ""

  - name: "expirationDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "featuredDescription"
    type: "string"
    description: ""

  - name: "fixedLotSize"
    type: "number, string"
    description: ""

  - name: "forwardConsumptionDays"
    type: "integer, string"
    description: ""

  - name: "fraudRisk"
    type: "varies"
    description: ""

  - name: "gainLossAccount"
    type: "varies"
    description: ""

  - name: "generateAccruals"
    type: "boolean, string"
    description: ""

  - name: "handlingCost"
    type: "number, string"
    description: ""

  - name: "handlingCostUnits"
    type: "string"
    description: ""

  - name: "hazmatHazardClass"
    type: "string"
    description: ""

  - name: "hazmatId"
    type: "string"
    description: ""

  - name: "hazmatItemUnits"
    type: "string"
    description: ""

  - name: "hazmatItemUnitsQty"
    type: "number, string"
    description: ""

  - name: "hazmatPackingGroup"
    type: "varies"
    description: ""

  - name: "hazmatShippingName"
    type: "string"
    description: ""

  - name: "immediateDownload"
    type: "boolean, string"
    description: ""

  - name: "includeChildren"
    type: "boolean, string"
    description: ""

  - name: "includeStartEndLines"
    type: "boolean, string"
    description: ""

  - name: "incomeAccount"
    type: "varies"
    description: ""

  - name: "intercoCogsAccount"
    type: "varies"
    description: ""

  - name: "intercoDefRevAccount"
    type: "varies"
    description: ""

  - name: "intercoExpenseAccount"
    type: "varies"
    description: ""

  - name: "intercoIncomeAccount"
    type: "varies"
    description: ""

  - name: "invtClassification"
    type: "varies"
    description: ""

  - name: "invtCountInterval"
    type: "integer, string"
    description: ""

  - name: "isDonationItem"
    type: "boolean, string"
    description: ""

  - name: "isDropShipItem"
    type: "boolean, string"
    description: ""

  - name: "isFulfillable"
    type: "boolean, string"
    description: ""

  - name: "isGcoCompliant"
    type: "boolean, string"
    description: ""

  - name: "isHazmatItem"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isOnline"
    type: "boolean, string"
    description: ""

  - name: "isPhantom"
    type: "boolean, string"
    description: ""

  - name: "isPreTax"
    type: "boolean, string"
    description: ""

  - name: "isSpecialOrderItem"
    type: "boolean, string"
    description: ""

  - name: "isSpecialWorkOrderItem"
    type: "boolean, string"
    description: ""

  - name: "isStorePickupAllowed"
    type: "boolean, string"
    description: ""

  - name: "isTaxable"
    type: "boolean, string"
    description: ""

  - name: "isVsoeBundle"
    type: "boolean, string"
    description: ""

  - name: "issueProduct"
    type: "varies"
    description: ""

  - name: "itemCarrier"
    type: "varies"
    description: ""

  - name: "itemId"
    type: "string"
    description: ""

  - name: "itemNumberOptionsList"
    type: "varies"
    description: ""

  - name: "itemOptionsList"
    type: "varies"
    description: ""

  - name: "itemRevenueCategory"
    type: "varies"
    description: ""

  - name: "itemShipMethodList"
    type: "varies"
    description: ""

  - name: "itemTaskTemplatesList"
    type: "varies"
    description: ""

  - name: "itemVendorList"
    type: "varies"
    description: ""

  - name: "lastInvtCountDate"
    type: "date-time"
    description: ""

  - name: "lastPurchasePrice"
    type: "number, string"
    description: ""

  - name: "leadTime"
    type: "integer, string"
    description: ""

  - name: "liabilityAccount"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "locationsList"
    type: "varies"
    description: ""

  - name: "manufacturer"
    type: "string"
    description: ""

  - name: "manufacturerAddr1"
    type: "string"
    description: ""

  - name: "manufacturerCity"
    type: "string"
    description: ""

  - name: "manufacturerState"
    type: "string"
    description: ""

  - name: "manufacturerTariff"
    type: "string"
    description: ""

  - name: "manufacturerTaxId"
    type: "string"
    description: ""

  - name: "manufacturerZip"
    type: "string"
    description: ""

  - name: "manufactureraddr1"
    type: "string"
    description: ""

  - name: "manufacturingChargeItem"
    type: "boolean, string"
    description: ""

  - name: "matchBillToReceipt"
    type: "boolean, string"
    description: ""

  - name: "matrixItemNameTemplate"
    type: "string"
    description: ""

  - name: "matrixOptionList"
    type: "varies"
    description: ""

  - name: "matrixType"
    type: "varies"
    description: ""

  - name: "maxDonationAmount"
    type: "number, string"
    description: ""

  - name: "memberList"
    type: "varies"
    description: ""

  - name: "metaTagHtml"
    type: "string"
    description: ""

  - name: "minimumQuantity"
    type: "integer, string"
    description: ""

  - name: "minimumQuantityUnits"
    type: "string"
    description: ""

  - name: "mpn"
    type: "string"
    description: ""

  - name: "multManufactureAddr"
    type: "boolean, string"
    description: ""

  - name: "nexTagCategory"
    type: "string"
    description: ""

  - name: "nextInvtCountDate"
    type: "date-time"
    description: ""

  - name: "noPriceMessage"
    type: "string"
    description: ""

  - name: "nonPosting"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numOfAllowedDownloads"
    type: "integer, string"
    description: ""

  - name: "numbersList"
    type: "varies"
    description: ""

  - name: "offerSupport"
    type: "boolean, string"
    description: ""

  - name: "onHandValueMli"
    type: "number, string"
    description: ""

  - name: "onSpecial"
    type: "boolean, string"
    description: ""

  - name: "originalItemSubtype"
    type: "varies"
    description: ""

  - name: "originalItemType"
    type: "varies"
    description: ""

  - name: "outOfStockBehavior"
    type: "varies"
    description: ""

  - name: "outOfStockMessage"
    type: "string"
    description: ""

  - name: "overallQuantityPricingType"
    type: "varies"
    description: ""

  - name: "overheadType"
    type: "varies"
    description: ""

  - name: "pageTitle"
    type: "string"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "paymentMethod"
    type: "varies"
    description: ""

  - name: "periodicLotSizeDays"
    type: "integer, string"
    description: ""

  - name: "periodicLotSizeType"
    type: "varies"
    description: ""

  - name: "preferenceCriterion"
    type: "varies"
    description: ""

  - name: "preferredLocation"
    type: "varies"
    description: ""

  - name: "preferredStockLevel"
    type: "number, string"
    description: ""

  - name: "preferredStockLevelDays"
    type: "number, string"
    description: ""

  - name: "preferredStockLevelUnits"
    type: "string"
    description: ""

  - name: "presentationItemList"
    type: "varies"
    description: ""

  - name: "pricesIncludeTax"
    type: "boolean, string"
    description: ""

  - name: "pricingGroup"
    type: "varies"
    description: ""

  - name: "pricingMatrix"
    type: "varies"
    description: ""

  - name: "printItems"
    type: "boolean, string"
    description: ""

  - name: "prodPriceVarianceAcct"
    type: "varies"
    description: ""

  - name: "prodQtyVarianceAcct"
    type: "varies"
    description: ""

  - name: "producer"
    type: "boolean, string"
    description: ""

  - name: "productFeedList"
    type: "varies"
    description: ""

  - name: "purchaseDescription"
    type: "string"
    description: ""

  - name: "purchaseOrderAmount"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantity"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantityDiff"
    type: "number, string"
    description: ""

  - name: "purchasePriceVarianceAcct"
    type: "varies"
    description: ""

  - name: "purchaseTaxCode"
    type: "varies"
    description: ""

  - name: "purchaseUnit"
    type: "varies"
    description: ""

  - name: "quantityAvailable"
    type: "number, string"
    description: ""

  - name: "quantityAvailableUnits"
    type: "string"
    description: ""

  - name: "quantityBackOrdered"
    type: "number, string"
    description: ""

  - name: "quantityCommitted"
    type: "number, string"
    description: ""

  - name: "quantityCommittedUnits"
    type: "string"
    description: ""

  - name: "quantityOnHand"
    type: "number, string"
    description: ""

  - name: "quantityOnHandUnits"
    type: "string"
    description: ""

  - name: "quantityOnOrder"
    type: "number, string"
    description: ""

  - name: "quantityOnOrderUnits"
    type: "string"
    description: ""

  - name: "quantityPricingSchedule"
    type: "varies"
    description: ""

  - name: "quantityReorderUnits"
    type: "string"
    description: ""

  - name: "rate"
    type: "number, string"
    description: ""

  - name: "receiptAmount"
    type: "number, string"
    description: ""

  - name: "receiptQuantity"
    type: "number, string"
    description: ""

  - name: "receiptQuantityDiff"
    type: "number, string"
    description: ""

  - name: "relatedItemsDescription"
    type: "string"
    description: ""

  - name: "reorderMultiple"
    type: "integer, string"
    description: ""

  - name: "reorderPoint"
    type: "number, string"
    description: ""

  - name: "reorderPointUnits"
    type: "string"
    description: ""

  - name: "rescheduleInDays"
    type: "integer, string"
    description: ""

  - name: "rescheduleOutDays"
    type: "integer, string"
    description: ""

  - name: "residual"
    type: "string"
    description: ""

  - name: "revRecForecastRule"
    type: "varies"
    description: ""

  - name: "revRecSchedule"
    type: "varies"
    description: ""

  - name: "revReclassFXAccount"
    type: "varies"
    description: ""

  - name: "revenueAllocationGroup"
    type: "varies"
    description: ""

  - name: "revenueRecognitionRule"
    type: "varies"
    description: ""

  - name: "roundUpAsComponent"
    type: "boolean, string"
    description: ""

  - name: "safetyStockLevel"
    type: "number, string"
    description: ""

  - name: "safetyStockLevelDays"
    type: "integer, string"
    description: ""

  - name: "safetyStockLevelUnits"
    type: "string"
    description: ""

  - name: "saleUnit"
    type: "varies"
    description: ""

  - name: "salesDescription"
    type: "string"
    description: ""

  - name: "salesTaxCode"
    type: "varies"
    description: ""

  - name: "scheduleBCode"
    type: "varies"
    description: ""

  - name: "scheduleBNumber"
    type: "string"
    description: ""

  - name: "scheduleBQuantity"
    type: "integer, string"
    description: ""

  - name: "scrapAcct"
    type: "varies"
    description: ""

  - name: "searchKeywords"
    type: "string"
    description: ""

  - name: "seasonalDemand"
    type: "boolean, string"
    description: ""

  - name: "serialNumbers"
    type: "string"
    description: ""

  - name: "shipIndividually"
    type: "boolean, string"
    description: ""

  - name: "shipPackage"
    type: "varies"
    description: ""

  - name: "shippingCost"
    type: "number, string"
    description: ""

  - name: "shippingCostUnits"
    type: "string"
    description: ""

  - name: "shoppingDotComCategory"
    type: "string"
    description: ""

  - name: "shopzillaCategoryId"
    type: "integer, string"
    description: ""

  - name: "showDefaultDonationAmount"
    type: "boolean, string"
    description: ""

  - name: "siteCategoryList"
    type: "varies"
    description: ""

  - name: "sitemapPriority"
    type: "varies"
    description: ""

  - name: "softDescriptor"
    type: "varies"
    description: ""

  - name: "specialsDescription"
    type: "string"
    description: ""

  - name: "stockDescription"
    type: "string"
    description: ""

  - name: "stockUnit"
    type: "varies"
    description: ""

  - name: "storeDescription"
    type: "string"
    description: ""

  - name: "storeDetailedDescription"
    type: "string"
    description: ""

  - name: "storeDisplayImage"
    type: "varies"
    description: ""

  - name: "storeDisplayName"
    type: "string"
    description: ""

  - name: "storeDisplayThumbnail"
    type: "varies"
    description: ""

  - name: "storeItemTemplate"
    type: "varies"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "supplyLotSizingMethod"
    type: "varies"
    description: ""

  - name: "supplyReplenishmentMethod"
    type: "varies"
    description: ""

  - name: "supplyTimeFence"
    type: "integer, string"
    description: ""

  - name: "supplyType"
    type: "varies"
    description: ""

  - name: "taxSchedule"
    type: "varies"
    description: ""

  - name: "totalValue"
    type: "number, string"
    description: ""

  - name: "trackLandedCost"
    type: "boolean, string"
    description: ""

  - name: "transferPrice"
    type: "number, string"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""

  - name: "unbuildVarianceAccount"
    type: "varies"
    description: ""

  - name: "undepFunds"
    type: "boolean, string"
    description: ""

  - name: "unitsType"
    type: "varies"
    description: ""

  - name: "upcCode"
    type: "string"
    description: ""

  - name: "urlComponent"
    type: "string"
    description: ""

  - name: "useBins"
    type: "boolean, string"
    description: ""

  - name: "useComponentYield"
    type: "boolean, string"
    description: ""

  - name: "useMarginalRates"
    type: "boolean, string"
    description: ""

  - name: "vendor"
    type: "varies"
    description: ""

  - name: "vendorName"
    type: "string"
    description: ""

  - name: "vsoeDeferral"
    type: "varies"
    description: ""

  - name: "vsoeDelivered"
    type: "boolean, string"
    description: ""

  - name: "vsoePermitDiscount"
    type: "varies"
    description: ""

  - name: "vsoePrice"
    type: "number, string"
    description: ""

  - name: "vsoeSopGroup"
    type: "varies"
    description: ""

  - name: "weight"
    type: "number, string"
    description: ""

  - name: "weightUnit"
    type: "varies"
    description: ""

  - name: "weightUnits"
    type: "string"
    description: ""

  - name: "wipAcct"
    type: "varies"
    description: ""

  - name: "wipVarianceAcct"
    type: "varies"
    description: ""
---