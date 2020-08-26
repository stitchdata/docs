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
  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "report_meeting_participants"
        join-on: "user_id" 
      - table: "report_webinar_participants"
        join-on: "user_id"   

  - id: "meeting-uuid"
    table: "meetings"
    attribute: "uuid"
    all-foreign-keys:
      - table: "meetings"
        join-on: "uuid"
      - table: "meeting_poll_results"
        join-on: "meeting_uuid"
      - table: "meeting_files"
        joini-on: "meeting_uuid"  

  - id: "meeting-files"
    table: "meeting_files"
    attribute: "file_name"
    all-foreign-keys:
      - table: "meeting_files"
        join-on: "file_name"  

  - id: "registrant-id"
    table: "meeting_registrants"
    attribute: "id"
    all-foreign-keys:
      - table: "meeting_registrants"
        join-on: "id"  

  - id: "meeting-id"
    table: "meeting_registrants"
    attribute: "meeting_id"
    all-foreign-keys:
      - table: "meeting_registrants"
        join-on: "meeting-id" 
      - table: "meeting_polls"   
        join-on: "meeting_id" 
      - table: "meeting_questions"
        join-on: "meeting_id"
      - table: "report_meeting_participants"
        join-on: "meeting_id" 
      - table: "meeting"
        join-on: "meeting_id"
      - table: "report_meetings"
        join-on: "meeting_id"     

  - id: "poll-id"
    table: "meeting_polls"
    attribute: "id"
    all-foreign-keys:
      - table: "meeting_polls"
        join-on: "id" 

  - id: "report-uuid"
    table: "report_meetings"
    attribute: "uuid"
    all-foreign-keys:
      - table: "report_meetings"
        join-on: "uuid"  

  - id: "participant-id"
    table: "report_meeting_participants"
    attribute: "id"
    all-foreign-keys:
      - table: "report_meeting_participants"
        join-on: "id"

  - id: "webinar-uuid"
    table: "webinars"
    attribute: "uuid"
    all-foreign-keys:
      - table: "webinars"
        join-on: "uuid"
      - table: "webinar_absentees"
        join-on: "webinar_uuid"
      - table: "webinar_files"
        join-on: "webinar_uuid"  
      - table: "report_webinars"
        join-on: "uuid"  

  - id: "absentee-id"
    table: "webinar_absentees"
    attribute: "id"
    all-foreign-keys:
      - table: "webinar_absentees"
        join-on: "id"                                        

  - id: "webinar-files"
    table: "webinar_files"
    attribute: "file_name"
    all-foreign-keys:
      - table: "webinar_files"
        join-on: "file_name" 

  - id: "webinar-id"
    table: "webinar_panelists"
    attribute: "webinar_id"
    all-foreign-keys:
      - table: "webinar_panelists"
        join-on: "webinar-id"
      - table: "webinar_registrants"
        join-on: "webinar_id" 
      - table: "webinar_polls"
        join-on: "webinar_id"
      - table: "webinar_questions"
        join-on: "webinar_id"  
      - table: "webinar_tracking_sources"
        join-on: "webinar_id"  
      - table: "report_webinar_participants"
        join-on: "webinar_id"   

  - id: "panelist-id"
    table: "webinar_panelists"
    attribute: "id"
    all-foreign-keys:
      - table: "webinar_panelists"
        join-on: "id"

  - id: "webinar-registrant-id"
    table: "webinar_registrants"
    attribute: "id"
    all-foreign-keys:
      - table: "webinar_registrants"
        join-on: "id"

  - id: "webinar-poll-id"
    table: "webinar_polls"
    attribute: "id"
    all-foreign-keys:
      - table: "webinar_polls"
        join-on: "id"    

  - id: "tracking-source-id"
    table: "webinar_tracking_sources"
    attribute: "id"
    all-foreign-keys:
      - table: "webinar_tracking_sources"
        join-on: "id"  

  - id: "webinar-participant-id"
    table: "report_webinar_participants"
    attribute: "id"
    all-foreign-keys:
      - table: "report_webinar_participants"
        join-on: "id"                                          
---