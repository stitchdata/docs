---
tap: "clubspeed"
version: "1"

name: "booking"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/booking.json"
description: |
  The `{{ table.name }}` table contains info about bookings. A booking record exposes a `heat` to the online booking inerface in {{ integration.display_name }}.

replication-method: "Full Table"

attributes:
  - name: "onlineBookingsId"
    type: "integer"
    primary-key: true
    description: "The ID for the booking."
    foreign-key-id: "booking-id"

  - name: "heatId"
    type: "integer"
    description: "The heat ID for the booking."
    foreign-key-id: "heat-id"

  - name: "isPublic"
    type: "boolean"
    description: "Indicates whether the booking is available to the online booking interface."

  - name: "productsId"
    type: "integer"
    description: "The ID of the product for the booking."
    foreign-key-id: "product-id"

  - name: "quantityTotal"
    type: "integer"
    description: "The total number of booking reserverations to make available."
---