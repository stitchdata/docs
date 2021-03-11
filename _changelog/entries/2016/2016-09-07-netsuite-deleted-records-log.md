---
title: "NetSuite (v10-15-2015) integrations: Deleted record support"
content-type: "changelog-entry"
date: 2016-09-07
entry-type: new-feature
entry-category: integration
connection-id: netsuite
connection-version: "10-15-2015"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The {{ this-connection.display_name }} integration now includes a table called `netsuite_deleted` which contains a row for every deleted record that supports deletes. 
Accounting for deleted records is especially important if you’re performing any sort of aggregate function, such as totaling invoices or balancing your books. 

Learn more about utilizing the {{ this-connection.display_name }} deletion log in our [docs]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#using-netsuite-deleted" }}.