---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "iterable"

version: "1"

foreign-keys:
  - id: "campaign-id"
    table: "campaigns"
    attribute: "id"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "email_bounce"
        join-on: "campaignId"
      - table: "email_click"
        join-on: "campaignId"
      - table: "email_click"
        join-on: "campaignId"
      - table: "email_complaint"
        join-on: "campaignId"
      - table: "email_open"
        join-on: "campaignId" 
      - table: "email_send"
        join-on: "campaignId" 
      - table: "email_send_skip"
        join-on: "campaignId"
      - table: "email_subscribe"
        join-on: "campaignId" 
      - table: "email_unsubscribe"
        join-on: "campaignId"
      - table: "templates"
        join-on: "campaignId"  



  - id: "channel-id"
    table: "channels"
    attribute: "id"
    all-foreign-keys:
      - table: "channels"
        join-on: "id"
      - table: "email_send"
        join-on: "channelId"
      - table: "email_send_skip"
        join-on: "channelId"
      - table: "email_subscribe"
        subattribute: "channelIds"
        join-on: "items"
      - table: "email_unsubscribe"
        subattribute: "channelIds"
        join-on: "items"
      - table: "email_unsubscribe"
        join-on: "channelId"
      - table: "message_types"
        join-on: "channelId"      


  - id: "email-id"
    table: "users"
    attribute: "email"
    all-foreign-keys:
      - table: "users"
        join-on: "email"
      - table: "email_ _bounce"
        join-on: "email"
      - table: "email_click"
        join-on: "email"
      - table: "email_complaint"
        join-on: "email"
      - table: "email_open"
        join-on: "email"
      - table: "email_send"
        join-on: "email"
      - table: "email_send_skip"
        join-on: "email"
      - table: "email_subscribe"
        join-on: "email"
      - table: "email_unsubscribe"
        join-on: "email"
      - table: "list_users"
        join-on: "email"   
        
  - id: "list-id"
    table: "lists"
    attribute: "id"
    all-foreign-keys:
      - table: "lists"
        join-on: "id"
      - table: "list_users"
        join-on: "listId"

  - id: "message-id"
    table: "message_types"
    attribute: "id"
    all-foreign-keys:
      - table: "message_types"
        join-on: "id"
      - table: "templates"
        join-on: "messageTypeId"

  - id: "template-id"
    table: "templates"
    attribute: "templateId"
    all-foreign-keys:
      - table: "templates"
        join-on: "templateId"
      - table: "campaigns"
        join-on: "templateId"
      - table: "email_bounce"
        join-on: "templateId" 
      - table: "email_click"
        join-on: "templateId"
      - table: "email_complaint"
        join-on: "templateId"
      - table: "email_open"
        join-on: "templateId"
      - table: "email_send"
        join-on: "templateId"
      - table: "email_send_skip"
        join-on: "templateId"
      - table: "email_subscribe"
        join-on: "templateId"
      - table: "email_unsubscribe"
        join-on: "templateId"  




---