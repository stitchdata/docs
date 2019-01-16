---
title: Redshift Data Loading Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply
permalink: /troubleshooting/destinations/redshift-data-loading-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "Received an error about Stitch loading data into your Redshift data warehouse? Check out these common errors and how to resolve them."
type: "redshift-destination, error, replication"
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

Below is a list of the most common errors that Stitch will encounter when attempting to load data into your Redshift data warehouse.

**Please note:**

- This isn't an exhaustive list. If you receive an error that isn't listed here and need help troubleshooting, please reach out to our support team.
- The info in this article is also applicable to Panoply data warehouses, as Panoply uses Redshift.

{% include tip.html content="Quickly find the fix for the error by entering keywords in the Search box above the table." %}

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
         1. ERROR: must be owner of relation [table_name]
         - Stitch is not the owner of tables in Redshift, which is needed to perform functions necessary to loading data.
         - Verify that the Stitch user has all the required permissions as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		
      </tr>
      <tr>
         1. ERROR: permission denied for schema [schema_name]
         - Stitch does not have permissions to create tables within a schema in Redshift.
         - Verify that the Stitch user has all the required permissions as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		     
      </tr>
       <tr>
         1. FATAL: password authentication failed for user "stitch_user"
         - The credentials that Stitch has for your Redshift instance are incorrect.
         - Verify that the correct password for the user Stitch is using to connect to Redshift is entered in the {{ app.page-names.dw-settings }} page of Stitch.
		
      </tr>
       <tr>
         1. FATAL: database "database_name" does not exist
         - Stitch can't find the database in Redshift it has been configured to use.
         - Verify that the correct database is entered in the {{ app.page-names.dw-settings }} page of Stitch. You can also perform a connection check in this page.
		
      </tr>
      <tr>
         1. 
          Encountered error while attempting to create new schema.
         
         - 
          Stitch is unable to create or load data into a schema in your data warehouse.
         
         - 
          Verify that the Stitch database user has the required permissions, [as outlined here]({{ link.destinations.setup.redshift | prepend: site.baseurl | append: "#required-permissions" }}).
          
      </tr>
       <tr>
         1. Connection refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.
         - Stitch can't connect to the Redshift instance, most likely due to firewall configurations.
         - Verify that your VPC settings in AWS are configured correctly as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		
      </tr>
       <tr>
         1. The connection attempt failed.
         - Stitch cannot connect to the Redshift instance.
         - Verify and test your Redshift configuration in the {{ app.page-names.dw-settings }} page of Stitch.
		
      </tr>
       <tr>
         1. An I/O error occured while sending to the backend.
         - Something went wrong during the communication with Redshift.
         - This is a transient error, and should clear itself during the next re-sync.
		
      </tr>
       <tr>
         1. ERROR: Cannot execute query because system is in resize mode<br><br>
          Detail: System is in resize mode, and ONLY read-only queries are allowed to execute.
         - Someone adjusted (up or down) the number of nodes of your Redshift instance and Amazon is currently applying that change.
         - This is a transient issue - Stitch should be able to resume syncing data once the resize is completed.
		    
      </tr>
       <tr>
         1. ERROR: cannot drop table SCHEMA.TABLE column type because other objects depend on it<br><br>
          Hint: Use DROP ... CASCADE to drop the dependent objects too.
         - Stitch is attempting to widen VARCHAR columns in Redshift and can't because a view is built on top of the table.
         - <a href="{{ site.baseurl }}/troubleshooting/destinations/redshift-dependent-view-errors">Temporarily dropping the dependent views</a>, which will allow Stitch to widen the columns. This process usually takes about an hour.
        
      </tr>
       <tr>
         1. 
          ERROR: Disk Full Detail:<br> 
          -----------------------------<br>
          error:  Disk Full<br>
          code:      1016<br>
          context:   node: 3<br>
          query:     1005177<br>
          location:  fdisk_api.cpp:345<br>
          process:   query3_66 [pid=27629]<br>
          -----------------------------
         
         - Your Redshift instance is full.
         - <ul>
          <li>Add additional nodes to make your Redshift instance larger, OR</li>
          <li>Remove tables and/or data from the existing instance to free up disk space.</li>
        </ul>

## Contacting Support

If you still encounter trouble after following the troubleshooting steps above, please reach out to support for assistance.