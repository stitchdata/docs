---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Loading and Row Usage for Nested Data Structures
display-title: "Loading Nested Data Structures"

permalink: /replication/loading/understanding-loading-row-usage-for-nested-data-structures
redirect_from: /data-structure/nested-data-structures-row-count-impact
keywords: denesting arrays, denesting objects, subtables, nested data
summary: "Depending on the type of destination you're using, Stitch may deconstruct nested data structures into relational tables."

key: "de-nesting-json"
category: "preparing, loading"
content-type: "data-structuring"

layout: general
toc: true
weight: 3


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% capture callout %}
  - **Destinations**: This article is applicable only to the following destinations, as they do not natively support nested data structures:
    - Amazon Redshift
    - Amazon S3 (CSV)
    - Microsoft Azure Synapse Analytics
    - Panoply
    - PostgreSQL
  - **PostgreSQL `JSON` & `JSONB` datatypes:** The info in this article is not applicable to PostgreSQL `JSON` and `JSONB` data types. These data types will be stored as strings in your destination.{% endcapture %}

  {% include important.html first-line="**Not applicable to all destinations and data types**" content=callout %}

  To understand how Stitch loads the data it receives, you need to know a little bit about JSON.

  MongoDB and many SaaS integrations use nested structures, which means each attribute (or column) in a table could have its own set of attributes. Stitch is designed to deconstruct these nested structures into separate tables to easily query the data.

  In this article, we'll cover:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}


example-table: |
  <table style="font-size: 13px;">
    <tr>
      {% for attribute in example-record %}
        <td>
          <strong>{{ attribute.name | flatify }}</strong>
        </td>
      {% endfor %}
    </tr>
    {% for record in records %}
      <tr>
        {% for attribute in example-record %}
          <td>
            {{ attribute[record] }}
          </td>
        {% endfor %}
      </tr>
    {% endfor %}
  </table>

schema-table: |
  <table>
    <tr>
      <td align="right" width="30%; fixed">
        <strong>Column name</strong>
      </td>
      <td>
        <strong>Description</strong>
      </td>
    </tr>
    {% for attribute in attributes %}
      <tr>
        <td align="right">
          <strong>{{ attribute.name | flatify }}</strong>
        </td>
        <td>
          {{ attribute.description | flatify | markdownify }}
        </td>
      </tr>
    {% endfor %}
  </table>


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Understanding JSON data structures"
    anchor: "json-data-structures"
    summary: "How JSON data is structured"
    content: |
      When Stitch pulls data from an integration, it's pulling a series of JSON records. JSON records can contain structures called **objects** and **arrays**.

    subsections:
      - title: "Objects"
        anchor: "json-objects"
        example-record:
          - name: "product_id"
            value: "5008798"
          - name: "name"
            value: "Awesome Dino Shirt"
          - name: "price"
            value: "5.99"
          - name: "attributes__color"
            value: "blue"
          - name: "attributes__size"
            value: "large"
          - name: "attributes__type"
            value: "clothing"
          - name: "attributes__ounces"
            value: "5"
        content: |
          An object is an unordered set of name and value pairs; each set is called a property. Objects begin with a left curly bracket ( `{` ) and end with a right curly bracket ( `}` ).

          {% capture code %}
          {  
             "product_id":"5008798",
             "name":"Awesome Dino Shirt",
             "price":"5.99",
             "attributes":{               // object begins
                "color":"blue",
                "size":"large",
                "type":"clothing",
                "ounces":"5"
             }                           // object ends
          }
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

          When Stitch receives an object, the properties in the object are "flattened" into the table and columns are created. Columns created from object properties follow this naming convention: `[object_name]__[property_name]`

          If a table were created for the object in the example above, the schema would look like this:

          {% assign example-record = subsection.example-record %}
          {% assign records = "value|" | split: "|" %}

          {{ page.example-table | flatify }}

      - title: "Arrays"
        anchor: "json-arrays"
        content: |
          An array is an ordered collection of values. Values are separated by commas and can be a string (contained in double quotes), numbers, boolean, an object, or another array. Arrays begin with a left square bracket ( `[` ) and end with a right square bracket ( `]` ).

          Here's an example:

          {% capture code %}
          {
             "order_id":"1234",
             "customer_id":"100",
             "line_items":[            // array begins
                {
                   "product_id":"5008798",
                   "price":"5.99"
                }
             ]                        // array ends
          }
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

          When Stitch receives a nested array - or an array that's inside a JSON record - like the one above, it will "denest" it from the parent structure and create a subtable.

  - title: "Deconstruction of nested arrays"
    anchor: "deconstructing-nested-structures"
    summary: "How nested structures are deconstructed"
    content: |
      To give you a better understanding of how Stitch denests arrays, we'll walk you through an example using a Shopify order record. In this example, the order record is composed of three parts:

      - Core order data
      - Line items
      - Tax lines

      Here's what the JSON for the Shopify order looks like:

      {% capture code %}
      {
         "order_id":"1234",
         "created_at":"2015-01-01 00:00:00",
         "customer_id":"100",
         "line_items":[                         // line item record begins
            {
               "product_id":"5008798",
               "price":"5.99",
               "quantity":"1",
               "tax_lines":[                    // tax line record begins
                  {
                     "price":"5.99",
                     "rate":"0.06",
                     "title":"State Tax"
                  }
               ]                               // tax line record ends
            }
         ]                                    // line item record ends
      }
      {% endcapture %}

      {% include layout/code-snippet.html code=code %}

      This record contains three levels of data due to the nested arrays. Stitch will denest the arrays from the top level record - in this case, the core order info - and create subtables.

      From this one order record, three tables will be created:

      <table>
        <tr>
          <td width="30%; fixed">
            <strong>Table name</strong>
          </td>
          <td>
            <strong>Description</strong>
          </td>
        </tr>
        <tr>
          <td>
            <strong>orders</strong>
          </td>
          <td>
            This table contains the core order data: order ID, created timestamp, and customer ID.
          </td>
        </tr>
        <tr>
          <td>
            <strong>orders__line_items</strong>
          </td>
          <td>
            This table contains the line item info: product ID, price, and quantity.
          </td>
        </tr>
        <tr>
          <td>
            <strong>orders__line_items__tax_lines</strong>
          </td>
          <td>
            This table contains the tax line info: price, rate, and title.
          </td>
        </tr>
      </table> 

  - title: "Connecting subtables to top level records"
    anchor: "connecting-subtables-to-top-level-records"
    summary: "How to connect subtables to top level records"
    content: |
      When subtables are created, Stitch will append a few columns to be used as composite keys that enable you to connect subrecords back to their parent. Let's take a look at the schemas for each of the Shopify tables to get a better idea of how this works.

      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Top level: Core order data"
        anchor: "top-level"
        example-record:
          - name: "order_id [pk]"
            value: "1234"
          - name: "created_at"
            value: "2015-01-01 00:00:00"
          - name: "customer"
            value: "100"
        content: |
          This table contains the order record's Primary Key, `order_id`.

          {% assign example-record = subsection.example-record %}
          {% assign records = "value|" | split:"|" %}

          {{ page.example-table | flatify }}

      - title: "Second level: Line items"
        anchor: "second-level"
        attributes:
          - &top-level-pk
            name: |
              {{ system-column.source-key | replace: "y_", "y_[pk_column_name]" }}
            description: |
              This contains the top level record's Primary Key.

              In your destination, `[pk_column_name]` will be replaced with the name of the Primary Key column for the top level record. In this example, the column would be `{{ system-column.source-key | append: "order_id" }}`.
          - name: |
              {{ system-column.level-id | replace: '#', '0' }}
            description: |
              This forms part of a composite primary key for this row and can be used to associate further down the line nested rows to this parent. This will auto-increment for each unique record in the table, beginning with 0. When used with the `{{ system-column.source-key | replace: "y_", "y" }}` column, it creates a unique identifier for the row.

               For the Shopify example, the value for the first line item record would be 0, the second 1, the third 2, and so on.

               **We recommend always joining the top level table to the nested table** - this will allow you to avoid queries that may have outdated data.
        example-record:
          - name: |
              {{ system-column.source-key | append: "order_id" }}
            value-1: "1234"
            value-2: "1234"
          - name: |
              {{ system-column.level-id | replace: '#', '0' }} 
            value-1: "0"
            value-2: "1"
          - name: "product_id"
            value-1: "5008798"
            value-2: "3445689"
          - name: "price"
            value-1: "5.99"
            value-2: "10.99"
          - name: "quantity"
            value-1: "1"
            value-2: "1"
        content: |
          In addition to the attributes in the nested record - in this case, product ID, price, and quantity for line items - Stitch will add these columns to second level tables:

          {% assign attributes = subsection.attributes %}
          {{ page.schema-table | flatify }}

          Here's what the `orders__line_items` table would look like if another line item were added to the order record:

          {% assign example-record = subsection.example-record %}
          {% assign records = "value-1|value-2" | split:"|" %}

          {{ page.example-table | flatify }}

          If you wanted to return all line items for order number `1234`, you’d run the following query:

          {% capture code %}SELECT *
            FROM orders__line_items li
           WHERE {{ system-column.source-key | append: "order_id" }} = 1234
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

      - title: "Third level: Tax lines"
        anchor: "third-level"
        attributes:
          - *top-level-pk
          - name: |
              {{ system-column.level-id | replace: '#', '0' }}
            description: |
              This is the foreign key for the second level (`orders__line_items`) table. Combined with the source key (`{{ system-column.source-key | append: "order_id" }}`), it can be used to find the parent.
          - name: |
              {{ system-column.level-id | replace: '#', '1' }}
            description: |
              This forms part of a composite primary key for this row and can be used to associate further down the line nested rows to this parent.

              For the Shopify example, the first tax line record would be 0, the second 1, the third 2, and so on.
        example-record:
          - name: |
              {{ system-column.source-key | append: "order_id" }}
            value-1: "1234"
            value-2: "1234"
          - name: |
              {{ system-column.level-id | replace: '#', '0' }} 
            value-1: "0"
            value-2: "1"
          - name: |
              {{ system-column.level-id | replace: '#', '1' }} 
            value-1: "0"
            value-2: "0"
          - name: "price"
            value-1: "5.99"
            value-2: "10.99"
          - name: "rate"
            value-1: ".06"
            value-2: ".06"
          - name: "title"
            value-1: "State Tax"
            value-2: "State Tax"
        content: |
          In addition to the attributes in the nested record - in this case, price, rate, and title for tax lines - Stitch will add these columns to third level tables:

          {% assign attributes = subsection.attributes %}
          {{ page.schema-table | flatify }}

          Here's what the `orders__line_items__tax_lines` table would look like if another tax line were added to the order record:

          {% assign example-record = subsection.example-record %}
          {% assign records = "value-1|value-2" | split:"|" %}

          {{ page.example-table | flatify }}

          If you wanted to return all line items and tax lines for order number `1234`, you’d run the following query:

          {% capture code %}SELECT *
                FROM orders__line_items li
          INNER JOIN orders__line_items__tax_lines tl
                  ON tl._{{ system-column.level-id | replace: '#', '0' }} = li._{{ system-column.level-id | replace: '#', '0' }}
                 AND tl._{{ system-column.source-key | append: "order_id" }} = li._{{ system-column.source-key | append: "order_id" }}
               WHERE {{ system-column.source-key | append: "order_id" }} = 1234
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

  - title: "Impact on total row count"
    anchor: "impact-on-total-row-count"
    summary: "How nested structures impact row count"
    content: |
      Because Stitch is built to denest nested arrays into separate tables, **you can expect to see more rows in Stitch and in your destination than what's in the source itself**. 

      To sum it up: row count in original data source ≠ the row count reflected in the Stitch app or your destination.

      Consider the Shopify example. Order 1234 isn't just a single row in the destination. Because Stitch had to denest subrecords and create tables to accommodate these records, you can expect to see more than just one row for order 1234 moving through Stitch.

      From the top level record, there's the row in the `orders` table:

      {% assign connect-subtables-section = page.sections | where:"anchor","connecting-subtables-to-top-level-records" | first %}
      {% assign top-level = connect-subtables-section.subsections | where:"anchor","top-level" | first %}

      {% assign example-record = top-level.example-record %}
      {% assign records = "value|" | split:"|" %}

      {{ page.example-table | flatify }}

      From the second level record, we have the rows in the `orders__line_items` table:

      {% assign second-level = connect-subtables-section.subsections | where:"anchor","second-level" | first %}
      {% assign example-record = second-level.example-record %}
      {% assign records = "value-1|value-2" | split:"|" %}

      {{ page.example-table | flatify }}

      From the third level record, we have the rows in the `orders__line_items__tax_lines` table:

      {% assign third-level = connect-subtables-section.subsections | where:"anchor","third-level" | first %}

      {% assign example-record = third-level.example-record %}
      {% assign records = "value-1|value-2" | split:"|" %}

      {{ page.example-table | flatify }}

      In total, Stitch will count each of these rows (a total of 5) towards your row count. So while there is only one record in the Shopify data source, inside of Stitch you'll see 5 replicated rows and there'll be 5 rows in your destination.

  - title: "Tips for reducing your row count"
    anchor: "reduce-your-row-count"
    content: |
      Understanding how Stitch handles nested data structures will in turn give you a deeper understanding of how your data is structured once it gets to your destination. While this knowledge will help comprehending the data's structure, what about applying it to how many rows you're using? How can you plan ahead?

      - **For starters**, check out the [Reducing Your Row Count]({{ link.getting-started.row-usage | prepend: site.baseurl | append: "#reducing-your-usage" }}) guide for detailed tips and gotchas on how to keep your row count in line.
      - **Take some time to learn about how the data for your integrations is structured and how it's replicated.**

         Check out the [SaaS Schemas section]({{ site.baseurl }}/integrations/saas) for detailed info on Replication Methods and the tables you can expect to see for each integration. Every article links to that service's API documentation, which is the best way to learn about the data for that integration is structured.
      - **Set your integrations to replicate less frequently,** if feasible.
---
{% include misc/data-files.html %}