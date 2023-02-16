---
tap: "hubspot"
version: "2"
key: ""

name: "tickets"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-hubspot/tree/master/tap_hubspot/schemas/tickets.json
description: "In HubSpot, tickets represents customer requests for help"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updatedAt"

api-method:
  name: "Tickets"
  doc-link: https://developers.hubspot.com/docs/api/crm/tickets

attributes:
  - name: "archived"
    type: "boolean"
    description: "Archiving a ticket lets you hide it from your content dashboard without deleting it permanently"

  - name: "associations"
    type: "object"
    description: "Associations represent the relationships between objects and activities in the HubSpot CRM"
    subattributes:
      - name: "companies"
        type: "object"
        description: "Companies store information about the organizations that interact with your business"
        subattributes:
        - name: "results"
          type: "array"
          description: "Array of objects"
          subattributes:
		    - name: "items"
		      type: "object"
			  description: ""
			  subattributes:
                - name: "id"
                  type: "string"
                  description: "The ID of the record to associate"

                - name: "type"
                  type: "string"
                  description: "Tickets association with companies. Eg - ticket_to_company, ticket_to_company_unlabeled"



    - name: "deals"
      type: "object"
      description: "Deals represent transactions with contacts or companies"
      subattributes:
        - name: "results"
          type: "array"
          description: "Array of objects"
          subattributes:
		    - name: "items"
		      type: "object"
			  description: ""
			  subattributes:
                - name: "id"
                  type: "string"
                  description: "The ID of the record to associate"

                - name: "type"
                  type: "string"
                  description: "Tickets association with deals. Eg - ticket_to_deal"

    - name: "contacts"
      type: "object"
      description: "Contacts store information about the individual people that interact with your business"
      subattributes:
      - name: "results"
        type: "array"
        description: "Array of objects"
        subattributes:
		  - name: "items"
		    type: "object"
			description: ""
			subattributes:
              - name: "id"
                type: "string"
                description: "The ID of the record to associate"

              - name: "type"
                type: "string"
                description: "Tickets association with cotacts. Eg - ticket_to_contact"

  - name: "createdAt"
    type: "date-time"
    description: "The date the ticket was created"

  - name: "id"
    type: "string"
    description: "The unique identifier for the ticket"
	primary-key: true

  - name: "properties"
    type: "object"
    description: "Ticket details are stored in ticket properties."
    subattributes:
      - name: "content"
        type: "string"
        description: "Content for ticket"

      - name: "createdate"
        type: "date-time"
        description: "The date the ticket was created"

      - name: "hs_lastmodifieddate"
        type: "date-time"
        description: "Last modified date for the record"

    - name: "hs_object_id"
      type: "string"
      description: "Stores information about customer requests for help or support."

    - name: "hs_pipeline"
      type: "string"
      description: "A pipeline is where deal stages or or ticket statuses are set"

    - name: "hs_pipeline_stage"
      type: "string"
      description: "The ticket's status"

    - name: "hs_ticket_category"
      type: "string"
      description: "Category of the ticket"

    - name: "hs_ticket_priority"
      type: "string"
      description: "Priority of the ticket"

    - name: "subject"
      type: "string"
      description: "The ticket's name"

  - name: "updatedAt"
    type: "date-time"
    description: "Last modified date for the record"
	replication-key: true
---