---
title: Selecting Amazon DynamoDB Fields Using Projection Queries
keywords: mongodb, mongo, whitelisting, blacklisting, field selection, column selection
permalink: /integrations/databases/amazon-dynamodb/field-selection-using-projection-queries
summary: "Specify or restrict the data Stitch replicates for Amazon DynamoDB collections using projection queries."
input: false

layout: general
toc: false
key: "dynamodb-projection-queries"

display_name: "DynamoDB"
name: "dynamodb"

this-version: "1.0"

intro: |
  {% include misc/data-files.html %}

  In Stitch's Amazon DynamoDB integration, projection queries serve as a method for selecting individual fields for replication. This is equivalent to [column selection]({{ link.replication.syncing | prepend: site.baseurl }}) in other integrations.

  By specifying a projection query, you can replicate only the data you need for each collection in your MongoDB integration.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Feature availability"
    anchor: "feature-availability"
    summary: "What versions of the MongoDB integration this feature is available for"
    content: |
      {% include shared/integrations/projection-column-selection.html type="feature-availability" %}

  - title: "What are projection queries?"
    anchor: "what-are-projection-queries"
    summary: "What projection queries are"
    content: |
      {% include shared/integrations/projection-column-selection.html type="what-are-projection-queries" %}

  - title: "Projection query requirements for Stitch"
    anchor: "projection-query-stitch-requirements"
    summary: "The requirements for projection queries in Stitch"
    content: |
      Projection queries are compatible with any of Stitch's Replication Methods, including Log-based Incremental.

      Projection queries entered into Stitch must adhere to the following:

      Projection queries that don't meet the above criteria will result in [errors during extraction](#error-troubleshooting).

  - title: "Defining a projection query in Stitch"
    anchor: "defining-projection-query-in-stitch"
    summary: "How to define a projection query in Stitch"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Adding a new projection query"
        anchor: "adding-new-projection-query"
        content: |
          {% include shared/integrations/projection-column-selection.html type="adding-new-projection-query" %}

      - title: "Modifying an existing projection query"
        anchor: "modifying-existing-projection-query"
        content: |
          {% include shared/integrations/projection-column-selection.html type="modifying-existing-projection-query" %}

  - title: "Example projection queries"
    anchor: "example-projection-queries"
    summary: "Some example projection queries"
    data:
      - name: "Finn"
        is_active: true
        details: |
          age: 15, type: human
        acquaintances: |
          - Jake
          - Ice King
      - name: "Jake"
        is_active: true
        details: |
          age: 6, type: dog
        acquaintances: |
          - Finn
          - Lady
      - name: "Bubblegum"
        is_active: false
        details: |
          age: 16, type: princess
        acquaintances: |
          - Finn
          - Bubblegum
      - name: "Lady"
        is_active: true
        details: |
          age: 50, type: unicorn
        acquaintances: |
          - Jake
          - Finn
      - name: "Ice King"
        is_active: false
        details: |
          age: 900, type: king
        acquaintances: |
          - Finn
          - Bubblegum
    examples:
      - title: "Return only specified fields"
        description: |
          Return only the specified fields (`name`, `is_active`) in the `customers` table. If including multiple fields, separate them with a comma.
        projection-query: |
          ```json
          "name, is_active"
          ```
        sql: |
          ```sql
          SELECT name,
                 is_active
            FROM customers
          ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|is_active" | split:"|" %}

      - title: "Return specified fields in a map element"
        description: |
          Using TODO: [dot notation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}, return specified fields in a map element. This is formatted as `"<map_element_name>.<field>"`

          In this example, the expression would return the top-level `name` field and `age` and `type` fields from the `details` map.

          Refer to TODO: [{{ page.display_name }}'s documentation](TODO){:target="new"} for more examples of dot notation for map elements.
        projection-query: |
          ```json
          "name", details.age, details.type"
          ```
        sql: |
          In destinations - like Snowflake - that also use dot notation to query nested data, the query might look like this:

          ```sql
          SELECT name,
                 "details.age",
                 "details.type"
            FROM customers
           ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|details" | split:"|" %}

      - title: "Return specified fields in a map element in a list"
        description: |
          Using [dot notation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}, return specified list items in a list element. This is formatted as `"list_name[n]"`

          In this example, the query would return the  top-level `name` field and selected element from the `acquaintances` list.

          Refer to [MongoDB's documentation](https://docs.mongodb.com/v4.0/core/document/#arrays){:target="new"} for more examples of dot notation for embedded documents and arrays.
        projection-query: |
          ```json
          "name, acquaintances[1]"
          ```
        sql: |
          In destinations - like Snowflake - that also use dot notation to query nested data, the query might look like this:

          ```sql
          SELECT name,
                 "acquaintances.name",
                 "acquaintances.type"
            FROM customers
           ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|acquaintances" | split:"|" %}
    content: |
      In this section, we'll look at some example projection queries and their SQL equivalents.

      - [Example collection data](#example-collection-data)
      {% for example in section.examples %}
      - [{{ example.title }}](#{{ example.title | slugify }})
      {% endfor %}

      ### Example collection data {#example-collection-data}

      The examples use data from a collection named `customers`, which contains the following documents:

      {% assign results = section.data %}
      {% assign headings = "name (string)|is_active (boolean)|details (object)|acquaintances (array)" | split:"|" %}
      {% assign attributes = "name|is_active|details|acquaintances" | split:"|" %}

      <table class="attribute-list" style="margin-top: 0px;">
      <tr>
      {% for heading in headings %}
      <td width="15%; fixed"><strong>{{ heading }}</strong></td>
      {% endfor %}
      </tr>
      {% for result in results %}
      <tr>
      {% for attribute in attributes %}
      <td>
      {{ result[attribute] | markdownify }}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

      {% assign example-attributes = "projection-query|sql|results" | split: "|" %}

      {% for example in section.examples %}
      ### {{ example.title }} {#{{ example.title | slugify }}}

      {{ example.description | flatify }}

      <table class="attribute-list">
      {% for attribute in example-attributes %}
      {% if example[attribute] %}
      <tr>
      <td width="20%; fixed" align="right">
      <strong>{{ attribute | replace:"-"," " | capitalize | replace:"Sql","SQL" }}</strong>
      </td>

      <td>
      {% case attribute %}
      {% when 'results' %}

      {{ example[attribute] | flatify }}

      <table class="attribute-list" style="margin-top: 0px;">
      <tr>
      {% for attribute in attributes %}
      <td><strong>{{ attribute }}</strong></td>
      {% endfor %}
      </tr>
      {% for result in results %}
      <tr>
      {% for attribute in attributes %}
      <td>
      {{ result[attribute] | markdownify }}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

      {% else %}
      {{ example[attribute] | flatify | markdownify }}
      {% endcase %}
      </td>

      </tr>
      {% endif %}
      {% endfor %}
      </table>
      {% endfor %}

  - title: "Error troubleshooting"
    anchor: "error-troubleshooting"
    summary: "How to troubleshoot projection query errors"
    content: |
      If a collection's projection query doesn't meet [Stitch's requirements](#projection-query-stitch-requirements), a critical error will arise during Extraction. Extractions will not be successful until the issue is resolved.

      For a list of possible errors and how to resolve them, refer to the [MongoDB Extraction Errors reference]({{ link.troubleshooting.mongodb-extraction-errors | prepend: site.baseurl }}).

  - title: "Resources"
    anchor: "projection-query-resources"
    summary: "Additional resources for projection queries"
    content: |
      - [MongoDB projection query documentation]({{ site.data.taps.links.mongodb.projection-queries }}){:target="new"}
      - [MongoDB dot notation documentation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}
      - [MongoDB Extraction Errors reference]({{ link.troubleshooting.mongodb-extraction-errors | prepend: site.baseurl }})

      ---
---