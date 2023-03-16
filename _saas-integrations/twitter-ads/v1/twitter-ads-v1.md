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

title: Twitter Ads (v1)
permalink: /integrations/saas/twitter-ads
keywords: twitter-ads, integration, schema, etl twitter-ads, twitter-ads etl, twitter-ads schema
layout: singer
# input: false

key: "twitter-ads-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "twitter-ads"
display_name: "Twitter Ads"

singer: true
status-url: ""

tap-name: "twitter-ads"
repo-url: https://github.com/singer-io/tap-twitter-ads

this-version: "1"

api: |
  [{{ integration.display_name }} API v.7](https://developer.twitter.com/en/docs/ads/general/overview){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.twitter-ads"

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
attribution-is-configurable: true

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration:

  - Replicates core object data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.
  - Supports configuring custom reports using Twitter's [Analytics API](https://developer.twitter.com/en/docs/ads/analytics/overview){:target="new"}


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To have access to the {{ integration.display_name }} accounts you want to replicate data from.**

setup-steps:
  - title: "Retrieve account ID"
    anchor: "retrieve-account-id"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Select the ads account that you'd like to use.
      3. Click your account icon upper right corner of the screen.
      4. Click **Settings** in the dropdown menu.
      5. Copy your account ID and keep it readily available for the next step.

      **Note**: If you would like to add multiple ads accounts for this integration, repeat the above steps for each account.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Account IDs** field, paste the account ID you copied from [Step 1](#retrieve-account-id). If you're adding multiple accounts IDs, format them as a comma-delimited list. For example: `accountId1, accountId2`
      5. **Optional**: In the **Attribution Window** field, enter the number of days you want to use as a lookback period for [conversion reporting](https://business.twitter.com/en/help/campaign-measurement-and-analytics/conversion-tracking-for-websites.html){:target="new"} to stabilize. Custom report tables use this value during Extraction.
      6. **Optional**: Check the **with deleted** box if you want to include deleted records in the extraction Stitch performs.
      7. In the **Country Codes** field, enter a comma-separated list of the [ISO alpha-2 country codes](https://www.iban.com/country-codes){:target="new"} for each country you want to include in segmentation and targeting.

         For example: A list of `US, DE, IE` corresponds to `United States, Germany, Ireland`.

         **Note**: This field is required to use some [segment types in custom reports](#custom-report-configuration-options--segments).
  
  - title: "Configure reports"
    anchor: "configure-reports"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is optional. If you don't want to configure any reports, click the **- Remove this report** link." %}

      Stitch's {{ integration.display_name }} integration supports the configuration of custom reports. For each report configured in the **Your Reports** section, a table will display in the **Tables to Replicate** tab as available for selection. 

      Refer to the [Table reference](#example-custom-report) for an example of a custom report table.

      - [Create a new report](#configure-reports--new-report)
      - [Remove a report](#configure-reports--remove-report)

      #### Create a new report {#configure-reports--new-report}

      {% capture notice-content %}
      {{ integration.display_name }} enforces compatibility rules, which can affect the data available for extraction. When setting up custom reports, we recommend referring to the [Custom report options compatibility reference](#custom-report-configuration-options) to ensure you get the data you want.
      {% endcapture %}
      {% include important.html type="single-line" content=notice-content %}

      To add a report, click the **+ Configure new report** link. For each report you configure, you'll define the following parameters:

      - **Report Name**: A name for the report, which is used to create the name of its corresponding destination table
      - **Entity**: The {{ integration.display_name }} entity (object) to report on. The entity you select determines the metrics (columns) available for selection and the segments you can apply to those metrics. Refer to the [Custom report options compatibility reference](#custom-report-configuration-options) for more info.
      - **Segment**: A segment to apply to the entity's available metrics. **Note**: Some entity and segment combinations may be incompatible. Refer to the [Segment compatibility reference](#custom-report-configuration-options--segments) for more info.
      - **Granularity**: The granularity of the report data. Possible options are `DAY`, `HOUR`, and `TOTAL`.

      #### Remove a report {#configure-reports--remove-report}

      To remove a report, click the **- Remove this report** link.

      **Note**: Removing a report will not remove the corresponding table or its data from your destination.
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
#     Replication Info       #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in integration.replication-sections %}
      {% if section.title %}
      - [{{ section.title }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Extraction"
    anchor: "extraction-details"
    summary: "Details about Extraction, including object discovery and selecting data for replication"
    content: |
      This section provides a high-level look at extraction, but you can check out the [sync review on Google Docs](https://docs.google.com/document/d/1MrXWHGyOsCv-xI7ecuUWG0VIAy8ko5fwKn-I91p-PSc/edit){:target="new"} for a more technical look at this process.

      For every table set to replicate, Stitch will perform the following during Extraction:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Discovery"
        anchor: "extraction--discovery"
        summary: "Discover available tables and columns"
        content: |
          During Discovery, Stitch will:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Determining table availability"
            anchor: "discovery--objects"
            summary: "Determine table availability"
            content: |
              At the start of each replication job, Stitch performs a structure sync. During this phase, Stitch detects the objects available for replication.

              There are two types of tables for {{ integration.display_name }}:

              - **Core object tables**: These are tables that aren't created using the **Custom reports** feature in the integration's settings page. Table availability depends on the {{ integration.display_name }} Singer tap, which powers Stitch's integration. The tap contains a [JSON schema](https://github.com/singer-io/tap-twitter-ads/tree/master/tap_twitter_ads/schemas){:target="new"} for each available table.

                 The [Table reference section](#schema) of this guide lists the tables currently available for replication, as well as info about how they replicate.

              - **Custom report tables**: These are tables that are created using the **Custom reports** feature in the integration's settings page. Table availability depends on configuration of the report in the integration's settings page. **Note**: Custom report tables must also be set to replicate in the **Tables to Replicate** tab - Stitch won't automatically replicate them.

                 Refer to the [Table reference](#example-custom-report) for an example of a custom report table.

          - title: "Determining column availability"
            anchor: "discovery--columns"
            summary: "Determine column availability"
            content: |
              Column availability is dependent upon the type of table:

              - **Core Object tables**: Column availability is determined by the [JSON schema](https://github.com/singer-io/tap-twitter-ads/tree/master/tap_twitter_ads/schemas){:target="new"} backing the table in the Singer tap.
              - **Custom report tables**: Column availability is determined by the **Entity** selected during report configuration. Each entity in {{ integration.display_name }} is compatible with one or more metric groups. Each metric in a metric group corresponds to a column available for replication.

                 For example: If the entity is compatible with the [BILLING metric group](https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#BILLING){:target="new"}, you'd see `billed_engagements` and `billed_charge_local_micro` columns available for replication.

                 Refer to the [Entity and metric group compatibility reference](#custom-report-configuration-options--compatibility) for more info.

      - title: "Data replication"
        anchor: "extraction--data-replication"
        summary: "Extract records from selected tables and columns"
        content: |
          After discovery is completed, Stitch will move onto extracting data for the tables and columns you set to replicate.

          How Stitch extracts data depends on the type of table being replicated:

          - **Core object tables**: For these tables, extraction depends on the type of Replication Method the table uses. Refer to the [Table reference](#schema) for the Replication Method each table uses.

          - **Custom report tables:** Custom report tables replicate using Key-based Incremental Replication and the [Attribution Window](#add-stitch-data-source) you define during setup. Attribution Windows are used in conjunction with Replication Keys to determine where Stitch should begin extraction for a table during each extraction job.

  - title: "Loading"
    anchor: "loading-details"
    summary: "Details about how data replicated from {{ integration.display_name }} is loaded into a destination"
    content: |
      How data replicated from an {{ integration.display_name }} integration is loaded into your destination depends on two factors:

      1. **The type of table being loaded**:
         - **Core object tables** are loaded using [Upsert loading behavior]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append: "#loading-behavior-types--upsert" }}).
         - **Custom report tables** are loaded using [Append-Only loading behavior]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append:"#loading-behavior-types--append-only" }}).

      2. **If your destination supports upserts, or updating existing rows**. For destinations that support upserts, Stitch uses Primary Keys to de-dupe data during loading. {{ site.data.tooltips.primary-key }}

      **Note**: For Append-Only destinations, data will be loaded in an Append-Only manner, regardless of the table type.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/twitter-ads

# -------------------------- #
#       Other Sections       #
# -------------------------- #

other-sections:
  - title: "Reference"
    anchor: "reference"
    content: |
      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    custom-report-options:
    # -------------------------- #
    #          ENTITIES          #
    # -------------------------- #
      entities:
        - name: "account"
          segment-compatibility: "some"
        - name: "campaign"
          segment-compatibility: "all"
        - name: "funding_investment"
          segment-compatibility: "some"
        - name: "line_item"
          segment-compatibility: "all"
        - name: "media_creative"
          segment-compatibility: "none"
        - name: "organic_tweet"
          segment-compatibility: "none"
        - name: "promoted_account"
          segment-compatibility: "some"
        - name: "promoted_tweet"
          segment-compatibility: "some"

    # -------------------------- #
    #      METRIC GROUPS         #
    # -------------------------- #
      metric-groups:
        - name: "billing"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#BILLING"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/billing.json"
          compatible-entities:
            - name: "funding_investment"
            - name: "campaign"
            - name: "line_item"
            - name: "promoted_account"
            - name: "promoted_tweet"
            - name: "media_creative"

        - name: "engagement"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#engagement"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/engagement_all.json"
          compatible-entities:
            - name: "account"
            - name: "funding_investment"
            - name: "campaign"
            - name: "line_item"
            - name: "promoted_account"
            - name: "promoted_tweet"
            - name: "media_creative"
            - name: "organic_tweet"

        - name: "life_time_value_mobiile_conversion"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#LIFE_TIME_VALUE_MOBILE_CONVERSION"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/mobile_conversion.json"
          compatible-entities: &conversion-entities
            - name: "campaign"
            - name: "line_item"
            - name: "promoted_account"
            - name: "promoted_tweet"
            - name: "media_creative"

        - name: "media"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#MEDIA"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/media.json"
          compatible-entities: *conversion-entities

        - name: "mobile_conversion"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#MOBILE_CONVERSION"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/mobile_conversion.json"
          compatible-entities: *conversion-entities

        - name: "video"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#VIDEO"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/video.json"
          compatible-entities:
            - name: "campaign"
            - name: "line_item"
            - name: "promoted_account"
            - name: "promoted_tweet"
            - name: "media_creative"
            - name: "organic_tweet"

        - name: "web_conversion"
          doc: "https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#WEB_CONVERSION"
          schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/shared/web_conversion.json"
          compatible-entities: *conversion-entities

    # -------------------------- #
    #          SEGMENTS          #
    # -------------------------- #
      segments:
        - name: "no_segment"
        - name: "age"
        - name: "amplify_marketplace_preroll_videos"
        - name: "amplify_publisher_tweets"
        - name: "app_store_category"
        - name: "audiences"
        - name: "conversions"
        - name: "conversion_tags"
          compatible-metric-groups: "web_conversion"
          compatible-entities:
            - name: "account"
            - name: "campaign"
            - name: "line_item"
            - name: "organic_tweet"
        - name: "devices"
        - name: "events"
        - name: "gender"
        - name: "interests"
        - name: "keywords"
        - name: "languages"
          compatible-entities:
            - name: "campaign"
            - name: "line_item"
            - name: "promoted_tweet"
            - name: "organic_tweet"
        - name: "location"
          parameter-required: "country codes"
        - name: "metros"
          parameter-required: "country codes"
        - name: "platform_versions"
        - name: "platforms"
        - name: "postal_codes"
          parameter-required: "country codes"
        - name: "regions"
          parameter-required: "country codes"
        - name: "similar_to_followers_of_user"
        - name: "swipeable_media"
        - name: "tv_ads"
        - name: "tv_shows"
    subsections:
      - title: "Entity and metric group compatibility reference"
        anchor: "custom-report-configuration-options--compatibility"
        content: |
          {% include misc/icons.html %}

          In the following table, you'll find info about the custom report options Stitch's {{ integration.display_name }} currently supports.

          The columns are as follows:

          - **Entity**: The name of the entity
          - **Metric group availability**: The metric groups {{ integration.display_name }} supports for the entity, which determines the columns that will be available for selection in Stitch.

             For example: If an entity supports the [BILLING metric group](https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation#BILLING){:target="new"}, you'll see the `billed_engagements` and `billed_charge_local_micro` metrics as available columns in the report in Stitch.

             Click the links in this column for more info about the data points (columns) the metric group contains.
          - **Segmentation compatibility**: Indicates the level of segment compatibility for the entity:

             - {{ supported | replace:"TOOLTIP", "Full compatibility" }} indicates the entity is compatible with all segments
             - {{ sometimes-supported | replace:"TOOLTIP", "Some compatibility"  }} indicates the entity is compatible with some segments
             - {{ not-supported | replace:"TOOLTIP", "Segmentation not supported" }} indicates {{ integration.display_name }} doesn't support segmentation for the entity

             Refer to the [Segment compatibility reference](#custom-report-configuration-options--segments) for more info.

          <table class="attribute-list table-hover" style="font-size: 13px;">
            <tr>
              <td align="right">
                <strong>Entity</strong>
              </td>
              <td>
                <strong>Metric group availability</strong>
              </td>
              <td>
                <strong>Segmentation compatibility</strong>
              </td>
            </tr>
            {% for entity in section.custom-report-options.entities %}
              <tr>
                <td align="right">
                  {{ entity.name | upcase }}
                </td>
                <td>
                  <ul style="margin-top: 0px;">
                    {% for metric-group in section.custom-report-options.metric-groups %}
                      {% for compatible-entity in metric-group.compatible-entities %}
                        {% if compatible-entity.name == entity.name %}
                          <li style="margin-top: 0px;">
                            <a href="{{ metric-group.doc }}" target="new">{{ metric-group.name | upcase }}</a> (<a href="{{ metric-group.schema }}" target="new">JSON schema</a>)
                          </li>
                        {% endif %}
                      {% endfor %}
                    {% endfor %}
                  </ul>
                </td>
                <td>
                  {% case entity.segment-compatibility %}
                    {% when 'all' %}
                      {{ supported | replace:"TOOLTIP", "Full compatibility" }} Full compatibility
                    {% when 'some' %}
                      {{ sometimes-supported | replace:"TOOLTIP", "Some compatibility"  }} Some compatibility
                    {% when 'none' %}
                      {{ not-supported | replace:"TOOLTIP", "Segmentation not supported" }} No compatibility
                  {% endcase %}
                </td>
              </tr>
            {% endfor %}
          </table>

      - title: "Segment compatibility reference"
        anchor: "custom-report-configuration-options--segments"
        content: |
          In the following table, you'll find info about the segment options Stitch's {{ integration.display_name }} integration currently supports.

          The columns are as follows:

          - **Segment**: The name of the segment
          - **Entity compatibility**: The entities {{ integration.display_name }} deems compatible with the segment. **Note**: Stitch's integration accounts for some undocumented incompatibilities. They're documented here, but you can view them in the [Singer tap's code](https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schema.py#L119){:target="new"}.
          - **Notes**: Additional notes about the segment. For example: Some segments may require that specific fields be defined in Stitch.

          <table class="attribute-list table-hover" style="font-size: 13px;">
            <tr>
              <td align="right" width="35%; fixed">
                <strong>Segment</strong>
              </td>
              <td>
                <strong>Entity compatibility</strong>
              </td>
              <td>
                <strong>Notes</strong>
              </td>
            </tr>
            {% for segment in section.custom-report-options.segments %}
              <tr>
                <td align="right">
                  {{ segment.name | upcase }}
                </td>
                <td>
                  {% if segment.compatible-entities %}
                    Compatible with the following entities: 
                    <ul>
                      {% for entity in segment.compatible-entities %}
                        <li style="margin-top: 0px;">{{ entity.name | upcase }}</li>
                      {% endfor %}
                    </ul>
                  {% else %}
                    Compatible with all entities{% unless segment.name == "no_segment" %} <strong>except</strong>:

                    <ul>
                      <li>MEDIA_CREATIVE</li>
                      <li>ORGANIC_TWEET</li>
                    </ul>
                    {% endunless %}
                  {% endif %}
                </td>
                <td>
                  {% if segment.parameter-required or segment.compatible-metric-groups %}
                    {% if segment.parameter-required and segment.compatible-metric-groups %}
                      <ul>
                        <li style="margin-top: 0px;">
                          The <a href="#add-stitch-data-source">{{ segment.parameter-required | camelcase }}</a> field must be defined to use this segment
                        </li>
                        <li style="margin-top: 0px;">
                          Only compatible with the following metric groups: {{ segment.compatible-metric-groups | upcase }}
                        </li>
                      </ul>
                    {% else %}
                      {% if segment.parameter-required %}
                        The <a href="#add-stitch-data-source">{{ segment.parameter-required | capitalize }}</a> field must be defined to use this segment
                      {% endif %}

                      {% if segment.compatible-metric-groups %}
                        Only compatible with the following metric groups: {{ segment.compatible-metric-groups | upcase }}
                      {% endif %}
                    {% endif %}
                  {% endif %}
                </td>
              </tr>
            {% endfor %}
          </table>

      - title: "Additional resources"
        anchor: "custom-report-configuration-options--resources"
        content: |
          - [{{ integration.display_name }} API Hierarchy and Terminology](https://developer.twitter.com/en/docs/tutorials/ads-api-hierarchy-terminology){:target="new"}
          - [{{ integration.display_name }} Metrics and Segmentation Rules](https://developer.twitter.com/en/docs/ads/analytics/overview/metrics-and-segmentation){:target="new"}
---
{% assign integration = page %}
{% include misc/data-files.html %}