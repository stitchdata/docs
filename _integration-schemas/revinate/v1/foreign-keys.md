---
tap-reference: "revinate"

version: "1.0"

foreign-keys:
  - id: "hotel-id"
    attribute: "hotel_id"
    table: "hotels"
    all-foreign-keys:
      - table: "hotel_reviews_snapshot"
      - table: "hotel_reviews_snapshot_by_site"
      - table: "hotel_reviews_snapshot_by_time"
      - table: "hotels"
      - table: "reviews"

  - id: "review-site-id"
    attribute: "review_site_id"
    table: ""
    all-foreign-keys:
      - table: "hotel_reviews_snapshot_by_site"
      - table: "reviews"
  
  - id: "trip-advisor-id"
    attribute: "trip_advisor_id"
    table: "hotels"
    all-foreign-keys:
      - table: "hotels"

  - id: "review-id"
    attribute: "review_id"
    table: "reviews"
    all-foreign-keys:
      - table: "reviews"
---