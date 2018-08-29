---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-heroku-object"

title: "Heroku Source Form Property"
description: "{{ api.form-properties.source-forms.heroku.description }}"

object-attributes:
  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.port }}"

  - name: "dbname"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"

  - name: "user"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"

  - name: "{{ connect.common.attributes.include-schemas-name }}"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.include-schemas-description | flatify }}"

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

examples:
  - code: |
      {  
       "type":"platform.heroku_pg",
       "properties":{  
          "host":"heroku.some-host.com",
          "port":"5432",
          "dbname":"stitch",
          "user":"stitch_user",
          "password":"<PASSWORD>",
          "{{ connect.common.attributes.include-schemas-name }}":"true",
          "ssh":"true",
          "ssh_host":"heroku-ssh.host.com",
          "ssh_port":"22",
          "ssh_user":"stitch_ssh_user",
          "ssl":"false"
        }
      }
---