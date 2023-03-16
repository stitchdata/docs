---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Chargebee (v1)
permalink: /integrations/saas/chargebee
keywords: chargebee, integration, schema, etl chargebee, chargebee etl, chargebee schema
layout: singer
# input: false

key: "chargebee-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "chargebee"
display_name: "Chargebee"

singer: true 
tap-name: "Chargebee"
repo-url: https://github.com/singer-io/tap-chargebee

this-version: "1"

api: |
  [{{ integration.display_name }} v2 API](https://apidocs.chargebee.com/docs/api){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "http://status.chargebee.com/"

api-type: "platform.chargebee"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true



# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  This integration supports {{ integration.display_name }} sites that use version 1.0 or version 2.0 of {{ integration.display_name }}'s Product Catalog. The Product Catalog version your site uses determines which tables and fields you can select for replication, however. Refer to the [Table and field availability and {{ integration.display_name }} product catalogs section](#product-catalog-versions) for more info.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirement-items:
- item: |
    Your **Order Management** feature must be enabled before you can sync your `orders` table. Refer to the [{{ integration.display_name }} docs](https://www.chargebee.com/docs/orders.html) for more information.

setup-steps:
  - title: "Generate an API Key"
    anchor: "generate-api-key"
    content: |
      First, you'll generate a {{ integration.display_name }} API Key for Stitch. This will allow Stitch to read data from your {{ integration.display_name }} account using the {{ integration.display_name }} API.

      {% include layout/image.html type="right" file="/integrations/chargebee-create-api-key.png" max-width="450" %}
      1. Sign into your [{{ integration.display_name }} account](https://app.chargebee.com/login){:target="new"}.
      2. In the left sidenav, click **Settings > Configure {{ integration.display_name }}**.
      3. Click the **API keys and webhooks** button.
      4. On the API Keys page, click the **+ Add API Key** button. The **Create an API Key** modal will display.
      5. Select **Read-Only Key** as the API key type.
      6. Select **All** to define the API key's access. This will grant read-only access to your {{ integration.display_name }} site.
      7. In the **Name the API key** field, enter `Stitch`.
      8. Click **Create Key**.

      {{ integration.display_name }} will create the API key and redirect you back to the API Keys page:

      ![]({{ site.baseurl }}/images/integrations/chargebee-api-key.png)

      Copy the API key somwhere handy - you'll need it to complete the setup in Stitch.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Key** field, paste the API key you generated in [Step 1](#generate-api-key).
      5. In the **Site** field, enter the name of your {{ integration.display_name }} site. This can be found in the URL of your {{ integration.display_name }} site. For example: If the URL was `https://stitch.chargebee.com`, only `stitch` would be entered into this field.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Table and field availability and {{ integration.display_name }} product catalogs"
    anchor: "product-catalog-versions"
    content: |
      The availability of some tables and fields is dependent on the {{ integration.display_name }} Product Catalog version your {{ integration.display_name }} site uses. Refer to [{{ integration.display_name }}'s documentation](https://www.chargebee.com/docs/2.0/product-catalog.html){:target="new"} for more info, including how to identify which Product Catalog version your site is using.

      The following table contains a list of the tables included in this version of Stitch's {{ integration.display_name }} integration and the Product Catalog version required to replicate the table.

      Additionally, some fields are also subject to Product Catalog version requirements. These fields are noted in the attribute documentation for individual tables.

      **Note**: If your site is using a Product Catalog version that a table or field doesn't support, the table/field won't display in the **Tables to Replicate** tab in Stitch. For example: If the site is using v2.0 of the Product Catalog, tables/fields that require v1.0 won't display in Stitch.

      {% assign all-integration-tables = site.integration-schemas | where:"tap",integration.name %}
        {% assign integration-tables-this-version = all-integration-tables | where:"version",integration.this-version | sort_natural:"name" %}

      <table>
        <tr>
          <td>
            <strong>Table name</strong>
          </td>
          <td> 
            <strong>Required Product Catalog version</strong>
          </td>
        </tr>
        {% for table in integration-tables-this-version %}
          <tr>
            <td>
              <a href="#{{ table.name | slugify }}">
                {{ table.name }}
              </a>
            </td>
            <td>
              {% case table.product-catalog-version %}
                {% when 'any' %}
                  Any
                {% else %}
                  {{ table.product-catalog-version | append: ".0 only" }}
              {% endcase %}
            </td>
          </tr>
        {% endfor %}
      </table>


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/chargebee/v1

table-type: |
  {% capture product-catalog-version %}
  {% case table.product-catalog-version %}
    {% when 'any' %}
    for sites using **any {{ integration.display_name }} Product Catalog version**.

    {% when 'v1' %}
    for {{ integration.display_name }} sites using **v1.0 of {{ integration.display_name }}'s Product Catalog**.

    {% when 'v2' %}
    for {{ integration.display_name }} sites using **v2.0 of {{ integration.display_name }}'s Product Catalog**.
  {% endcase %}
  {% endcapture %}

  **Note**: This table is available {{ product-catalog-version | flatify | strip_newlines }} Refer to the [Table and field availability and {{ integration.display_name }} Product Catalogs section](#product-catalog-versions) for more info.

product-catalog-v2: |
  This attribute will be present only if your {{ integration.display_name }} site uses v2.0 of {{ integration.display_name }}'s Product Catalog. Refer to the [Table and field availability and {{ integration.display_name }} Product Catalogs section](#product-catalog-versions) for more info.

product-catalog-v1: |
  This attribute will be present only if your {{ integration.display_name }} site uses v1.0 of {{ integration.display_name }}'s Product Catalog. Refer to the [Table and field availability and {{ integration.display_name }} Product Catalogs section](#product-catalog-versions) for more info.
---
{% assign integration = page %}
{% include misc/data-files.html %}