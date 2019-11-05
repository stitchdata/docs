---
title: Google BigQuery and Storing Nested Data Structures
permalink: /replication/loading/google-bigquery-storing-nested-data-structures

layout: general
toc: true
feedback: false

keywords: TODO
summary: "todo"

key: "bigquery-nested-data"

this-version: "2.0"

intro: |
  {% include misc/data-files.html %}

  Google BigQuery supports nested records within tables, [whether it's a single record or repeated values]({{ site.data.destinations.resource-links.bigquery.nested-repeated }}){:target="new"}.

  Unlike the conventional method to [denormalization](https://en.wikipedia.org/wiki/Denormalization){:target="new"}, in Google BigQuery records are expressed using nested and repeated fields.

  Instead of flattening attributes into a table, this approach localizes a record's subattributes into a single table. Maintaining nested records removes the need for repeating data, creating additional subtables, or using joins during analysis.

  For example: Below is a record from a table named `people`. In this table, each person can only have a single `type`, but they might have multiple `friends`:

  ```json
  {
     "id":1,
     "name":"Finn",
     "details":{
        "type":"human",
        "has_magic":false
     },
     "friends":[
        {
           "id":2,
           "name":"Jake"
        },
        {
           "id":3,
           "name":"Bubblegum"
        },
        {
           "id":4,
           "name":"BMO"
        }
     ]
  }
  ```

  In this guide, we'll how this data will be loaded into Google BigQuery, including:
  
  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


schema-display-table: |
  {% assign attributes ="field-name|type|mode" | split:"|" %}

  <table class="attribute-list">
  <tr>
  {% for attribute in attributes %}
  {% if forloop.first == true %}
  <td class="attribute-name">
  {% else %}
  <td>
  {% endif %}
  <strong>
  {{ attribute | replace:"-"," " | capitalize }}
  </strong>
  </td>
  {% endfor %}
  </tr>
  {% for field in table-schema %}
  <tr>
  {% for attribute in attributes %}
  {% if forloop.first == true %}
  <td class="attribute-name">
  {{ field[attribute] }}
  {% else %}
  <td>
  {{ field[attribute] | upcase }}
  {% endif %}
  </td>
  {% endfor %}
  </tr>
  {% endfor %}
  </table>

data-display-table: |
  {% assign displayable-fields = table-schema | where:"displayable",true %}

  <table class="attribute-list">
  <tr>
  {% for field in displayable-fields %}
  <td>
  <strong>
  {{ field.field-name }}
  </strong>
  </td>
  {% endfor %}
  </tr>
  {% for record in table-data %}
  <tr>
  {% for field in displayable-fields %}
  {% assign clean-field-name = field.field-name | remove: "<strong>" | remove: "</strong>" %}
  <td>
  {{ record[clean-field-name] }}
  </td>
  {% endfor %}
  </tr>
  {% endfor %}
  </table>

sections:
  - title: "Storing nested maps (JSON objects)"
    anchor: "storing-nested-maps"
    summary: "How Stitch stores nested maps, or JSON objects"
    table-schema:
      - field-name: "<strong>id</strong>"
        type: "integer"
        mode: "nullable"
        displayable: true

      - field-name: "<strong>name</strong>"
        type: "string"
        mode: "nullable"
        displayable: true

      - field-name: "<strong>details</strong>"
        type: "record"
        mode: "nullable"
        displayable: false

      - field-name: "details.<strong>type</strong>"
        type: "string"
        mode: "nullable"
        displayable: true

      - field-name: "details.<strong>has_magic</strong>"
        type: "boolean"
        mode: "nullable"
        displayable: true
    table-data:
      - id: "1"
        name: "Finn"
        details.type: "human"
        details.has_magic: "false"
    content: |
      A nested map is also called an `object` in JSON. An object is surrounded by curly braces (`{ }`) and contains a series of key/value pairs. Keys are strings enclosed in double quotes (`" "`).

      For example: This record contains a `details` object, which contains `type` and `has_magic` keys:

      ```json
      {
         "id":1,
         "name":"Finn",
         "details":{
            "type":"human",
            "has_magic":false
         }
      }
      ```

      When records containing objects are loaded into Google BigQuery, the object is loaded using the `RECORD` type and a mode of `NULLABLE`.

      For example: The above record would create this table schema in Google BigQuery:

      {% assign table-schema = section.table-schema %}
      {% assign table-data = section.table-data %}

      {{ page.schema-display-table | flatify }}

      And the data in the table would be similar to the following:

      {{ page.data-display-table | flatify }}

      To query nested data using the [standard SQL syntax]({{ site.data.destinations.resource-links.bigquery.standard-sql-syntax }}){:target="new"}, you can use dot notation to indicate the field(s) you want to reference. For example: The sample query below will return the `id`, `name`, and `details.type` fields:

      ```sql
      SELECT id,
             name,
             details.type
        FROM people

      +----+------+--------------+
      | id | name | details.type |
      +----+------+--------------+
      | 1  | Finn | human        |
      +----+------+--------------+
      ```

  - title: "Storing nested records (JSON arrays)"
    anchor: "storing-nested-records"
    summary: "How Stitch stores nested records, or JSON arrays"
    content: |
      A nested record is also called an `array` in JSON. An array is surrounded by square brackets (`[ ]`) and contains an ordered list of values. Values can be strings, numbers, booleans, objects, null, or more arrays. [todo- IS NULL VALID HERE?]

      When records containing arrays are loaded into Google BigQuery, the array is loaded using the `RECORD` type and a mode of [`REPEATED`]({{ site.data.destinations.resource-links.bigquery.nested-repeated }}){:target="new"}. By using the `REPEATED` mode to store nested records, Stitch can avoid repeating data or creating additional subtables. This functionality removes the need for joins when analyzing data, making raw data easier to read and faster to compute.

      For items in the array, Stitch will handle each item like an object field. Items will be loaded using the `RECORD` type, a mode of `NULLABLE`, and a field name of `value`.

      How the array is structured determines how the data it contains will be loaded into Google BigQuery. In this section, we'll cover some examples and demonstrate how the source data for each one would be loaded into Google BigQuery:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

      Refer to [Google's documentation]({{ site.data.destinations.resource-links.bigquery.query-nested-records }}){:target="new"} for more info on querying nested records.

    subsections:
      - title: "Array of strings or numbers"
        anchor: "arrays--strings-numbers"
        table-schema:
          - field-name: "<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friends</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friends.<strong>value</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friend_ids</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.<strong>value</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true
        table-data:
          - id: "1"
            name: "Finn"
            friends.value: "Jake"
            friend_ids.value: "2"

          - id: ""
            name: ""
            friends.value: "Bubblegum"
            friend_ids.value: "3"

          - id: ""
            name: ""
            friends.value: "BMO"
            friend_ids.value: "4"
        content: |
          In this example, the record contains two arrays: `friends`, an array of strings, and `friend_ids`, an array of integers:

          ```json
          {
             "id":1,
             "name":"Finn",
             "friends":["Jake","Bubblegum","BMO"],
             "friend_ids":[2, 3, 4]
          }
          ```

          The above record would create this table schema in Google BigQuery:

          {% assign table-schema = subsection.table-schema %}
          {% assign table-data = subsection.table-data %}

          {{ page.schema-display-table | flatify }}

          And the data in the table would be similar to the following:

          {{ page.data-display-table | flatify }}

      - title: "Array of objects"
        anchor: "arrays--objects"
        table-schema:
          - field-name: "<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friends</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friends.<strong>value</strong>"
            type: "record"
            mode: "nullable"
            displayable: false

          - field-name: "friends.value.<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "friends.value.<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true
        table-data:
          - id: "1"
            name: "Finn"
            friends.value.id: "2"
            friends.value.name: "Jake"

          - id: ""
            name: ""
            friends.value.id: "3"
            friends.value.name: "Bubblegum"

          - id: ""
            name: ""
            friends.value.id: "4"
            friends.value.name: "BMO"
        content: |
          In this example, the record contains a single array named `friends`, which contains a series of objects:

          ```json
          {
             "id":1,
             "name":"Finn",
             "friends":[
                {
                   "id":2,
                   "name":"Jake"
                },
                {
                   "id":3,
                   "name":"Bubblegum"
                },
                {
                   "id":4,
                   "name":"BMO"
                }
             ]
          }
          ```

          The above record would create this table schema in Google BigQuery:

          {% assign table-schema = subsection.table-schema %}
          {% assign table-data = subsection.table-data %}

          {{ page.schema-display-table | flatify }}

          And the data in the table would be similar to the following:

          {{ page.data-display-table | flatify }}

      - title: "Array of arrays"
        anchor: "arrays--arrays"
        table-schema:
          - field-name: "<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friend_ids</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.<strong>value</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.value.<strong>value</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true
        table-data:
          - id: "1"
            name: "Finn"
            friend_ids.value.value: "2"

          - id: ""
            name: ""
            friend_ids.value.value: "3"

          - id: ""
            name: ""
            friend_ids.value.value: "4"

          - id: ""
            name: ""
            friend_ids.value.value: "5"
        content: |
          In this example, the record contains an array (`friend_ids`) which contains a series of arrays:

          ```json
          {
             "id":1,
             "name":"Finn",
             "friend_ids":[
                [2,3],
                [4,5]
             ]
          }
          ```

          The above record would create this table schema in Google BigQuery:

          {% assign table-schema = subsection.table-schema %}
          {% assign table-data = subsection.table-data %}

          {{ page.schema-display-table | flatify }}

          And the data in the table would be similar to the following:

          {{ page.data-display-table | flatify }}

      - title: "Array containing multiple data types"
        anchor: "array--multiple-data-types"
        table-schema:
          - field-name: "<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friend_ids</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.<strong>value</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "friend_ids.<strong>value__st</strong>"
            type: "string"
            mode: "nullable"
            displayable: true
        table-data:
          - id: "1"
            name: "Finn"
            friend_ids.value: ""
            friend_ids.value__st: "2"

          - id: ""
            name: ""
            friend_ids.value: ""
            friend_ids.value__st: "3"

          - id: ""
            name: ""
            friend_ids.value: "4"
            friend_ids.value__st: ""
        content: |
          In this example, the record contains a single array named `friend_ids`. Notice that the first two values in the array are strings (ex: `"2"` versus `2`), and the last value is an integer (ex: `4` versus `"4"`):

          ```json
          {
             "id":1,
             "name":"Finn",
             "friend_ids":["2", "3", 4]
          }
          ```

          To accommodate the multiple data types, Stitch will create additional `value` columns, one for each data type, and append a data type suffix to the name of each additional column.

          In this example, the `friend_ids.value` column will store all `INTEGER` data, and Stitch will create an additional `friend_ids.value__st` column to store all `STRING` data:

          {% assign table-schema = subsection.table-schema %}
          {% assign table-data = subsection.table-data %}

          {{ page.schema-display-table | flatify }}

          And the data in the table would be similar to the following:

          {{ page.data-display-table | flatify }}

          [TODO- ADD LINK TO DATA TYPING/COLUMN SPLIT DOCS]

      - title: "Array of nested arrays"
        anchor: "array--nested-arrays"
        table-schema:
          - field-name: "<strong>id</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>name</strong>"
            type: "string"
            mode: "nullable"
            displayable: true

          - field-name: "<strong>friend_ids</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.<strong>value</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.value.<strong>value</strong>"
            type: "record"
            mode: "repeated"
            displayable: false

          - field-name: "friend_ids.value.value.<strong>value</strong>"
            type: "integer"
            mode: "nullable"
            displayable: true
        table-data:
          - id: "1"
            name: "Finn"
            friend_ids.value.value.value: "2"

          - id: ""
            name: ""
            friend_ids.value.value.value: "3"

          - id: ""
            name: ""
            friend_ids.value.value.value: "4"

          - id: ""
            name: ""
            friend_ids.value.value.value: "5"
        content: |
          In this example, the record contains an array (`friend_ids`) which contains a series of nested arrays:

          ```json
          {
             "id":1,
             "name":"Finn",
             "friend_ids":[
                [
                  [2,3]
                ],
                [
                  [4,5]
                ]
             ]
          }
          ```

          The above record would create this table schema in Google BigQuery:

          {% assign table-schema = subsection.table-schema %}
          {% assign table-data = subsection.table-data %}

          {{ page.schema-display-table | flatify }}

          And the data in the table would be similar to the following:

          {{ page.data-display-table | flatify }}

  - title: "Resources"
    anchor: "resources"
    summary: "Some additional resources"
    content: |
      - [Querying nested records (Google documentation)]({{ site.data.destinations.resource-links.bigquery.query-nested-records }}){:target="new"}
      - [Nested and repeated records (Google documentation)]({{ site.data.destinations.resource-links.bigquery.nested-repeated }}){:target="new"}


---