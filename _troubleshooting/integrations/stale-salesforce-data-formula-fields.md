---
title: Stale Salesforce Data & Formula Fields
keywords: troubleshooting, integration, saas integration, trouble, issue, help, error, data discrepancy, stale data, salesforce
permalink: /troubleshooting/stale-salesforce-data-formula-fields
tags: [troubleshooting_integrations, saas_integrations, data_discrepancy]

summary: "If you've noticed some out-of-date Salesforce data in your data warehouse, the root cause may be a formula field. "
type: "discrepancy, saas-integration, replication"
---
{% include misc/data-files.html %}

If you've noticed some out-of-date Salesforce data in your data warehouse, we recommend checking to see if the field in question is a formula field.

[Formula fields](https://help.salesforce.com/apex/HTViewHelpDoc?id=customize_formuladef.htm) are algorithms that derive their value from other fields, expressions, or values. These fields can automatically calculate their value based on other fields.

---

## Impact on Data Freshness

A formula field that's calculated with another object's modification stamp might not cause the [field Stitch is using as the Replication Key]({{ site.baseurl }}/integrations/saas/salesforce#replication) to change. This means that Stitch may not always identify formula fields as having new values.

For example: `Opportunity.Custom_Field_Account_Name__c` is an opportunity field that calculates the Account Name. If the Account Name changes, Salesforce may not indicate that the Opportunity formula field has changed, meaning the Opportunity record won't be detected by an incremental update.

---

## Workarounds for Formula Fields

- If you're using it as a join, you could recreate the join using SQL.
- If the field isn't a join, depending on what you need, you could still recreate it using SQL or change the field to be a native field that's updated through a workflow or apex trigger.
- Configure the table to use [full-table replication](https://www.stitchdata.com/docs/replication/replication-methods#full-table-replication). Note that this will increase the integration's consumption of Salesforce API quota, as well as your Stitch row usage.
