---
title: "SurveyMonkey (v2) bug fix: heading field in simplified_responses stream"
content-type: "changelog-entry"
date: 2023-12-13
entry-type: bug-fix
entry-category: integration
connection-id: surveymonkey
connection-version: 2
pull-request: "https://github.com/singer-io/tap-surveymonkey/pull/29"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the missing `heading` field issue in the `simplified_responses` stream.