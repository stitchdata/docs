---
title: "Mambu (v2) improvement: Changed `deposit_accounts` sorting field"
content-type: "changelog-entry"
date: 2022-09-12
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/91"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've changed the sorting field from `id` to `lastModifiedDate` for the `deposit_accounts` table in our {{ this-connection.display_name }} integration.  The `MultithreadedBookmarkGenerator` changes the filter at every `n` records so switching to the `lastModifiedDate` ensures that we don't miss older records during the extraction process.