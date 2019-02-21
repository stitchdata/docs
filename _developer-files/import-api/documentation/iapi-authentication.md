---
title: Authentication
product-type: "import-api"
content-type: "api-doc"
order: 3

sections:
  - content: |
      The Import API uses an [API access token]({{ link.import-api.guides.access-tokens | prepend: site.baseurl }}) and your Stitch client ID to authenticate requests. Import API access tokens can be generated and managed in the **{{ app.page-names.int-settings }}** page for any Import API integration in your [Stitch account]({{ site.sign-in }}){:target="new"}.

      Authentication is performed via bearer auth, where your Import API access token is provided in the header of your request as `-H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>'`. 

      Every record in the request body must also contain your [Stitch client ID](#stitch-client-id):

      ```json
      curl -X POST {{ site.data.import-api.api.base-url | append: site.data.import-api.api.core-objects.push.url }} \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>' \
        -d $
        '[
          {
            "client_id": 7723,              /* Stitch client ID */
            "table_name": "customers",
            "sequence": 106,
            "data": {
              "id": 4,
              "name": "Beamo"
            },
            "key_names": [
              "id"
            ],
            "action": "upsert"
          },
          {
            "client_id": 7723,              /* Stitch client ID */
            "table_name": "orders",
            "sequence": 100,
            "key_names": [
              "order_id"
            ],
            "data": {
              "order_id": 561,
              "customer_id": 4
            },
            "action": "upsert"
          }
        ]'
      ```

      Your API access token has write access to the Stitch integration schema or dataset in your destination. Because of this, API access tokens should be thought of like passwords - don't share them in publicly accessible places like Stackoverflow, GitHub, etc. If an API access token is ever lost or compromised, you can revoke it and create a new token.

      Refer to the [Stitch Import API access token]({{ link.import-api.guides.access-tokens | prepend: site.baseurl }}) documentation for more info.

  - title: "Stitch client IDs"
    anchor: "stitch-client-id"
    content: |
      Your Stitch client ID is the unique ID associated with your Stitch account. Your client ID must be provided for every record contained in a request body.

      {{ site.data.import-api.general.attributes.client-id | remove: "The Stitch client ID associated with your Stitch account." }}

      A client ID may have multiple API access tokens associated with it, but an API access token will only ever be associated with a single client ID.
---