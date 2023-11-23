---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "clubspeed"

version: "1"

foreign-keys:
  - id: "booking-id"
    table: "booking"
    attribute: "onlineBookingsId"
    all-foreign-keys:
      - table: "booking"
      - table: "booking_availability"
        subtable: "products"
      - table: "reservations"

  - id: "check-detail-id"
    table: "check_details"
    attribute: "checkDetailId"
    all-foreign-keys:
      - table: "check_details"
      - table: "gift_card_history"

  - id: "check-id"
    table: "checks"
    attribute: "checkId"
    all-foreign-keys:
      - table: "check_details"
      - table: "checks"
      - table: "event_reservation_links"
      - table: "gift_card_history"
      - table: "payments"
      - table: "payments_voided"
      - table: "reservations"

  - id: "customer-id"
    table: "customers"
    attribute: "customerId"
    all-foreign-keys:
      - table: "check_details"
        join-on: "g_CustId"
      - table: "check_details"
        join-on: "p_CustId"
      - table: "check_details"
        join-on: "s_CustId"
      - table: "checks"
      - table: "event_heat_details"
      - table: "gift_card_history"
      - table: "heat_main_details"
      - table: "memberships"
      - table: "payments"
      - table: "payments_voided"
      - table: "reservations"

  - id: "discount-id"
    table: "discount_types"
    attribute: "discountId"
    all-foreign-keys:
      - table: "check_details"
      - table: "checks"
      - table: "discount_types"

  - id: "event-heat-type-id"
    table: "event_heat_types"
    attribute: "eventHeatTypeId"
    all-foreign-keys:
      - table: "event_heat_types"

  - id: "event-reservation-link-id"
    table: "event_reservation_links"
    attribute: "eventReservationLinkId"
    all-foreign-keys:
      - table: "event_reservation_links"

  - id: "event-reservation-type-id"
    table: "event_reservation_types"
    attribute: "eventReservationTypeId"
    all-foreign-keys:
      - table: "event_reservation_types"
      - table: "event_reservations"
        join-on: "typeId"

  - id: "event-reservation-id"
    table: "event_reservations"
    attribute: "eventReservationId"
    all-foreign-keys:
      - table: "event_reservations"
      - table: "event_reservations"
        join-on: "mainId"
      - table: "event_tasks"

  - id: "event-round-id"
    table: "event_rounds"
    attribute: "eventRoundId"
    all-foreign-keys:
      - table: "event_rounds"
      - table: "heat_main"
        join-on: "eventRound"

  - id: "event-status-id"
    table: "event_statuses"
    attribute: "eventStatusId"
    all-foreign-keys:
      - table: "event_statuses"

  - id: "event-task-type-id"
    table: "event_task_types"
    attribute: "eventTaskTypeId"
    all-foreign-keys:
      - table: "event_task_types"
      - table: "event_tasks"

  - id: "event-task-id"
    table: "event_tasks"
    attribute: "eventTaskId"
    all-foreign-keys:
      - table: "event_tasks"

  - id: "event-type-id"
    table: "event_types"
    attribute: "eventTypeId"
    all-foreign-keys:
      - table: "event_reservations"
      - table: "event_types"
      - table: "events"

  - id: "event-id"
    table: "events"
    attribute: "eventId"
    all-foreign-keys:
      - table: "event_heat_details"
      - table: "event_heat_types"
      - table: "event_rounds"
      - table: "events"

  - id: "gift-card-history-id"
    table: "gift_card_history"
    attribute: "giftCardHistoryId"
    all-foreign-keys:
      - table: "gift_card_history"
  
  - id: "heat-id"
    table: "heat_main"
    attribute: "heatId"
    all-foreign-keys:
      - table: "booking"
      - table: "booking_availability"
      - table: "booking_availability"
        join-on: "heatSpotsAvailableCombined"
      - table: "heat_main"
      - table: "heat_main_details"

  - id: "heat-type-id"
    table: "heat_types"
    attribute: "heatTypeId"
    all-foreign-keys:
      - table: "booking_availability"
      - table: "event_heat_types"
      - table: "event_rounds"
      - table: "heat_main"
        join-on: "type"
      - table: "heat_types"
        join-on: "heatTypesId"

  - id: "membership-type-id"
    table: "membership_types"
    attribute: "membershipTypeId"
    all-foreign-keys:
      - table: "membership_types"
      - table: "memberships"

  - id: "payment-id"
    table: "payments"
    attribute: "paymentId"
    all-foreign-keys:
      - table: "payments"
      - table: "payments_voided"

  - id: "product-class-id"
    table: "product_classes"
    attribute: "productClassId"
    all-foreign-keys:
      - table: "discount_types"
      - table: "product_classes"
      - table: "products"

  - id: "product-id"
    table: "products"
    attribute: "producstId"
    all-foreign-keys:
      - table: "booking"
      - table: "booking_availability"
        subtable: "products"
      - table: "check_details"
      - table: "event_types"
        join-on: "onlineProductId"
      - table: "products"

  - id: "reservation-id"
    table: "reservations"
    attribute: "reservationId"
    all-foreign-keys:
      - table: "event_reservation_links"
      - table: "events"
      - table: "reservations"
        join-on: "onlineBookingReservationsId"

  - id: "source-id"
    table: "sources"
    attribute: "sourceId"
    all-foreign-keys:
      - table: "customers"
      - table: "sources"

  - id: "tax-id"
    table: "taxes"
    attribute: "taxId"
    all-foreign-keys:
      - table: "check_details"
      - table: "products"
      - table: "taxes"

  - id: "track-id"
    table: ""
    attribute: "trackId"
    all-foreign-keys:
      - table: "event_types"
      - table: "heat_main"
      - table: "heat_types"

  - id: "user-id"
    table: "users"
    attribute: "userId"
    all-foreign-keys:
      - table: "check_detail"
        join-on: "discountUserId"
      - table: "checks"
        join-on: "discountUserId"
      - table: "checks"
      - table: "event_tasks"
        join-on: "completedBy"
      - table: "gift_card_history"
      - table: "users"
      - table: "event_reservations"
      - table: "heat_main_details"
      - table: "memberships"
        join-on: "byUserId"
      - table: "payments"
      - table: "payments"
        join-on: "voidUser"
      - table: "payments_voided"
      - table: "payments_voided"
        join-on: "voidUser"
      - table: "users"
---