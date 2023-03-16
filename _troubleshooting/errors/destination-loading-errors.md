---
title: Destination Loading Error Reference
keywords: troubleshooting, destination, destination, trouble, issue, help, error, errors, loading issue, loading
layout: general

permalink: /troubleshooting/destinations/destination-loading-error-reference
redirect_from: 
  - /troubleshooting/destinations/redshift-data-loading-errors
  - /troubleshooting/destinations/postgres-data-loading-errors
  - /troubleshooting/destinations/destination-data-loading-errors

summary: "Resolve errors related to loading data into your Stitch destination."

key: "destination-loading-errors"

level: "guide"
top-level: ""
category: "loading-errors"
type: "all-destinations, destination, error"
popular: true

display_name: "[DESTINATION]"

intro: |
  {% assign destination = page %}

  In this reference:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Common loading errors"
    anchor: "common-error-reference"
    content: |
      {% assign errors = site.data.destinations.common.loading-errors.all | sort_natural:"message" %}

      The following errors are applicable to multiple or all destinations:

      {% include troubleshooting/error-messages.html top-anchor="common-error-reference" display-name="Common" %}

  - title: "Amazon Redshift and Panoply loading errors"
    anchor: "amazon-redshift-error-reference"
    content: |
      {% assign errors = site.data.destinations.redshift.loading-errors.all | sort_natural:"message" %}

      {% include note.html type="single-line" content="**Note**: The errors in this section are applicable to Amazon Redshift and Panoply destinations." %}

      {% include troubleshooting/error-messages.html top-anchor="amazon-redshift-error-reference" display-name="Amazon Redshift" %}

  - title: "Databricks Delta Lake loading errors"
    anchor: "databricks-delta-lake-error-reference"
    content: |
      {% assign errors = site.data.destinations.databricks-delta.loading-errors.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="databricks-delta-lake-error-reference" display-name="Databricks Delta Lake" %}

  - title: "Google BigQuery loading errors"
    anchor: "google-bigquery-error-reference"
    content: |
      {% assign errors = site.data.destinations.bigquery.loading-errors.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="google-bigquery-error-reference" display-name="Google BigQuery" %}

  - title: "Microsoft SQL Server loading errors"
    anchor: "microsoft-sql-server-error-reference"
    content: |
      {% assign errors = site.data.destinations.microsoft-sql-server.loading-errors.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="microsoft-sql-server-error-reference" display-name="Microsoft SQL Server" %}

  - title: "PostgreSQL loading errors"
    anchor: "postgresql-error-reference"
    content: |
      {% assign errors = site.data.destinations.postgres.loading-errors.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="postgresql-error-reference" display-name="PostgreSQL" %}

  - title: "Snowflake loading errors"
    anchor: "snowflake-error-reference"
    content: |
      {% assign errors = site.data.destinations.snowflake.loading-errors.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="snowflake-error-reference" display-name="Snowflake" %}
---
{% include misc/data-files.html %}