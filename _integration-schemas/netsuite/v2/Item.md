---
tap: "netsuite"
version: "2"
name: Item
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Item.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Item
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: intercoDefRevAccount
  type: varies
  description: ""
- name: distributionCategory
  type: varies
  description: ""
- name: supplyTimeFence
  type: string, integer
  description: ""
- name: description
  type: string
  description: ""
- name: hazmatItemUnitsQty
  type: string, number
  description: ""
- name: memberList
  type: varies
  description: ""
- name: relatedItemsDescription
  type: string
  description: ""
- name: nonPosting
  type: boolean, string
  description: ""
- name: quantityPricingSchedule
  type: varies
  description: ""
- name: vendor
  type: varies
  description: ""
- name: quantityCommitted
  type: string, number
  description: ""
- name: availableToPartners
  type: boolean, string
  description: ""
- name: mpn
  type: string
  description: ""
- name: autoPreferredStockLevel
  type: boolean, string
  description: ""
- name: trackLandedCost
  type: boolean, string
  description: ""
- name: pageTitle
  type: string
  description: ""
- name: preferredStockLevel
  type: string, number
  description: ""
- name: pricingMatrix
  type: varies
  description: ""
- name: stockUnit
  type: varies
  description: ""
- name: receiptAmount
  type: string, number
  description: ""
- name: department
  type: varies
  description: ""
- name: billingSchedule
  type: varies
  description: ""
- name: shipPackage
  type: varies
  description: ""
- name: dontShowPrice
  type: boolean, string
  description: ""
- name: searchKeywords
  type: string
  description: ""
- name: quantityAvailableUnits
  type: string
  description: ""
- name: intercoIncomeAccount
  type: varies
  description: ""
- name: gainLossAccount
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: intercoCogsAccount
  type: varies
  description: ""
- name: defaultReturnCost
  type: string, number
  description: ""
- name: isPreTax
  type: boolean, string
  description: ""
- name: isHazmatItem
  type: boolean, string
  description: ""
- name: costCategory
  type: varies
  description: ""
- name: matrixOptionList
  type: varies
  description: ""
- name: quantityAvailable
  type: string, number
  description: ""
- name: hazmatPackingGroup
  type: varies
  description: ""
- name: taxSchedule
  type: varies
  description: ""
- name: quantityOnHand
  type: string, number
  description: ""
- name: producer
  type: boolean, string
  description: ""
- name: manufacturingChargeItem
  type: boolean, string
  description: ""
- name: itemRevenueCategory
  type: varies
  description: ""
- name: copyDescription
  type: boolean, string
  description: ""
- name: vsoeDeferral
  type: varies
  description: ""
- name: minimumQuantityUnits
  type: string
  description: ""
- name: isPhantom
  type: boolean, string
  description: ""
- name: binNumberList
  type: varies
  description: ""
- name: featuredDescription
  type: string
  description: ""
- name: cogsAccount
  type: varies
  description: ""
- name: revenueAllocationGroup
  type: varies
  description: ""
- name: maximumQuantity
  type: string, integer
  description: ""
- name: numOfAllowedDownloads
  type: string, integer
  description: ""
- name: supplyLotSizingMethod
  type: varies
  description: ""
- name: accountingBookDetailList
  type: varies
  description: ""
- name: minimumQuantity
  type: string, integer
  description: ""
- name: parent
  type: varies
  description: ""
- name: weightUnit
  type: varies
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: seasonalDemand
  type: boolean, string
  description: ""
- name: matchBillToReceipt
  type: boolean, string
  description: ""
- name: preferredStockLevelDays
  type: string, number
  description: ""
- name: billExchRateVarianceAcct
  type: varies
  description: ""
- name: assetAccount
  type: varies
  description: ""
- name: costEstimateUnits
  type: string
  description: ""
- name: locationsList
  type: varies
  description: ""
- name: roundUpAsComponent
  type: boolean, string
  description: ""
- name: useMarginalRates
  type: boolean, string
  description: ""
- name: matrixItemNameTemplate
  type: string
  description: ""
- name: consumptionUnit
  type: string
  description: ""
- name: createJob
  type: boolean, string
  description: ""
- name: secondarySaleUnit
  type: string
  description: ""
- name: residual
  type: string
  description: ""
- name: metaTagHtml
  type: string
  description: ""
- name: intercoExpenseAccount
  type: varies
  description: ""
- name: isStorePickupAllowed
  type: boolean, string
  description: ""
- name: dateConvertedToInv
  type: string
  description: ""
- name: originalItemSubtype
  type: varies
  description: ""
- name: secondaryBaseUnit
  type: string
  description: ""
- name: issueProduct
  type: varies
  description: ""
- name: noPriceMessage
  type: string
  description: ""
- name: displayName
  type: string
  description: ""
- name: contingentRevenueHandling
  type: boolean, string
  description: ""
- name: stockDescription
  type: string
  description: ""
- name: storeDisplayName
  type: string
  description: ""
- name: purchaseOrderAmount
  type: string, number
  description: ""
- name: daysBeforeExpiration
  type: string, integer
  description: ""
- name: averageCost
  type: string, number
  description: ""
- name: costEstimateType
  type: varies
  description: ""
- name: wipVarianceAcct
  type: varies
  description: ""
- name: purchaseOrderQuantityDiff
  type: string, number
  description: ""
- name: vsoePermitDiscount
  type: varies
  description: ""
- name: wipAcct
  type: varies
  description: ""
- name: isGcoCompliant
  type: boolean, string
  description: ""
- name: includeStartEndLines
  type: boolean, string
  description: ""
- name: manufacturerState
  type: string
  description: ""
- name: pricesIncludeTax
  type: boolean, string
  description: ""
- name: quantityOnOrder
  type: string, number
  description: ""
- name: transferPrice
  type: string, number
  description: ""
- name: manufacturerCity
  type: string
  description: ""
- name: preferredStockLevelUnits
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: reorderPoint
  type: string, number
  description: ""
- name: manufacturerTariff
  type: string
  description: ""
- name: defaultItemShipMethod
  type: varies
  description: ""
- name: createRevenuePlansOn
  type: varies
  description: ""
- name: _type
  type: string
  description: ""
- name: isFulfillable
  type: boolean, string
  description: ""
- name: reorderPointUnits
  type: string
  description: ""
- name: distributionNetwork
  type: varies
  description: ""
- name: multManufactureAddr
  type: boolean, string
  description: ""
- name: safetyStockLevelUnits
  type: string
  description: ""
- name: scheduleBQuantity
  type: string, integer
  description: ""
- name: rescheduleInDays
  type: string, integer
  description: ""
- name: shipIndividually
  type: boolean, string
  description: ""
- name: isSpecialWorkOrderItem
  type: boolean, string
  description: ""
- name: quantityOnHandUnits
  type: string
  description: ""
- name: itemNumberOptionsList
  type: varies
  description: ""
- name: scrapAcct
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: softDescriptor
  type: varies
  description: ""
- name: fraudRisk
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: receiptQuantityDiff
  type: string, number
  description: ""
- name: costUnits
  type: string
  description: ""
- name: hazmatShippingName
  type: string
  description: ""
- name: revRecForecastRule
  type: varies
  description: ""
- name: lowerWarningLimit
  type: string, number
  description: ""
- name: useBins
  type: boolean, string
  description: ""
- name: manufactureraddr1
  type: string
  description: ""
- name: shoppingDotComCategory
  type: string
  description: ""
- name: costingMethod
  type: varies
  description: ""
- name: showDefaultDonationAmount
  type: boolean, string
  description: ""
- name: buildTimeLotSize
  type: string, number
  description: ""
- name: billQtyVarianceAcct
  type: varies
  description: ""
- name: urlComponent
  type: string
  description: ""
- name: shopzillaCategoryId
  type: string, integer
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: rate
  type: string, number
  description: ""
- name: nexTagCategory
  type: string
  description: ""
- name: isVsoeBundle
  type: boolean, string
  description: ""
- name: billOfMaterialsList
  type: varies
  description: ""
- name: authCodesList
  type: varies
  description: ""
- name: storeDisplayThumbnail
  type: varies
  description: ""
- name: vendorName
  type: string
  description: ""
- name: secondaryConsumptionUnit
  type: varies
  description: ""
- name: isDonationItem
  type: boolean, string
  description: ""
- name: immediateDownload
  type: boolean, string
  description: ""
- name: sitemapPriority
  type: varies
  description: ""
- name: conversionRate
  type: string, number
  description: ""
- name: offerSupport
  type: boolean, string
  description: ""
- name: autoReorderPoint
  type: boolean, string
  description: ""
- name: account
  type: varies
  description: ""
- name: purchaseUnit
  type: varies
  description: ""
- name: excludeFromSitemap
  type: boolean, string
  description: ""
- name: serialNumbers
  type: string
  description: ""
- name: deferredRevenueAccount
  type: varies
  description: ""
- name: paymentMethod
  type: varies
  description: ""
- name: planningItemCategory
  type: string
  description: ""
- name: secondaryStockUnit
  type: string
  description: ""
- name: purchaseOrderQuantity
  type: string, number
  description: ""
- name: purchasePriceVarianceAcct
  type: varies
  description: ""
- name: currency
  type: string
  description: ""
- name: preferredLocation
  type: varies
  description: ""
- name: manufacturerAddr1
  type: string
  description: ""
- name: shippingCost
  type: string, number
  description: ""
- name: alternateDemandSourceItem
  type: varies
  description: ""
- name: fixedLotSize
  type: string, number
  description: ""
- name: effectiveBomControl
  type: varies
  description: ""
- name: costingMethodDisplay
  type: string
  description: ""
- name: unbuildVarianceAccount
  type: varies
  description: ""
- name: presentationItemList
  type: varies
  description: ""
- name: safetyStockLevel
  type: string, number
  description: ""
- name: periodicLotSizeDays
  type: string, integer
  description: ""
- name: costEstimate
  type: string, number
  description: ""
- name: invtClassification
  type: varies
  description: ""
- name: prodQtyVarianceAcct
  type: varies
  description: ""
- name: isSpecialOrderItem
  type: boolean, string
  description: ""
- name: quantityCommittedUnits
  type: string
  description: ""
- name: supplyType
  type: varies
  description: ""
- name: pricingGroup
  type: varies
  description: ""
- name: weight
  type: string, number
  description: ""
- name: itemCarrier
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: billingRatesMatrix
  type: varies
  description: ""
- name: storeDetailedDescription
  type: string
  description: ""
- name: lastInvtCountDate
  type: string
  description: ""
- name: originalItemType
  type: varies
  description: ""
- name: itemShipMethodList
  type: varies
  description: ""
- name: lastPurchasePrice
  type: string, number
  description: ""
- name: countryOfManufacture
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: isDropShipItem
  type: boolean, string
  description: ""
- name: vsoeDelivered
  type: boolean, string
  description: ""
- name: numbersList
  type: varies
  description: ""
- name: buildTime
  type: string, number
  description: ""
- name: itemTaskTemplatesList
  type: varies
  description: ""
- name: reorderMultiple
  type: string, integer
  description: ""
- name: revenueRecognitionRule
  type: varies
  description: ""
- name: leadTime
  type: string, integer
  description: ""
- name: itemVendorList
  type: varies
  description: ""
- name: futureHorizon
  type: string, integer
  description: ""
- name: weightUnits
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: unitsType
  type: varies
  description: ""
- name: forwardConsumptionDays
  type: string, integer
  description: ""
- name: amortizationTemplate
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: storeItemTemplate
  type: varies
  description: ""
- name: secondaryPurchaseUnit
  type: string
  description: ""
- name: secondaryUnitsType
  type: string
  description: ""
- name: isTaxable
  type: boolean, string
  description: ""
- name: revRecSchedule
  type: varies
  description: ""
- name: vsoePrice
  type: string, number
  description: ""
- name: upperWarningLimit
  type: string, number
  description: ""
- name: demandTimeFence
  type: string, integer
  description: ""
- name: handlingCost
  type: string, number
  description: ""
- name: translationsList
  type: varies
  description: ""
- name: handlingCostUnits
  type: string
  description: ""
- name: prodPriceVarianceAcct
  type: varies
  description: ""
- name: salesDescription
  type: string
  description: ""
- name: enableCatchWeight
  type: boolean, string
  description: ""
- name: manufacturer
  type: string
  description: ""
- name: billPriceVarianceAcct
  type: varies
  description: ""
- name: outOfStockBehavior
  type: varies
  description: ""
- name: incomeAccount
  type: varies
  description: ""
- name: hazmatItemUnits
  type: string
  description: ""
- name: hazmatHazardClass
  type: string
  description: ""
- name: storeDescription
  type: string
  description: ""
- name: maxDonationAmount
  type: string, number
  description: ""
- name: scheduleBNumber
  type: string
  description: ""
- name: cost
  type: string, number
  description: ""
- name: createdDate
  type: string
  description: ""
- name: onSpecial
  type: boolean, string
  description: ""
- name: amortizationPeriod
  type: string, integer
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
- name: productFeedList
  type: varies
  description: ""
- name: hazmatId
  type: string
  description: ""
- name: safetyStockLevelDays
  type: string, integer
  description: ""
- name: rescheduleOutDays
  type: string, integer
  description: ""
- name: useComponentYield
  type: boolean, string
  description: ""
- name: manufacturerZip
  type: string
  description: ""
- name: quantityOnOrderUnits
  type: string
  description: ""
- name: outOfStockMessage
  type: string
  description: ""
- name: dropshipExpenseAccount
  type: varies
  description: ""
- name: undepFunds
  type: boolean, string
  description: ""
- name: purchaseDescription
  type: string
  description: ""
- name: manufacturerTaxId
  type: string
  description: ""
- name: quantityBackOrdered
  type: string, number
  description: ""
- name: revReclassFXAccount
  type: varies
  description: ""
- name: preferenceCriterion
  type: varies
  description: ""
- name: saleUnit
  type: varies
  description: ""
- name: periodicLotSizeType
  type: varies
  description: ""
- name: generateAccruals
  type: boolean, string
  description: ""
- name: backwardConsumptionDays
  type: string, integer
  description: ""
- name: totalValue
  type: string, number
  description: ""
- name: matrixType
  type: varies
  description: ""
- name: scheduleBCode
  type: varies
  description: ""
- name: salesTaxCode
  type: varies
  description: ""
- name: printItems
  type: boolean, string
  description: ""
- name: location
  type: varies
  description: ""
- name: liabilityAccount
  type: varies
  description: ""
- name: specialsDescription
  type: string
  description: ""
- name: fixedBuildTime
  type: string, number
  description: ""
- name: shippingCostUnits
  type: string
  description: ""
- name: itemOptionsList
  type: varies
  description: ""
- name: vsoeSopGroup
  type: varies
  description: ""
- name: nextInvtCountDate
  type: string
  description: ""
- name: directRevenuePosting
  type: boolean, string
  description: ""
- name: supplyReplenishmentMethod
  type: varies
  description: ""
- name: enforceMinQtyInternally
  type: boolean, string
  description: ""
- name: demandModifier
  type: string, number
  description: ""
- name: expenseAccount
  type: varies
  description: ""
- name: deferralAccount
  type: varies
  description: ""
- name: overallQuantityPricingType
  type: varies
  description: ""
- name: deferRevRec
  type: boolean, string
  description: ""
- name: invtCountInterval
  type: string, integer
  description: ""
- name: receiptQuantity
  type: string, number
  description: ""
- name: buildEntireAssembly
  type: boolean, string
  description: ""
- name: purchaseTaxCode
  type: varies
  description: ""
- name: demandSource
  type: varies
  description: ""
- name: defaultRevision
  type: string
  description: ""
- name: itemId
  type: string
  description: ""
- name: overheadType
  type: varies
  description: ""
- name: expirationDate
  type: string
  description: ""
- name: onHandValueMli
  type: string, number
  description: ""
- name: upcCode
  type: string
  description: ""
- name: autoLeadTime
  type: boolean, string
  description: ""
- name: storeDisplayImage
  type: varies
  description: ""
- name: siteCategoryList
  type: varies
  description: ""
- name: quantityReorderUnits
  type: string
  description: ""
---