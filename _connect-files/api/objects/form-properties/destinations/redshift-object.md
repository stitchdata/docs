---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-redshift-object"

title: "Redshift"
description: "{{ api.form-properties.destination-forms.redshift.description }}"

object-attributes:
  - name: "host"
    type: "string"
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "integer"
    description: "{{ connect.common.attributes.port }}"

  - name: "database"
    type: "string"
    description: "{{ connect.common.attributes.database }}"

  - name: "username"
    type: "string"
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    description: "{{ connect.common.attributes.password }}"

  - name: "ssl"
    type: "boolean"
    description: "{{ connect.common.attributes.ssl }}"

examples:
  - code: |
      {
         "connection":{
            "host":"redshift.somewhere-on-aws.com",
            "port":5439,
            "database":"stitch",
            "username":"stitch_user",
            "password":"<PASSWORD>",
            "ssl":true
         }
      }
---