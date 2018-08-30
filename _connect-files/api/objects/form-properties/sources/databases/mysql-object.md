---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mysql-object"

title: "MySQL Source Form Property"
api-type: "mysql"
display-name: "MySQL"
integration-type: "database"
docs-name: "mysql"

description: "{{ api.form-properties.source-forms.mysql.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"
    value: "{{ sample-property-data.host }}"

  - name: "port"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.port }}"
    value: "3306"

  - name: "database"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"
    value: "{{ sample-property-data.database }}"

  - name: "user"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"
    value: "{{ sample-property-data.user }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"
    value: "{{ sample-property-data.password }}"

  - name: "ssh"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh }}"
    value: "{{ sample-property-data.ssh }}"

  - name: "ssh_host"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-host }}"
    value: "{{ sample-property-data.ssh-host }}"

  - name: "ssh_port"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-port }}"
    value: "{{ sample-property-data.ssh-port }}"

  - name: "ssh_user"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssh-user }}"
    value: "{{ sample-property-data.ssh-user }}"

  - name: "ssl"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.ssl }}"
    value: "{{ sample-property-data.ssl }}"

  - name: "use_log_based_replication"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.use-log-based-replication }}"
    value: "{{ sample-property-data.use-log-based-replication }}"

  - name: "filter_dbs"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.filter-dbs }}"
    value: "{{ sample-property-data.filter-dbs }}"
---