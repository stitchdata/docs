---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-oracle-object"

title: "Oracle Source Form Property"
api-type: "oracle"
display-name: "Oracle"

description: "{{ api.form-properties.source-forms.oracle.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Bing Ads" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"
    value: "{{ sample-property-data.host }}"

  - name: "port"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.port }}"
    value: ""

  - name: "dbname"
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

  - name: "default_replication_method"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.default-replication-method }}"
    value: "{{ sample-property-data.default-replication-method }}"

  - name: "filter_schemas"
    type: "string"
    required: false
    description: "[PLACEHOLDER]"
    value: ""

  - name: "sid"
    type: "string"
    required: false
    description: "[PLACEHOLDER]"
    value: ""

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
---