---
tap: "clubspeed"
version: "1.0"

name: "booking_availability"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/booking_availability.json"
description: |
  The `{{ table.name }}` table contains info about the current availability for online bookings. These take into account both online and local booking reservations.

replication-method: "Full Table"

attributes:
  - name: "heatId"
    type: "integer"
    primary-key: true
    description: "The heat ID for the booking."
    foreign-key-id: "heat-id"

  - name: "heatDescription"
    type: "string"
    description: "The description of the heat."

  - name: "heatSpotsAvailableCombined"
    type: "integer"
    description: "The heat ID for the booking."
    foreign-key-id: "heat-id"

  - name: "heatSpotsAvailableOnline"
    type: "integer"
    description: "The number of spots to be exposed to the online interface for the entire heat."

  - name: "heatSpotsTotalActual"
    type: "integer"
    description: "The original number of total spots for the heat."

  - name: "heatStartsAt"
    type: "date-time"
    description: "The start time for the heat."

  - name: "heatTypeId"
    type: "integer"
    description: "The heat type ID."
    foreign-key-id: "heat-type-id"

  - name: "isPublic"
    type: "boolean"
    description: "Indicates whether the booking should be made available in the online booking interface."

  - name: "products"
    type: "array"
    description: "A list of products associated with the booking."
    array-attributes:
      - name: "productsId"
        type: "integer"
        description: "The product ID."
        foreign-key-id: "product-id"

      - name: "onlineBookingsId"
        type: "integer"
        description: "The booking ID."
        foreign-key-id: "booking-id"

      - name: "price1"
        type: "number"
        description: "The price of the product for the booking."

      - name: "productDescription"
        type: "string"
        description: "The description of the product for the booking."

      - name: "productSpotsAvailableOnline"
        type: "integer"
        description: "The number of spots intended to be exposed to the online interface for the product."

      - name: "productSpotsTotal"
        type: "integer"
        description: "The total number of spots originally made available through the product pairing."

      - name: "productType"
        type: "string"
        description: "The ID of the product type."
---