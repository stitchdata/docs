---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-redshift-object"

title: "Redshift Destination Form Property"
description: "{{ api.form-properties.destination-forms.redshift.description }}"

object-attributes:
  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "integer"
    required: true
    description: "{{ connect.common.attributes.port }}"

  - name: "database"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"

  - name: "username"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"

  - name: "ssl"
    type: "boolean"
    required: false
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