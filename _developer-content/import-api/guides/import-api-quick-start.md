---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Import API Quick Start
doc-type: "tutorial"

product-type: "import-api"
content-type: "guide"
content-id: "stitch-import-api-quick-start"
layout: tutorial

permalink: /developers/import-api/guides/quick-start
icon: file
order: 1

summary: "Stitch's Import API allows you to push arbitrary data from a source to your Stitch account. Generate your API credentials and push your first batch of data with this guide."

## This is used only on the /import-api/guides page.
display-title: "Import API Quick Start"
description: "Generate your Import API credentials and push your first batch of data."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Stitch Import API Access Tokens"
    link: "{{ link.import-api.guides.access-tokens | prepend: site.baseurl }}"

  - title: "Structuring Data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"



# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **An active Stitch account.** To create an account, [sign up for a free one here]({{ site.home }}){:target="new"}.


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
      The Import API uses your Stitch client ID and an API access token to authenticate requests. In this step, you'll retrieve your client ID, create an Import API integration in your Stitch account, and generate an API access token.

    substeps:
      - title: "Retrieve your Stitch client ID"
        anchor: "retrieve-stitch-client-id"
        content: |
          Your Stitch client ID is the unique ID associated with your Stitch account. Your client ID must be provided for every record contained in a request body.

          {{ site.data.import-api.general.attributes.client-id | remove: "The Stitch client ID associated with your Stitch account." }}

      - title: "Generate an Import API access token"
        anchor: "generate-import-api-access-token"
        content: |
          Next, you'll generate an Import API access token. We're using the Stitch app to generate the access token, but you can also use the [Connect API if your Stitch account has access]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl }}).

          {% include developers/import-api/obtaining-credentials.html type="generate-new-access-token" %}

  - title: "Check the status of the Import API"
    anchor: "check-import-api-status"
    content: |
      Next, check the status of the Import API. This will ensure that the test request you send in the next step, which will validate your credentials and some sample data, will not fail due to an API outage.

      **Note**: Using the [Import API status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.api-status.anchor }}) endpoint doesn't require authentication.

      ```json
      {{ site.data.import-api.code-examples.requests.get-status | flatify | strip }}
      ```

      When the Import API is operating correctly, it will return a `200 OK` status and an [API status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.api-status.object-anchor }}) object:

      ```json
      {{ site.data.import-api.code-examples.responses.get-status | flatify | strip }}
      ```

      If the Import API returns a `5xx` response, check the [Stitch Status page]({{ site.status }}){:target="new"} for reported outages and try again later.

  - title: "Make a test API request"
    anchor: "send-test-api-request"
    content: |
      In this step, you'll send a test request to the Import API using the [Validate request]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.validate.anchor }}) endpoint.

      The Validate request endpoint allows you to validate your API access token and the data you want to send without it being persisted to Stitch. This is useful for testing during development.

      In the example below, the request is sending a single record for a table named `customers`:

      ```json
      {{ site.data.import-api.code-examples.requests.validate-request | flatify | strip }}
      ```

      If your API credentials and the data in the request are both valid, the Import API will return a `200 OK` status and a [Batch Status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.data-structures.batch-status.section }}) object with a `Batch is valid!` message:

      ```json
      {{ site.data.import-api.code-examples.responses.validate-request | flatify | strip }}
      ```

      If an error is returned, refer to the [errors for the Validate request endpoint]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.core-objects.validate.anchor | append: "--returns" }}) to identify and resolve the issue.

  - title: "Push data to Stitch"
    anchor: "push-data-to-stitch"
    content: |
      Once your test request is successful, you're ready to send data to Stitch.

      To push data to the Import API, use the [Push data]() endpoint. This endpoint is identical to the Validate request endpoint, but requests will be persisted to Stitch. Once the request is processed, data will be loaded into the destination connected to the account.

      In the example below, the request will send a single record for the `customers` table to the Import API:

      ```json
      {{ site.data.import-api.code-examples.requests.push-data | flatify }}
      ```

      If successful, the Import API will return a `201 Created` or `202 Accepted` status and a [Batch Status]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.data-structures.batch-status.section }}) object:

      ```json
      /* 201 Created */
      {{ site.data.import-api.code-examples.responses.push-data.batch-created }}

      /* 202 Accepted */
      {{ site.data.import-api.code-examples.responses.push-data.batch-accepted }}
      ```

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
  Congratulations on pushing your first batch of data! Check out the other [Import API guides]({{ link.import-api.category | prepend: site.baseurl }}) to get started building your own project.
---