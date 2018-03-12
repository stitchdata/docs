---
title: Quick Start
content-type: "embed-doc"
order: 2

sections:
  - title: "Register as an API Client"
    anchor: "quick-start--register-api-client"
    content: |
      Reach out to [{{ page.contact-email }}](mailto:{{ page.contact-email }}) to obtain a `partner_id` and `partner_key` for your application. These credentials are necessary to authenticate your API calls.

  - title: "Obtain an Access Token"
    anchor: "quick-start--obtain-access-token"
    content: |
      After you receive your `partner_id` and `partner_key`, you'll need to obtain an access token. Calls to the API are authenticated with an access token associated with a Stitch account. Your application can get an access token in one of two ways:

        - By creating a [new Stitch client account](#generate-access-token-new-stitch-client), or
        - By using OAuth to get authorization to an [existing Stitch account](##existing-stitch-clients-oauth2)

        Either method will provide your application with an access token and a Stitch client ID. This information should be stored somewhere safe and passed into the header of every API request for the Stitch client's account. The token will never expire, but the user may revoke access at any time.

        Keep in mind that Stitch client accounts are both owned and managed by the users themselves. For more information on authenticating with the API, refer to the [Authentication guide]({{ page.anchors.authentication | flatify }}).

  - title: "Create a Destination"
    anchor: "quick-start--create-a-destination"
    content: |
      If you're providing a destination for the Stitch client's account, we recommend connecting the destination immediately after the account is created. This ensures that Stitch will have a place to load replicated data as soon as data sources are added.

      The first step to [creating a destination]({{ page.anchors.core-objects.destinations.create-a-destination | flatify }}) is providing the attributes required for the destination's configuration, or form. These attributes are passed in the body of your request as the `connection` argument, along with the destination's `type`:

      ```curl
      curl -X POST {{ page.api-base-url }}/v3/destinations
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "type":"redshift",
                "connection": {
                  "host": "<HOST>",
                  "port": 5439,
                  "username": "<USERNAME>",
                  "database": "<DATABASE>",
                  "password": "<PASSWORD>",
                  "ssl": false
                  }
               }"
      ```

      Refer to the [Destination Form Properties object]({{ page.anchors.form-properties.destination-forms.section | flatify }}) to retrieve the attributes required for the `connection` argument for each destination type. **Note**: Each destination has its own unique configuration and set of form attributes.

  - title: "Create a Source"
    anchor: "quick-start--create-a-source"
    content: |
      Source creation is performed through a sequence of [connection steps]({{ page.anchors.data-structures.connection-steps | flatify }}). The required steps and the order of those steps are unique to the source type and are defined in its [Report Card]({{ page.anchors.data-structures.report-cards | flatify }}) object. All source creation, however, begins at the `form` step.

      We recommend using the [Source Type endpoint]({{ page.anchors.core-objects.source-types.section | flatify }}) to prep for source creation. This endpoint contains information about the configuration process and expected properties within each connection step for all source types. For example: You could use this endpoint to dynamically generate a UI or initial setup forms for each source type.

      When [creating a source]({{ page.anchors.core-objects.sources.create-a-source | flatify }}), you can choose to include the [source's form properties]({{ page.anchors.form-properties.source-forms.section | flatify }}) in the `properties` argument. This information can be retrieved using the Source Type endpoint.

      After a source's form is created, the `report_card` object within the source should be used to complete its configuration. The [Report Card]({{ page.anchors.data-structures.report-cards | flatify }}) object provides information about the steps required to configure the connection, their sequence, and the progress towards completing the steps.

      In the sections below, we'll demonstrate two methods for creating a HubSpot source.

    subsections:
      - title: "Method 1: Use the Source Types Endpoint to Provide Properties "
        anchor: "quick-start--source-creation-method-1"
        content: "In this example, we'll use the Source Types endpoint to retrieve the source form properties for HubSpot, which has a `type` of `platform.hubspot`."

        steps:
          - title: "Retrieve HubSpot's Report Card"
            anchor: "quick-start--source-creation-method-1--step-1"
            content: |
              Using the Source Types endpoint, retrieve the report card for `platform.hubspot`:

              ```curl
              curl -X GET {{ page.api-base-url}}/v4/source-types/platform.hubspot
                   -H 'Authorization: Bearer <ACCESS_TOKEN>'
              ```

          - title: "Locate Required Properties for the HubSpot Form"
            anchor: "quick-start--source-creation-method-1--step-2"
            content: |
              Use the response from Step 1 to locate the required properties for the `form` step. **Note**: You do not have to provide system-provided properties to create a source.

              ```json
              {  
                 "type":"platform.hubspot",
                 "current_step":1,
                 "current_step_hints":{  
                    "api":{  
                       "method":"POST",
                       "url":"/v4/sources"
                    },
                    "js":{  
                       "function":"addSource",
                       "options":{  
                          "type":"platform.hubspot"
                       }
                    }
                 },
                 "steps":[  
                    {  
                       "type":"form",                                 // form step
                       "properties":[
                          {  
                             "name":"image_version",                  // system-provided property
                             "required_to_be_fully_configured":true,
                             "provided":false,
                             "is_credential":false,
                             "system_provided":true
                          },
                          {  
                             "name":"frequency_in_minutes",           // required property
                             "required_to_be_fully_configured":true,
                             "provided":false,
                             "is_credential":false,
                             "system_provided":false
                          },
                          {  
                             "name":"start_date",                     // required property
                             "required_to_be_fully_configured":true,
                             "provided":false,
                             "is_credential":false,
                             "system_provided":false
                          }
                       ]
                    },
                    {  
                       "type":"oauth",
                       "properties":[...]
                    },
                    {  
                       "type":"discover_schema",
                       "properties":[ ]
                    },
                    {  
                       "type":"field_selection",
                       "properties":[ ]
                    },
                    {  
                       "type":"fully_configured",
                       "properties":[ ]
                    }
                 ]
              }
              ```

          - title: "Create the HubSpot Source"
            anchor: "quick-start--source-creation-method-1--step-3"
            content: |
              Now that you've retrieved the required `properties` for HubSpot, create the source by using the Create a Source endpoint:

              ```curl
              curl -X POST {{ page.api-base-url}}/v4/sources
                   -H "Authorization: Bearer <ACCESS_TOKEN>" 
                   -H "Content-Type: application/json"
                   -d "{  
                           "type":"platform.hubspot",
                           "display_name":"Hubspot",
                           "properties":{  
                              "start_date":"2018-01-01T00:00:00Z",
                              "frequency_in_minutes":"360"
                           }
                        }"
              ```

      - title: "Method 2: Use the Source's Report Card to Provide Properties"
        anchor: "quick-start--source-creation-method-2"
        content: "In this example, we'll rely on the source's report card to determine which properties we need to provide to create a HubSpot source."
        steps:
          - title: "Create the HubSpot Source"
            anchor: "quick-start--source-creation-method-2--step-1"
            content: |
              First, create the HubSpot source. Notice that we're not providing the `properties` argument this time:

              ```curl
              curl -X POST {{ page.api-base-url}}/v4/sources
                   -H "Authorization: Bearer <ACCESS_TOKEN>" 
                   -H "Content-Type: application/json"
                   -d "{  
                           "type":"platform.hubspot",
                           "display_name":"Hubspot"
                        }"
              ```
          - title: "Locate the Current Step and Current Step Hints"
            anchor: "quick-start--source-creation-method-2--step-2"
            content: |
              Use the response to the request to locate the source's `id`, `current_step`, and `current_step_hints` attributes.

              The data in `current_step` and `current_step_hints` can be used to determine which step is next in the source's configuration, and which properties need to be provided to successfully complete it. **Note**: You do not have to provide system-provided properties to create a source.

              Because we didn't provide the `properties` argument, we're on step 1, which is the `form` step:

              ```json
              {  
                 "properties":{  
                    "image_version":"1.latest"
                 },
                 "updated_at":"2018-01-01T19:13:41Z",
                 "check_job_name":null,
                 "name":"display_name",
                 "type":"platform.hubspot",
                 "deleted_at":null,
                 "system_paused_at":null,
                 "stitch_client_id":"CLIENT_ID",
                 "paused_at":null,
                 "id":12345,                                          // source ID
                 "display_name":"DISPLAY_NAME",
                 "created_at":"2018-01-01T19:13:41Z",
                 "report_card":{  
                    "type":"platform.hubspot",
                    "current_step":1,                                 // current step
                    "current_step_hints":{                            // current step hints
                       "api":{  
                          "method":"PUT",
                          "url":"/v4/sources/12345"
                       }
                    },
                    "steps":[  
                       {  
                          "type":"form",                              // step 1 = form step
                          "properties":[  
                             {  
                                "name":"image_version",               // system-provided property
                                "required_to_be_fully_configured":true,
                                "provided":true,
                                "is_credential":false,
                                "system_provided":true
                             },
                             {  
                                "name":"frequency_in_minutes",        // required property
                                "required_to_be_fully_configured":true,
                                "provided":false,
                                "is_credential":false,
                                "system_provided":false
                             },
                             {  
                                "name":"start_date",                  // required property
                                "required_to_be_fully_configured":true,
                                "provided":false,
                                "is_credential":false,
                                "system_provided":false
                             }
                          ]
                       },
                       {  
                          "type":"oauth",
                          "properties":[...]
                       },
                       {  
                          "type":"discover_schema",
                          "properties":[ ]
                       },
                       {  
                          "type":"field_selection",
                          "properties":[ ]
                       },
                       {  
                          "type":"fully_configured",
                          "properties":[ ]
                       }
                    ]
                 }
              }
              ```
          - title: "Complete the Form Step"
            anchor: "quick-start--source-creation-method-2--step-3"
            content: |
              Now that you've located the necessary information, complete the `form` step by using the [Update a Source]({{ page.anchors.core-objects.sources.update-a-source | flatify }}) endpoint and providing the source's `id` and the `properties` required to complete the step:

              ```curl
              curl -X POST {{ page.api-base-url}}/v4/sources/12345        // source ID
                   -H "Authorization: Bearer <ACCESS_TOKEN>" 
                   -H "Content-Type: application/json"
                   -d "{  
                         "properties":{  
                            "start_date":"2018-01-01T00:00:00Z",
                            "frequency_in_minutes":"360"
                         }
                      }"
              ```

---