---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mariadb-object"

title: "MariaDB Source Form Property"
description: "{{ api.form-properties.source-forms.mariadb.description }}"

object-attributes:
  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "string"
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

  - name: "ssh"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh }}"

  - name: "ssh_host"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-host }}"

  - name: "ssh_port"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-port }}" 

  - name: "ssh_user"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-user }}" 

  - name: "ssl"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssl }}"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","MariaDB" }}

  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time }}


examples:
  - code: |
      {  
       "type":"platform.mariadb",
       "properties":{  
          "host":"mariadb.some-host.com",
          "port":"3306",
          "database":"stitch",
          "username":"stitch_user",
          "password":"<PASSWORD>",
          "ssh":"true",
          "ssh_host":"mariadb-ssh.host.com",
          "ssh_port":"22",
          "ssh_user":"stitch_ssh_user",
          "ssl":"false",
          "frequency_in_minutes":"60",
          "anchor_time":""
        }
      }
---

