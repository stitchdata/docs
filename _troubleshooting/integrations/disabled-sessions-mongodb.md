---
title: Mongo Disabled Sessions
keywords: troubleshooting, integration, database integration, trouble, issue, help, mongo, mongodb, session, cursor timeout
permalink: /troubleshooting/disabled-sessions-mongodb

key: "disabled-sessions-mongodb"

summary: "Cursor timeouts may occur when sessions are disabled on your MongoDB server."
toc: true
type: "database-integration"

layout: general

intro: |
  {% assign all-databases = site.database-integrations | where:"input",true %}
  {% assign mongodb-databases = all-databases | where:"db-type","mongodb" | where: "this-version", "3" | sort: title %}

  This article is applicable to the following database integrations:

  {% for database in mongodb-databases %}
  - [{{ database.title }}]({{ database.url | prepend: site.baseurl }})
  {% endfor %}

sections:
  - title: "Symptoms"
    anchor: "symptoms"
    content: |
      Cursor timeouts in MongoDB integrations when the processing of a batch of oplog entries takes a long time.

  - title: "Cause"
    anchor: "cause"
    content: |
      Sessions are enabled by default on MongoDB. However, if sessions are disabled on your MongoDB server, cursor timeouts can occur.

  - title: "Solution"
    anchor: "solution"
    content: |
      Enable sessions on your MongoDB server.
      
      
---