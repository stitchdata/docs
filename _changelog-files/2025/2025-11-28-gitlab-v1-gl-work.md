---
title: "GitLab (v1): Multiple updates"
content-type: "changelog-entry"
date: 2025-11-28
entry-type: improvement
entry-category: integration
connection-id: gitlab
connection-version: 1
pull-request: "https://github.com/singer-io/tap-gitlab/pull/37"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to:
- Implement discovery logic.
- Add schema files for all schemas.
- Develop full sync logic for all parent and child streams.
- Create Unit tests (test_client.py) for core client methods.
- Add `.circleci/config.yml` with Unit test execution.