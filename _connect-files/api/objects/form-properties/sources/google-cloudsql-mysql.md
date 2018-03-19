---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-cloudsql-mysql-object"

title: "Google CloudSQL MySQL Source Form Property"
description: "{{ api.form-properties.source-forms.cloudsql-mysql.description }}"

object-attributes:
  - name: "host"
    type: "string"
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "string"
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

  # - name: "ssh"
  #   type: "boolean"
  #   description: "{{ connect.common.attributes.ssh }}"

  # - name: "ssh_host"
  #   type: "string"
  #   description: "{{ connect.common.attributes.ssh-host }}"

  # - name: "ssh_port"
  #   type: "integer"
  #   description: "{{ connect.common.attributes.ssh-port }}" 

  # - name: "ssh_user"
  #   type: "string"
  #   description: "{{ connect.common.attributes.ssh-user }}" 

  # - name: "ssl"
  #   type: "boolean"
  #   description: "{{ connect.common.attributes.ssl }}"

examples:
  - code: |
      {  
       "type":"platform.cloudsql",
       "properties":{  
          "host":"google-cloudsql-mysql.some-host.com",
          "port":"3306",
          "database":"stitch",
          "username":"stitch_user",
          "password":"<PASSWORD>"
        }
      }
---