---
title: Selecting Amazon DynamoDB Fields Using Projection Expressions
keywords: dynamodb, amazon dynamodb, whitelisting, blacklisting, field selection, column selection
permalink: /integrations/databases/amazon-dynamodb/field-selection-using-projection-expressions
summary: "Specify or restrict the data Stitch replicates for Amazon DynamoDB tables using projection expressions."
input: false

layout: general
toc: false
key: "dynamodb-projection-queries"

display_name: "DynamoDB"
name: "dynamodb"
db-type: "dynamodb"

this-version: "1"

intro: |
  {% include misc/data-files.html %}

  In Stitch's Amazon DynamoDB integration, projection expressions serve as a method for selecting individual fields for replication. This is equivalent to [column selection]({{ link.replication.syncing | prepend: site.baseurl }}) in other integrations.

  By specifying a projection expression, you can replicate only the data you need for each table in your DynamoDB integration.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary | flatify }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Feature availability"
    anchor: "feature-availability"
    summary: "What versions of the {{ page.display_name }} integration this feature is available for"
    content: |
      {% include shared/integrations/projection-column-selection.html type="feature-availability" %}

  - title: "What are projection expressions?"
    anchor: "what-are-projection-queries"
    summary: "What projection expressions are"
    content: |
      {% include shared/integrations/projection-column-selection.html type="what-are-projection-queries" %}

  - title: "Projection expression requirements for Stitch"
    anchor: "projection-query-stitch-requirements"
    summary: "The requirements for projection expressions in Stitch"
    content: |
      Projection expressions are compatible with any of Stitch's Replication Methods, including Log-based Incremental.

      Projection expressions must adhere to the following:

      - **Include the table's hash/partition key (Primary Key).** If you're unsure which field is the partition key for a table, sign into your Amazon Web Services (AWS) account and look at the **Table Details** section for the table. The field in the **Primary partition key** field is the table's Primary Key.

      - **Cannot include conditional (condition) expressions.** Stitch's {{ page.display_name }} integration doesn't currently support using conditions in projection expressions.

      Projection expressions that don't meet the above criteria will result in [errors during extraction](#error-troubleshooting).

  - title: "Defining a projection expression in Stitch"
    anchor: "defining-projection-query-in-stitch"
    summary: "How to define a projection expression in Stitch"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Adding a new projection expression"
        anchor: "adding-new-projection-query"
        content: |
          {% include shared/integrations/projection-column-selection.html type="adding-new-projection-query" %}

      - title: "Modifying an existing projection expression"
        anchor: "modifying-existing-projection-query"
        content: |
          {% include shared/integrations/projection-column-selection.html type="modifying-existing-projection-query" %}

  - title: "Example projection expressions"
    anchor: "example-projection-queries"
    summary: "Some example projection expressions"
    data:
      - name: "Finn"
        is_active: true
        details: |
          age: 15, type: human
        acquaintances: |
          - Jake
          - Ice King
        acquaintances-list: |
          - Ice King
      - name: "Jake"
        is_active: true
        details: |
          age: 6, type: dog
        acquaintances: |
          - Finn
          - Lady
        acquaintances-list: |
          - Lady
      - name: "Bubblegum"
        is_active: false
        details: |
          age: 16, type: princess
        acquaintances: |
          - Finn
          - Bubblegum
        acquaintances-list: |
          - Bubblegum
      - name: "Lady"
        is_active: true
        details: |
          age: 50, type: unicorn
        acquaintances: |
          - Jake
          - Finn
        acquaintances-list: |
          - Finn
      - name: "Ice King"
        is_active: false
        details: |
          age: 900, type: king
        acquaintances: |
          - Finn
          - Bubblegum
        acquaintances-list: |
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
          Using [dot notation]({{ site.data.taps.links.dynamodb.accessing-elements  }}){:target="new"}, return specified fields in a map element. This is formatted as `<map_element_name>.<field>`.

          In this example, the expression would return the top-level `name` field and `age` and `type` fields from the `details` map.

          Refer to [{{ page.display_name }}'s documentation]({{ site.data.taps.links.dynamodb.expressions-attributes }}){:target="new"} for more examples of dot notation for map elements.
        projection-query: |
          ```json
          "name, details.age, details.type"
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

      - title: "Return specified fields in a list element"
        description: |
          To access an element in a list, use [the dereference operator]({{ site.data.taps.links.dynamodb.accessing-elements }}){:target="new"} (`[n]`), where `n` is the number of the element in the list. This is formatted as `<list_element_name>[n]`.

          In this example, the expression would return the top-level `name` field and second element from the `acquaintances` list.

          Refer to [{{ page.display_name }}'s documentation]({{ site.data.taps.links.dynamodb.expressions-attributes }}){:target="new"} for more examples of accessing fields in lists.
        projection-query: |
          ```json
          "name, acquaintances[1]"
          ```
        results: |
          {% assign results = section.data %}
          {% assign attributes = "name|acquaintances-list" | split:"|" %}
    content: |
      In this section, we'll look at some example projection expressions and their SQL equivalents.

      - [Example table data](#example-table-data)
      {% for example in section.examples %}
      - [{{ example.title }}](#{{ example.title | slugify }})
      {% endfor %}

      ### Example table data {#example-table-data}

      The examples use data from a table named `customers`, which uses the `name` field as a Primary Key. This table contains the following records:

      {% assign results = section.data %}
      {% assign headings = "name [pk] (string)|is_active (boolean)|details (object)|acquaintances (array)" | split:"|" %}
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
      <td><strong>{{ attribute | remove: "-list" }}</strong></td>
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
    summary: "How to troubleshoot projection expression errors"
    content: |
      If a table's projection expression doesn't meet [Stitch's requirements](#projection-query-stitch-requirements), a critical error will arise during Extraction. Extractions will not be successful until the issue is resolved.

  - title: "Resources"
    anchor: "projection-query-resources"
    summary: "Additional resources for projection expressions"
    content: |
      - [{{ page.display_name }} projection expression documentation]({{ site.data.taps.links.dynamodb.projection-expressions }}){:target="new"}

      ---
---