---
title: "Mambu (v4) bug fix: Date windowing pagination use"
content-type: "changelog-entry"
date: 2024-05-13
entry-type: bug-fix
entry-category: integration
connection-id: mambu
connection-version: 4
pull-request: "https://github.com/singer-io/tap-mambu/pull/113"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix issues during the integration execution: 

- Out-Of-Memory Issue:
Initially, all records from the start date to the current date were pulled, and the integration allowed generator buffers to grow without limit, surpassing the default extraction memory limits rapidly.
To address this, we implemented date windowing (default size = 1 day) and pagination for multi-threaded streams, a limited generator buffer growth to finite boundaries and we eliminated performance metrics to reduce performance overheads.
- Execution Time:
Previously, to address performance concerns, a single-threaded implementation was adopted, resulting in slow extraction speeds.
Multi-threaded execution has been reintroduced to expedite historical sync execution with a maximum thread count equal to 20.
- Data Discrepancy:
Data discrepancies were reported in certain streams after the extraction gets interrupted due to extraction timeout and memory issue.
The bookmark strategy has been revised for multi-threaded generators to address data discrepancies.
We segregated the `LoanAccounts` sub-stream bookmarking to rectify data inconsistencies.