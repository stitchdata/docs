---
tap: "bing-ads"
# version: "1.0"

name: "ads"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/ad
singer-schema: 
description: |
  The `ads` table contains info about the ads in your Bing Ads account.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
api-method:
  name: "getAdsByAdGroupId"
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getadsbyadgroupid

attributes:
  - name: "id"
    type: ""
    primary-key: true
    description: "The ad ID."
    doc-link:

  - name: "adFormatPreference"
    type: "string"
    description: |
      Indicates whether or not the ad copy is shown to users as a search or native ad. Search ads tend to be written as a call to action, whereas intent ads are written in a more informational style.

      Possible values are:

      - `Native` - Ad will be eligible only for the native ad format
      - `All` - Ad will be eligible for both search and native ad formats

  - name: "devicePreference"
    type: ""
    description: "Determines the device preference for showing the ad."

  - name: "editorialStatus"
    type: ""
    description: "The editorial review status of the ad, which indicates whether the ad is pending review, approved, or disapproved."

  - name: "finalAppUrls"
    type: ""
    description: ""

  - name: "finalMobileUrls"
    type: ""
    description: "The mobile landing page URL. This is only supported for text ads."

  - name: "finalUrls"
    type: ""
    description: "The last or final URl where a user is taken, whether or not the click to final URL path included any redirects."

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility "
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    array-attributes:

  - name: "status"
    type: ""
    description: "The status of the ad. Possible values are `Active` and `Paused`."

  - name: "trackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all landing page URLs."

  - name: "type"
    type: ""
    description: "The type of the ad."

  - name: "urlCustomParameters"
    type: ""
    description: "The custom collection of key and value parameters for URL tracking."

---