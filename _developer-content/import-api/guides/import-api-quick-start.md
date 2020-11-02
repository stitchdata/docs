---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Import API Quick Start
permalink: /developers/import-api/guides/quick-start
summary: "Stitch's Import API allows you to push arbitrary data from a source to your Stitch account. Generate your API credentials and push your first batch of data with this guide."

doc-type: "tutorial"

product-type: "import-api"
content-type: "guide"
content-id: "stitch-import-api-quick-start"

key: "import-api-quick-start"

region-selector: true

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /import-api/guides page.
icon: file
order: 1

display-title: "Import API Quick Start"
description: "Generate your Import API credentials and push your first batch of data."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Manage Import API access tokens in Stitch"
    link: "{{ link.import-api.guides.manage-access-tokens-stitch | prepend: site.baseurl }}"

  - title: "Structuring and typing data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Sequencing data for the Import API"
    link: "{{ link.import-api.guides.sequence-data | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"



# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **An active Stitch account.** To create an account, [sign up for a free trial here]({{ site.home }}){:target="new"}.


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }}


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #

steps:
  - title: "Obtain your API credentials"
    anchor: "obtain-api-credentials"
    content: |
      The Import API uses an API access token to authenticate requests. In this step, you'll create an Import API integration in your Stitch account and generate an API access token.

      We're using the Stitch app to generate the access token, but you can also use the [Connect API if your Stitch account has access]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl }}).

      {% include developers/import-api/obtaining-credentials.html type="generate-new-access-token" %}

  - title: "Retrieve the correct Import API base URL for your region"
    anchor: "verify-your-data-pipeline-region"
    content: |
      Next, you'll identify the [data pipeline region]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) your Stitch account is in. You'll use this to retrieve the correct Import API base URL for your account's region.

      The base URL is used in requests submitted to the Import API and is similar to `{{ site.data.import-api.api.base-url }}`.

      To identify your region and get your base URL:

      1. Use [these instructions]({{ link.security.supported-operating-regions | prepend: site.baseurl | append: "#identify-data-pipeline-region" }}) to locate your account's data pipeline region.
      2. Refer to the [Import API base URL reference]({{ link.import-api.api | prepend: site.baseurl | append: "#base-urls" }}) to locate the base URL for your region.
      3. Use the **Select your region** menu at the top right corner of this page to select your data pipeline region. This will display all API requests in this guide with the correct base URL for your region.

      Your base URL is currently set to: <code class='apiUrl'></code>

  - title: "Check the status of the Import API"
    anchor: "check-import-api-status"
    content: |
      {% assign api = site.data.connect.api %}

      Next, check the status of the Import API by sending a request to [GET {{ site.data.import-api.core-objects.api-status.url }}]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.api-status.anchor }}). This will ensure that the test request you send in the next step, which will validate your credentials and some sample data, will not fail due to an API outage.

      **Note**: Using this endpoint doesn't require authentication.

      {% assign request-url = site.data.import-api.core-objects.api-status.url | flatify | strip_newlines %}

      {% assign description = "GET " | append: request-url %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.no-token-required request-url=request-url %}

      When the Import API is operating correctly, it will return a `200 OK` status and an [API status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.api-status.object-anchor }}) object:

      {% capture code %}{{ site.data.import-api.code-examples.responses.get-status | flatify | strip }}
      {% endcapture %}

      {% assign description = "Response for GET " | append: site.data.import-api.core-objects.api-status.url %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      If the Import API returns a `5xx` response, check the [Stitch Status page]({{ site.status }}){:target="new"} for reported outages and try again later.

  - title: "Push a batch of data to Stitch"
    anchor: "push-data-to-stitch"
    endpoint: "POST {{ site.data.import-api.core-objects.batch.url }}"
    content: |
      To push data to Stitch, use the [Create a batch]({{ site.data.import-api.core-objects.batch.anchor | prepend: link.import-api.api | prepend: site.baseurl }}) endpoint. This endpoint uses a JSON schema to validate and type the data in the records sent to the Import API.

      Once the request is processed, data will be loaded into the destination connected to your Stitch account.

      In the example below, the request will send a single record for the `customers` table to the Import API:

      {% assign request-url = site.data.import-api.core-objects.batch.url | flatify | strip_newlines %}

      {% capture code %}{{ site.data.import-api.code-examples.requests.push-data }}
      {% endcapture %}

      {% assign description = step.endpoint %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.post.with-body request-url=request-url code=code %}

      If successful, the Import API will return a `2xx` status and a [Batch Status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.data-structures.batch-status.section }}) object.

      {% assign response-codes = site.data.import-api.response-codes.general-codes.all-codes %}

      {% for response-code in response-codes %}
      {% if response-code.code == "201" or response-code.code == "202" %}
      If the status is `{{ response-code.code }}`, this means that {{ response-code.description | replace: "The request was","the request was" }} The response body will be:
      
      {% capture code %}{{ response-code.example | flatify | strip }}
      {% endcapture %}

      {% assign description = "Response for " | append: step.endpoint | append: " ("  | append: response-code.code | append: " status)" %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}
      {% endif %}
      {% endfor %}

  - title: "Verify the data in the destination"
    anchor: "verify-data-destination"
    content: |
      After you've pushed a batch of data to the Import API, Stitch will queue it for processing.

      Stitch's replication process consists of three distinct steps: Extraction, preparation, and loading. Each step occurs independently and takes a bit of time to complete, which means you won't immediately see data in your destination after it's been pushed to the Import API. Refer to the [Monitoring replication progress]({{ link.replication.rep-progress | prepend: site.baseurl }}) documentation for more info.

      When Stitch loads the data into the destination, it will be in the schema or dataset associated with the [Import API integration you created in Stitch](#generate-import-api-access-token). The integration's schema name is located on the **{{ app.page-names.int-details }}** page in Stitch, under the integration's display name:

      ![Highlighted integration schema name field in Stitch]({{ site.baseurl }}/images/integrations/locate-integration-schema-name.png)

      In this example, Stitch would create a table named `customers` with a single record in a schema named `import_api`:

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

      **Note**: How data is structured in your destination depends on how attributes are typed in API requests **and** the type of destination Stitch loads data into. Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for more info.

      ---

next-steps: |
  Congratulations on pushing your first batch of data! Next, we recommend checking out:

  - [**Structuring data for the Import API**]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}): Learn how to structure and type data in your Import API requests.
  - [**Sequencing data for the Import API**]({{ link.import-api.guides.sequence-data | prepend: site.baseurl }}): Learn how the Import API considers data points for loading, which affects how data is updated in your destination.
---