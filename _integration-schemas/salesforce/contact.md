---
tap: "salesforce"
version: "1.0"

name: "contact"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm
singer-schema: 
description: |
  The `contact` table contains info about your contacts, who are individuals associated with accounts in your Salesforce instance.

replication-method: "Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The contact ID."

  - name: "systemModStamp"
    type: "date-time"
    replication-key: true
    description: "The time when a user or automated process (ex: a trigger) last modified the contact."

  - name: "accountId"
    type: "string"
    description: "The ID of the account that is the parent of the contact."
    # foreign-key:
    #   - table: "account"
    #     attribute: "id"

  - name: "assistantName"
    type: "string" 
    description: "The name of the assistant."

  - name: "assistantPhone"
    type: "string"
    description: "The phone number associated with the contact."

  - name: "birthdate"
    type: "date"
    description: "The birthdate of the contact."

  - name: "canAllowPortalSelfReg"
    type: "boolean"
    description: "Indicates if the contact can self-register for your organization's Customer Portal (`true`) or not (`false`)."

  - name: "cleanStatus"
    type: "string"
    description: |
      The contact's clean status as compared with Data.com. Possible values are:

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
    description: "The ID of the `PartnerNetworkConnection` that shared the contact record with your organization. **Only available if Salesforce to Salesforce is enabled.**"

  - name: "connectionSentId"
    type: "string"
    description: "The ID of the `PartnerNetworkConnection` that you shared the contact record with. **Deprecated by Salesforce.**"

  - name: "department"
    type: "string"
    description: "The department of the contact."

  - name: "description"
    type: "string"
    description: "The description of the contact."

  - name: "doNotCall"
    type: "boolean"
    description: "Indicates if the contact does not want to be called (`true`)."

  - name: "email"
    type: "string"
    description: "The email address associated with the contact."

  - name: "emailBouncedDate"
    type: "date-time"
    description: "If bounce management is activated and an email sent to the contact bounces, the date and time the bounce occurred."

  - name: "emailBouncedReason"
    type: "string"
    description: "If bounce management is activated and an email sent to the contact bounces, the reason the bounce occurred."

  - name: "fax"
    type: "string"
    description: "The fax number associated with the contact."

  - name: "firstName"
    type: "string"
    description: "The first name of the contact."

  - name: "hasOptedOutOfEmail"
    type: "boolean"
    description: "Indicates if the contact would prefer not to receive email from Salesforce (`true`) or not (`false`)."

  - name: "hasOptedOutOfFax"
    type: "boolean"
    description: "Indicates if the contact would prefer not to receive faxes (`true`) or not (`false`)."

  - name: "homePhone"
    type: "string"
    description: "The home phone number associated with the contact."

  - name: "isDeleted"
    type: "boolean"
    description: "Indicates if the contact has been moved to the Recycle Bin (`true`) or not (`false`)."

  - name: "isEmailBounced" 
    type: "boolean"
    description: "If bounce management is activated and an email is sent to a contact, indicates if the email bounced (`true`) or not (`false`)."

  - name: "isPersonAccount"
    type: "boolean"
    description: "Indicates if the contact has a record type of Person Account (`true`) or not (`false`). Refer to [Salesforce's documentation](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm#i1438505) for info on the additional fields associated with this record type."

  - name: "jigsaw"
    type: "string"
    description: "The contact's ID from Data.com. If a contact has a value in this field, it means that the contact was imported from Data.com."

  - name: "lastActivityDate"
    type: "date-time"
    description: "The due date of the most recently logged event OR the most recently closed task associated with the contact, whichever is more recent."

  - name: "lastName"
    type: "string"
    description: "The last name of the contact."

  - name: "lastReferenceDate"
    type: "date-time"
    description: "The date a record associated with the contact was last viewed."

  - name: "lastViewedDate"
    type: "date-time"
    description: "The date the contact was last viewed."

  - name: "leadSource"
    type: "string"
    description: "The source of the lead."

  - name: "mailingAddress"
    type: "string"
    doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    description: |
      The compound form of the contact's mailing address. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `mailingStreet`
      - `mailingCity`
      - `mailingState`
      - `mailingStateCode`
      - `mailingCountry`
      - `mailingCountryCode`
      - `mailingPostalCode`
      - `mailingLatitude`
      - `mailingLongitude`
      - `mailingGeocodeAccuracy`

  - name: "mailingCity"
    type: "string"
    description: "The contact's mailing city."

  - name: "mailingCountry"
    type: "string"
    description: "The contact's mailing country."

  - name: "mailingCountryCode"
    type: "string"
    description: "The ISO country code for the contact's mailing address."

  - name: "mailingGeocodeAccuracy"
    type: "string"
    description: |
      The compound form of the accuracy level of the geocode for the contact's mailing address.

  - name: "mailingLatitude"
    type: "integer"
    description: "Used with `mailingLongitude` to specify the precise geolocation of a mailing address."

  - name: "mailingLongitude"
    type: "integer"
    description: "Used with `mailingLatitude` to specify the precise geolocation of a mailing address."

  - name: "mailingPostalCode"
    type: "string"
    description: "The postal code for the contact's mailing address."

  - name: "mailingState"
    type: "string"
    description: "The state for the contact's mailing address."

  - name: "mailingStateCode"
    type: "string"
    description: "The ISO state code for the contact's mailing address."

  - name: "mailingStreet"
    type: "string"
    description: "The street address for the contact's mailing address."

  - name: "masterRecordId"
    type: "string"
    description: |
      If the contact was deleted as the result of a merge, this field will contain the ID of the record that was kept.

      If this contact was deleted for any other reason (or hasn't been deleted), the value will be `NULL`.

  - name: "middleName"
    type: "string"
    description: "The middle name of the contact."

  - name: "mobilePhone"
    type: "string"
    description: "The mobile phone number associated with the contact."

  - name: "name"
    type: "string"
    description: |
      The concatenation of `firstName`, `middleName`, `lastName`, and `suffix`. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `firstName`
      - `middleName`
      - `lastName`
      - `suffix`

  - name: "otherAddress"
    type: "string"
    doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    description: |
      The compound form of the contact's alternate address. **Only available if using the REST API.**

      **If using the Bulk API**, track the following fields to replicate the same data:

      - `otherStreet`
      - `otherCity`
      - `otherState`
      - `otherStateCode`
      - `otherCountry`
      - `otherCountryCode`
      - `otherPostalCode`
      - `otherLatitude`
      - `otherLongitude`
      - `otherGeocodeAccuracy`

  - name: "otherCity"
    type: "string"
    description: "The contact's alternate city."

  - name: "otherCountry"
    type: "string"
    description: "The contact's alternate country."

  - name: "otherCountryCode"
    type: "string"
    description: "The ISO country code for the contact's alternate address."

  - name: "otherGeocodeAccuracy"
    type: "string"
    description: |
      The compound form of the accuracy level of the geocode for the contact's alternate address.

  - name: "otherLatitude"
    type: "integer"
    description: "Used with `otherLongitude` to specify the precise geolocation of the contact's alternate address."

  - name: "otherLongitude"
    type: "integer"
    description: "Used with `otherLatitude` to specify the precise geolocation of the contact's alternate address."

  - name: "otherPostalCode"
    type: "string"
    description: "The postal code for the contact's alternate address."

  - name: "otherState"
    type: "string"
    description: "The state for the contact's alternate address."

  - name: "otherStateCode"
    type: "string"
    description: "The ISO state code for the contact's alternate address."

  - name: "otherStreet"
    type: "string"
    description: "The street address for the contact's alternate address."

  - name: "otherPhone"
    type: "string"
    description: "The phone number associated with the contact's alternate address."

  - name: "ownerId"
    type: "string"
    description: "The ID of the owner of the account associated with the contact."
    # foreign-keys:
    #  - table: "account"
    #    attribute: "ownerId"
    #  - table: "lead"
    #    attribute: "ownerId"

  - name: "phone"
    type: "string"
    description: "The phone number associated with the contact."

  - name: "photoUrl"
    type: "string"
    description: |

      The path to be combined with the URL of a Salesforce instance to generate a URL to request the social network profile image associated with the contact.

      This field will be blank if Social Accounts and Contacts aren't enabled for the organization or requesting user.

  - name: "recordTypeId"
    type: "string"
    description: "The ID of the record type assigned to the contact."

  - name: "reportsToId"
    type: "string"
    description: "If `isPersonAccount` is `true`, this field will be `NULL`."

  - name: "salutation"
    type: "string"
    description: "The honorific added to the contact's name for use in letters, etc."

  - name: "suffix"
    type: "string"
    description: "The name suffix of the contact."

  - name: "title"
    type: "string"
    description: "The title of the contact. For example: `CEO`, `Director of Product`, etc."

---