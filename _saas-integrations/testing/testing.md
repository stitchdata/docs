---
title: HubSpot
permalink: /integrations/saas/testing/
keywords: salesforce, integration, schema, etl salesforce, salesforce etl, salesforce schema
summary: "Connections instructions, replication info, and schema details for Stitch's Salesforce integration."
layout: general

sections:
  - content: |
      <table class="table-snapshot table-hover">
      <tr>
      <td align="right" width="23%; fixed">
      <strong>Latest version</strong>:
      </td>
      <td>
      2.0
      </td>
      <td align="right" width="23%; fixed">
      <strong>Supported by</strong>:
      </td>
      <td>
      Stitch
      </td>
      </tr>
      <tr>
      <td align="right" width="23%; fixed">
      <strong>Stitch plan</strong>:
      </td>
      <td>
      Standard
      </td>
      <td align="right" width="23%; fixed">
      <strong>Singer repository</strong>:
      </td>
      <td>
      <a href="https://github.com/singer-io/tap-hubspot">HubSpot repository</a>
      </td>
      </tr>
      </table>

      HubSpot is inbound marketing and sales software.

  - title: "Version release and deprecation"
    anchor: "version-release-deprecation"
    content: |
      <table class="attribute-list">
      <tr>
      <td align="right">
      <strong>Version</strong>
      </td>
      <td>
      <strong>Status</strong>
      </td>
      <td>
      <strong>Release</strong>
      </td>
      <td>
      <strong>Deprecation</strong>
      </td>
      <td>
      <strong>Sunset</strong>
      </td>
      </tr>
      <tr>
      <td align="right">
      <strong>v2 (latest)</strong>
      </td>
      <td>
      Released
      </td>
      <td>
      May 30, 2018
      </td>
      <td>
      -
      </td>
      <td>
      -
      </td>
      </tr>
      <tr>
      <td align="right">
      <strong>v1</strong>
      </td>
      <td>
      Deprecated
      </td>
      <td>
      August 22, 2017
      </td>
      <td>
      September 1, 2018
      </td>
      <td>
      -
      </td>
      </tr>
      <tr>
      <td align="right">
      <strong>v01-03-2017</strong>
      </td>
      <td>
      Sunset
      </td>
      <td>
      March 1, 2017
      </td>
      <td>
      November 22, 2017
      </td>
      <td>
      February 1, 2018
      </td>
      </tr>
      </table>

  - title: "Version comparison"
    anchor: "version-comparison"
    content: |
      In this section:

        - Features
        - Available data

    subsections:        
      - title: "Features"
        anchor: "features"
        content: |
          {% include misc/icons.html %}

          A comparison of Stitch features across all HubSpot versions:

          <table class="attribute-list">
          <tr>
          <td align="right" width="35%; fixed">
          <strong>Feature</strong>
          </td>
          <td width="25%; fixed">
          <strong>v2 (latest)</strong>
          </td>
          <td>
          <strong>v1</strong>
          </td>
          <td>
          <strong>v01-03-2017</strong>
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Table selection
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Column selection
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Scheduling
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Configurable methods
          </strong>
          </td>
          <td>
          {{ not-supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Resets
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          On-demand replication
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Extraction Logs
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          Loading Reports
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          <tr>
          <td align="right">
          <strong>
          API availability
          </strong>
          </td>
          <td>
          {{ supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          <td>
          {{ not-supported }}
          </td>
          </tr>
          </table>

      - title: "Available data comparison"
        anchor: "available-data-comparison"
        content: |
          A comparison of all available data across all HubSpot versions. Clicking the link in the **[version] table** column will open the schema documentation for the table.

          <table class="attribute-list">
             <tbody>
                <tr class="c13">
                   <td class="c52 c36" colspan="1" rowspan="1">
                      <strong>Object</strong>
                   </td>
                   <td class="c17 c36" colspan="1" rowspan="1">
                      <strong>v2 table</strong>
                   </td>
                   <td class="c30 c36" colspan="1" rowspan="1">
                      <strong>v1 table</strong>
                   </td>
                   <td class="c17 c36" colspan="1" rowspan="1">
                      <strong>v01-03-2017 table</strong>
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Campaign</strong>
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      campaigns
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      campaigns
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      campaigns
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Company</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      companies
                   </td>
                   <td class="c29 c30" colspan="1" rowspan="1">
                      companies
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      companies
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Contact list</strong>
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      contact_lists
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      contact_lists
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      contact_lists
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Contact by company</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      contacts_by_company
                   </td>
                   <td class="c30 c29" colspan="1" rowspan="1">
                      contacts_by_company
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      {{ not-supported }}
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Deal pipeline</strong>
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      deal_pipelines
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      deal_pipelines
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      {{ not-supported }}
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Deal</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      deals
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      deals
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      deals
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Email event</strong>
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      email_events
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      email_events
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      email_events
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Engagement</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      engagements
                   </td>
                   <td class="c30 c29" colspan="1" rowspan="1">
                      engagements
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      engagements
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Form</strong>
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      forms
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      forms
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      forms
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Keyword</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      {{ not-supported }}
                   </td>
                   <td class="c30 c29" colspan="1" rowspan="1">
                      {{ not-supported }}
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      keywords
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52" colspan="1" rowspan="1">
                      <strong>Owner</strong>
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      owners
                   </td>
                   <td class="c30" colspan="1" rowspan="1">
                      owners
                   </td>
                   <td class="c17" colspan="1" rowspan="1">
                      owners
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c29" colspan="1" rowspan="1">
                      <strong>Subscription change</strong>
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      subscription_changes
                   </td>
                   <td class="c30 c29" colspan="1" rowspan="1">
                      subscription_changes
                   </td>
                   <td class="c10" colspan="1" rowspan="1">
                      subscription_changes
                   </td>
                </tr>
                <tr class="c13">
                   <td class="c52 c15" colspan="1" rowspan="1">
                      <strong>Workflow</strong>
                   </td>
                   <td class="c17 c15" colspan="1" rowspan="1">
                      workflows
                   </td>
                   <td class="c30 c15" colspan="1" rowspan="1">
                      {{ not-supported }}
                   </td>
                   <td class="c17 c15" colspan="1" rowspan="1">
                      workflows
                   </td>
                </tr>
             </tbody>
          </table>

  - title: "Changelog"
    anchor: "changelog"
    content: |
      Stay in the loop on updates to the HubSpot integration by following the changelog.
---