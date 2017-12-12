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
         <td width="30%; fixed" valign="top">ERROR: must be owner of relation <code>[table_name]</code></td>
         <td valign="top">Stitch is not the owner of tables in Redshift, which is needed to perform functions necessary to loading data.</td>
         <td valign="top">Verify that the Stitch user has all the required permissions as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		</td>
      </tr>
      <tr>
         <td width="30%; fixed" valign="top">ERROR: permission denied for schema <code>[schema_name]</code></td>
         <td valign="top">Stitch does not have permissions to create tables within a schema in Redshift.</td>
         <td valign="top">Verify that the Stitch user has all the required permissions as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		     </td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">FATAL: password authentication failed for user <code>"stitch_user"</code></td>
         <td valign="top">The credentials that Stitch has for your Redshift instance are incorrect.</td>
         <td valign="top">Verify that the correct password for the user Stitch is using to connect to Redshift is entered in the <strong>{{ app.page-names.dw-settings }}</strong> page of Stitch.
		</td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">FATAL: database <code>"database_name"</code> does not exist</td>
         <td valign="top">Stitch can't find the database in Redshift it has been configured to use.</td>
         <td valign="top">Verify that the correct database is entered in the <strong>{{ app.page-names.dw-settings }}</strong> page of Stitch. You can also perform a connection check in this page.
		</td>
      </tr>
      <tr>
         <td width="30%; fixed" valign="top">
          Encountered error while attempting to create new schema.
         </td>
         <td valign="top">
          Stitch is unable to create or load data into a schema in your data warehouse.
         </td>
         <td valign="top" markdown="span">
          Verify that the Stitch database user has the required permissions, [as outlined here]({{ link.destinations.setup.redshift | prepend: site.baseurl | append: "#required-permissions" }}).
          </td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">Connection refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.</td>
         <td valign="top">Stitch can't connect to the Redshift instance, most likely due to firewall configurations.</td>
         <td valign="top">Verify that your VPC settings in AWS are configured correctly as outlined <a href="{{ link.destinations.setup.redshift | prepend: site.baseurl }}">in this article</a>.
		</td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">The connection attempt failed.</td>
         <td valign="top">Stitch cannot connect to the Redshift instance.</td>
         <td valign="top">Verify and test your Redshift configuration in the <strong>{{ app.page-names.dw-settings }}</strong> page of Stitch.
		</td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">An I/O error occured while sending to the backend.</td>
         <td valign="top">Something went wrong during the communication with Redshift.</td>
         <td valign="top">This is a transient error, and should clear itself during the next re-sync.
		</td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">ERROR: Cannot execute query because system is in resize mode<br><br>
          Detail: System is in resize mode, and ONLY read-only queries are allowed to execute.</td>
         <td valign="top">Someone adjusted (up or down) the number of nodes of your Redshift instance and Amazon is currently applying that change.</td>
         <td valign="top">This is a transient issue - Stitch should be able to resume syncing data once the resize is completed.
		    </td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">ERROR: cannot drop table <code>SCHEMA.TABLE</code> column type because other objects depend on it<br><br>
          Hint: Use <code>DROP ... CASCADE</code> to drop the dependent objects too.</td>
         <td valign="top">Stitch is attempting to widen <code>VARCHAR</code> columns in Redshift and can't because a view is built on top of the table.</td>
         <td valign="top"><a href="{{ site.baseurl }}/troubleshooting/destinations/redshift-dependent-view-errors">Temporarily dropping the dependent views</a>, which will allow Stitch to widen the columns. This process usually takes about an hour.
        </td>
      </tr>
       <tr>
         <td width="30%; fixed" valign="top">
          ERROR: Disk Full Detail:<br> 
          -----------------------------<br>
          error:  Disk Full<br>
          code:      1016<br>
          context:   node: 3<br>
          query:     1005177<br>
          location:  fdisk_api.cpp:345<br>
          process:   query3_66 [pid=27629]<br>
          -----------------------------
         </td>
         <td valign="top">Your Redshift instance is full.</td>
         <td valign="top"><ul>
          <li>Add additional nodes to make your Redshift instance larger, OR</li>
          <li>Remove tables and/or data from the existing instance to free up disk space.</li>
        </ul>
        </td>
      </tr>
   </tbody>
</table>

## Contacting Support

If you still encounter trouble after following the troubleshooting steps above, please reach out to support for assistance.