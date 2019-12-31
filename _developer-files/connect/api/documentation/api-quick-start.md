---
# title: Quick start
# product-type: "connect"
# content-type: "api-doc"
# order: 2

sections:
  - title: "Obtain an access token"
    anchor: "quick-start--obtain-access-token"
    content: |
      Stitch authenticates requests to the API using an API access token. How you obtain an access token depends on the type of user you are:

      - **Individual Stitch user**: You will be using the API to programmatically control your own Stitch client account. You can create, revoke, and delete API access tokens on the [Account Settings page]({{ link.account.manage-api-keys | prepend: site.baseurl }}) of your Stitch client account.

      - **Stitch partner**: You will be performing actions in Stitch client accounts on behalf of users who authorize your API client. You'll need to [register as an API client]({{ site.data.connect.api.interest-form }}){:target="new"} and refer to the [Partner API Authentication guide]({{ link.connect.guides.partner-authentication | prepend: site.baseurl }}) for instructions.

      After you obtain an API access token, it should be stored somewhere safe and passed into the header of every API request made for the Stitch client account. This token will never expire, but it may be revoked at any time.

      {% capture partner-auth-note %}
      Stitch client accounts are both owned and managed by the users themselves. For more info on authenticating with the API as a partner, refer to the [Partner API Authentication guide]({{ link.connect.guides.partner-authentication | prepend: site.baseurl }}).
      {% endcapture %}

      {% include note.html first-line="**Stitch account ownership:**" content=partner-auth-note %}

  - title: "Make a test API request"
    anchor: "quick-start--test-api-request"
    content: |
      {% assign right-bracket = "}" %}

      To check that your access token is working correctly, send a test request to the [Source Types](#{{ site.data.connect.core-objects.source-types.get.anchor }}) endpoint and retrieve configuration info about the `platform.hubspot` source:

      ```json
      curl -X {{ site.data.connect.core-objects.source-types.get.method | upcase }} {{ site.data.connect.core-objects.source-types.get.name | prepend: site.data.connect.api.base-url | flatify | remove: right-bracket | replace:"{source_type","platform.hubspot" | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
      ```

      If successful, the API will return a status of `200 OK` and a [Source Report Card object]({{ api.data-structures.report-cards.source.section }}) corresponding to `platform.hubspot`.

  # - title: "Create a destination"
  #   anchor: "quick-start--create-a-destination"
  #   content: |
  #     If you're providing a destination for the Stitch client's account, we recommend connecting the destination immediately after the account is created. This ensures that Stitch will have a place to load replicated data as soon as data sources are added.

  #     The first step to [creating a destination]({{ api.core-objects.destinations.create.anchor }}) is providing the attributes required for the destination's configuration, or form. These attributes are passed in the body of your request as the `properties` argument, along with the destination's `type`:

  #     ```curl
  #     curl -X POST {{ api.base-url }}{{ api.core-objects.destinations.create.name | flatify }}
  #          -H "Authorization: Bearer <ACCESS_TOKEN>" 
  #          -H "Content-Type: application/json"
  #          -d "{
  #               "type":"redshift",
  #               "properties": {
  #                 "host": "<HOST>",
  #                 "port": 5439,
  #                 "username": "<USERNAME>",
  #                 "database": "<DATABASE>",
  #                 "password": "<PASSWORD>",
  #                 "ssl": false
  #                 }
  #              }"
  #     ```

  #     Refer to the [Destination Form Properties object]({{ api.form-properties.destination-forms.section | flatify }}) to retrieve the attributes required for the `properties` argument for each destination type. **Note**: Each destination has its own unique configuration and set of form attributes.

  # - title: "Create a source"
  #   anchor: "quick-start--create-a-source"
  #   content: |
  #     Source creation is performed through a sequence of [connection steps]({{ api.data-structures.connection-steps.section }}). The required steps and the order of those steps are unique to the source type and are defined in its [Report Card]({{ api.data-structures.report-cards.section }}) object. All source creation, however, begins at the `form` step.

  #     {% capture tip-source-types %}
  #     Use the [Source Type endpoint]({{ api.core-objects.source-types.section }}) to prep for source creation. This endpoint contains information about the configuration process, including the required [Source Form Properties]({{ api.form-properties.source-forms.section }}) (`step: form`) and expected properties within each subsequent connection step.<br><br>

  #     With this endpoint, you could dynamically generate a UI or initial setup forms for each source type you want to include in your application.
  #     {% endcapture %}

  #     {% include tip.html content=tip-source-types %}

  #     In the example below, we'll use the Source Types endpoint to retrieve the source form properties for HubSpot, which has a `type` of `platform.hubspot`.

  #   subsections:
  #     - title: "Get the source's Report Card"
  #       anchor: "quick-start--get-hubspot-report-card"
  #       content: |
  #         Using the Source Types endpoint, retrieve the report card for `platform.hubspot`:

  #         ```curl
  #         curl -X GET {{ api.base-url}}{{ api.core-objects.source-types.base | flatify }}/platform.hubspot
  #              -H 'Authorization: Bearer <ACCESS_TOKEN>'
  #         ```

  #         The response, or the report card for `platform.hubspot`, will include HubSpot's [Source Form Properties]({{ api.core-objects.sources.create.anchor }}). These are the parameters that are required to complete a source's `form` step.

  #     - title: "Locate required form properties in the Report Card"
  #       anchor: "quick-start--locate-form-properties"
  #       content: |
  #         Use the response from the previous step to locate the required properties for the `form` step.

  #         **Note**: You do not have to provide system-provided properties to create a source.

  #         ```json
  #         {  
  #            "type":"platform.hubspot",
  #            "current_step":1
  #            "steps":[  
  #               {  
  #                  "type":"form",                                 /* form step */
  #                  "properties":[
  #                     {  
  #                        "name":"image_version",                  /* system-provided property */
  #                        "required_to_be_fully_configured":true,
  #                        "provided":false,
  #                        "is_credential":false,
  #                        "system_provided":true
  #                     },
  #                     {  
  #                        "name":"frequency_in_minutes",           /* required property */
  #                        "required_to_be_fully_configured":true,
  #                        "provided":false,
  #                        "is_credential":false,
  #                        "system_provided":false
  #                     },
  #                     {  
  #                        "name":"start_date",                     /* required property */
  #                        "required_to_be_fully_configured":true,
  #                        "provided":false,
  #                        "is_credential":false,
  #                        "system_provided":false
  #                     }
  #                  ]
  #               },
  #               {  
  #                  "type":"oauth",
  #                  "properties":[...]
  #               },
  #               {  
  #                  "type":"discover_schema",
  #                  "properties":[ ]
  #               },
  #               {  
  #                  "type":"field_selection",
  #                  "properties":[ ]
  #               },
  #               {  
  #                  "type":"fully_configured",
  #                  "properties":[ ]
  #               }
  #            ]
  #         }
  #         ```

  #         For `platform.hubspot`, the `frequency_in_minutes` and `start_date` properties must be provided to complete the `form` step.

  #     - title: "Create the source"
  #       anchor: "quick-start--create-source"
  #       content: |
  #         Now that the required `properties` for HubSpot have been retrieved, we can create the HubSpot source:

  #         ```curl
  #           curl -X POST {{ api.base-url}}{{ api.core-objects.sources.create.name | flatify }}
  #                -H "Authorization: Bearer <ACCESS_TOKEN>" 
  #                -H "Content-Type: application/json"
  #                -d "{  
  #                        "type":"platform.hubspot",
  #                        "display_name":"HubSpot",
  #                        "properties":{  
  #                           "start_date":"2018-01-01T00:00:00Z",
  #                           "frequency_in_minutes":"30"
  #                        }
  #                     }"
  #           ```

  #         If successful, the API will return a `200 OK` status and a [Source object]({{ api.core-objects.sources.object }}) with a `report_card` property:

  #         ```json
  #         {
  #            "properties":{
  #               "frequency_in_minutes":"30",
  #               "image_version":"1.latest",
  #               "start_date":"2018-01-01T00:00:00Z"
  #            },
  #            "updated_at":"2018-02-06T16:25:06Z",
  #            "check_job_name":null,
  #            "name":"hubspot",
  #            "type":"platform.hubspot",
  #            "deleted_at":null,
  #            "system_paused_at":null,
  #            "stitch_client_id":<ACCOUNT_ID>,
  #            "paused_at":null,
  #            "id":45612,
  #            "display_name":"HubSpot",
  #            "created_at":"2018-02-06T16:25:06Z",
  #            "report_card":{
  #               "type":"platform.hubspot",
  #               "current_step":2,
  #               "steps":[
  #                  {
  #                     "type":"form",
  #                     "properties":[
  #                        {
  #                           "name":"image_version",
  #                           "is_required":true,
  #                           "provided":true,
  #                           "is_credential":false,
  #                           "system_provided":true,
  #                           "json_schema":null
  #                        },
  #                        {
  #                           "name":"frequency_in_minutes",
  #                           "is_required":true,
  #                           "provided":true,
  #                           "is_credential":false,
  #                           "system_provided":false,
  #                           "json_schema":{
  #                              "type":"string",
  #                              "pattern":"^\\d+$"
  #                           }
  #                        },
  #                        {
  #                           "name":"start_date",
  #                           "is_required":true,
  #                           "provided":true,
  #                           "is_credential":false,
  #                           "system_provided":false,
  #                           "json_schema":{
  #                              "type":"string",
  #                              "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
  #                           }
  #                        }
  #                     ]
  #                  },
  #                  {
  #                     "type":"oauth",
  #                     "properties":[
  #                        {
  #                           "name":"client_id",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        },
  #                        {
  #                           "name":"client_secret",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        },
  #                        {
  #                           "name":"redirect_uri",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string",
  #                              "format":"uri"
  #                           }
  #                        },
  #                        {
  #                           "name":"refresh_token",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        }
  #                     ]
  #                  },
  #                  {
  #                     "type":"discover_schema",
  #                     "properties":[

  #                     ]
  #                  },
  #                  {
  #                     "type":"field_selection",
  #                     "properties":[

  #                     ]
  #                  },
  #                  {
  #                     "type":"fully_configured",
  #                     "properties":[

  #                     ]
  #                  }
  #               ]
  #            }
  #         }
  #         ```

  #         After a source's form is created, the `report_card` object within the source should be used to complete its configuration. 

  #     - title: "Identify the current step"
  #       anchor: "quick-start--identify-current-step"
  #       content: |
  #         The [Source Report Card]({{ api.data-structures.report-cards.source.section }}) object provides information about the steps required to configure the connection, their sequence, and the progress towards completing the steps.

  #         Looking at the report card for our HubSpot source, we can see that we're now on step `2` of configuration, which is the `oauth` step:

  #         ```json
  #         {
  #            "report_card":{
  #               "type":"platform.hubspot",
  #               "current_step":2,                                           /* Current step */
  #               "steps":[
  #                  {
  #                     "type":"form",
  #                     "properties":[ ... ]
  #                  },
  #                  {
  #                     "type":"oauth",
  #                     "properties":[
  #                        {
  #                           "name":"client_id",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        },
  #                        {
  #                           "name":"client_secret",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        },
  #                        {
  #                           "name":"redirect_uri",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string",
  #                              "format":"uri"
  #                           }
  #                        },
  #                        {
  #                           "name":"refresh_token",
  #                           "is_required":true,
  #                           "provided":false,
  #                           "is_credential":true,
  #                           "system_provided":true,
  #                           "json_schema":{
  #                              "type":"string"
  #                           }
  #                        }
  #                     ]
  #                  },
  #                  {
  #                     "type":"discover_schema",
  #                     "properties":[ ]
  #                  },
  #                  {
  #                     "type":"field_selection",
  #                     "properties":[ ]
  #                  },
  #                  {
  #                     "type":"fully_configured",
  #                     "properties":[ ]
  #                  }
  #               ]
  #            }
  #         }
  #         ```

  # - title: "Use the {{ js.name }} to complete source configuration"
  #   anchor: "quick-start--stitch-js-complete-configuration"
  #   content: |
  #     To initiate the OAuth flow, use the [`authorizeSource`]({{ js.section | prepend: site.baseurl | append: js.authorize-a-source.section | flatify }}) function in the {{ js.name }}. This function expects an `options` argument containing the source's `id`:

  #     ```javascript
  #     Stitch.authorizeSource({
  #         "id": 45612
  #     }).then((result) => {
  #         console.log(`Integration created, type=${result.type}, id=${result.id}`);
  #     }).catch((error) => {
  #         console.log("Integration not created.", error);
  #     });
  #     ```

  #     This function will send the user to Stitch, where they will be prompted to sign into their Stitch account and grant access to HubSpot.

  #     After the user grants access, Stitch will automatically prompt the user to complete the remaining steps to configure the source, including selecting table and field for replication.

---