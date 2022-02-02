---
title: "Bing Ads integration: New version (v2)"
content-type: "changelog-entry"
date: 2018-10-04
entry-type: new-feature
entry-category: integration
connection-id: bing-ads
connection-version: 2

schema-changes:
  - name: "All report tables"
    renamed:
      - v1: "GregorianDate"
        v2: "TimePeriod"
      - v1: "Search query"
        v2: "SearchQuery"
      - v1: "CountryOrRegion"
        v2: "Country"
      - v1: "Device type"
        v2: "DeviceType"
      - v1: "Status"
        v2: "CampaignStatus"
      - v1: "AudienceTargetSetting"
        v2: "TargetingSetting"
      - v1: "NodeId"
        v2: "AdGroupCriterionId"
      - v1: "FinalAppURL"
        v2: "FinalAppUrl"
      - v1: "FinalURL"
        v2: "FinalUrl"
      - v1: "FinalMobileURL"
        v2: "FinalMobileUrl"
  - name: "AdGroundPerformanceReport, CampaignPerformanceReport, and KeywordPerformanceReport tables"
    renamed:
      - v1: "HistoricQualityScore"
        v2: "HistoricalQualityScore"
      - v1: "HistoricExpectedCtr"
        v2: "HistoricalExpectedCtr"
      - v1: "HistoricAdRelevance"
        v2: "HistoricalAdRelevance"
      - v1: "HistoricLandingPageExperience"
        v2: "HistoricalLandingPageExperience"
  - name: "KeyWordPerformanceReport"
    renamed:
      - v1: "SidebarBid"
        v2: "FirstPageBid"
  - name: "Accounts"
    renamed:
      - v1: "CurrencyType"
        v2: "CurrencyCode"
    removed:
      - name: "AccountType"
      - name: "CountryCode"
  - name: "AdGroups"
    renamed:
      - v1: "SearchBid"
        v2: "CpcBid"
      - v1: "NativeBidAdjustment"
        v2: "AudienceAdsBigAdjustment"
    removed:
      - name: "RemarketingTargetingSetting"
      - name: "PricingModel"
      - name: "AdDistribution"
      - name: "ContentBid"
  - name: "Campaigns"
    renamed:
      - v1: "NativeBidAdjustment"
        v2: "AudienceAdsBidAdjustment"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our Bing Ads integration is now available! This version takes advantage of the latest Bing Ads API, version 12.

Here's a high-level look at the updates to our integration:

- **Support for multi-user credentials**: The new integration allow for extracting data where you use one Microsoft account and manage accounts across different customers.

- **Column restrictions**: Bing now prevents the extraction of reports with invalid field combinations. Stitch will automatically show these exclusions within the field selection interface when setting up your reports. Refer to [Bing's documentation](https://docs.microsoft.com/en-us/bingads/guides/reports?view=bingads-12#columnrestrictions){:target="new"} for a full list of [column restrictions](https://docs.microsoft.com/en-us/bingads/guides/reports?view=bingads-12#columnrestrictions){:target="new"}.

- **Schema updates**: The following changes have been made to table schemas:
{% for table in page.schema-changes %}
  - **{{ table.name }}**: 
    <table>
      <tr>
        <td colspan="2" class="table-subheading">
          <strong>
            RENAMED ATTRIBUTES
          </strong>
        </td>
      </tr>
      <tr>
        <td>
          <strong>
            Bing Ads v1
          </strong>
        </td>
        <td>
          <strong>
            Bing Ads v{{ this-connection.this-version }}
          </strong>
        </td>
      </tr>
      {% for attribute in table.renamed %}
        <tr>
          <td>
            {{ attribute.v1 }}
          </td>
          <td>
            {{ attribute.v2 }}
          </td>
        </tr>
      {% endfor %}

      {% if table.removed %}
        <tr>
          <td colspan="2" class="table-subheading">
            <strong>
              REMOVED ATTRIBUTES
            </strong>
          </td>
        </tr>
        {% for attribute in table.removed %}
          <tr>
            <td>
              {{ attribute.name }}
            </td>
            <td>
            </td>
          </tr>
        {% endfor %}
      {% endif %}
    </table>
{% endfor %}