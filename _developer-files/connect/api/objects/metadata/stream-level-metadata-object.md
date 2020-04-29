---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-sub-structure"
key: "stream-level-metadata-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stream-level Metadata"
description: |
  {% include misc/data-files.html %}
  {{ api.data-structures.metadata.stream-level.description | flatify }}


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "database-name"
    type: "string"
    description: "**For database sources only**. The name of the database containing the stream."
    modifiable: false
    applies-to: "mysql, oracle, postgres"
    value: |
      <DATABASE_NAME>

  - name: "forced-replication-method"
    type: "string"
    description: |
      Indicates which Replication Method is required for the stream. Possible values are:

      - `FULL_TABLE` - The stream is using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }})
      - `INCREMENTAL` - The stream is using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }})
      - `LOG_BASED` - The stream is using [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}).
    modifiable: false
    applies-to: "xero, salesforce, shopify, zendesk, hubspot, uservoice"
    value: |
      INCREMENTAL

  - name: "is-view"
    type: "boolean"
    description: "**For database sources only.** Indicates if the stream is a database view."
    modifiable: false
    applies-to: ""
    value: |
      false

  - name: "replication-key"
    type: "string"
    description: "Indicates the field being used as the stream's [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }})."
    modifiable: true
    applies-to: "mysql, oracle, salesforce, db2, postgres"
    value: |
      updated_at

  - name: "replication-method"
    type: "string"
    description: |
      The Replication Method the stream uses to replicate data. Accepted values are:

      - `FULL_TABLE` - The stream is using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }})
      - `INCREMENTAL` - The stream is using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }})
      - `LOG_BASED` - The stream is using [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}). **Note**: This method is only available for certain database sources, and requires additional setup to use.
    modifiable: true
    applies-to: "xero, shopify, salesforce, zendesk, hubspot"
    value: |
      INCREMENTAL

  - name: "row-count"
    type: "integer"
    description: "**For database sources only.** The number of rows (records) in the stream."
    modifiable: false
    applies-to: "oracle, mysql"
    value: |
      55

  - name: "schema-name"
    type: "string"
    description: "**For database sources only.** The name of the schema containing the stream."
    modifiable: false
    applies-to: "oracle, postgres"
    value: |
      <SCHEMA_NAME>

  - name: "selected"
    type: "boolean"
    description: |
      Indicates whether a stream should be set to replicate. Accepted values are:

      - `true` - The stream is selected and data for selected fields will be replicated
      - `false` - The stream is not selected and no data will be replicated
    modifiable: true
    applies-to: "all"
    value: |
      true

  - name: "table-key-properties"
    type: "array"
    description: |
      An array of strings listing the fields that make up the key properties of the table. These are the table's defined Primary Keys.
    modifiable: false
    applies-to: "all"
    value: |
      id, created_at

  - name: "valid-replication-keys"
    type: "array"
    description: |
      An array of strings indicating the fields valid for use as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) in [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) (`replication-method: INCREMENTAL`).

      **Note**: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.
    modifiable: false
    applies-to: "bronto, hubspot, harvest-forecast, db2, shopify, salesforce, xero"
    value: |
      updated_at

  - name: "view-key-properties"
    type: "array"
    description: "**For database sources only.** An array of strings listing the fields that make up the key properties of the view."
    modifiable: false 
    applies-to: "oracle, postgres, mysql, db2"
    value: |
      <TODO>

  # Source: https://github.com/singer-io/tap-google-analytics/blob/master/spikes/discover_metrics_and_dimensions.py#L158
  - name: "tap_google_analytics.all_cubes"
    type: "array"
    description: |
      **For Google Analytics sources only.** An array of strings listing all the 'cubes' available in the Google Analytics source. A cube is a group of metrics and dimensions that are compatible together.

      We recommend using [Google's Dimensions and Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets){:target="new"} to test combinations of metrics and dimensions for compatibility.
    modifiable: false
    applies-to: "google-analytics"


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - type: "Database source (non-view)"
    code: |
      {
        "metadata": {
          "database-name": "demni2mf59dt10",
          "selected": true,
          "is-view": false,
          "replication-method": "FULL_TABLE",
          "row-count": 13,
          "schema-name": "public",
          "table-key-properties": [
            "id"
          ]
        }
      }

  - type: "Database source (view)"
    code: |
      {
        "metadata": {
          "database-name": "demni2mf59dt10",
          "selected": true,
          "replication-method":"INCREMENTAL",
          "replication-key":"updated_at",
          "is-view": true,
          "row-count": 156,
          "schema-name": "heroku",
          "view-key-properties": [
            "customer_id"
          ]
        }
      }

  - type: "SaaS source"
    code: |
      {
        "metadata": {
          "forced-replication-method": "INCREMENTAL",
          "selected": true,
          "table-key-properties": [
            "id"
          ],
          "valid-replication-keys": [
            "updated_at"
          ]
        }
      }

  - type: "Google Analytics source"
    code: |
      {
         "metadata":{
            "inclusion":"available",
            "selected":null,
            "table-key-properties":[
               "_sdc_record_hash"
            ],
            "tap_google_analytics.all_cubes":[
               "audience_size",
               "per_active_visitors_date_active_visitors_14",
               "cohorts_overview_nth_day",
               "all_metrics_for_audiences_overview",
               "Cube:analytics/per_ecommerce_refund_import_without_transaction_product_metrics",
               "per_campaign_segmented_with_local_currency",
               "per_social",
               "per_geo_dimension_widening",
               "per_exception",
               "per_orphan",
               "smart_goals",
               "gwo_transaction_subcube",
               "phone_analytics",
               "per_dfa_floodlight_model",
               "per_wmx_url",
               "ga_experiment_results_metrics",
               "per_active_visitors_day_active_visitors_30",
               "per_active_visitors_day_active_visitors_28",
               "per_dimension_widening",
               "per_geo_dimension_widening_sub_continent_code",
               "ga_exp_objective_metrics",
               "cohorts_overview_nth_week",
               "all_metrics_for_active_visitors_cubes",
               "per_geo_dimension_widening_region_id",
               "per_content_id_dimension_widening",
               "per_active_visitors_date_active_visitors_7",
               "per_active_visitors_nthday_active_visitors_14",
               "per_sitelink_extension",
               "per_ecommerce_dimension_widening",
               "per_content_with_gwo_id_and_outcomes",
               "per_active_visitors_nthday_active_visitors_28",
               "per_cost_data_import",
               "all_metrics_for_cohorts_overview",
               "per_active_visitors_date_active_visitors_28",
               "per_active_visitors_date_active_visitors_1",
               "per_active_visitors_date_active_visitors_30",
               "local_transaction",
               "gdn_targeting",
               "channel_grouping_rule_key",
               "per_campaign_content",
               "Cube:analytics/per_value_site_search_without_transaction_product_dimensions",
               "per_product_with_local_currency",
               "enhanced_campaign",
               "Cube:analytics/per_value_site_search_without_transaction_product_metrics",
               "per_active_visitors_day_active_visitors_14",
               "store_visits",
               "per_geo_dimension_widening_city_id",
               "gwo_bandit_combination_metrics",
               "per_active_visitors_day_active_visitors_1",
               "per_geo_dimension_widening_country_iso_code",
               "per_goal_request_uri",
               "per_active_visitors_nthday_active_visitors_1",
               "per_active_visitors_day_active_visitors_7",
               "per_query_with_cost_metrics",
               "per_active_visitors_nthday_active_visitors_30",
               "per_campaign_shasta_with_local_currency",
               "per_campaign_dart_search",
               "individual_user_report",
               "per_goal_funnel_request",
               "per_tv_campaign",
               "smart_data_dimension_subcube",
               "gwo_bandit_metrics",
               "per_web_property_query_RESTRICTED",
               "per_campaign_with_local_currency",
               "per_absolute_unique_visitors",
               "per_campaign_id_dimension_widening",
               "per_wmx_query",
               "cohorts_overview_nth_month",
               "per_active_visitors_nthday_active_visitors_7",
               "per_user_id_dimension_widening",
               "per_events_with_local_currency",
               "per_wmx_site",
               "per_dfa_model",
               "per_content_with_local_currency",
               "per_social_plus_site",
               "Cube:analytics/per_ecommerce_refund_import_without_transaction_product_dimensions"
            ]
         }
      }
---