---
title: Databricks Delta Issues
keywords: troubleshooting, destination, trouble, issue, help, error, errors, databricks delta
permalink: /troubleshooting/destinations/databricks-delta-issues

summary: "If you’re having trouble with setting up or connecting to your Databricks Delta data warehouse in Stitch, try these troubleshooting steps before reaching out to support."
type: "databricks-delta-destination, error"

key: "databricks-delta-issues"

promote: "false"
---
{% include misc/data-files.html %}

{{ page.summary }}

---

## Automatic schema evolution issue

The automatic schema evolution feature available for Delta tables can cause issues when loading data to your Databricks Delta destination. It is recommended to disable this option on your destination tables. For more information about this feature, see the [Databricks documentation](https://docs.databricks.com/delta/delta-update.html#automatic-schema-evolution).

To avoid this issue, make sure the `spark.databricks.delta.schema.autoMerge.enabled` property is disabled on your table before loading data:
1. To check if this option is enabled, you can use this SQL query: 
    `SET spark.databricks.delta.schema.autoMerge.enabled;`
2. If the value of this property is `true`, disable it using this query: 
    `SET spark.databricks.delta.schema.autoMerge.enabled=false;`



---

## Contact Support

If you’re still running into problems with Databricks Delta in Stitch, reach out to [support]({{ site.support }}).