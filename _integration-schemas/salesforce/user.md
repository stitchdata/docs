---
tap: "salesforce"
version: "1.0"

name: "user"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm
singer-schema: 
description: |
  The `user` table contains info about the users in your organization.

replication-method: "Key-based Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."

  - name: "systemModStamp"
    type: "date-time"
    replication-key: true
    description: "The time when a user or automated process (ex: a trigger) last modified the user."

  - name: "aboutMe"
    type: "string"
    description: "Information about the user, such as areas of interest or skills."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with a Customer Portal user. This field will be `NULL` for Salesforce users."

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

  - name: "alias"
    type: "string"
    description: "The user's alias."

  - name: "badgeText"
    type: "string"
    description: "The text description of a user badge that appears over the user's photo."

  - name: "bannerPhotoUrl"
    type: "string"
    description: "The URL for the user's banner photo."

  - name: "callCenterId"
    type: "string"
    description: "The call center to which the user is assigned. **Only available if Salesforce CRM Call Center is enabled.**"

  - name: "city"
    type: "string"
    description: "The city associated with the user."

  - name: "communityNickname"
    type: "string"
    description: "The name used to identify this user in the Community application, which includes the ideas and answers features."

  - name: "companyName"
    type: "string"
    description: "The name of the user's company."

  - name: "contactId"
    type: "string"
    description: "The ID of the contact associated with the account."

  - name: "country"
    type: "string"
    description: "The country associated with the user."

  - name: "countryCode"
    type: "string"
    description: "The ISO country code associated with the user."

  - name: "defaultCurrencyIsoCode"
    type: "string"
    description: "The user's default currency setting for new records."

  - name: "defaultDivision"
    type: "string"
    description: "The user's default division. **Only applicable if divisions are enabled.**"

  - name: "defaultGroupNotificationFrequency"
    type: "string"
    description: |
      The default frequency for sending the user's Chatter group email notifications when the user joins groups. Possible values are:

      - `P` - Email on every post
      - `D` - Daily digests
      - `W` - Weekly digests
      - `N` - Never

  - name: "delegatedApproverId"
    type: "string"
    description: "The ID of the user who is a delegated approver for the user."

  - name: "department"
    type: "string"
    description: "The company department associated with the user."

  - name: "digestFrequency"
    type: "string"
    description: |
      The frequency at which the system sends the user's Chatter personal digest. Possible values are:

      - `D` - Daily
      - `W` - Weekly
      - `N` - Never

  - name: "division"
    type: "string"
    description: "The division associated with the user. This is similar to `department` and unrelated to `defaultDivision`."

  - name: "email"
    type: "string"
    description: "The email address associated with the user."

  - name: "emailEncodingKey"
    type: "string"
    description: "The email encoding for the user, such as `ISO-8859-` or `UTF-8`."

  - name: "emailPreferencesAutoBcc"
    type: "boolean"
    description: "Indicates if the user receives copies of sent emails (`true`) or not (`false`). **Only applicable if compliance BCC emails aren't enabled.**"

  - name: "employeeNumber"
    type: "string"
    description: "The user's employee number."

  - name: "extension"
    type: "string"
    description: "The user's phone extension number."

  - name: "fax"
    type: "string"
    description: "The fax number associated with the user."

  - name: "federationIdentifier"
    type: "string"
    description: "The value that must be listed in the `Subject` element of a Security Assertion Markup Language (SAML) IDP certificate to authenticate the user for a client application using single-on."

  - name: "firstName"
    type: "string"
    description: "The user's first name."

  - name: "forecastEnabled"
    type: "boolean"
    description: "Indicates if the user is enabled as a Forecast Manager (`true`) or not (`false`) in customizable forecasting."

  - name: "fullPhotoUrl"
    type: "string"
    description: "The URL for the user's current profile photo."

  - name: "isActive"
    type: "boolean"
    description: "Indicates if the user has access to log in (`true`) or not (`false`)."

  - name: "isPortalEnabled"
    type: "boolean"
    description: "Indicates if the user has access to Communities or portals (`true`) or not (`false`)."

  - name: "isPortalSelfRegistered"
    type: "boolean"
    description: "Indicates if the user is a Customer Portal user who self-registered for your organization's Customer Portal (`true`) or not (`false`)."

  - name: "isPrmSuperUser"
    type: "boolean"
    description: "Indicates if the user has super user access in the partner portal (`true`) or (`false`). **This field must be enabled by Salesforce.**"

  - name: "isProfilePhotoActive"
    type: "boolean"
    description: "Indicates if the user has a profile photo (`true`) or not (`false`)."

  - name: "jigsawImportLimitOverride"
    type: "integer"
    description: "The Data.com user's monthly addition limit."

  - name: "languageLocaleKey"
    type: "string"
    description: "The user's language. For example: `English` or `French`"

  - name: "lastLoginDate"
    type: "date-time"
    description: "The date and time when the user last successfully logged in."

  - name: "lastName"
    type: "string"
    description: "The user's last name."

  - name: "lastReferenceDate"
    type: "date-time"
    description: "The date a record associated with the lead was last viewed."

  - name: "lastViewedDate"
    type: "date-time"
    description: "The date the lead was last viewed."

  - name: "latitude"
    type: "integer"
    description: "Used with `Longitude` to specify the precise geolocation of a address."

  - name: "localeSidKey"
    type: "string"
    description: 

  - name: "longitude"
    type: "integer"
    description: "Used with `Latitude` to specify the precise geolocation of a address."

  - name: "manager"
    type: "string"
    description: "The user's manager."

  - name: "managerId"
    type: "string"
    description: "The ID of the user who manages the user."

  - name: "mediumBannerPhotoUrl"
    type: "string"
    description: "The URL for the user's medium-sized user profile banner photo."

  - name: "middleName"
    type: "string"
    description: "The user's middle name. **This field must be enabled by Salesforce.**"

  - name: "mobilePhone"
    type: "string"
    description: "The mobile phone number associated with the user."

  - name: "name"
    type: "string"
    description: |
      The concatenation of `firstName` and `lastName`. **Only available if using the REST API.**

      **If using the Bulk API**, track the `firstName` and `lastName` fields to replicate the same data.

  - name: "offlineTrialExpirationDate"
    type: "date-time"
    description: "The date and time when the user's Connect Offline trial expires."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the user."

  - name: "portalRole"
    type: "string"
    description: |
      The role of the user in the Customer Portal. Possible values are:

      - `Executive`
      - `Manager`
      - `User`
      - `PersonAccount`

      **Only available if Customer Portal is enabled or Communities is enabled and there are available partner portal, Customer Portal, or High-Volume Portal User licenses.**

  - name: "postalCode"
    type: "string"
    description: "The user's postal or ZIP code."

  - name: "profileId"
    type: "string"
    description: "The ID of the user's profile."

  - name: "receivesAdminInfoEmails"
    type: "boolean"
    description: "Indicates if the user receives email for administrators from Salesforce (`true`) or not (`false`)."

  - name: "receivesInfoEmails"
    type: "boolean"
    description: "Indicates if the user receives informational email from Salesforce (`true`) or not (`false`)."

  - name: "senderEmail"
    type: "string"
    description: "The `From` email address when the user sends email."

  - name: "senderName"
    type: "string"
    description: "The name used as the email sender when the user sends emails."

  - name: "signature"
    type: "string"
    description: "The signature text added to emails."

  - name: "smallBannerPhotoUrl"
    type: "string"
    description: "The URL for the user's small user profile banner photo."

  - name: "smallPhotoUrl"
    type: "string"
    description: "The URL for the thumbnail of the user's current profile photo."

  - name: "state"
    type: "string"
    description: "The state associated with the user."

  - name: "stateCode"
    type: "string"
    description: "The ISO state code of the state associated with the user."

  - name: "street"
    type: "string"
    description: "The street address for the lead's address."

  - name: "suffix"
    type: "string"
    description: "The name suffix of the lead."

  - name: "timeZoneSidKey"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: "The business title of the user. For example: `CEO`, `Director of Product`, etc."

  - name: "username"
    type: "string"
    description: "The name the user enters to log into the API or user interface."

  - name: "userPermissionsCallCenterAutoLogin"
    type: "boolean"
    description: "Indicates if the user is enabled to use the auto login feature of the call center (`true`) or not (`false`). **Only applicable if Salesforce CRM Call Center is enabled.**"

  - name: "userPermissionsChatterAnswersUser"
    type: "boolean"
    description: "Indicates if the portal user is enabled to use the Chatter Answers feature (`true`) or not (`false`)."

  - name: "userPermissionsInteractionUser"
    type: "boolean"
    description: "Indicates if the user can run flows (`true`) or not (`false`)."

  - name: "userPermissionsJigsawProspectingUser"
    type: "boolean"
    description: "Indicates if the user is allocated one Data.com user license (`true`) or not (`false`)."

  - name: "userPermissionsKnowledgeUser"
    type: "boolean"
    description: "Indicates if the user is enabled to use Salesforce Knowledge (`true`) or not (`false`)."

  - name: "userPermissionsLiveAgentUser"
    type: "boolean"
    description: "Indicates if the user is enabled to use Live Agent (`true`) or not (`false`)."

  - name: "userPermissionsMarketingUser"
    type: "boolean"
    description: "Indicates if the user is enabled to manage campaigns in the user interface (`true`) or not (`false`)."

  - name: "userPermissionsMobileUser"
    type: "boolean"
    description: "Indicates if the user is allocated one Salesforce Mobile Classic license (`true`) or not (`false`)."

  - name: "userPermissionsOfflineUser"
    type: "boolean"
    description: "Indicates if the user is enabled to use Offline Edition (`true`) or not (`false`)."

  - name: "userPermissionsSFContentUser"
    type: "boolean"
    description: "Indicates if the user is allocated one Salesforce CRM Content User license (`true`) or not (`false`)."

  - name: "userPermissionsSiteforceContributorUser"
    type: "boolean"
    description: "Indicates if the user is allocated one Site.com Contributor feature license (`true`) or not (`false`)."

  - name: "userPermissionsSiteforcePublisherUser"
    type: "boolean"
    description: "Indicates if the user is allocated one Site.com Publisher feature license  (`true`) or not (`false`)."

  - name: "userPermissionsSupportUser"
    type: "boolean"
    description: "Indicates if the user is enabled to use the Salesforce console (`true`) or not (`false`)."

  - name: "userPermissionsWorkDotComeUserFeature"
    type: "boolean"
    description: "Indicates if the Work.com feature is enabled for the user (`true`) or not (`false`)."

  - name: "userPreferencesAcitivityRemindersPopup"
    type: "boolean"
    description: "When `true`, a reminder popup window will automatically open when an activity reminder is due for the user."

  - name: "userPreferencesApexPagesDeveloperMode"
    type: "boolean"
    description: "When `true`, indicates the user has enabled developer mode for editing Visualforce pages and controllers."

  - name: "userPreferencesContentEmailAsAndWhen"
    type: "boolean"
    description: "When `false`, a user with Salesforce CRM Content subscriptions receives a once daily email summary if activity occurs on their subscribed content, libraries, tags, or authors."

  - name: "userPreferencesContentNoEmail"
    type: "boolean"
    description: "When `false`, a user with Salesforce CRM Content subscriptions receives email notifications if activity occurs on their subscribed content, libraries, tags, or authors."

  - name: "userPreferencesEnableAutoSubForFeeds"
    type: "boolean"
    description: "When `true`, the user automatically subscribes to feeds for any objects that the user creates."

  - name: "userPreferencesDisableAllFeedsEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email for all updates to Chatter feeds, based on the types of feed emails and digests the user has enabled."

  - name: "userPreferencesDisableBookmarkEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone comments on a Chatter feed item after the user bookmarks it."

  - name: "userPreferencesDisableChangeCommentEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone comments on a change the user has made. For example: an update to their profile."

  - name: "userPreferencesDisableEndorsementEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone endorses them for a topic."

  - name: "userPreferencesDisableFileShareNotificationsForApi"
    type: "boolean"
    description: "When `false`, email notifications are sent from the person who has shared a file to the users with whom the file has been shared."

  - name: "userPreferencesDisableFollowersEmail"
    type: "boolean"
    description: "When `false`, the user will automatically receive an email every time someone starts following the user in Chatter."

  - name: "userPreferencesDisableLaterCommentEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives an email every time someone comments on a feed item after the user has commented on a feed item."

  - name: "userPreferencesDisableLikeEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone likes a post or comment the user made."

  - name: "userPreferencesDisableMentionsPostEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time the user is mentioned in posts."

  - name: "userPreferencesDisableMentionsPostEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time the user is mentioned in a post."

  - name: "userPreferencesDisableProfilePostEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone posts to the users profile."

  - name: "userPreferencesDisableSharePostEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time the user's post is shared."

  - name: "userPreferencesDisableFeedbackEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email related to Work.com feedback."

  - name: "userPreferencesDisCommentAfterLikeEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone comments on a post the user has liked."

  - name: "userPreferencesDisMentionsCommentEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time the user is mentioned in a comment."

  - name: "userPreferencesDisableMessageEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email for Chatter messages sent to the user."

  - name: "userPreferencesDisableRewardEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email related to Work.com rewards."

  - name: "userPreferencesDisableWorkEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives emails related to Work.com feedback, goals, and coaching."

  - name: "userPreferencesDisProfPostCommentEmail"
    type: "boolean"
    description: "When `false`, the user automatically receives email every time someone comments on posts on the user's profile."

  - name: "userPreferencesEventRemindersCheckboxDefault"
    type: "boolean"
    description: "When `true`, a reminder popup is automatically set on the user's events."

  - name: "userPreferencesHideBiggerPhotoCallout"
    type: "boolean"
    description: "When `true`, users can choose to hide the callout text below the large profile photo."

  - name: "userPreferencesHideChatterOnboardingSplash"
    type: "boolean"
    description: "When `true`, the initial Chatter onboarding prompts won't appear for the user."

  - name: "userPreferencesHideCSNDesktopTask"
    type: "boolean"
    description: "When `true`, the Chatter recommendations panel never displays the recommendation to install Chatter Desktop for the user."

  - name: "userPreferencesHideCSNGetChatterMobileTask"
    type: "boolean"
    description: "When `true`, the Chatter recommendations panel never displays the recommendation to install Chatter Mobile for the user."

  - name: "userPreferencesHideHideSecondChatterOnboardingSplash"
    type: "boolean"
    description: "When `true`, the secondary Chatter onboarding prompts won't appear for the user."

  - name: "userPreferencesHideS1BrowserUI"
    type: "boolean"
    description: "When `true`, the user will see the full Salesforce site. If `false`, the user will be automatically redirected to the Salesforce mobile web."

  - name: "userPreferencesHideSfxWelcomeMat"
    type: "boolean"
    description: "Indicates if the user sees the Lightning Experience new user message (`true`) or not (`false`)."

  - name: "userPreferencesJigsawListUser"
    type: "boolean"
    description: "When `true`, the user is a Data.com List user and shares record additions from a pool."

  - name: "userPreferencesLightningExperiencePreferred"
    type: "boolean"
    description: "When `true`, the user will be redirected to the Lighting Experience Interface."

  - name: "userPreferencesPathAssistantCollapsed"
    type: "boolean"
    description: "When `true`, Sales Path appears collapsed or hidden to the user."

  - name: "userPreferencesReminderSoundOff"
    type: "boolean"
    description: "When `true`, a sound automatically plays when an activity reminder is due for the user."

  - name: "userPreferencesShowCityToExternalUsers"
    type: "boolean"
    description: "When `true`, the city in the user's contact info will be visible to external users."

  - name: "userPreferencesShowCityToGuestUsers"
    type: "boolean"
    description: "When `true`, the city in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowCountryToExternalUsers"
    type: "boolean"
    description: "When `true`, the country in the user's contact info will be visible to external users."

  - name: "userPreferencesShowCountryToGuestUsers"
    type: "boolean"
    description: "When `true`, the country in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowEmailToExternalUsers"
    type: "boolean"
    description: "When `true`, the email address in the user's contact info will be visible to external users."

  - name: "userPreferencesShowEmailToGuestUsers"
    type: "boolean"
    description: "When `true`, the email address in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowFaxToExternalUsers"
    type: "boolean"
    description: "When `true`, the fax number in the user's contact info will be visible to external users."

  - name: "userPreferencesShowFaxToGuestUsers"
    type: "boolean"
    description: "When `true`, the fax number in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowManagerToExternalUsers"
    type: "boolean"
    description: "When `true`, the user's manager in the user's contact info will be visible to external users."

  - name: "userPreferencesShowManagerToGuestUsers"
    type: "boolean"
    description: "When `true`, the user's manager in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowMobilePhoneToExternalUsers"
    type: "boolean"
    description: "When `true`, the mobile phone number in the user's contact info will be visible to external users."

  - name: "userPreferencesShowMobilePhoneToGuestUsers"
    type: "boolean"
    description: "When `true`, the mobile phone number in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowPostalCodeToExternalUsers"
    type: "boolean"
    description: "When `true`, the postal code in the user's contact info will be visible to external users."

  - name: "userPreferencesShowPostalCodeToGuestUsers"
    type: "boolean"
    description: "When `true`, the postal code in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowProfilePicToExternalUsers"
    type: "boolean"
    description: "When `true`, the user's profile photo will be visible to external users."

  - name: "userPreferencesShowProfilePicToGuestUsers"
    type: "boolean"
    description: "When `true`, the user's profile photo will be visible to guest users."

  - name: "userPreferencesShowStateToExternalUsers"
    type: "boolean"
    description: "When `true`, the state in the user's contact info will be visible to external users."

  - name: "userPreferencesShowStateToGuestUsers"
    type: "boolean"
    description: "When `true`, the state in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowStreetAddressToExternalUsers"
    type: "boolean"
    description: "When `true`, the street address in the user's contact info will be visible to external users."

  - name: "userPreferencesShowStreetAddressToGuestUsers"
    type: "boolean"
    description: "When `true`, the street address in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowTitleToExternalUsers"
    type: "boolean"
    description: "When `true`, the business title in the user's contact info will be visible to external users."

  - name: "userPreferencesShowTitleToGuestUsers"
    type: "boolean"
    description: "When `true`, the business title in the user's contact info will be visible to guest users."

  - name: "userPreferencesShowWorkPhoneToExternalUsers"
    type: "boolean"
    description: "When `true`, the work phone number in the user's contact info will be visible to external users."

  - name: "userPreferencesShowWorkPhoneToGuestUsers"
    type: "boolean"
    description: "When `true`, the work phone number in the user's contact info will be visible to guest users."

  - name: "userPreferencesSortFeedByComment"
    type: "boolean"
    description: "When `true`, the user's feed is sorted by most recent comment activity. If `false`, the feed is sorted by post date."

  - name: "userPreferencesTaskRemindersCheckboxDefault"
    type: "boolean"
    description: "When `true`, a reminder popup is automatically set on the user's tasks."

  - name: "userRoleId"
    type: "string"
    description: "The ID of the user role assigned to the user."

  - name: "userType"
    type: "string"
    doc-link: "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm#profilelicensetype"
    description: |
      The category of the user license allocated to the user. Possible values include:

      - `Standard`
      - `PowerPartner`
      - `CSPLitePortal`
      - `CustomerSuccess`
      - `PowerCustomerSuccess`
      - `CsnOnly`
---
