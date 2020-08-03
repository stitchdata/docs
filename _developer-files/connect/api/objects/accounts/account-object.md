---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "accounts"
order: 1


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Account"
endpoint-url: "/accounts"

description: "{{ api.core-objects.accounts.description }}"
intro-short: "Create Stitch client accounts (Partners only)" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "3"
versions:
  - number: "3"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "create-an-account"
    title: "Create an account"
    method: "post"
    short: "{{ api.core-objects.accounts.create.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "company"
    type: "string"
    description: "A name for the Stitch client. This is typically the name of the company using the Stitch client account."

  - name: "email"
    type: "string"
    description: "The email address of the user signing up for a Stitch client account. Upon successful account creation, Stitch will send an email to this address with instructions for completing the setup."

  - name: "first_name"
    type: "string"
    description: "The first name of the user signing up for a Stitch client account."

  - name: "last_name"
    type: "string"
    description: "The last name of the user signing up for a Stitch client account."

  - name: "partner_id"
    type: "string"
    description: "The unique ID for your API client, obtained when you register to use the API."

  - name: "partner_secret"
    type: "string"
    description: "The secret for your API client, obtained when you registered to use the API."


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {
        "partner_id": "<PARTNER_ID>",
        "partner_secret": "<PARTNER_SECRET>",
        "first_name": "Stitch",
        "last_name": "Product Team",
        "company": "Stitch Product Team",
        "email": "stitch-api-test@stitchdata.com"
      }
---