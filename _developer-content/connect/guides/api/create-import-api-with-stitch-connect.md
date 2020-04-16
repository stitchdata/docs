---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Create and Configure an Import API Source with the Connect API
permalink: /developers/stitch-connect/guides/create-import-api-integration-with-stitch-connect
summary: "Using the Stitch Connect API, create a new Import API source and generate an access token. You'll also learn how to push data to the Import API after the source has been configured."

product-type: "connect"
content-type: "guide"
content-id: "create-import-api-source"
topics: "sources, import api, authentication"

key: "import-api-connect"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: source
order: 5

description: "Create an Import API source using the Stitch Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Manage Import API access tokens in Connect"
    link: "{{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl }}"

  - title: "Structuring data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% capture import-api-notice %}
  **Note**: This guide focuses on creating an Import API source using Stitch Connect. Refer to the [Managing Import API access tokens in Stitch guide]({{ link.import-api.guides.manage-access-tokens-stitch | prepend: site.baseurl }}) for instructions on generating API access tokens in the Stitch web app.
  {% endcapture %}

  {% include note.html type="single-line" content=import-api-notice %}

  {{ page.summary }}


# -------------------------- #
#     EXAMPLE TABLE DATA     #
# -------------------------- #

example-table:
  - name: "{{ system-column.batched-at }}"
    value: "2019-02-02 00:44:38.988+00"
  - name: "{{ system-column.received-at }}"
    value: "2019-02-02 00:43:53.75+00"
  - name: "{{ system-column.sequence }}"
    value: "100"
  - name: "{{ system-column.table-version }}"
    value: "0"
  - name: "id"
    value: "1"
  - name: "name"
    value: "Finn"
  - name: "updated_at"
    value: "2019-02-02T00:38:33+00:00"


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch Enterprise feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.


# -------------------------- #
#       TUTORIAL STEPS       #
# -------------------------- #

steps:
  - title: "Get the Import API's report card"
    anchor: "get-iapi-report-card"
    content: |
      When preparing for source creation, the first step is to get the report card for the source you want to create. The report card contains information about the steps required to fully configure a source.

      Use [GET {{ site.data.connect.core-objects.source-types.get.name | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.source-types.get.anchor | prepend: site.baseurl }}) to get the report card for source `type: import_api`:

      {% assign right-bracket = "}" %}

      {% capture code %}curl {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.source-types.get.name | flatify | remove: right-bracket | replace:"{source_type","import_api" | strip_newlines }} \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
      {% endcapture %}

      {% assign description = "GET " | append: site.data.connect.core-objects.source-types.get.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) with a [Connection step object]({{ link.connect.api | append: site.data.connect.data-structures.connection-steps.section | prepend: site.baseurl }}):

      {% capture code %}{
        "type": "import_api",
        "current_step": 1,
        "current_step_type": "form",
        "steps": [
          {
            "type": "form",
            "properties": []
          },
          {
            "type": "fully_configured",
            "properties": []
          }
        ],
        "details": {
          "pricing_tier": "standard",
          "pipeline_state": "released",
          "default_start_date": "-1 year",
          "default_scheduling_interval": 60,
          "protocol": "import_api",
          "access": true
        }
      }
      {% endcapture %}

      {% assign description = "Response for GET " | append: site.data.connect.core-objects.source-types.get.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      For Import API sources, the only step to being `fully_configured` is to complete the `form` step.

  - title: "Create the source and complete the form step"
    anchor: "create-source-complete-form-step"
    content: |
      Use [POST {{ site.data.connect.core-objects.sources.create.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create.anchor }}) to create the Import API source. The request body must include the following top-level properties:

      - `type`: This must be `import_api`.
      - `display_name`: {{ site.data.connect.general.common.attributes.display-name }}

         For example:  A display name of `Import API` will create a destination schema named `import_api`.

      This request will complete the `form` step outlined in the source's report card, which you retrieved in [Step 1](#get-iapi-report-card):

      {% capture code %}curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create.name | flatify | strip_newlines }} \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>' \
           -d $'{
                  "type": "import_api",
                  "display_name": "Import API"
                }
      {% endcapture %}

      {% assign description = "POST " | append: site.data.connect.core-objects.sources.create.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) containing the ID, [report card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.report-cards.source.section }}), and current configuration status of the Import API source, which will be `fully_configured`:

      {% capture code %}{{ site.data.connect.code-examples.sources.import-api.full-object }}
      {% endcapture %}

      {% assign description = "Response for POST " | append: site.data.connect.core-objects.sources.create.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      Note the `id` value - you'll need it to complete the next step.

  - title: "Generate an Import API access token"
    anchor: "generate-an-import-api-access-token"
    content: |
      Requests made to the Import API must include an access token associated with the Import API source. In this step, you'll generate an access token for the Import API.

      Using the Import API source's ID, make a request to [POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create-iapi-token.anchor }}):

      {% capture code %}curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify | remove: right-bracket | replace:"{source_id","126890" | strip_newlines }} \
           -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
           -H "Content-Type: application/json"
      {% endcapture %}

      {% assign description = "POST " | append: site.data.connect.core-objects.sources.create-iapi-token.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      The response will be an [Import API access token object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.import-api-access-token.section }}) with an `access_token` property. The value of this property is the access token you'll need to include in requests made to the Import API:

      {% capture code %}{
        "id": 828792559,
        "access_token": "<IMPORT_API_ACCESS_TOKEN>"
      }
      {% endcapture %}

      {% assign description = "Response for POST " | append: site.data.connect.core-objects.sources.create-iapi-token.name %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      **Note**: The API will only return the Import API access token once, immediately after generation. Store the access token and its ID somewhere secure, [as you'll need the access token ID to revoke the token]({{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl | append: "#rotate-import-api-access-tokens" }}).

  - title: "Push data to the Import API"
    anchor: "push-data-import-api"
    content: |
      Now that the Import API is `fully_configured`, you start pushing data to it.

      While you used the Connect API to create the Import API source, to actually push data, you'll need to use the [Import API]({{ link.import-api.api | prepend: site.baseurl }}). 

      {% for substep in step.substeps %}
      - [Step 4.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Build the request header"
        anchor: "build-import-api-request-header"
        content: |
          Pushing data to the Import API is accomplished by making a request to [POST {{ site.data.import-api.core-objects.batch.url }}]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.batch.anchor }}). The request header must include the Import API access token and a supported media type of `Content-Type: application/json`:

          {% capture code %}curl -X POST {{ site.data.import-api.api.base-url | strip_newlines }}{{ site.data.import-api.core-objects.batch.url | flatify | strip_newlines }} \
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>' \
          {% endcapture %}

          {% assign description = "POST " | append: site.data.import-api.core-objects.batch.url %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

      - title: "Submit the request"
        anchor: "submit-request-to-import-api"
        ## NOTE: Part of this content lives in _developer-content/import-api/guides/import-api-quick-start.md. See the `iapi-push` assignment, below.
        content: |
          {% assign iapi-quick-start = site.developer-content | where:"key","import-api-quick-start" | first %}
          {% assign iapi-push = iapi-quick-start.steps | where:"anchor","push-data-to-stitch" | first %}

          {% capture out-of-scope-notice %}
          **Note**: Instructions for structuring the data in request bodies for the Import API is outside the scope of this guide. Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for instructions and examples.
          {% endcapture %}

          {% include note.html type="single-line" content=out-of-scope-notice %}

          {{ iapi-push.content | flatify | markdownify }}

          **Note**: Due to the structure of Stitch's replication process, data pushed to the Import API will not immediately be available in the destination. The successful response in this section refers only to Stitch **accepting** the data, not it being loaded.

  - title: "Verify the data in the destination"
    anchor: "verify-data-destination"
    content: |
      After you've pushed a batch of data to the Import API, Stitch will queue it for processing.

      Stitch's replication process consists of three distinct steps: Extraction, preparation, and loading. Each step occurs independently and takes a bit of time to complete, which means you won't immediately see data in your destination after it's been pushed to the Import API. 

      When Stitch loads the data into the destination, it will be in the schema or dataset associated with the [Import API source you created](#create-source-complete-form-step). In this example, Stitch would create a table named `customers` with a single record in a schema named `import_api`:

      <table class="attribute-list">
      <tr>
      <td><strong>id</strong></td>
      <td><strong>name</strong></td>
      <td><strong>age</strong></td>
      <td><strong>has_magic</strong></td>
      </tr>
      <tr>
      <td>1</td>
      <td>Finn</td>
      <td>15</td>
      <td>false</td>
      </tr>
      </table>

      **Note**: How data is structured in your destination depends on how attributes are typed in Import API requests **and** the type of destination Stitch loads data into. Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for more info.

      ---


# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  Congratulations on configuring your Import API source! Next, we recommend checking out:

  - [**Structuring data for the Import API**]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}): Learn how to structure and type data in your Import API requests.
  - [**Sequencing data for the Import API**]({{ link.import-api.guides.sequence-data | prepend: site.baseurl }}): Learn how the Import API considers data points for loading, which affects how data is updated in your destination.
  - [**Managing and revoking Import API access tokens via the Connect API**]({{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl }}): Learn how to manage and revoke Import API access tokens using the Connect API.
---