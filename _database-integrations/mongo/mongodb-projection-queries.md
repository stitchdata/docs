---
title: Selecting MongoDB Fields Using Projection Queries
keywords: mongodb, mongo, whitelisting, blacklisting, field selection, column selection
permalink: /integrations/databases/mongodb/field-selection-using-projection-queries
summary: "Specify or restrict the data Stitch replicates for MongoDB collections using projection queries."
input: false

layout: general
toc: false
key: "mongodb-projection-queries"

display_name: "MongoDB"
name: "mongodb"
db-type: "mongo"

this-version: "1"

intro: |
  {% include misc/data-files.html %}

  In Stitch's MongoDB integration, projection queries serve as a method for selecting individual fields for replication. This is equivalent to [column selection]({{ link.replication.syncing | prepend: site.baseurl }}) in other integrations.

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

      - **Cannot exclude the `_id` field.** This is equivalent to `{ "_id": 0 }`. Stitch uses this field for replication.
      - **Cannot specify conditional criteria.** In SQL, this is equivalent to specifying a `WHERE` clause. For example: `{ "is_active": true }` is equal to `WHERE is_active = true`. This type of projection query is not currently supported in Stitch.
      - **Cannot combine inclusion and exclusion statements.** This means that a projection query can't both include and exclude fields. For example: `{ "name": 0, "type": 1 }`
      - **Must be valid JSON.** Projection queries must be valid JSON. Keys and string values must be enclosed in double quotes (`"`). You can use [JSONFormatter](https://jsonformatter.curiousconcept.com/){:target="new"} to validate the projection query before entering it into Stitch.
      - **Must exclude the `_acl` field** if using access control list plugins with MongoDB. If the projection query is inclusion-based, then you must remove it.

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
          - name: Jake, type: best_friend
          - name: Ice King, type: nemesis
      - name: "Jake"
        is_active: true
        details: |
          age: 6, type: dog
        acquaintances: |
          - name: Finn, type: best_friend
          - name: Lady, type: spouse
      - name: "Bubblegum"
        is_active: false
        details: |
          age: 16, type: princess
        acquaintances: |
          - name: Finn, type: friend
          - name: Bubblegum, type: best_friend
      - name: "Lady"
        is_active: true
        details: |
          age: 50, type: unicorn
        acquaintances: |
          - name: Jake, type: spouse
          - name: Finn, type: friend
      - name: "Ice King"
        is_active: false
        details: |
          age: 900, type: king
        acquaintances: |
          - name: Finn, type: nemesis
          - name: Bubblegum, type: nemesis
    examples:
      # Commenting out as we don't currently support conditional logic in projection queries
      # - title: "Return all fields in matching documents"
      #   description: |
      #     Return all fields in documents in the `customers` collection where `is_active = true`.
      #   projection-query: |
      #     ```json
      #     { "is_active": true }
      #     ```
      #   sql: |
      #     ```sql
      #     SELECT *
      #       FROM customers
      #      WHERE is_active = true
      #      ```
      #   results: |
      #     {% assign results = section.data | where:"is_active",true %}
      #     {% assign attributes = "name|is_active|details|acquaintances" | split:"|" %}

      - title: "Return only specified fields"
        description: |
          Return only the specified fields (`name`, `is_active`) for documents in the `customers` collection. Fields are marked for inclusion by setting their value to `1` in the projection query.
        projection-query: |
          ```json
          { "name": 1, "is_active": 1 }
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

      # Commenting out as we don't currently support conditional logic in projection queries
      # - title: "Return only specified fields in matching documents"
      #   description: |
      #     Return only the specified fields (`name`, `details`) for documents in the `customers` collection where `is_active = true`.
      #   projection-query: |
      #     ```json
      #     { "is_active": true }, { "name": 1, "details": 1 }
      #     ```
      #   sql: |
      #     ```sql
      #     SELECT name,
      #            details
      #       FROM customers
      #      WHERE is_active = true
      #      ```
      #   results: |
      #     {% assign results = section.data | where:"is_active",true %}
      #     {% assign attributes = "name|details" | split:"|" %}

      - title: "Return all except excluded fields"
        description: |
          Return all fields except those that are excluded. Fields are marked for exclusion by setting their value to `0` in the projection query.

          **Note**: The `_id` field cannot be excluded in projection queries added in Stitch, as Stitch requires it for replication.

          In this example, the query would return only the `name` and `acquaintances` fields.
        projection-query: |
          ```json
          { "is_active": 0, "details": 0 }
          ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|acquaintances" | split:"|" %}

      - title: "Return specified fields in an embedded document"
        description: |
          Using [dot notation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}, return specified fields in an embedded document. This is formatted as `"<embedded_document_name>.<field>"`

          In this example, the query would return the `name` and `name` and `type` fields from the `details` document.

          Refer to [MongoDB's documentation](https://docs.mongodb.com/v4.0/core/document/#embedded-documents){:target="new"} for more examples of dot notation for embedded documents.
        projection-query: |
          ```json
          { "name": 1, "details.name": 1, "details.type": 1 }
          ```
        sql: |
          In destinations - like Snowflake - that also use dot notation to query nested data, the query might look like this:

          ```sql
          SELECT name,
                 "details.name",
                 "details.type"
            FROM customers
           ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|details" | split:"|" %}

      - title: "Return specified fields in an embedded document in an array"
        description: |
          Using [dot notation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}, return specified fields in an embedded document contained in an array. This is formatted as `"<embedded_document_name>.<field>"`

          In this example, the query would return the `name` and `name` and `type` fields from the documents in the `acquaintances` array.

          Refer to [MongoDB's documentation](https://docs.mongodb.com/v4.0/core/document/#arrays){:target="new"} for more examples of dot notation for embedded documents and arrays.
        projection-query: |
          ```json
          { "name": 1, "acquaintances.name": 1, "acquaintances.type": 1 }
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

      For a list of possible errors and how to resolve them, refer to the [MongoDB Extraction Errors reference]({{ link.troubleshooting.mongodb-extraction-errors | flatify | prepend: site.baseurl }}).

  - title: "Resources"
    anchor: "projection-query-resources"
    summary: "Additional resources for projection queries"
    content: |
      - [MongoDB projection query documentation]({{ site.data.taps.links.mongodb.projection-queries }}){:target="new"}
      - [MongoDB dot notation documentation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}
      - [MongoDB Extraction Errors reference]({{ link.troubleshooting.mongodb-extraction-errors | flatify | prepend: site.baseurl }})

      ---
---