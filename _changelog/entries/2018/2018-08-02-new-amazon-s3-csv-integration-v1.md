---
title: "New integration: Amazon S3 CSV"
content-type: "changelog-entry"
date: 2018-08-02
entry-type: new-feature
entry-category: integration
connection-id: amazon-s3-csv
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new {{ this-connection.display_name }} integration is now available!

This integration can connect to your S3 bucket and replicate CSV files to your Stitch destination. Some highlights of this new integration include:

- Replication of data from CSV files stored in your S3 buckets
- Support for incremental updates based on new or modified CSV files 
- Column selection for choosing which columns you want to extract from your CSV files 
- Automatic inference of data types and the ability to explicitly specify datetime fields

Get started by creating a new {{ this-connection.display_name }} integration or learning more in [our documentation]({{ this-connection.url | prepend: site.baseurl }}).