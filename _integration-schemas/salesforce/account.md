---
tap: "salesforce"
version: "1.0"

name: "account"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm#!
singer-schema: 
description: |
  The `account` table contains info about the individual accounts (organizations and persons) involved with your business. This could be a customer, a competitor, a partner, and so on.

notes: 

replication-method: "Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."

  - name: "systemModStamp"
    type: "date-time"
    replication-key: true
    description: "The time when a user or automated process (ex: a trigger) last modified the account."

  - name: "accountNumber"
    type: "string"
    description: "The account number assigned to this account."

  - name: "accountSource"
    type: "string"
    description: "The source of the account record. For example: `Trade Show`"

  - name: "annualRevenue"
    type: "number"
    description: "The estimated annual revenue of the account."

  - name: "billingAddress"
    type: "string"
    doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    description: |
      The compound form of the account's billing address. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `billingStreet`
      - `billingCity`
      - `billingState`
      - `billingStateCode`
      - `billingCountry`
      - `billingCountryCode`
      - `billingPostalCode`
      - `billingLatitude`
      - `billingLongitude`
      - `billingGeocodeAccuracy`

  - name: "billingCity"
    type: "string"
    description: "The account's billing city."

  - name: "billingCountry"
    type: "string"
    description: "The account's billing country."

  - name: "billingCountryCode"
    type: "string"
    description: "The ISO country code for the account's billing address."

  - name: "billingGeocodeAccuracy"
    type: "string"
    description: |
      The compound form of the accuracy level of the geocode for the account's billing address. **Only available if using the REST API.**

      **If using the Bulk API**, track the `billingLatitude` and `billingLongitude` fields to replicate the same data.

  - name: "billingLatitude"
    type: "integer"
    description: "Used with `billingLongitude` to specify the precise geolocation of a billing address."

  - name: "billingLongitude"
    type: "integer"
    description: "Used with `billingLatitude` to specify the precise geolocation of a billing address."

  - name: "billingPostalCode"
    type: "string"
    description: "The postal code for the account's billing address."

  - name: "billingState"
    type: "string"
    description: "The state for the account's billing address."

  - name: "billingStateCode"
    type: "string"
    description: "The ISO state code for the account's billing address."

  - name: "billingStreet"
    type: "string"
    description: "The street address for the account's billing address."

  - name: "cleanStatus"
    type: "string"
    description: |
      The account's clean status as compared with Data.com. Possible values are:

      - `Matched`
      - `Different`
      - `Acknowledged`
      - `NotFound`
      - `Inactive`
      - `Pending`
      - `SelectMatch`
      - `Skipped`

  - name: "connectionReceivedId"
    type: "string"
    description: "The ID of the `PartnerNetworkConnection` that shared the account record with your organization. **Only available if Salesforce to Salesforce is enabled.**"

  - name: "description"
    type: "string"
    description: "The description of the account."

  - name: "dunsNumber"
    type: "string"
    description: "The Data Universal Numbering System (DUNS) number associated with the account. **Only available if using Data.com Prospector or Data.com Clean.**"

  - name: "fax"
    type: "string"
    description: "The fax number associated with the account."

  - name: "industry"
    type: "string"
    description: "The industry associated with the account."

  - name: "isCustomerPortal"
    type: "boolean"
    description: "Indicates whether the account has at least one contact enabled to use the organization's Customer Portal. This field will be `true` if at least one contact is enabled to use the portal. **Only available if Customer Portal or Communities is enabled and there are Customer Portal licenses.**"

  - name: "isDeleted"
    type: "boolean"
    description: "Indicates if the account has been moved to the Recycle Bin (`true`) or not (`false`)."

  - name: "isPartner"
    type: "boolean"
    description: "Indicates whether the account has at least one contact enabled to use the organization's partner portal (`true`) or not (`false`). **Only available if Partner Portal or Communities is enabled and there are partner portal licenses.**"

  - name: "isPersonAccount"
    type: "boolean"
    description: "Indicates if the account has a record type of Person Account (`true`) or not (`false`). Refer to [Salesforce's documentation](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm#i1438505) for info on the additional fields associated with this record type."

  - name: "jigsaw"
    type: "string"
    description: "The account's ID from Data.com. If an account has a value in this field, it means that the account was imported from Data.com."

  - name: "lastActivityDate"
    type: "date-time"
    description: "The due date of the most recently logged event OR the most recently closed task associated with the account, whichever is more recent."

  - name: "lastReferenceDate"
    type: "date-time"
    description: "The date a record associated with the account was last viewed."

  - name: "lastViewedDate"
    type: "date-time"
    description: "The date the account was last viewed."

  - name: "masterRecordId"
    type: "string"
    description: |
      If the account was deleted as the result of a merge, this field will contain the ID of the record that was kept.

      If this account was deleted for any other reason (or hasn't been deleted), the value will be `NULL`.

  - name: "naicsCode"
    type: "string"
    description: "The North American Industry Classification System (NAICS) code associated with the account. **Only available if using Data.com Prospector or Data.com Clean.**"

  - name: "naicsDescription"
    type: "string"
    description: "The description associated with the account's NAICS code. **Only available if using Data.com Prospector or Data.com Clean.**"

  - name: "name"
    type: "string"
    description: |
      The name of the account.

      If the account's record type is `PersonAccount`, the value of this field will be a concatenation of the `FirstName`, `MiddleName`, `LastName`, and `Suffix` fields of the associated person contact.

  - name: "name"
    type: "string"
    description: |
      The name of the account. 

      If the account's record type is `PersonAccount`, the value of this field will be a concatenation of the `firstName`, `middleName`, `lastName`, and `suffix` fields of the associated person contact. **Only available if using the REST API.**

  - name: "numberOfEmployees"
    type: "number"
    description: "The number of employees working at the company represented by the account."

  - name: "operatingHoursId"
    type: "string"
    description: "The operating hours associated with the account. **Only available if Field Service Lightning is enabled.**"

  - name: "ownerId"
    type: "string"
    description: "The ID of the user who currently owns the account."

  - name: "ownership"
    type: "string"
    description: "The ownership type for the account. For example: `Private`"

  - name: "parentId"
    type: "string"
    description: "The ID of the account's parent object, if applicable."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the account."

  - name: "photoUrl"
    type: "string"
    description: |

      The path to be combined with the URL of a Salesforce instance to generate a URL to request the social network profile image associated with the account.

      This field will be blank if Social Accounts and Contacts aren't enabled for the organization or requesting user.

  - name: "rating"
    type: "string"
    description: "The account's prospect rating. For example: `Cold`"

  - name: "recordTypeId"
    type: "string"
    description: "The ID of the record type assigned to the account."

  - name: "salutation"
    type: "string"
    description: "The honorific added to the name for use in letters, etc."

  - name: "shippingAddress"
    type: "string"
    doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    description: |
      The compound form of the account's shipping address. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `shippingStreet`
      - `shippingCity`
      - `shippingState`
      - `shippingStateCode`
      - `shippingCountry`
      - `shippingCountryCode`
      - `shippingPostalCode`
      - `shippingLatitude`
      - `shippingLongitude`
      - `shippingGeocodeAccuracy`

  - name: "shippingCity"
    type: "string"
    description: "The account's shipping city."

  - name: "shippingCountry"
    type: "string"
    description: "The account's shipping country."

  - name: "shippingCountryCode"
    type: "string"
    description: "The ISO country code for the account's shipping address."

  - name: "shippingGeocodeAccuracy"
    type: "string"
    description: |
      The compound form of the accuracy level of the geocode for the account's shipping address. **Only available if using the REST API.**

      **If using the Bulk API**, track the `shippingLatitude` and `shippingLongitude` fields to replicate the same data.

  - name: "shippingLatitude"
    type: "integer"
    description: "Used with `shippingLongitude` to specify the precise geolocation of a shipping address."

  - name: "shippingLongitude"
    type: "integer"
    description: "Used with `shippingLatitude` to specify the precise geolocation of a shipping address."

  - name: "shippingPostalCode"
    type: "string"
    description: "The postal code for the account's shipping address."

  - name: "shippingState"
    type: "string"
    description: "The state for the account's shipping address."

  - name: "shippingStateCode"
    type: "string"
    description: "The ISO state code for the account's shipping address."

  - name: "shippingStreet"
    type: "string"
    description: "The street address for the account's shipping address."

  - name: "sic"
    type: "string"
    description: "The Standard Industrial Classification code of the company's main business organization."

  - name: "sicDesc"
    type: "string"
    description: "The description associated with the account's SIC code."

  - name: "site"
    type: "string"
    description: "The name of the account's location. For example: `Philadelphia` or `Main Office`"

  - name: "tickerSymbol"
    type: "string"
    description: "The stock market symbol associated with the account."

  - name: "tradeStyle"
    type: "string"
    description: "Similar to `doing business as`, this is the name (different from its legal name), that the organization may use for conducting business. **Only available if using Data.com Prospector or Data.com Clean.**"

  - name: "type"
    type: "string"
    description: "The type of the account. For example: `Customer`"

  - name: "website"
    type: "string"
    description: "The website associated with the account."

  - name: "yearStarted"
    type: "string"
    description: "The date when the account (organization) was legally established. **Only available if using Data.com Prospector or Data.com Clean.**"

---