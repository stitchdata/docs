---
tap: "salesforce"
version: "1.0"

name: "lead"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm
singer-schema: 
description: |
  The `lead` table contains info about your leads, who are prospects or potential Opportunities.

notes: 

replication-method: "Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The lead ID."

  - name: "systemModStamp"
    type: "date-time"
    replication-key: true
    description: "The time when a user or automated process (ex: a trigger) last modified the lead."

  - name: "address"
    type: "string"
    doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    description: |
      The compound form of the lead's address. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `street`
      - `city`
      - `state`
      - `stateCode`
      - `country`
      - `countryCode`
      - `postalCode`
      - `latitude`
      - `longitude`
      - `geocodeAccuracy`

  - name: "annualRevenue"
    type: "number"
    description: "The estimated annual revenue for the lead's company."

  - name: "city"
    type: "string"
    description: "The city for the address of the lead."

  - name: "cleanStatus"
    type: "string"
    description: |
      The lead's clean status as compared with Data.com. Possible values are:

      - `Matched`
      - `Different`
      - `Acknowledged`
      - `NotFound`
      - `Inactive`
      - `Pending`
      - `SelectMatch`
      - `Skipped`

  - name: "company"
    type: "string"
    description: "The company associated with the lead."

  - name: "companyDunsNumber"
    type: "string"
    description: "The Data Universal Numbering System (DUNS) number associated with the lead's company. **Only available if using Data.com Prospector or Data.com Clean.**"

  - name: "connectionReceivedId"
    type: "string"
    description: "The ID of the `PartnerNetworkConnection` that shared the lead record with your organization. **Only available if Salesforce to Salesforce is enabled.**"

  - name: "convertedAccountId"
    type: "string"
    description: "The reference ID that points to the Account into which the lead has been converted."
    # foreign-keys:
    #   - table: "account"
    #     attribute: "id"

  - name: "convertedContactId"
    type: "string"
    description: "The reference ID that points to the Contact into which the lead has been converted."
    # foreign-keys:
    #   - table: "contact"
    #     attribute: "id"

  - name: "convertedDate"
    type: "date-time"
    description: "The date on which the lead was converted."

  - name: "convertedOpportunityId"
    type: "string"
    description: "The reference ID that points to the Opportunity into which the lead has been converted."
    # foreign-keys:
    #   - table: "opportunity"
    #     attribute: "id"

  - name: "country"
    type: "string"
    description: "The country for the address of the lead."

  - name: "countryCode"
    type: "string"
    description: "The ISO country code for the lead's address."

  - name: "currencyIsoCode"
    type: "string"
    description: "The ISO code for any currency allowed by the organization. **Only available for organizations with the multicurrency feature enabled.**"

  - name: "description"
    type: "string"
    description: "The description of the lead."

  - name: "division"
    type: "string"
    description: "The logical segment of your organization's data. For example: `North America`, `Consulting`, `Operations`. **Only available if the organization has the Division permission enabled.**"

  - name: "email"
    type: "string"
    description: "The email address associated with the lead."

  - name: "emailBouncedDate"
    type: "date-time"
    description: "If bounce management is activated and an email sent to the lead bounces, the date and time the bounce occurred."

  - name: "emailBouncedReason"
    type: "string"
    description: "If bounce management is activated and an email sent to the lead bounces, the reason the bounce occurred."

  - name: "fax"
    type: "string"
    description: "The fax number associated with the lead."

  - name: "firstName"
    type: "string"
    description: "The first name of the lead."

  - name: "hasOptedOutOfEmail"
    type: "boolean"
    description: "Indicates if the lead would prefer not to receive email from Salesforce (`true`) or not (`false`)."

  - name: "geocodeAccuracy"
    type: "string"
    description: |
      The compound form of the accuracy level of the geocode for the lead's address.

  - name: "industry"
    type: "string"
    description: "The industry the lead works in."

  - name: "isConverted"
    type: "boolean"
    description: "Indicates if the lead has been converted (`true`) or not (`false`)."

  - name: "isDeleted"
    type: "boolean"
    description: "Indicates if the lead has been moved to the Recycle Bin (`true`) or not (`false`)."

  - name: "isUnreadByOwner"
    type: "boolean"
    description: "If `true`, the lead has been assigned but not yet viewed."

  - name: "jigsaw"
    type: "string"
    description: "The lead's ID from Data.com. If a lead has a value in this field, it means that the contact was imported from Data.com."

  - name: "lastActivityDate"
    type: "date-time"
    description: "The due date of the most recently logged event OR the most recently closed task associated with the lead, whichever is more recent."

  - name: "lastName"
    type: "string"
    description: "The last name of the lead."

  - name: "lastReferenceDate"
    type: "date-time"
    description: "The date a record associated with the lead was last viewed."

  - name: "lastViewedDate"
    type: "date-time"
    description: "The date the lead was last viewed."

  - name: "latitude"
    type: "integer"
    description: "Used with `Longitude` to specify the precise geolocation of a address."

  - name: "longitude"
    type: "integer"
    description: "Used with `Latitude` to specify the precise geolocation of a address."

  - name: "leadSource"
    type: "string"
    description: "The source from which the lead was obtained."

  - name: "masterRecordId"
    type: "string"
    description: |
      If the lead was deleted as the result of a merge, this field will contain the ID of the record that was kept.

      If this lead was deleted for any other reason (or hasn't been deleted), the value will be `NULL`.

  - name: "middleName"
    type: "string"
    description: "The middle name of the lead."

  - name: "mobilePhone"
    type: "string"
    description: "The mobile phone number associated with the lead."

  - name: "name"
    type: "string"
    description: |
      The concatenation of `firstName`, `middleName`, `lastName`, and `suffix`. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `firstName`
      - `middleName`
      - `lastName`
      - `suffix`

  - name: "numberOfEmployees"
    type: "integer"
    description: "The number of employees at the lead's company."

  - name: "ownerId"
    type: "string"
    description: "The ID of the owner of the lead."
    # foreign-keys:
    #   - table: "account"
    #     attribute: "ownerId"
    #   - table: "contact"
    #     attribute: "ownerId"

  - name: "partnerAccountId"
    type: "string"
    description: "The ID of the partner account for the partner that owns the lead. **Only available if Partner Relationship Management is enabled or Communities is enabled and you have partner licenses.**"

  - name: "phone"
    type: "string"
    description: "The phone number associated with the lead."

  - name: "photoUrl"
    type: "string"
    description: |

      The path to be combined with the URL of a Salesforce instance to generate a URL to request the social network profile image associated with the lead.

      This field will be blank if Social Accounts and Contacts aren't enabled for the organization or requesting user.

  - name: "PostalCode"
    type: "string"
    description: "The postal code for the lead's address."

  - name: "rating"
    type: "string"
    description: "The rating of the lead."

  - name: "recordTypeId"
    type: "string"
    description: "The ID of the record type assigned to the lead."

  - name: "salutation"
    type: "string"
    description: "The salutation of the lead."

  - name: "scoreIntelligenceId"
    type: "string"
    description: "The ID of the intelligent field record that contains the lead score."

  - name: "state"
    type: "string"
    description: "The state for the lead's address."

  - name: "stateCode"
    type: "string"
    description: "The ISO state code for the lead's address."

  - name: "status"
    type: "string"
    description: "The status code of the converted lead."

  - name: "street"
    type: "string"
    description: "The street address for the lead's address."

  - name: "suffix"
    type: "string"
    description: "The name suffix of the lead."

  - name: "title"
    type: "string"
    description: "The title of the lead. For example: `CEO`, `Director of Product`, etc."

  - name: "website"
    type: "string"
    description: "The website for the lead."
---