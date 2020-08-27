---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "zoom"

version: "1"

foreign-keys:
  - id: "meeting-uuid"
    table: "meetings"
    attribute: "uuid"
    all-foreign-keys:
      - table: "meeting_poll_results"
        join-on: "meeting_uuid"
      - table: "meeting_files"
        joini-on: "meeting_uuid"
      - table: "meetings"
        join-on: "uuid"

  - id: "meeting-id"
    table: "meeting_registrants"
    attribute: "meeting_id"
    all-foreign-keys:
      - table: "meeting_polls"   
      - table: "meeting_questions"
      - table: "meeting_registrants"
      - table: "meetings"
      - table: "report_meeting_participants"
      - table: "report_meetings" 

  # - id: "poll-id"
  #   table: "meeting_polls"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "meeting_polls"
  #       join-on: "id"   

  - id: "user-id"
    table: "users"
    attribute: "user_id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "report_meeting_participants"
      - table: "report_webinar_participants"

  - id: "webinar-id"
    table: "webinar_panelists"
    attribute: "webinar_id"
    all-foreign-keys:
      - table: "report_webinar_participants"
      - table: "report_webinars"
      - table: "webinar_panelists"
      - table: "webinar_registrants"
      - table: "webinar_polls"
      - table: "webinar_questions"
      - table: "webinar_registrants"
      - table: "webinar_tracking_sources"

  - id: "webinar-uuid"
    table: "webinars"
    attribute: "webinar_uuid"
    all-foreign-keys:
      - table: "report_webinars"
        join-on: "uuid"
      - table: "webinar_absentees"
      - table: "webinar_files"
      - table: "webinar_poll_results"
      - table: "webinar_qna_results"
      - table: "webinars"
        join-on: "uuid"

  # - id: "absentee-id"
  #   table: "webinar_absentees"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "webinar_absentees"
  #       join-on: "id"

  # - id: "participant-id"
  #   table: "report_meeting_participants"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "report_meeting_participants"
  #       join-on: "id"

  # - id: "registrant-id"
  #   table: "meeting_registrants"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "meeting_registrants"
  #       join-on: "id"  

  # - id: "panelist-id"
  #   table: "webinar_panelists"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "webinar_panelists"
  #       join-on: "id"

  # - id: "webinar-registrant-id"
  #   table: "webinar_registrants"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "webinar_registrants"
  #       join-on: "id"

  # - id: "webinar-poll-id"
  #   table: "webinar_polls"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "webinar_polls"
  #       join-on: "id"    

  # - id: "tracking-source-id"
  #   table: "webinar_tracking_sources"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "webinar_tracking_sources"
  #       join-on: "id"  

  # - id: "webinar-participant-id"
  #   table: "report_webinar_participants"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "report_webinar_participants"
  #       join-on: "id"                                          
---