---
# tap: "outbrain"
# version: "1"

# Not currently persisted as endpoint is too slow

name: "links"
doc-link: 
description: "info about links in your Outbrain campaigns."
notes: 
replication-method: "Key-based Incremental"
primary-key: "id"
nested-structures: false
attribute-notes: 
attributes:
  - name: Link ID (<code>id</code>)
  - name: campaignid
  - name: text
  - name: lastmodified
  - name: creationtime
  - name: url
  - name: sitename
  - name: sectionname
  - name: status
  - name: cachedimageurl
  - name: enabled
  - name: archived
  - name: documentlanguage
  - name: cpc
---