---
tap: "bing-ads"
version: "1.0"

name: "ads"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/ad
singer-schema: 
description: |
  The `ads` table contains info about the following ad types:

  - `AppInstall`
  - `DynamicSearch`
  - `ExpandedText`
  - `Product`
  - `Text`
  - `Image`

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
api-method:
  name: "getAdsByAdGroupId"
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getadsbyadgroupid

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ad ID."
    foreign-key-id: "ad-id"

  - name: "adFormatPreference"
    type: "string"
    description: |
      Indicates whether or not the ad copy is shown to users as a search or native ad. Search ads tend to be written as a call to action, whereas intent ads are written in a more informational style.

      Possible values are:

      - `Native` - Ad will be eligible only for the native ad format
      - `All` - Ad will be eligible for both search and native ad formats

  - name: "devicePreference"
    type: "integer"
    description: "Determines the device preference for showing the ad."

  - name: "editorialStatus"
    type: "string"
    description: "The editorial review status of the ad, which indicates whether the ad is pending review, approved, or disapproved."

  - name: "finalAppUrls"
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

  - name: "finalMobileUrls"
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

  - name: "finalUrls"
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

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the ad."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    subattributes:
      - name: "keyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the ad's forward compatibility settings."
        subattributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "status"
    type: "string"
    description: "The status of the ad. Possible values are `Active` and `Paused`."

  - name: "trackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all landing page URLs."

  - name: "type"
    type: "string"
    description: "The type of the ad."

  - name: "urlCustomParameters"
    type: "string"
    description: "The custom collection of key and value parameters for URL tracking."
---