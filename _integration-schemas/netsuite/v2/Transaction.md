---
tap: "netsuite"
version: "2"
name: Transaction
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Transaction.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Transaction
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: ancillaryEndorsementFedEx
  type: varies
  description: ""
- name: shipIsResidential
  type: boolean, string
  description: ""
- name: halAddr1FedEx
  type: string
  description: ""
- name: ccSecurityCodeMatch
  type: varies
  description: ""
- name: refundCheck
  type: boolean, string
  description: ""
- name: ccZipCode
  type: string
  description: ""
- name: termsOfSaleFedEx
  type: varies
  description: ""
- name: shippingTax1Rate
  type: string, number
  description: ""
- name: amountPaid
  type: string, number
  description: ""
- name: leadSource
  type: varies
  description: ""
- name: saturdayDeliveryFedEx
  type: boolean, string
  description: ""
- name: amount
  type: string, number
  description: ""
- name: halPhoneFedEx
  type: string
  description: ""
- name: billAddressList
  type: varies
  description: ""
- name: userTaxTotal
  type: string, number
  description: ""
- name: inboundShipment
  type: varies
  description: ""
- name: shipGroupList
  type: varies
  description: ""
- name: companyContributionList
  type: varies
  description: ""
- name: shipComplete
  type: boolean, string
  description: ""
- name: checkNum
  type: string
  description: ""
- name: apAcct
  type: varies
  description: ""
- name: estGrossProfit
  type: string, number
  description: ""
- name: messageSel
  type: varies
  description: ""
- name: shippingTax2Rate
  type: string, number
  description: ""
- name: advance
  type: string, number
  description: ""
- name: sendShipNotifyEmailUps
  type: boolean, string
  description: ""
- name: excludeCommission
  type: boolean, string
  description: ""
- name: ccSecurityCode
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: endOperation
  type: varies
  description: ""
- name: thirdPartyTypeFedEx
  type: varies
  description: ""
- name: supervisorApproval
  type: boolean, string
  description: ""
- name: billingSchedule
  type: varies
  description: ""
- name: halStateFedEx
  type: string
  description: ""
- name: giftCertAvailable
  type: string, number
  description: ""
- name: ccIsPurchaseCardBin
  type: boolean, string
  description: ""
- name: termsFreightChargeFedEx
  type: string, number
  description: ""
- name: validFrom
  type: string
  description: ""
- name: backupEmailAddressUps
  type: string
  description: ""
- name: fax
  type: string
  description: ""
- name: blanketEndDateUps
  type: string
  description: ""
- name: email
  type: string
  description: ""
- name: sourceTransactionLine
  type: string, integer
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: syncPartnerTeams
  type: boolean, string
  description: ""
- name: accountingBook
  type: varies
  description: ""
- name: paymentProcessingProfile
  type: varies
  description: ""
- name: paymentEventDate
  type: string
  description: ""
- name: pnRefNum
  type: string
  description: ""
- name: useItemCostAsTransferCost
  type: boolean, string
  description: ""
- name: insideDeliveryFedEx
  type: boolean, string
  description: ""
- name: homeDeliveryDateFedEx
  type: string
  description: ""
- name: drAccount
  type: varies
  description: ""
- name: nexus
  type: varies
  description: ""
- name: estimatedTotalValue
  type: string, number
  description: ""
- name: payPalProcess
  type: boolean, string
  description: ""
- name: ccProcessAsPurchaseCard
  type: boolean, string
  description: ""
- name: nextBill
  type: string
  description: ""
- name: outputReferenceCode
  type: string
  description: ""
- name: payeeAddress
  type: varies
  description: ""
- name: companyTaxList
  type: varies
  description: ""
- name: holdAtLocationFedEx
  type: boolean, string
  description: ""
- name: payeeAddressList
  type: varies
  description: ""
- name: blanketStartDateUps
  type: string
  description: ""
- name: adjLocation
  type: varies
  description: ""
- name: shipAddress
  type: string
  description: ""
- name: billingAccount
  type: varies
  description: ""
- name: isBackflush
  type: boolean, string
  description: ""
- name: firmed
  type: boolean, string
  description: ""
- name: nextApprover
  type: varies
  description: ""
- name: tax2Amt
  type: string, number
  description: ""
- name: eccNumberUps
  type: string
  description: ""
- name: applied
  type: string, number
  description: ""
- name: depositList
  type: varies
  description: ""
- name: postingPeriod
  type: varies
  description: ""
- name: promotionsList
  type: varies
  description: ""
- name: billOfMaterialsRevision
  type: varies
  description: ""
- name: itemCostDiscRate
  type: string
  description: ""
- name: saveOnAuthDecline
  type: boolean, string
  description: ""
- name: itemCostDiscount
  type: varies
  description: ""
- name: accountingBookDetailList
  type: varies
  description: ""
- name: salesRep
  type: varies
  description: ""
- name: recurAnnually
  type: string, number
  description: ""
- name: assemblyItem
  type: varies
  description: ""
- name: creditList
  type: varies
  description: ""
- name: depDate
  type: string
  description: ""
- name: discountDate
  type: string
  description: ""
- name: deferredRevenue
  type: string, number
  description: ""
- name: reversalDate
  type: string
  description: ""
- name: partiesToTransactionUps
  type: boolean, string
  description: ""
- name: revision
  type: varies
  description: ""
- name: bookingConfirmationNumFedEx
  type: string
  description: ""
- name: terms
  type: varies
  description: ""
- name: revRecOnRevCommitment
  type: boolean, string
  description: ""
- name: reversalDefer
  type: boolean, string
  description: ""
- name: deductionList
  type: varies
  description: ""
- name: fob
  type: string
  description: ""
- name: partner
  type: varies
  description: ""
- name: timeList
  type: varies
  description: ""
- name: tax2Total
  type: string, number
  description: ""
- name: thirdPartyAcctFedEx
  type: string
  description: ""
- name: altShippingCost
  type: string, number
  description: ""
- name: entryNumberUps
  type: string
  description: ""
- name: halZipFedEx
  type: string
  description: ""
- name: actualProductionStartDate
  type: string
  description: ""
- name: shipDateFedEx
  type: string
  description: ""
- name: discountTotal
  type: string, number
  description: ""
- name: packageUspsList
  type: varies
  description: ""
- name: itemCostTaxRate1
  type: string, number
  description: ""
- name: thirdPartyAcctUps
  type: string
  description: ""
- name: handlingTax2Rate
  type: string, number
  description: ""
- name: payment
  type: string, number
  description: ""
- name: shipNotifyEmailAddressFedEx
  type: string
  description: ""
- name: isBookSpecific
  type: boolean, string
  description: ""
- name: exchangeRate
  type: string, number
  description: ""
- name: includeInForecast
  type: boolean, string
  description: ""
- name: giftCertApplied
  type: string, number
  description: ""
- name: ccAvsStreetMatch
  type: varies
  description: ""
- name: itemCostDiscTax1Amt
  type: string, number
  description: ""
- name: paymentEventUpdatedBy
  type: string
  description: ""
- name: shipmentWeightUps
  type: string, number
  description: ""
- name: payPalTranId
  type: string
  description: ""
- name: earningList
  type: varies
  description: ""
- name: outputAuthCode
  type: string
  description: ""
- name: pending
  type: string, number
  description: ""
- name: isCargoAircraftOnlyFedEx
  type: boolean, string
  description: ""
- name: tranType
  type: string
  description: ""
- name: giftCertRedemptionList
  type: varies
  description: ""
- name: built
  type: string, number
  description: ""
- name: schedulingMethod
  type: varies
  description: ""
- name: creditCardProcessor
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: recurMonthly
  type: string, number
  description: ""
- name: handlingMode
  type: varies
  description: ""
- name: expCostDiscAmount
  type: string, number
  description: ""
- name: tax1Amt
  type: string, number
  description: ""
- name: item
  type: varies
  description: ""
- name: vsoeAutoCalc
  type: boolean, string
  description: ""
- name: ccStreet
  type: string
  description: ""
- name: timeDiscTaxable
  type: boolean, string
  description: ""
- name: arAcct
  type: varies
  description: ""
- name: overrideInstallments
  type: boolean, string
  description: ""
- name: tranStatus
  type: string
  description: ""
- name: _type
  type: string
  description: ""
- name: shipNotifyEmailMessageUps
  type: string
  description: ""
- name: expenseList
  type: varies
  description: ""
- name: handlingTax1Rate
  type: string, number
  description: ""
- name: paymentEventResult
  type: varies
  description: ""
- name: landedCostsList
  type: varies
  description: ""
- name: timeTaxRate2
  type: string, number
  description: ""
- name: packageUpsList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: recurringBill
  type: boolean, string
  description: ""
- name: hazmatTypeFedEx
  type: varies
  description: ""
- name: subTotal
  type: string, number
  description: ""
- name: paymentHold
  type: boolean, string
  description: ""
- name: ignoreAvs
  type: boolean, string
  description: ""
- name: pickedDate
  type: string
  description: ""
- name: expCostDiscTax1Amt
  type: string, number
  description: ""
- name: timeDiscTax1Amt
  type: string, number
  description: ""
- name: revenueStatus
  type: varies
  description: ""
- name: itemList
  type: varies
  description: ""
- name: creditLimit
  type: string, number
  description: ""
- name: itemCostDiscPrint
  type: boolean, string
  description: ""
- name: manufacturingRouting
  type: varies
  description: ""
- name: paypalAuthId
  type: string
  description: ""
- name: checkNumber
  type: string
  description: ""
- name: toPrint2
  type: boolean, string
  description: ""
- name: approved
  type: boolean, string
  description: ""
- name: generateIntegratedShipperLabel
  type: boolean, string
  description: ""
- name: incoterm
  type: varies
  description: ""
- name: orderStatus
  type: varies
  description: ""
- name: expectedCloseDate
  type: string
  description: ""
- name: signatureHomeDeliveryFedEx
  type: boolean, string
  description: ""
- name: paymentCardCsc
  type: string
  description: ""
- name: sourceTransactionId
  type: string
  description: ""
- name: amountRemaining
  type: string, number
  description: ""
- name: taxRate
  type: string, number
  description: ""
- name: timeDiscount
  type: varies
  description: ""
- name: softDescriptor
  type: string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: partnersList
  type: varies
  description: ""
- name: thirdPartyTypeUps
  type: varies
  description: ""
- name: actualProductionEndDate
  type: string
  description: ""
- name: toSubsidiary
  type: varies
  description: ""
- name: chargeIt
  type: boolean, string
  description: ""
- name: componentList
  type: varies
  description: ""
- name: inbondCodeUps
  type: string
  description: ""
- name: altHandlingCost
  type: string, number
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: canHaveStackable
  type: boolean, string
  description: ""
- name: methodOfTransportUps
  type: varies
  description: ""
- name: requestedBy
  type: varies
  description: ""
- name: payPalAuthId
  type: string
  description: ""
- name: userTotal
  type: string, number
  description: ""
- name: shipmentWeightFedEx
  type: string, number
  description: ""
- name: source
  type: string
  description: ""
- name: expCostTaxRate2
  type: string, number
  description: ""
- name: autoApply
  type: boolean, string
  description: ""
- name: entityTaxRegNum
  type: varies
  description: ""
- name: taxDetailsOverride
  type: boolean, string
  description: ""
- name: salesOrderRequiredDepositDue
  type: string, number
  description: ""
- name: licenseExceptionUps
  type: varies
  description: ""
- name: probability
  type: string, number
  description: ""
- name: shippingTaxCode
  type: varies
  description: ""
- name: itemCostTaxRate2
  type: string, number
  description: ""
- name: unapplied
  type: string, number
  description: ""
- name: expCostDiscPrint
  type: boolean, string
  description: ""
- name: employeeTaxList
  type: varies
  description: ""
- name: actualShipDate
  type: string
  description: ""
- name: itemCostTaxCode
  type: varies
  description: ""
- name: createdFromShipGroup
  type: string, integer
  description: ""
- name: paypalProcess
  type: boolean, string
  description: ""
- name: vatRegNum
  type: string
  description: ""
- name: debitCardIssueNo
  type: string
  description: ""
- name: trackingNumbers
  type: string
  description: ""
- name: employee
  type: varies
  description: ""
- name: revRecEndDate
  type: string
  description: ""
- name: isMultiShipTo
  type: boolean, string
  description: ""
- name: landedCostPerLine
  type: boolean, string
  description: ""
- name: title
  type: string
  description: ""
- name: customer
  type: varies
  description: ""
- name: account
  type: varies
  description: ""
- name: sendBackupEmailUps
  type: boolean, string
  description: ""
- name: thirdPartyCountryUps
  type: varies
  description: ""
- name: accountingApproval
  type: boolean, string
  description: ""
- name: serialNumbers
  type: string
  description: ""
- name: opportunity
  type: varies
  description: ""
- name: carrierIdUps
  type: string
  description: ""
- name: giftCertTotal
  type: string, number
  description: ""
- name: toBePrinted
  type: boolean, string
  description: ""
- name: toBeEmailed
  type: boolean, string
  description: ""
- name: paymentMethod
  type: varies
  description: ""
- name: linkedTrackingNumbers
  type: string
  description: ""
- name: thirdPartyCountryFedEx
  type: varies
  description: ""
- name: ccAvsZipMatch
  type: varies
  description: ""
- name: approvalStatus
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: inventoryValue
  type: string, number
  description: ""
- name: landedCostMethod
  type: varies
  description: ""
- name: paymentOption
  type: string
  description: ""
- name: timeDiscRate
  type: string
  description: ""
- name: estGrossProfitPercent
  type: string, number
  description: ""
- name: printVoucher
  type: boolean, string
  description: ""
- name: timeTaxRate1
  type: string, number
  description: ""
- name: isRecurringPayment
  type: boolean, string
  description: ""
- name: taxPointDate
  type: string
  description: ""
- name: specialOrder
  type: boolean, string
  description: ""
- name: shippingCost
  type: string, number
  description: ""
- name: dynamicDescriptor
  type: string
  description: ""
- name: intlExemptionNumFedEx
  type: string
  description: ""
- name: totalCostEstimate
  type: string, number
  description: ""
- name: endDate
  type: string
  description: ""
- name: autoCalculateLag
  type: boolean, string
  description: ""
- name: balance
  type: string, number
  description: ""
- name: itemFulfillment
  type: varies
  description: ""
- name: total
  type: string, number
  description: ""
- name: onCreditHold
  type: string
  description: ""
- name: binNumbers
  type: string
  description: ""
- name: fxAccount
  type: varies
  description: ""
- name: saturdayDeliveryUps
  type: boolean, string
  description: ""
- name: getAuth
  type: boolean, string
  description: ""
- name: shipTo
  type: varies
  description: ""
- name: otherList
  type: varies
  description: ""
- name: altSalesTotal
  type: string, number
  description: ""
- name: paymentEventType
  type: varies
  description: ""
- name: inputReferenceCode
  type: string
  description: ""
- name: packageList
  type: varies
  description: ""
- name: isInTransitPayment
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: subsidiaryTaxRegNum
  type: varies
  description: ""
- name: handlingTaxCode
  type: varies
  description: ""
- name: taxRegOverride
  type: boolean, string
  description: ""
- name: status
  type: string
  description: ""
- name: inventoryList
  type: varies
  description: ""
- name: toBeFaxed
  type: boolean, string
  description: ""
- name: paymentOperation
  type: varies
  description: ""
- name: paymentList
  type: varies
  description: ""
- name: salesGroup
  type: varies
  description: ""
- name: timeDiscAmount
  type: string, number
  description: ""
- name: itemCostDiscAmount
  type: string, number
  description: ""
- name: backupEmailAddressFedEx
  type: string
  description: ""
- name: b13AStatementDataFedEx
  type: string
  description: ""
- name: isWip
  type: boolean, string
  description: ""
- name: visibleToCustomer
  type: boolean, string
  description: ""
- name: policyViolated
  type: boolean, string
  description: ""
- name: halAddr2FedEx
  type: string
  description: ""
- name: unApplied
  type: string, number
  description: ""
- name: customForm
  type: varies
  description: ""
- name: licenseDateUps
  type: string
  description: ""
- name: billPay
  type: boolean, string
  description: ""
- name: dueDate
  type: string
  description: ""
- name: purchaseContract
  type: varies
  description: ""
- name: timeDiscPrint
  type: boolean, string
  description: ""
- name: orderQuantity
  type: string, number
  description: ""
- name: intercoStatus
  type: varies
  description: ""
- name: costComponentList
  type: varies
  description: ""
- name: useMultiCurrency
  type: boolean, string
  description: ""
- name: giftCert
  type: varies
  description: ""
- name: completedQuantity
  type: string, number
  description: ""
- name: isRoutedExportTransactionUps
  type: boolean, string
  description: ""
- name: halCountryFedEx
  type: string
  description: ""
- name: deposit
  type: varies
  description: ""
- name: intercoTransaction
  type: varies
  description: ""
- name: recipientTaxIdUps
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: unitsType
  type: varies
  description: ""
- name: paymentEventHoldReason
  type: varies
  description: ""
- name: exportTypeUps
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: revCommitStatus
  type: varies
  description: ""
- name: halAddr3FedEx
  type: string
  description: ""
- name: salesTeamList
  type: varies
  description: ""
- name: itemCostDiscTaxable
  type: boolean, string
  description: ""
- name: isTaxable
  type: boolean, string
  description: ""
- name: revRecSchedule
  type: varies
  description: ""
- name: licenseNumberUps
  type: string
  description: ""
- name: discountAmount
  type: string, number
  description: ""
- name: shipDate
  type: string
  description: ""
- name: timeTaxCode
  type: varies
  description: ""
- name: threeDStatusCode
  type: string
  description: ""
- name: handlingCost
  type: string, number
  description: ""
- name: payPalStatus
  type: string
  description: ""
- name: expCostDiscprint
  type: boolean, string
  description: ""
- name: tranIsVsoeBundle
  type: boolean, string
  description: ""
- name: creditCard
  type: varies
  description: ""
- name: expCostTaxCode
  type: varies
  description: ""
- name: reversalEntry
  type: string
  description: ""
- name: accessibilityTypeFedEx
  type: varies
  description: ""
- name: shipNotifyEmailAddressUps
  type: string
  description: ""
- name: shipStatus
  type: varies
  description: ""
- name: scrapQuantity
  type: string, number
  description: ""
- name: expenseReportExchangeRate
  type: string, number
  description: ""
- name: packageFedExList
  type: varies
  description: ""
- name: expandAssembly
  type: boolean, string
  description: ""
- name: expenseReportCurrency
  type: varies
  description: ""
- name: expCostDiscRate
  type: string
  description: ""
- name: promoCode
  type: varies
  description: ""
- name: applyList
  type: varies
  description: ""
- name: complete
  type: boolean, string
  description: ""
- name: b13AFilingOptionFedEx
  type: varies
  description: ""
- name: expCostTaxRate1
  type: string, number
  description: ""
- name: units
  type: varies
  description: ""
- name: salesOrder
  type: varies
  description: ""
- name: options
  type: varies
  description: ""
- name: acctCorpCardExp
  type: varies
  description: ""
- name: recurQuarterly
  type: string, number
  description: ""
- name: billOfMaterials
  type: varies
  description: ""
- name: installmentList
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: recognizedRevenue
  type: string, number
  description: ""
- name: transactionNumber
  type: string
  description: ""
- name: inputAuthCode
  type: string
  description: ""
- name: requestedDate
  type: string
  description: ""
- name: unitCost
  type: string, number
  description: ""
- name: thirdPartyZipcodeUps
  type: string
  description: ""
- name: tranDate
  type: string
  description: ""
- name: syncSalesTeams
  type: boolean, string
  description: ""
- name: lineList
  type: varies
  description: ""
- name: undepFunds
  type: boolean, string
  description: ""
- name: quantity
  type: string, number
  description: ""
- name: voidJournal
  type: varies
  description: ""
- name: saturdayPickupFedex
  type: boolean, string
  description: ""
- name: shipNotifyEmailAddress2Ups
  type: string
  description: ""
- name: tranId
  type: string
  description: ""
- name: toAch
  type: boolean, string
  description: ""
- name: discountRate
  type: string
  description: ""
- name: operationList
  type: varies
  description: ""
- name: availableVendorCredit
  type: string, number
  description: ""
- name: oneTime
  type: string, number
  description: ""
- name: cashBackList
  type: varies
  description: ""
- name: taxDetailsList
  type: varies
  description: ""
- name: transferLocation
  type: varies
  description: ""
- name: authCode
  type: string
  description: ""
- name: halCityFedEx
  type: string
  description: ""
- name: inventoryDetail
  type: varies
  description: ""
- name: ccApproved
  type: boolean, string
  description: ""
- name: itemCostList
  type: varies
  description: ""
- name: availableBalance
  type: string, number
  description: ""
- name: shippingAddress
  type: varies
  description: ""
- name: shipAddressList
  type: varies
  description: ""
- name: salesEffectiveDate
  type: string
  description: ""
- name: createdFrom
  type: varies
  description: ""
- name: expCostList
  type: varies
  description: ""
- name: contribPct
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: entity
  type: varies
  description: ""
- name: parentExpenseAlloc
  type: varies
  description: ""
- name: forecastType
  type: varies
  description: ""
- name: currencyName
  type: string
  description: ""
- name: revRecStartDate
  type: string
  description: ""
- name: ccExpireDate
  type: string
  description: ""
- name: taxTotal
  type: string, number
  description: ""
- name: recurWeekly
  type: string, number
  description: ""
- name: buildable
  type: string, number
  description: ""
- name: expCostDiscTaxable
  type: boolean, string
  description: ""
- name: ccNumber
  type: string
  description: ""
- name: memo
  type: string
  description: ""
- name: ccName
  type: string
  description: ""
- name: shippedDate
  type: string
  description: ""
- name: sendBackupEmailFedEx
  type: boolean, string
  description: ""
- name: discountItem
  type: varies
  description: ""
- name: purchaseOrderList
  type: varies
  description: ""
- name: termsInsuranceChargeFedEx
  type: string, number
  description: ""
- name: shipMethod
  type: varies
  description: ""
- name: otherRefNum
  type: string
  description: ""
- name: billingAddress
  type: varies
  description: ""
- name: startOperation
  type: varies
  description: ""
- name: expirationDate
  type: string
  description: ""
- name: entityStatus
  type: varies
  description: ""
- name: shopperIpAddress
  type: string
  description: ""
- name: message
  type: string
  description: ""
- name: sendShipNotifyEmailFedEx
  type: boolean, string
  description: ""
- name: insidePickupFedEx
  type: boolean, string
  description: ""
- name: packedDate
  type: string
  description: ""
- name: homeDeliveryTypeFedEx
  type: varies
  description: ""
- name: taxItem
  type: varies
  description: ""
- name: job
  type: varies
  description: ""
- name: expCostDiscount
  type: varies
  description: ""
