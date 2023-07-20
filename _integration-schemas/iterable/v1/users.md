---
tap: "iterable-core"
version: "1"
key: ""

name: "users"
doc-link: https://api.iterable.com/api/docs#export_exportDataJson
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/users.json
description: |
  The **{{ table.name }}** table contains information about all users in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Export data to JSON"
  doc-link: "ttps://api.iterable.com/api/docs#export_exportDataJson"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The user email."
    foreign-key-id: "email-id"

  - name: "profileUpdatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the profile was updated."  

  - name: "CCProvider"
    type: "string"
    description: ""

  - name: "Industry"
    type: "string"
    description: ""

  - name: "accessIp"
    type: "string"
    description: ""

  - name: "acquisition_source"
    type: "string"
    description: ""

  - name: "actively_seeking"
    type: "boolean"
    description: ""

  - name: "age"
    type: "integer"
    description: ""

  - name: "auctionDigest"
    type: "object"
    description: ""


  - name: "auctionDigest"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "auctionDigest.auctionDateLocation"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "auctionDigest.auctionHouse"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "auctionDigest.auctionImageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "auctionDigest.auctionInfo"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "auctionDigest.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "averageOrderValue"
    type: "number"
    description: ""

  - name: "badgeCount"
    type: "integer"
    description: ""

  - name: "bestFriend"
    type: "string"
    description: ""

  - name: "booked_activity_before"
    type: "boolean"
    description: ""

  - name: "booked_package_before"
    type: "boolean"
    description: ""

  - name: "browserTokens"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "congressional Districts"
    type: "string"
    description: ""

  - name: "counties"
    type: "string"
    description: ""

  - name: "current_employer"
    type: "string"
    description: ""

  - name: "current_employer_id"
    type: "string"
    description: ""

  - name: "date_last_booked_package"
    type: "date-time"
    description: ""

  - name: "daysSinceLastOrder"
    type: "integer"
    description: ""

  - name: "designation"
    type: "string"
    description: ""

  - name: "devices"
    type: "object"
    description: ""


  - name: "devices"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "devices.applicationName"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "devices.endpointEnabled"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "boolean"
      description: ""

  - name: "devices.platform"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "devices.platformEndpoint"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "devices.token"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "emailListIds"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "estimatedSizing"
    type: "string"
    description: ""

  - name: "experience"
    type: "string"
    description: ""

  - name: "favoriteAnimal"
    type: "string"
    description: ""

  - name: "favoriteCategories"
    type: "object"
    description: ""


  - name: "favoriteCategories"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "favoriteCategories.category"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "favoriteCategory"
    type: "string"
    description: ""

  - name: "favoriteCuisine"
    type: "string"
    description: ""

  - name: "favoriteItem"
    type: "string"
    description: ""

  - name: "favoriteProduct"
    type: "string"
    description: ""

  - name: "favoriteRestaurant"
    type: "string"
    description: ""

  - name: "favoriteShowCategories"
    type: "string"
    description: ""

  - name: "favorite_category"
    type: "string"
    description: ""

  - name: "favoritedShows"
    type: "string"
    description: ""

  - name: "fb_follow"
    type: "boolean"
    description: ""

  - name: "featuredDeal"
    type: "string"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "gender"
    type: "string"
    description: ""

  - name: "hasMobileApp"
    type: "boolean"
    description: ""

  - name: "highestBidPrice"
    type: "string"
    description: ""

  - name: "house Districts"
    type: "string"
    description: ""

  - name: "industry"
    type: "string"
    description: ""

  - name: "installedDropbox"
    type: "boolean"
    description: ""

  - name: "installed_sync"
    type: "boolean"
    description: ""

  - name: "interested_in_detergent"
    type: "boolean"
    description: ""

  - name: "interested_in_soap"
    type: "boolean"
    description: ""

  - name: "interested_in_toilet_paper"
    type: "boolean"
    description: ""

  - name: "invoice"
    type: "object"
    description: ""


  - name: "invoice"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "invoice.customAmount"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "invoice.customSubTotal"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "invoice.customerEmail"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice.customerName"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice.invoiceDate"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice.invoiceNumber"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice.merchantName"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice.totalDue"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_available"
    type: "boolean"
    description: ""

  - name: "itblInternal.emailDomain"
    type: "string"
    description: ""

  - name: "jobRecommendations"
    type: "object"
    description: ""


  - name: "jobRecommendations"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "jobRecommendations.applicationURL"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "jobRecommendations.description"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "jobRecommendations.id"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "jobRecommendations.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "jobRecommendations.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "job_categories_interested"
    type: "string"
    description: ""

  - name: "job_title"
    type: "string"
    description: ""

  - name: "lastAccessedAgent"
    type: "string"
    description: ""

  - name: "lastKnownLatitude"
    type: "number"
    description: ""

  - name: "lastKnownLongitude"
    type: "number"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "lastOrderlocation"
    type: "string"
    description: ""

  - name: "lastOrderrestaurant"
    type: "string"
    description: ""

  - name: "last_game_played"
    type: "string"
    description: ""

  - name: "last_purchased"
    type: "string"
    description: ""

  - name: "last_purchased_category"
    type: "string"
    description: ""

  - name: "last_session_date"
    type: "date-time"
    description: ""

  - name: "level"
    type: "integer"
    description: ""

  - name: "lifetime Dontation"
    type: "string"
    description: ""

  - name: "lifetime_Spent"
    type: "string"
    description: ""

  - name: "locale"
    type: "string"
    description: ""

  - name: "location"
    type: "string"
    description: ""

  - name: "loyalty_member"
    type: "boolean"
    description: ""

  - name: "loyalty_points"
    type: "integer"
    description: ""

  - name: "loyalty_program"
    type: "boolean"
    description: ""

  - name: "major"
    type: "string"
    description: ""

  - name: "marketSmith_subscription"
    type: "boolean"
    description: ""

  - name: "merchantId"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "newListedVehicles"
    type: "object"
    description: ""


  - name: "newListedVehicles"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "newListedVehicles.category"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.miles"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.noHagglePrice"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.price"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "newListedVehicles.sku"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers"
    type: "object"
    description: ""


  - name: "offers"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "offers.Intro APR"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "offers.categories"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.description"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.id"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.intro APR"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "offers.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.quantity"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "offers.sku"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "offers.url"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "onboardingCohort"
    type: "string"
    description: ""

  - name: "paid_user"
    type: "boolean"
    description: ""

  - name: "passively_seeking"
    type: "boolean"
    description: ""

  - name: "phoneNumber"
    type: "string"
    description: ""

  - name: "phoneNumberDetails"
    type: "object"
    description: ""


  - name: "phoneNumberDetails"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "phoneNumberDetails.carrier"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "phoneNumberDetails.countryCodeISO"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "phoneNumberDetails.lineType"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "phoneNumberDetails.updatedAt"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "promoCode"
    type: "string"
    description: ""

  - name: "readingList"
    type: "object"
    description: ""


  - name: "readingList"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "readingList.avgRating"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "readingList.bookAuthor"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "readingList.bookName"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "readingList.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles"
    type: "object"
    description: ""


  - name: "recommendedVehicles"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "recommendedVehicles.TrueCar Estimate"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles.category"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles.estimateDescription"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "recommendedVehicles.sku"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "region"
    type: "string"
    description: ""

  - name: "sat"
    type: "string"
    description: ""

  - name: "scheduled_ride"
    type: "date-time"
    description: ""

  - name: "selected_games"
    type: "string"
    description: ""

  - name: "senate Districts"
    type: "string"
    description: ""

  - name: "shoppingCartItems"
    type: "object"
    description: ""


  - name: "shoppingCartItems"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "shoppingCartItems.categories"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.description"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.id"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.imageUrl"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.price"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "number"
      description: ""

  - name: "shoppingCartItems.quantity"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "shoppingCartItems.sku"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shoppingCartItems.url"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shopppingCartTotal"
    type: "integer"
    description: ""

  - name: "should_receive_recommendation"
    type: "boolean"
    description: ""

  - name: "signupDate"
    type: "date-time"
    description: ""

  - name: "signupSource"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "streetAddress"
    type: "string"
    description: ""

  - name: "swingTrader_subscription"
    type: "boolean"
    description: ""

  - name: "tagline"
    type: "string"
    description: ""

  - name: "timeZone"
    type: "string"
    description: ""

  - name: "times donated"
    type: "string"
    description: ""

  - name: "times_purchased"
    type: "string"
    description: ""

  - name: "totalOrderCount"
    type: "integer"
    description: ""

  - name: "totalOrders"
    type: "string"
    description: ""

  - name: "totalPurchases"
    type: "integer"
    description: ""

  - name: "totalSpent"
    type: "number"
    description: ""

  - name: "total_playtime"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "university_interest"
    type: "string"
    description: ""

  - name: "unsubscribedChannelIds"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "unsubscribedMessageTypeIds"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "uploaded_resume"
    type: "boolean"
    description: ""

  - name: "userId"
    type: "string"
    description: ""

  - name: "user_type"
    type: "string"
    description: ""

  - name: "vegetarian_menu"
    type: "object"
    description: ""


  - name: "vegetarian_menu"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "vegetarian_menu.featured_item_availability"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vegetarian_menu.featured_item_description"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vegetarian_menu.featured_item_id"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vegetarian_menu.featured_item_image_url"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vegetarian_menu.featured_item_menu_availability"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vegetarian_menu.featured_item_menu_date"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "vip"
    type: "boolean"
    description: ""

  - name: "wishList"
    type: "object"
    description: ""


  - name: "wishList"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""


  - name: "wishList.name"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "wishList.price"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "number"
      description: ""

  - name: "zip"
    type: "string"
    description: ""

---
