---
title: Zuora
permalink: /integrations/saas/zuora
tags: [saas_integrations]
keywords: zuora, integration, schema, etl zuora, zuora etl, zuora schema
summary: "Connection instructions and schema details for Stitch's Zuora integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zuora"
display_name: "Zuora"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://trust.zuora.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/zuora.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Account
  - name: "zuora_account"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Account_Data_Source
    description: "customer account info."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Account ID (<code>id</code>)
      - name: autopay
      - name: invoicedeliveryprefsemail
      - name: balance
      - name: crmid
      - name: billcycleday
      - name: defaultpaymentmethodid
      - name: invoicetemplateid
      - name: communicationprofileid
      - name: accountnumber
      - name: paymentterm
      - name: purchaseordernumber
      - name: status
      - name: createdbyid
      - name: invoicedeliveryprefsprint
      - name: bcdsettingoption
      - name: updatedbyid
      - name: batch
      - name: creditbalance
      - name: billtoid
      - name: soldtoid
      - name: allowinvoiceedit
      - name: createddate
      - name: updateddate
      - name: customerservicerepname
      - name: lastinvoicedate
      - name: currency
      - name: name
      - name: totalinvoicebalance
      - name: notes
      - name: salesrepname
      - name: parentid

## Accounting Code
  - name: "zuora_accounting_code"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Accounting_Code_Data_Source
    description: "info relevant to the various accounting codes used in Zuora."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Accounting Code ID (<code>id</code>)
      - name: category
      - name: createdbyid
      - name: createddate
      - name: glaccountname
      - name: glaccountnumber
      - name: name
      - name: status
      - name: type
      - name: updatedbyid
      - name: updateddate

## Accounting Period
  - name: "zuora_accounting_period"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/AccountingPeriod#Field_Descriptions
    description: "info about accounting periods."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Accounting Period ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: enddate
      - name: fiscalquarter
      - name: fiscalyear
      - name: name
      - name: notes
      - name: startdate
      - name: status
      - name: updatedbyid
      - name: updateddate

## Amendment
  - name: "zuora_amendment"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Amendment#Field_Descriptions
    description: "info about amendments, or changes to customer subscriptions."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Amendment ID (<code>id</code>)
      - name: autorenew
      - name: code
      - name: contracteffectivedate
      - name: createdbyid
      - name: createddate
      - name: currentterm
      - name: currenttermperiodtype
      - name: customeracceptancedate
      - name: description
      - name: destinationaccountid
      - name: destinationinvoiceonwerid
      - name: effectivedate
      - name: name
      - name: rateplandata
      - name: renewalsetting
      - name: renewalterm
      - name: renewaltermperiodtype
      - name: serviceactivationdate
      - name: specificupdatedate
      - name: status
      - name: subscriptionid
      - name: termstartdate
      - name: termtype
      - name: type
      - name: updatedbyid
      - name: updateddate

## Billing Run
  - name: "zuora_billing_run"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/BillRun#Field_Descriptions
    description: "info about ad hoc billing runs."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Billing Run ID (<code>id</code>)
      - name: accountid
      - name: autoemail
      - name: autopost
      - name: autorenewal
      - name: batch
      - name: billcycleday
      - name: billrunnumber
      - name: chargetypetoexclude
      - name: errormessage
      - name: executeddate
      - name: invoicedate
      - name: invoicesemailed
      - name: lastemailsenttime
      - name: noemailforzeroamountinvoice
      - name: numberofaccounts
      - name: numberofinvoices
      - name: status
      - name: targetdate
      - name: createdbyid
      - name: createddate
      - name: updatedbyid
      - name: updateddate

## Communication Profile
  - name: "zuora_communication_profile"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Communication_Profile#Field_Descriptions
    description: "info about communication profiles. Communication Profiles are sets of policies that determine how to communicate with the contacts associated with an account."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Communication Profile ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: description
      - name: profilename
      - name: updatedbyid
      - name: updateddate

## Contact
  - name: "zuora_contact"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Contact_Data_Source
    description: "info about an account's point-of-contact."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Contact ID (<code>id</code>)
      - name: accountid
      - name: address1
      - name: address2
      - name: city
      - name: country
      - name: createdbyid
      - name: createddate
      - name: firstname
      - name: lastname
      - name: mobiilephone
      - name: nickname
      - name: otherphonetype
      - name: postalcode
      - name: state
      - name: workemail
      - name: workphone
      - name: updatedbyid
      - name: updateddate

## Credit Balance Adjustment
  - name: "zuora_credit_balance_adjustment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Credit_Balance_Adjustment_Data_Source
    description: "info about changes to customers' credit balances."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Credit Balance Adjustment ID (<code>id</code>)
      - name: accountid
      - name: accountingcode
      - name: adjustmentdate
      - name: amount
      - name: comment
      - name: createdbyid
      - name: createddate
      - name: number
      - name: reasoncode
      - name: referenceid
      - name: sourcetransactionid
      - name: sourcetransactionnumber
      - name: sourcetransactiontype
      - name: status
      - name: type
      - name: updatedbyid
      - name: updateddate

## Export 
  - name: "zuora_export"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Export
    description: "info about export items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Export ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: encrypted
      - name: fileid
      - name: format
      - name: name
      - name: query
      - name: size
      - name: status
      - name: zip
      - name: updatedbyid
      - name: updateddate

## Import 
  - name: "zuora_import"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Import
    description: "info about import functions."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Import ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: importedcount
      - name: importtype
      - name: name
      - name: originalresourceurl
      - name: resultresourceurl
      - name: status
      - name: statusreason
      - name: totalcount
      - name: updatedbyid
      - name: updateddate

## Invoice 
  - name: "zuora_invoice"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Invoice#Field_Descriptions
    description: "info about invoices."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice ID (<code>id</code>)
      - name: accountid
      - name: adjustmentamount
      - name: amount
      - name: balance
      - name: createdbyid
      - name: createddate
      - name: creditbalanceadjustmentamount
      - name: duedate
      - name: includesometime
      - name: includesrecurring
      - name: includesusage
      - name: invoicedate
      - name: invoicenumber
      - name: lastemailssentdate
      - name: paymentamount
      - name: postedby
      - name: posteddate
      - name: refundamount
      - name: status
      - name: targetdate
      - name: updatedbyid
      - name: updateddate

## Invoice Adjustment
  - name: "zuora_invoice_adjustment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Invoice_Adjustment_Data_Source
    description: "info about invoice adjustments, or changes to an existing invoice."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Adjustment ID (<code>id</code>)
      - name: accountid
      - name: accountingperiod
      - name: accountsreceivableaccountingcode
      - name: billtocontact
      - name: createdbyid
      - name: createddate
      - name: defaultpaymentmethod
      - name: deferredrevenueaccountingcode
      - name: entity
      - name: invoiceid
      - name: soldtocontact
      - name: updatedbyid
      - name: updateddate

## Invoice File
  - name: "zuora_invoice_file"
    doc-link: 
    description: "info about invoice files. These are the generated PDF versions of invoices, hosted on Zuora."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice File ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: invoiceid
      - name: pdffileurl
      - name: versionnumber
      - name: updatedbyid
      - name: updateddate

## Invoice Item
  - name: "zuora_invoice_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Invoice_Item_Data_Source
    description: "info about the line items in invoices."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Item ID (<code>id</code>)
      - name: accountid
      - name: accountingperiod
      - name: chargedate
      - name: chargedescription
      - name: chargeid
      - name: chargename
      - name: chargenumber
      - name: chargetype
      - name: createdbyid
      - name: createddate
      - name: invoiceid
      - name: processingtype
      - name: productid
      - name: productname
      - name: quantity
      - name: rateplanchargeid
      - name: serviceenddate
      - name: servicestartdate
      - name: sku
      - name: subscriptionid
      - name: subscriptionnumber
      - name: unitprice
      - name: uom
      - name: updatedbyid
      - name: updateddate

## Invoice Item Adjustment
  - name: "zuora_invoice_item_adjustment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Invoice_Item_Adjustment_Data_Source
    description: "info about adjustments made to invoice items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Item Adjustment ID (<code>id</code>)
      - name: accountid
      - name: accountingperiod
      - name: accountsreceivableaccountingcode
      - name: adjustmentdate
      - name: adjustmentnumber
      - name: amount
      - name: amendment
      - name: cancelleddate
      - name: comment
      - name: createdbyid
      - name: createddate
      - name: invoiceid
      - name: invoiceitemname
      - name: invoicenumber
      - name: reasoncode
      - name: referenceid
      - name: serviceenddate
      - name: servicestartdtae
      - name: sourceid
      - name: sourcetype
      - name: status
      - name: type
      - name: updatedbyid
      - name: updateddate

## Invoice Payment 
  - name: "zuora_invoice_payment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Invoice_Payment_Data_Source
    description: "info about payments applied to invoices."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Payment ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: invoiceid
      - name: paymentid
      - name: refundamount
      - name: updatedbyid
      - name: updateddate

## Invoice Split
  - name: "zuora_invoice_split"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/InvoiceSplit#Field_Descriptions
    description: "info about 'split' invoices, or one of several invoices that once made up a single invoice."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Split ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: invoiceid
      - name: updatedbyid
      - name: updateddate

## Invoice Split Item
  - name: "zuora_invoice_split_item"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/InvoiceSplitItem#Field_Descriptions
    description: "info about the line items contained in split invoices."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Split Item ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: invoicedate
      - name: invoiceid
      - name: invoicesplititd
      - name: paymentterm
      - name: splitpercentage
      - name: updatedbyid
      - name: updateddate

## Journal Entry Item
  - name: "zuora_journal_entry_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Journal_Entry_Item_Data_Source
    description: "info about journal entries."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Journal Entry ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: type
      - name: updatedbyid
      - name: updateddate

## Payment
  - name: "zuora_payment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Payment_Data_Source
    description: "info about customer payments."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Payment ID (<code>id</code>)
      - name: accountid
      - name: accountingcode
      - name: amount
      - name: appliedcreditbalanceamount
      - name: bankidentifcationnumber
      - name: cancelledon
      - name: comment
      - name: createdbyid
      - name: createddate
      - name: effectivedate
      - name: gateway
      - name: gatewayresponse
      - name: gatewayresponsecode
      - name: gatewaystate
      - name: paymentmethodid
      - name: paymentmethodsnapshotid
      - name: paymentnumber
      - name: referenceid
      - name: refundamount
      - name: source
      - name: sourcename
      - name: status
      - name: submittedon
      - name: type
      - name: updatedbyid
      - name: updateddate

## Payment Method
  - name: "zuora_payment_method"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Payment_Method_Data_Source
    description: "info about payment methods, or the ways customers pay for their subscriptions."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Payment Method ID (<code>id</code>)
      - name: accountid
      - name: achaddress1
      - name: achadress2
      - name: active
      - name: bankidentificationnumber
      - name: createdbyid
      - name: createddate
      - name: creditcardaddress1
      - name: creditcardaddress2
      - name: creditcardcity
      - name: creditcardcountry
      - name: creditcardexpirationmonth
      - name: creditcardexpirationyear
      - name: creditcardholdername
      - name: creditcardmasknumber
      - name: creditcardpostalcode
      - name: creditcardstate
      - name: creditcardtype
      - name: email
      - name: lastfailedsaletransactiondate
      - name: lasttransactiondatetime
      - name: lasttransactionstatus
      - name: name
      - name: numconsecutivefailures
      - name: paymentmethodstatus
      - name: phone
      - name: totalnumberoferrorpayments
      - name: totalnumberofprocessedpayments
      - name: type
      - name: useddefaultentryrule
      - name: updatedbyid
      - name: updateddate

## Payment Method Snapshot
  - name: "zuora_payment_method_snapshot"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Payment_Method_Snapshot_ID#Field_Descriptions
    description: "snapshot info about payment methods."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Payment Method Snapshot ID (<code>id</code>)
      - name: accountid
      - name: bankidentificationnumber
      - name: createdbyid
      - name: createddate
      - name: creditcardaddress1
      - name: creditcardaddress2
      - name: creditcardcity
      - name: creditcardcountry
      - name: creditcardexpirationmonth
      - name: creditcardexpirationyear
      - name: creditcardholdername
      - name: creditcardmasknumber
      - name: creditcardpostalcode
      - name: creditcardstate
      - name: creditcardtype
      - name: email
      - name: lastfailedsaletransactiondate
      - name: lasttransactiondatetime
      - name: lasttransactionstatus
      - name: name
      - name: numconsecutivefailures
      - name: paymentmethodstatus
      - name: phone
      - name: totalnumberoferrorpayments
      - name: totalnumberofprocessedpayments
      - name: type
      - name: useddefaultentryrule
      - name: updatedbyid
      - name: updatedon

## Payment Transaction Log
  - name: "zuora_payment_transaction_log"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Payment_Transaction_Log_Data_Source
    description: "info about transaction logs sent from Zuora to the gateway for payment."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Payment Transaction Log ID (<code>id</code>)
      - name: gateway
      - name: gatewayreasoncode
      - name: gatewayreasoncodedescription
      - name: gatewaytransactiontype
      - name: paymentmethodid
      - name: paymentmethodtype
      - name: requeststring
      - name: responsestring
      - name: transactiondate
      - name: transactionid

## Product
  - name: "zuora_product"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Product#Field_Descriptions
    description: "info about your company's product offerings."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Product ID (<code>id</code>)
      - name: allowfeaturechanges
      - name: category
      - name: description
      - name: effectiveenddate
      - name: effectivestartdate
      - name: name
      - name: sku
      - name: createdbyid
      - name: createddate
      - name: updatedbyid
      - name: updateddate

## Product Rate Plan
  - name: "zuora_product_rate_plan"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/ProductRatePlan#Field_Descriptions
    description: "info about product rate plans, or the part of a product that customers can subscribe to."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Product Rate Plan ID (<code>id</code>)
      - name: activecurrencies
      - name: createdbyid
      - name: createddate
      - name: description
      - name: effectiveenddate
      - name: effectivestartdate
      - name: name
      - name: productid
      - name: updatedbyid
      - name: updateddate

## Product Rate Plan Charge
  - name: "zuora_product_rate_plan_charge"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/ProductRatePlanCharge#Field_Descriptions
    description: "info about product rate plan charges, which are a charge model or set of fees associated with a product rate plan."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Product Rate Plan Charge ID (<code>id</code>)
      - name: accountingcode
      - name: applydiscountto
      - name: billcycleday
      - name: billcycletype
      - name: billingperiod
      - name: billingperiodalignment
      - name: billingtiming
      - name: chargemodel
      - name: chargetype
      - name: createdbyid
      - name: createddate
      - name: defaultquantity
      - name: deferredrevenueaccount
      - name: description
      - name: discountlevel
      - name: enddatecondition
      - name: includedunits
      - name: listpricebase
      - name: maxquantity
      - name: minquantity
      - name: model
      - name: name
      - name: numberofperiod
      - name: overagecalculationoption
      - name: overageunusedunitscreditoption
      - name: pricechangeoption
      - name: priceincreaseoption
      - name: priceincreasepercentage
      - name: productrateplanid
      - name: recognizedrevenuerulename
      - name: revreccode
      - name: revrectriggercondition
      - name: smoothingmodel
      - name: specificbillingperiod
      - name: taxable
      - name: taxcode
      - name: taxmode
      - name: triggerevent
      - name: type
      - name: uom
      - name: updatedbyid
      - name: updateddate
      - name: uptoperiods
      - name: uptoperiodstype
      - name: usagerecordratingoption
      - name: usediscountspecificaccountingcode
      - name: usetenantdfaultforpricechange
      - name: weeklybillcycleday

## Product Rate Plan Charge Tier
  - name: "zuora_product_rate_plan_charge_tier"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/ProductRatePlanChargeTier#Field_Descriptions
    description: "pricing info for product rate plan charges."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Product Rate Plan Charge Tier ID (<code>id</code>)
      - name: active
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: discountamount
      - name: discountpercentage
      - name: endingunit
      - name: isoverageprice
      - name: price
      - name: priceformat
      - name: productrateplanchargeid
      - name: startingunit
      - name: tier
      - name: updatedbyid
      - name: updateddate

## Rate Plan
  - name: "zuora_rate_plan"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/RatePlan#Field_Descriptions
    description: "info about rate plans, which is a price or collection of prices for services."
    notes: &custom |
      ### Custom Fields
      In addition to the attributes listed below, our Zuora integration will also replicate any custom fields.
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Rate Plan ID (<code>id</code>)
      - name: amendmentid
      - name: amendmentsubscriptionrateplanid
      - name: amendmenttype
      - name: createdbyid
      - name: createddate
      - name: name
      - name: productrateplanid
      - name: subscriptionid
      - name: updatedbyid
      - name: updateddate

## Rate Plan Charge
  - name: "zuora_rate_plan_charge"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/RatePlanCharge#Field_Descriptions
    description: "info about rate plan charges, which are the parts of a subscription or subscription amendment that come from product rate charges."
    notes: *custom
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Rate Plan Charge ID (<code>id</code>)
      - name: accountingcode
      - name: applydiscountto
      - name: billcycleday
      - name: billcycletype
      - name: billingperiod
      - name: billingperiodalignment
      - name: billingtiming
      - name: chargedthroughdate
      - name: chargemodel
      - name: chargenumber
      - name: chargetype
      - name: createdbyid
      - name: createddate
      - name: description
      - name: discountamount
      - name: discountlevel
      - name: discountpercentage
      - name: dmrc
      - name: dtcv
      - name: effectiveenddate
      - name: effectivestartdate
      - name: enddatecondition
      - name: includedunits
      - name: islastsegment
      - name: listpricebase
      - name: mrr
      - name: name
      - name: numberofperiods
      - name: originalid
      - name: overagecalculationoption
      - name: overageprice
      - name: overageunusedunitscreditoption
      - name: price
      - name: pricechangeoption
      - name: priceincreasepercentage
      - name: processedthroughdate
      - name: productrateplanchargeid
      - name: quantity
      - name: rateplanid
      - name: recognizedrevenuerulename
      - name: revreccode
      - name: revrectriggercondition
      - name: rolloverbalance
      - name: segment
      - name: specificbillingperiod
      - name: specificenddate
      - name: tcv
      - name: triggerdate
      - name: triggerevent
      - name: unusedunitscreditrates
      - name: uom
      - name: updatedbyid
      - name: updateddate
      - name: uptoperiods
      - name: uptoperiodstype
      - name: usagerecordratingoption
      - name: usediscountspecificaccountingcode
      - name: version
      - name: weeklybillcycleday

## Rate Plan Charge Tier
  - name: "zuora_rate_plan_charge_tier"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/RatePlanChargeTier#Field_Descriptions
    description: "pricing info for rate plan charges."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Rate Plan Charge Tier ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: endingunit
      - name: isoverageprice
      - name: price
      - name: priceformat
      - name: rateplanchargeid
      - name: startingunit
      - name: tier
      - name: updatedbyid
      - name: updateddate

## Refund
  - name: "zuora_refund"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Refund#Field_Descriptions
    description: "info about refunds, or transactions where money is returned to a customer."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Refund ID (<code>id</code>)
      - name: accountid
      - name: accountingcode
      - name: amount
      - name: cancelledon
      - name: comment
      - name: createdbyid
      - name: createddate
      - name: effectivedate
      - name: gateway
      - name: gatewayoptiondata
      - name: gatewayresponse
      - name: gatewayresponsecode
      - name: gatewaystate
      - name: markedforsubmissionon
      - name: methodtype
      - name: paymentid
      - name: paymentmethodid
      - name: paymentmethodsnapshotid
      - name: reasoncode
      - name: referenceid
      - name: refundamount
      - name: refunddate
      - name: refundinvoicepaymentdata
      - name: refundnumber
      - name: refundtransactiontime
      - name: secondrefundreferenceid
      - name: settledon
      - name: softdescriptor
      - name: softdescriptionphone
      - name: sourcetype
      - name: status
      - name: submittedon
      - name: transferredtoaccounting
      - name: type
      - name: updatedbyid
      - name: updateddate

## Refund Invoice Payment
  - name: "zuora_refund_invoice_payment"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/RefundInvoicePayment
    description: "info about refund invoice payments, or parts of refunds that are being made against payments applied to invoices."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Refund Invoice Payment ID (<code>id</code>)
      - name: createdbyid
      - name: createddate
      - name: invoiceidid
      - name: invoicepaymentid
      - name: refundamount
      - name: refundid
      - name: updatedbyid
      - name: updateddate

## Refund Transaction Log 
  - name: "zuora_refund_transaction_log"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Refund_Transaction_Log_Data_Source
    description: "info about transactions related to refunds."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Refund Transaction Log ID (<code>id</code>)
      - name: gateway
      - name: gatewayreasoncode
      - name: gatewayreasoncodedescription
      - name: gatewaytransactiontype
      - name: refundid
      - name: requeststring
      - name: responsestring
      - name: transactiondate
      - name: transactionid

## Revenue Charge Summary Item
  - name: "zuora_revenue_charge_summary_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Revenue_Charge_Summary_Item_Data_Source
    description: "info about revenue charge summary items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Revenue Charge Summary Item ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: updatedbyid
      - name: updateddate

## Revenue Event Item
  - name: "zuora_revenue_event_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Revenue_Event_Item_Data_Source
    description: "info about revenue events."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Revenue Event Item ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: updatedbyid
      - name: updateddate

## Revenue Schedule Item
  - name: "zuora_revenue_schedule_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Revenue_Schedule_Item_Data_Source
    description: "info about revenue schedule items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Revenue Schedule Item ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: updatedbyid
      - name: updateddate

## Revenue Schedule Item Invoice Item Adjustment
  - name: "zuora_revenue_schedule_item_invoice_item_adjustment"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Revenue_Schedule_Item_Invoice_Item_Adjustment_Data_Source
    description: "info about adjustments made to revenue schedule item - invoice items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Revenue Schedule Item Invoice Item ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: updatedbyid
      - name: updateddate

## Revenue Schedule Item Invoice Item 
  - name: "zuora_revenue_schedule_item_invoice_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Revenue_Schedule_Item_Invoice_Item_Data_Source
    description: "info about revenue schedule item - invoice items."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Revenue Schedule Item Invoice Item ID (<code>id</code>)
      - name: amount
      - name: createdbyid
      - name: createddate
      - name: currency
      - name: updatedbyid
      - name: updateddate

## Subscription
  - name: "zuora_subscription"
    doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Subscription#Field_Descriptions
    description: "info about your products and/or services with recurring charges."
    notes: *custom
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Subscription ID (<code>id</code>)
      - name: accountid
      - name: ancestoraccountid
      - name: autorenew
      - name: cancelleddate
      - name: contractacceptancedate
      - name: contracteffectivedate
      - name: createdbyid
      - name: createddate
      - name: creatoraccountid
      - name: creatorinvoiceownerid
      - name: currentterm
      - name: currenttermperiodtype
      - name: initialterm
      - name: intitaltermperiodtype
      - name: invoiceownerid
      - name: isinvoiceseparate
      - name: name
      - name: notes
      - name: originalcreateddate
      - name: originalid
      - name: previoussubscriptionid
      - name: renewalsetting
      - name: renewalterm
      - name: renewaltermperiodtype
      - name: serviceactivationdate
      - name: status
      - name: subscriptionenddate
      - name: subscriptionstartdate
      - name: termenddate
      - name: termstartdate
      - name: termtype
      - name: updatedbyid
      - name: updateddate
      - name: version
      - name: versioncreateddate

## Taxation Item
  - name: "zuora_taxation_item"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Taxation_Item_Data_Source
    description: "info about taxation items, or items that are used to add a tax amount to an invoice item."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Taxation Item ID (<code>id</code>)
      - name: accountingcode
      - name: createdbyid
      - name: createddate
      - name: exemptamount
      - name: invoiceid
      - name: invoiceitemid
      - name: jurisdiction
      - name: locationcode
      - name: name
      - name: taxamount
      - name: taxcode
      - name: taxcodedescription
      - name: taxdate
      - name: taxrate
      - name: taxratedescription
      - name: taxratetype
      - name: updatedbyid
      - name: updateddate

## Unit of Measure
  - name: "zuora_unit_of_measure"
    doc-link: http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/UnitOfMeasure
    description: "info about units of measure. These are definable units that you measure when determining charges. For example: if a subscription plan includes 5 licenses, then 5 is the <strong>quantity</strong> and the license is the <strong>unit of measure</strong>."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Unit of Measure ID (<code>id</code>)
      - name: active
      - name: createdbyid
      - name: createddate
      - name: decimalplaces
      - name: displayedas
      - name: roundingmode
      - name: uomname
      - name: updatedbyid
      - name: updateddate

## Not sure what's going on with this table - commenting it out for the time being.
## Updater Detail
  ## - name: "zuora_updater_detail"
    ## doc-link: http://knowledgecenter.zuora.com/CB_Billing/L_Payment_Methods/D_Payment_Method_Updater
    ## description: "information about the Payment Method Updater."
    ## notes: 
    ## replication-method: "Incremental"
    ## primary-key: "id"
    ## nested-structures: false
    ## attributes:
      ## - name: Updater Detail ID (<code>id</code>)

## Usage 
  - name: "zuora_usage"
    doc-link: http://knowledgecenter.zuora.com/CD_Reporting/Data_Exports/Z_Data_Source_Reference/Usage_Data_Source
    description: "info about the amount of resources a customer uses."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Usage ID (<code>id</code>)
      - name: accountid
      - name: accountnumber
      - name: ancestoraccountid
      - name: chargeid
      - name: chargenumber
      - name: createdbyid
      - name: createddate
      - name: creatoraccountid
      - name: description
      - name: enddatetime
      - name: importid
      - name: invoiceid
      - name: invoicenumber
      - name: quantity
      - name: rbestatus
      - name: sourcename
      - name: sourcetype
      - name: startdatetime
      - name: submissiondatetime
      - name: subscriptionid
      - name: subscriptionnumber
      - name: uom
      - name: updatedbyid
      - name: updateddate
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Zuora data to Stitch is a five-step process:

1. [Create a Stitch Zuora user](#create-stitch-zuora-user)
2. [Add Zuora as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)
5. [Select tables to sync](#syncing-data)

### Prerequisites

1. **Verify that your Zuora account is a Production account.** At this time, Stitch can't connect to [Sandbox accounts](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments).
2. **Verify that you have Administrator permissions in Zuora.** This is required to create a Zuora user for Stitch.

### Creating a Stitch Zuora User {#create-stitch-zuora-user}

To connect your Zuora account, we recommend that you [create a user](http://knowledgecenter.zuora.com/CF_Users_and_Administrators/Administrator_Settings/Manage_Users) for Stitch. **Note that you must have Administrator permissions in your Zuora account to create a new user.**

To read and replicate your Zuora data, Stitch requires a user that:

1. **Has Standard user permissions**. Note that we will only ever read your data.
2. **Has two-factor authentication disabled.** If this type of authentication is enabled for the Stitch user, you'll encounter connection and replication issues after the Zuora setup is complete.

   Need some help disabling this setting? Check out the **Disable or Reset Two-Factor Authentication section** in this [Zuora documentation](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication).
3. **Has credentials that don't expire.** This is only applicable if your company enforces **Password Expiration rules.** If Stitch's Zuora credentials expire in the future, you may encounter connection issues. For a workaround, refer to [this Zuora support article.](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F)

When entering the user credentials in the next step, **be sure to use the username and password associated with the user**. Entering anything else, such as an API token or secret, will result in an unsuccessful connection.

{% include integrations/shared-setup/connection-setup.html %}
4. Enter the username and password of the Stitch user. Note that Stitch needs the username and password - entering a token and secret will result in an unsuccessful connection.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/saas/setup/saas-syncing.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
To get a better understanding of how Zuora objects relate to each other, check out Zuora's [Entity Relationship Diagram](http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E0_API_Object_Relationships). It's incredibly handy for figuring out how to combine different data sets, which will allow you to perform more in-depth and complex analyses.
{% endcontentfor %}