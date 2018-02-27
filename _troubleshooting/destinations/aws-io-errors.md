---
title: AWS & Redshift I/O Connection Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply, io, i/o
permalink: /troubleshooting/destinations/aws-io-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "While typically transient, I/O errors arise from connection issues between Stitch and your data warehouse. If persistent, these errors may be indicative of a larger issue."
type: "redshift-destination, error"
promote: "false"
---
{% include misc/data-files.html %}

> An I/O error occurred while sending to the backend.

{{ page.summary }} To ensure Stitch can continue loading your data, these errors should be addressed promptly.

**Note**: While we've only seen this issue affect Amazon Redshift users, it is possible that PostgreSQL destinations may also be affected.

---

## I/O Errors, Explained {#io-error-explanation}

I/O errors arise from connection issues between Stitch and your data warehouse. When Stitch connects to your destination to perform a connection check or load data, an I/O error can arise if the connection to the destination is severed. This is typically caused by a timeout issue.

For example: Stitch attempts to load a large amount of data into your destination. Due to the data volume, Stitch's query takes a long time to run and, as a result, the connection becomes idle.

The timeout settings on the destination's server define how long a connection can remain idle before it's terminated. If Stitch is unable to complete its query before the timeout limits, the connection will be terminated and an I/O error may occur.

---

## Recommendations

To work through this section, you'll need some technical expertise and familiarity with Amazon Web Services. If need be, we suggest looping in a developer or a member of your engineering team to help out.

### Check the Server's Firewall Timeout Settings {#firewall-timeout-settings}

One potential source of timeout issues may be due to the destination server's firewall timeout settings. If the connection is from any other computer than an Amazon EC2 instance, these settings govern how long the connection may be inactive before it is terminated by the firewall.

Stitch sends a TCP keepalive signal within 200 seconds of a connection going idle, and every 75 seconds thereafter. To avoid a timeout with Stitch, we recommend increasing the values of the `KeepAlive` settings for your destination's server. This will ensure that Stitch's connection isn't prematurely terminated. For more info on these settings, refer to [Amazon's documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-firewall-guidance.html).

### Check the Server's Command/Query Settings {#command-query-settings}

In addition to the destination server's firewall timeout settings, the `statement_timeout` and WLM (Work Load Management) Timeout settings may be potential causes.

- **Statement timeout:** [The `statement_timeout` setting](https://docs.aws.amazon.com/redshift/latest/dg/r_statement_timeout.html) defines how long, in milliseconds, a statement may take to complete before it is aborted by the server. For example: If `statement_timeout` is set to 100 milliseconds, any query that takes longer than 100 milliseconds to complete will be canceled.

   If the current period of this setting is very short - 1 millisecond, for example - we suggest increasing this setting to ensure Stitch's queries can complete successfully.

   **Note**: This parameter applies to the entire cluster.

- **WLM timeout**: The WLM timeout parameter (`max_execution_time`) is functionally similar to `statement_timeout`, but only applies to a single queue in a WLM configuration. For more info on query queues, refer to [Amazon's documentation](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-defining-query-queues.html).

### Implement Performance and Workload Management {#performance-workload-management}

In addition to increasing the values of the timeout settings, you should also consider implementing performance improvement features like Encodings, SORT, and DIST keys. These features can improve query efficiency, thus reducing the time it takes for Stitch's queries to complete.

Refer to our [Encodings, SORT, and DIST Keys guide]({{ link.destinations.storage.redshift-encodings | prepend: site.baseurl }}) for more info and application instructions.

---

## Next Steps

If increasing the destination server's timeout settings or applying performance improvement features doesn't resolve the occurrence of I/O errors, we recommend reaching out to [Amazon Support](https://aws.amazon.com/contact-us/) or [Panoply Support](https://panoply.io) for assistance.