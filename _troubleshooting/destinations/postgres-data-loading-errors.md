---
title: Postgres Data Loading Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, postgres
permalink: /troubleshooting/destinations/postgres-data-loading-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "Received an error about Stitch loading data into your Postgres data warehouse? Check out these common errors and how to resolve them."
type: "postgres-destination, error, replication"
datatable: true
---
{% include misc/data-files.html %}

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

Below is a list of the most common errors that Stitch will encounter when attempting to load data into your Postgres data warehouse.

**Note that this isn't an exhaustive list.** If you receive an error that isn't listed here and need help troubleshooting, please reach out to our support team.

{% include tip.html content="Quickly find the fix for the error by entering keywords in the <strong>Search</strong> box above the table." %}

<table id="sampleTable" class="display">
   <thead>
      <tr>
         <th>Error Message</th>
         <th>Interpretation</th>
         <th>Fix</th>
      </tr>
   </thead>
   <tbody>
    <tr>
         <td width="30%; fixed" valign="top">
          Encountered error while attempting to create new schema.
         </td>
         <td valign="top">
          Stitch is unable to create or load data into a schema in your data warehouse.
         </td>
         <td valign="top" markdown="span">
          Verify that the Stitch database user has the required permissions, [as outlined here]({{ link.destinations.setup.self-hosted-postgres | prepend: site.baseurl | append: "#create-stitch-user" }}).
          </td>
      </tr>
      <tr>
         <td width="30%; fixed" valign="top">ERROR: could not write block 3440 of temporary file: No space left on device</td>
         <td valign="top">Your Postgres database is full.</td>
         <td valign="top">
        	<ul>
         	<li>Add additional space to make your Postgres database larger, OR</li>
			<li>Remove tables and/or data from the existing instance to free up disk space.</li>
			</ul>
		</td>
      </tr>
      <tr>
         <td width="30%; fixed" valign="top">ERROR: could not extend file <code>"base/16389/t2_285302"</code>: No space left on device
Hint: Check free disk space.
Where: <code>COPY staging_0_13_19423-24427690-551e-4338-b5df-018f20e64fd9, line 1142260</code></td>
         <td valign="top">Your Postgres database is full.</td>
         <td valign="top">
        	<ul>
         	<li>Add additional space to make your Postgres database larger, OR</li>
			<li>Remove tables and/or data from the existing instance to free up disk space.</li>
			</ul>
		</td>
      </tr>
   </tbody>
</table>