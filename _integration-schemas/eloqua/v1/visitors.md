---
tap: "eloqua"
version: "1.0"

name: "visitors"
key: "visitors"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-data-visitors-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/visitors.json"
description: |
  The `{{ table.name }}` table contains info about your {{ integration.display_name }} visitors. According to {{ integration.display_name }}, _"A visitor is a data entity that represents a unique cookie. The tracked activity data from that cookie is associated with the Visitor. There can be multiple visitors linked to a single contact."_

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve visitor data"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The visitor ID."
    foreign-key-id: "visitor-id"

  - name: "V_LastVisitDateAndTime"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "V_Browser_Type"
    type: "string"
    description: ""

  - name: "V_CityFromIP"
    type: "string"
    description: ""

  - name: "V_CompanyDNSName"
    type: "string"
    description: ""

  - name: "V_CompanyNameFromIP1"
    type: "string"
    description: ""

  - name: "V_CountryFromIP"
    type: "string"
    description: ""

  - name: "V_CountryName"
    type: "string"
    description: ""

  - name: "V_Current_Total_Pages"
    type: "integer"
    description: ""

  - name: "V_Current_Visit_Length"
    type: "integer"
    description: ""

  - name: "V_FirstPageInVisit"
    type: "string"
    description: ""

  - name: "V_FirstVisitDateAndTime"
    type: "date-time"
    description: ""

  - name: "V_HostName"
    type: "string"
    description: ""

  - name: "V_IPAddress"
    type: "string"
    description: ""

  - name: "V_ISPFromIP"
    type: "string"
    description: ""

  - name: "V_LastPageInVisit"
    type: "string"
    description: ""

  - name: "V_LatitudeFromIP"
    type: "number"
    description: ""

  - name: "V_LongitudeFromIP"
    type: "number"
    description: ""

  - name: "V_Name"
    type: "string"
    description: ""

  - name: "V_ProvinceFromIP"
    type: "string"
    description: ""

  - name: "V_TimeZone"
    type: "string"
    description: ""

  - name: "V_TimeZoneOffsetMin"
    type: "integer"
    description: ""

  - name: "V_Total_Pages"
    type: "integer"
    description: ""

  - name: "V_Total_Time"
    type: "integer"
    description: ""

  - name: "V_Total_Visits"
    type: "integer"
    description: ""

  - name: "V_ZipCodeFromIP"
    type: "string"
    description: ""

  - name: "contactId"
    type: "string"
    description: "The contact record ID associated to this profile, if any."
    foreign-key-id: "contact-id"

  - name: "createdAt"
    type: "string"
    description: "The date and time the visitor was created, expressed in Unix time."

  - name: "currentStatus"
    type: "string"
    description: "The current status of the visitor."

  - name: "externalId"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: "The visitor's type in {{ integration.display_name }}."

  - name: "visitorId"
    type: "string"
    description: "The ID of the visitor profile."
---