---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "stargazer"

name: "stargazers"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/stargazers.json
description: |
  The `{{ table.name }}` table contains info about users who have starred the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List stargazers"
  doc-link: "https://docs.github.com/en/rest/reference/activity#list-stargazers"

replication-method: "Full Table"
replication-key:
  name: "since"
  based-on: "starred_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "user_id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    # foreign-key-id: "stargazer-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "starred_at"
    type: "string"
    description: "The time the user starred the repository."

  - name: "user"
    type: "object"
    description: "Details about the user who starred the repository."
    subattributes:
       - name: "name"
         type: "string"
         description: "The name of the user."
         
       - name: "email"
         type: "string"
         description: "The email address of the user."

       - name: "login"
         type: "string"
         description: "The login name of the user."

       - name: "id"
         type: "string"
         description: "The ID of the user."

       - name: "node_id"
         type: "string"
         description: "The node ID of the user."

       - name: "avatar_url"
         type: "string"
         description: "The URL of the avatar of the user."

       - name: "gravatar_id"
         type: "string"
         description: "The URL of the Gravatar of the user."

       - name: "url"
         type: "string"
         description: "The API URL of the user."

       - name: "html_url"
         type: "string"
         description: "The GitHub URL of the user."

       - name: "followers_url"
         type: "string"
         description: "The URL to the user's followers page."

       - name: "following_url"
         type: "string"
         description: "The URL to the user's following page."

       - name: "gists_url"
         type: "string"
         description: "The URL to the user's gists page."

       - name: "starred_url"
         type: "string"
         description: "The URL to the user's starred page."

       - name: "subscriptions_url"
         type: "string"
         description: "The URL to the user's subscriptions page."

       - name: "organizations_url"
         type: "string"
         description: "The URL to the user's organizations page."

       - name: "repos_url"
         type: "string"
         description: "The URL to the user's repositories page."

       - name: "events_url"
         type: "string"
         description: "The URL to the user's events page."

       - name: "received_events_url"
         type: "string"
         description: "The URL to the user's received events page."

       - name: "type"
         type: "string"
         description: "The type of the user."

       - name: "site_admin"
         type: "string"
         description: "Indicates if the user is a site administrator."
         
       - name: "starred_at"
         type: "string"
         description: ""
---
