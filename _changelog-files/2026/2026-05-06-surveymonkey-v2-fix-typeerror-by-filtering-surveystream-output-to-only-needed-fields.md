---
title: "SurveyMonkey (v2): Fix TypeError by filtering SurveyStream output to only needed fields"
content-type: "changelog-entry"
date: 2026-05-06
entry-type: bug-fix
entry-category: integration
connection-id: surveymonkey
connection-version: 2
pull-request: "https://github.com/singer-io/tap-surveymonkey/pull/43"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix TypeError by filtering SurveyStream output to only needed fields.