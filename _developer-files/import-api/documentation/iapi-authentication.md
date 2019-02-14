---
title: Authentication
product-type: "import-api"
content-type: "api-doc"
order: 3

sections:
  - content: |
      The Import API uses an API access token and your Stitch client ID to authenticate requests. Import API access tokens can be generated and managed in the **{{ app.page-names.int-settings }}** page for any Import API integration in your [Stitch account]({{ site.sign-in }}){:target="new"}.

      Authentication is performed via bearer auth, where your Import API access token is provided in the header of your request as `-H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>'`. The request body must also contain your [Stitch client ID](#stitch-client-id):

      ```json
      curl -X POST {{ site.data.import-api.api.base-url | append: site.data.import-api.api.core-objects.push.url }} \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>' \
        -d $
          '[
            {
              "client_id": 7723,            /* Stitch client ID */
              "table_name": "customers",
              "sequence": 100,
              "key_names": [
                "id"
              ],
              "data": {
                "id": 1,
                "name": "Finn"
              },
              "action": "upsert"
            }
          ]'
      ```

      Your API access token has write access to the Stitch integration schema or dataset in your destination. Because of this, API access tokens should be thought of like passwords - don't share them in publicly accessible places like Stackoverflow, GitHub, etc. If an API access token is ever lost or compromised, you can revoke it and create a new token.

  - title: "Generate or revoke Import API access tokens"
    anchor: "generate-revoke-import-api-access-token"
    content: |
      Import API access tokens can be created and managed in two ways:

      1. **In the Stitch web app**. Anyone with a Stitch account can use this method. Refer to the [Generate and revoke Import API tokens in the Stitch app]({{ link.import-api.guides.generate-revoke-access-tokens | prepend: site.baseurl }}) for instructions.
      2. **Through the Stitch Connect API**. This method requires access to [Stitch Connect]({{ link.connect.api | prepend: site.baseurl }}). Refer to the [Connect API documentation]({{ site.data.connect.api.access-api }}) for more info on getting access.

  - title: "Stitch client IDs"
    anchor: "stitch-client-id"
    content: |
      {{ site.data.import-api.general.attributes.client-id | remove: "The Stitch client ID associated with your Stitch account." }}

      A client ID may have multiple API access tokens associated with it, but an API access token will only ever be associated with a single client ID.

      Additionally, API access tokens are specific to the Import API integration they are created for. This means that data successfully pushed using a given API access token will only ever be loaded into the schema or dataset created for that integration.
---