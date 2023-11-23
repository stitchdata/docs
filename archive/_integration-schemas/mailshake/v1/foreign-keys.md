---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "mailshake"

version: "1"

foreign-keys:
  - id: "campaign-id"
    table: "campaigns"
    attribute: "id"
    all-foreign-keys:
      - table: "campaigns"
      - table: "campaigns"
        subattribute: "messages"
      - table: "clicks"
        subattribute: "campaign"
      - table: "leads"
        subattribute: "campaign"
      - table: "opens"
        subattribute: "campaign"
      - table: "recipients"
        join-on: "campaignId"
      - table: "replies"
        subattribute: "campaign"
      - table: "sent_messages"
        subattribute: "campaign"

  - id: "message-id"
    table: ""
    attribute: "id"
    all-foreign-keys:
      - table: "campaigns"
        subattribute: "messages"
      - table: "clicks"
        subattribute: "parent.message"
      - table: "leads"
        subattribute: "parent.message"
      - table: "opens"
        subattribute: "parent.message"
      - table: "replies"
        subattribute: "parent.message"
      - table: "sent_messages"
        subattribute: "message"

  - id: "recipient-id"
    table: "recipients"
    attribute: "id"
    all-foreign-keys:
      - table: "clicks"
        subattribute: "recipient"
      - table: "leads"
        subattribute: "recipient"
      - table: "opens"
        subattribute: "recipient"
      - table: "recipients"
      - table: "replies"
        subattribute: "parent.message"
      - table: "sent_messages"
        subattribute: "recipient"

  - id: "sender-id"
    table: "senders"
    attribute: "id"
    all-foreign-keys:
      - table: "campaigns"
        subattribute: "sender"
      - table: "senders"

  - id: "team-member-id"
    table: "team_members"
    attribute: "id"
    all-foreign-keys:
      - table: "leads"
        subattribute: "assignedTo"
      - table: "team_members"
---