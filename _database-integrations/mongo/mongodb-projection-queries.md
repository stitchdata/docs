---
title: Selecting MongoDB Fields Using Projection Queries
keywords: mongodb, mongo, whitelisting, blacklisting, field selection, column selection
permalink: /integrations/databases/mongodb/field-selection-using-projection-queries
summary: "Specify or restrict the data Stitch replicates for MongoDB collections using projection queries.."
input: false

layout: general
toc: false
key: "mongodb-projection-queries"

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
      {% include misc/icons.html %}

      {% assign mongo-integrations = site.database-integrations | where:"name","mongodb" %}

      The following table indicates the availability of Stitch's MongoDB projection query feature for each version of the MongoDB integration.

      <table class="attribute-list">
      <tr>
      <td class="attribute-name">
      <strong>Integration version</strong>
      </td>
      <td>
      <strong>Availability</strong>
      </td>
      </tr>
      {% for integration in mongo-integrations %}
      {% if integration.this-version %}
      <tr>
      <td class="attribute-name">
      <strong>
      <a href="{{ integration.url | prepend: site.baseurl }}">{{integration.this-version | prepend: "v" }}</a>
      </strong>
      </td>
      <td>
      {% case integration.column-selection %}
      {% when true %}
      {{ supported | replace:"TOOLTIP","Field selection via projection queries is supported for this integration version." }} Supported
      {% when false %}
      {{ not-supported | replace:"TOOLTIP","Field selection via projection queries is not supported for this integration version." }} Unsupported
      {% endcase %}
      </td>
      </tr>
      {% endif %}
      {% endfor %}
      </table>

  - title: "What are projection queries?"
    anchor: "what-are-projection-queries"
    summary: "What projection queries are"
    content: |
      In MongoDB, the default for queries is to return all fields in matching documents. [Projection queries]({{ site.data.taps.links.mongodb.projection-queries }}){:target="new"} are used to specify or restrict the data returned in query results. By specifying a projection query, you can specify the fields you want to return or exclude, the conditions documents must meet to match, etc.

      For example: The default query behavior in MongoDB is similar to `SELECT *` in SQL. If you wanted to only return records where `name = 'Finn'`, you could specify this condition in a `WHERE` clause:

      ```sql
      SELECT *
        FROM customers
       WHERE name = 'Finn'
      ```

  - title: "Projection query requirements for Stitch"
    anchor: "projection-query-stitch-requirements"
    summary: "The requirements for projection queries in Stitch"
    content: |
      - Cannot exclude the `_id` field. (Equivalent to `{ _id: 0 }`) Stitch uses this field for replication.
      - MongoDB doesn't support combining inclusion and exclusion statements in the same projection query, with the exception of the `_id` field.
      - Limits on data embedded in arrays? https://docs.mongodb.com/v4.0/tutorial/project-fields-from-query-results/#project-specific-array-elements-in-the-returned-array
      - Must be valid JSON? 

  - title: "Defining a projection query in Stitch"
    anchor: "defining-projection-query-in-stitch"
    summary: "How to define a projection query in Stitch"
    content: |
      When you set a collection to replicate in Stitch, you can define a projection query for the collection in the **Collection Settings** page.

      1. In the MongoDB integration, click the **Collections to Replicate** tab.
      2. Navigate to the desired collection.
      3. Click the checkbox to the left of the collection to set it to replicate. This will also open the **Collection Details** page:

         ![The MongoDB Collection Details page in Stitch.]({{ site.baseurl }}/images/integrations/mongodb-collection-details.png)
      4. Click the **View Collection Settings** button.
      5. On the **Collection Settings** page, scroll down to the **Fields to Replicate** section.
      6. Enter the projection query you want the collection to use in the **Projection query** field:

         ![The Projection query field in the Collection Settings page in Stitch.]({{ site.baseurl }}/images/integrations/mongodb-projection-queries.png)

         **Note**: Projection queries include the `_id` field by default, so you don't need to specify it in your query.
      7. Click {{ app.buttons.save-table-settings }} to save your changes.

      Stitch will use the collection's projection query during the next scheduled replication job, even if a job is currently in progress.

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
      - title: "Return all fields in matching documents"
        description: |
          Return all fields in documents in the `customers` collection where `is_active = true`.
        projection-query: |
          ```json
          { "is_active": true }
          ```
        sql: |
          ```sql
          SELECT *
            FROM customers
           WHERE is_active = true
           ```
        results: |
          {% assign results = section.data | where:"is_active",true %}
          {% assign attributes = "name|is_active|details|acquaintances" | split:"|" %}

          <table class="attribute-list" style="margin-top: 0px;">
          <tr>
          {% for attribute in attributes %}
          <td><strong>{{ attribute }}</strong></td>
          {% endfor %}
          </tr>
          {% for result in results %}
          <tr>
          {% for attribute in attributes %}
          <td width="25%; fixed">
          {{ result[attribute] | markdownify }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

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
          {{ result[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

      - title: "Return only specified fields in matching documents"
        description: |
          Return only the specified fields (`name`, `details`) for documents in the `customers` collection where `is_active = true`.
        projection-query: |
          ```json
          { "is_active": true }, { "name": 1, "details": 1 }
          ```
        sql: |
          ```sql
          SELECT name,
                 details
            FROM customers
           WHERE is_active = true
           ```
        results: |
          {% assign results = section.data | where:"is_active",true %}
          {% assign attributes = "name|details" | split:"|" %}

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
          {{ result[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

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
          {{ result[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

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
      {{ example[attribute] | flatify | markdownify }}
      </td>

      </tr>
      {% endif %}
      {% endfor %}
      </table>
      {% endfor %}

  - title: "Resources"
    anchor: "projection-query-resources"
    summary: "Additional resources for projection queries"
    content: |
      - [MongoDB projection query documentation]({{ site.data.taps.links.mongodb.projection-queries }}){:target="new"}
      - [MongoDB dot notation documentation]({{ site.data.taps.links.mongodb.dot-notation }}){:target="new"}

---