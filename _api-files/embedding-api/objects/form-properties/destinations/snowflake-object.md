---
content-type: "embed-form"
form-type: "destination"
key: "destination-form-properties-snowflake-object"

title: "Snowflake"
description: "A Snowflake destination writes data to an Snowflake data warehouse and corresponds to the destination type = `snowflake`."

object-attributes:
  - name: "host"
    type: "string"
    description: "The IP address or hostname of the database server."

  - name: "port"
    type: "integer"
    description: "The port of the database server."

  - name: "database"
    type: "string"
    description: "The name of the logical database to connect to."

  - name: "username"
    type: "string"
    description: "The username of the database user."

  - name: "password"
    type: "string"
    description: "The password for the user connecting to the database server. **Note**: This property will never be returned by the API, but it can be submitted when creating or modifying a connection."

  - name: "role"
    type: "string"
    description: "**Optional**: The role to use."
---