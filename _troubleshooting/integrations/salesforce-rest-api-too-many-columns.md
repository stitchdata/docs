---
title: Salesforce Replication & Selecting Too Many Columns
keywords: troubleshooting, integration, saas integration, trouble, issue, help, syncing columns, salesforce columns, too many columns, object, salesforce
permalink: /troubleshooting/salesforce-replication-too-many-columns
tags: [troubleshooting_integrations, saas_integrations, error_notifications]

summary: "If a single Salesforce object has a large number of columns set to replicate, issues with replication may arise."
type: "saas-integration, replication"
---
{% include misc/data-files.html %}

{{ site.data.alerts.note }} <strong>Applicable Versions</strong><br>
This issue is applicable to:

<ul>
<li><a href="{{ site.baseurl}}/integrations/saas/salesforce/v15-10-2015">Salesforce v15-10-2015</a></li>
<li>Salesforce v1 (<a href="{{ site.baseurl }}/integrations/saas/salesforce#configure-salesforce-api-usage">only if using the REST API</a>)</li>
</ul>
{{ site.data.alerts.end }}

{{ page.summary }}

---

## Extraction Log Error

{% include note.html type="single-line" content="Extraction logs are unavailable for Salesforce integrations using version 15-10-2017." %}

If the version of your Salesforce integration supports [extraction logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}), this is the error message that will display in Stitch:

```shell
Bad Message 431 reason: Request Header Fields Too Large
```

---

## The Salesforce API and Stitch Replication Issues

When Stitch extracts data from Salesforce, it passes the names of all the object fields you set to replicate to the corresponding Salesforce REST API endpoint in what is called a `GET` request.

The names of the fields set to replicate is used to construct a URL that is sent to Salesforce in the `GET` request. This is how Stitch extracts the data you want from Salesforce.

Take a look at the following cURL request example. The line beginning with `-d` contains the URL made up the names of the fields we want to replicate. For example: `Id`, `IsDeleted`, `MasterRecordId`, `Name`, and so on:

```shell
curl -G 
    -H 'Authorization: Bearer [access_token]'   https://[salesforce_instance]/services/data/v33.0/queryAll
    -d 'q=select+Id%2C+IsDeleted%2C+MasterRecordId%2C+Name%2C+LastName%2C+FirstName%2C+Salutation%2C+Type%2C+RecordTypeId%2C+ParentId%2C+BillingStreet%2C+BillingCity%2C+BillingState%2C+BillingPostalCode%2C+BillingCountry%2C+BillingLatitude%2C+BillingLongitude%2C+BillingAddress%2C+ShippingStreet%2C+ShippingCity%2C+ShippingState%2C+ShippingPostalCode%2C+ShippingCountry%2C+ShippingLatitude%2C+ShippingLongitude%2C+ShippingAddress%2C+Phone%2C+Fax%2C[...]
```

The more fields that are set to replicate in an object, the longer the URL Stitch sends to Salesforce. Selecting large numbers of fields - or fields with long names - can result in the URL exceeding [Salesforce's character limit](https://salesforce.stackexchange.com/questions/195449/what-is-the-longest-uri-that-salesforce-will-accept-through-the-rest-api/195450). In Stitch, this will surface as an integration error and lead to unsuccessful replication.

### Total Columns vs. Column Name Length

This issue is dependent on the cumulative length of the fields' names in the URL sent by Stitch, not necessarily the number of fields set to replicate.

While a large number of fields set to replicate can result in this issue, it can also be caused by a smaller number of replicating fields with longer names.

---

## Workarounds

Depending on your needs and the setup of your Salesforce integration, there are a few ways you can approach this issue:

- **Option 1:** Create a new Salesforce integration and use the Bulk API. **Note**: The Bulk API has its own limitations, [which you can read about here]({{ site.baseurl }}/integrations/saas/salesforce#configure-salesforce-api-usage).
- **Option 2:** Review your field selections and de-select any that are unnecessary. Keep in mind that issue is not dependent on the number of selected fields and may require some trial and error.