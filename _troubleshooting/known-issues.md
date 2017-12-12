---
title: Known Third-Party Issues
keywords: troubleshooting, integration, trouble, issue, help, bug, defect, bugs, third-party bugs, third party
permalink: /troubleshooting/known-third-party-issues
datatable: true

summary: "Occasionally, some integrations used by Stitch may encounter bugs or other issues. Whenever we’ve identified a third-party issue - meaning on the integration provider’s end - we’ll post an update here."
type: "all-integrations, error, discrepancy"
toc: true
---

<script>
$(document).ready(function(){

    $('table.display').DataTable( {
        paging: false,
        stateSave: true,
        searching: true
    }
        );
});
</script>

Occasionally, some integrations used by Stitch may encounter bugs or other issues. Whenever we’ve identified a third-party issue - meaning on the integration provider’s end - we’ll post an update here. Additionally, we’ll also update any issues that have been resolved.

---

## Identified Issues

There currently aren't any identified issues.

---

## Resolved Issues

<table id="resolvedIssues" class="display">
   <thead>
      <tr>
         <th width="15%; fixed">Integration</th>
         <th width="15%; fixed">Identified / Resolved</th>
         <th>Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>Facebook Ads</td>
         <td>06/21/16 / <br>
         	11/02/16</td>
         <td><a href="https://developers.facebook.com/bugs/260496180990955/" target="_blank">Facebook has identified an issue with the Ad Insights endpoint.</a> This results in async jobs running for long periods of time and then stopping with a status of "Job Failed."<br><br>
         This can result in data not replicating for customers using the Facebook Ads integration and syncing the Ad Insights endpoint.</td>
      </tr>
   </tbody>
</table>