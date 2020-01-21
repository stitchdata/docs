---
tap: "bing-ads"
version: "2"

name: "ads"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/ad
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about the following ad types:

  - `AppInstall`
  - `DynamicSearch`
  - `ExpandedText`
  - `Product`
  - `Text`
  - `Image`

  [This is a **Core Object** table](#replication).

  #### Schema changes from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, the schema of this table has changed. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `Domain` has been added
  - `TextPart2` has been added
  - `TitlePart3` has been added

replication-method: "Full Table"
api-method:
  name: "getAdsByAdGroupId"
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getadsbyadgroupid

attributes:
  - name: "Id"
    type: "integer"
    primary-key: true
    description: "The ad ID."
    foreign-key-id: "ad-id"

  - name: "AdFormatPreference"
    type: "string"
    description: |
      Indicates whether or not the ad copy is shown to users as a search or native ad. Search ads tend to be written as a call to action, whereas intent ads are written in a more informational style.

      Possible values are:

      - `Native` - Ad will be eligible only for the native ad format
      - `All` - Ad will be eligible for both search and native ad formats

  - name: "DevicePreference"
    type: "integer"
    description: "Determines the device preference for showing the ad."

  - name: "Domain"
    type: "string"
    description: |
      **Applicable to `Type: ExpandedText` ads.** The URL that will be displayed instead of the final URL. The final URL will still be used for the landing page URL.

  - name: "EditorialStatus"
    type: "string"
    description: "The editorial review status of the ad, which indicates whether the ad is pending review, approved, or disapproved."

  - name: "FinalAppUrls"
    type: "string"
    description: "The last or final URL where a user who clicks on an in-app ad is taken."
    subattributes:
      - name: "string"
        type: "array"
        description: "The app landing page URL."
        subattributes:
          - name: "value"
            type: "string"
            description: "The app landing page URL."

  - name: "FinalMobileUrls"
    type: "array"
    description: "The last or final URL where a user who clicks on a mobile ad is taken."
    subattributes:
      - name: "string"
        type: "array"
        description: "The mobile landing page URL. This is only supported for text ads."
        subattributes:
          - name: "value"
            type: "string"
            description: "The mobile landing page URL. This is only supported for text ads."

  - name: "FinalUrls"
    type: "string"
    description: "The last or final URL where a user is taken, whether or not the click to final URL path included any redirects."
    subattributes:
      - name: "string"
        type: "array"
        description: "The last or final URL where a user is taken, whether or not the click to final URL path included any redirects."
        subattributes:
          - name: "value"
            type: "string"
            description: "The last or final URL where a user is taken, whether or not the click to final URL path included any redirects."

  - name: "ForwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the ad."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    subattributes:
      - name: "KeyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the ad's forward compatibility settings."
        subattributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "Status"
    type: "string"
    description: "The status of the ad. Possible values are `Active` and `Paused`."

  - name: "TextPart2"
    type: "string"
    description: |
      **Applicable to `Type: ExpandedText` ads.** As per Microsoft, this field is reserved for future use.

  - name: "TitlePart1"
    type: "string"
    description: |
      **Applicable to `Type: ExpandedText` ads.** The first part of the ad title.

  - name: "TitlePart2"
    type: "string"
    description: |
      **Applicable to `Type: ExpandedText` ads.** The second part of the ad title.

  - name: "TitlePart3"
    type: "string"
    description: |
      **Applicable to `Type: ExpandedText` ads.** As per Microsoft, this field is reserved for future use.

  - name: "TrackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all landing page URLs."

  - name: "Type"
    type: "string"
    description: "The type of the ad."

  - name: "UrlCustomParameters"
    type: "string"
    description: "The custom collection of key and value parameters for URL tracking."
---