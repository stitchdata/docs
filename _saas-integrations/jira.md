---
title: JIRA
permalink: /integrations/saas/jira
tags: [saas_integrations]
keywords: jira, integration, schema, etl jira, jira etl, jira schema
summary: "Connection instructions and schema details for Stitch's JIRA integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "jira"
display_name: "JIRA"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://status.atlassian.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"
icon: /images/integrations/icons/jira.svg
whitelist-ips: true ## if true, Stitch's IP addresses must be whitelisted to access this integration's data

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Issues
  - name: "jira_issues"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/issue-getIssue
    description: "info about the issues in your JIRA account."
    notes: |
      ### Accounting for Deleted Issues
      When an issue is hard-deleted in JIRA, the record for the issue will remain in your data warehouse. This happens because of the Replication Method the `jira_issues` table uses and how JIRA's API functions.
      
      - The `jira_issues` table is incrementally replicated based on the `updated_at` column. This means that rows with values in this column that are greater than or equal to the last recorded MAX value will be selected for replication. If a record is hard-deleted, there won't be a value to check and thus no way to detect changes to the record.
      - JIRA's API doesn't include a flag to indicate deletes.
      
      [The suggested workaround](https://answers.atlassian.com/questions/75537/how-do-i-find-if-an-issue-has-been-deleted) (although it may be a bit cumbersome) is to use the `fields__status__name` column - which indicates the current status of an issue - to track deletes. Before deleting the issue, you could change the status to something that would only indicate a delete and then use that status as a filter in your queries.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Issue ID (<code>id</code>)
      - name: self
      - name: key
      - name: expand
      - name: changelog
      - name: description
      - name: attachment<code>*</code>
      - name: subtasks<code>*</code>
      - name: labels<code>*</code>
      - name: fixversions<code>*</code>
      - name: comments<code>*</code>
      - name: Creator Info
      - name: Status Info
      - name: Summary
      - name: Votes
      - name: Reporter
      - name: Priority
      - name: Issue Type

## Projects
  - name: "jira_projects"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project-getAllProjects
    description: "info about individual projects in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Project ID (<code>id</code>)
      - name: avatarurls
      - name: description
      - name: expand
      - name: key
      - name: lead__active
      - name: lead__avatarurls
      - name: lead__displayname
      - name: lead__key
      - name: lead__name
      - name: lead__self
      - name: name
      - name: projecttypekey
      - name: projectkeys<code>*</code>
      - name: self

## Project Categories
  - name: "jira_project_categories"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/projectCategory-getAllProjectCategories
    description: "info about the categories assigned to the projects in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Project Category ID (<code>id</code>)
      - name: self
      - name: name
      - name: description

## Project Roles
  - name: "jira_project_roles"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/role-getProjectRoles
    description: "info about the roles that can be assigned to projects in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Project Role ID (<code>id</code>)
      - name: self
      - name: name
      - name: description
      - name: <a href="https://docs.atlassian.com/jira/REST/ondemand/#api/2/role-getProjectRoleActorsForRole">roles__actors</a><code>*</code>

## Project Types
  - name: "jira_project_types"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project/type-getAllProjectTypes
    description: "info about the project types defined in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "key"
    nested-structures: false
    attributes:
      - name: Project Type Key (<code>key</code>)
      - name: formattedkey
      - name: description18nkey
      - name: icon
      - name: color

## Resolutions
  - name: "jira_resolutions"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/resolution-getResolutions
    description: "info about the resolutions in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Resolution ID (<code>id</code>)
      - name: self
      - name: name
      - name: description

## Users
  - name: "jira_users"
    doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/user-findUsers
    description: "info about the users in your JIRA account."
    notes: 
    replication-method: "Full Table"
    primary-key: "key"
    nested-structures: false
    attributes:
      - name: User Key (<code>key</code>)
      - name: active
      - name: avatarurls
      - name: displayname
      - name: emailaddress
      - name: key
      - name: locale
      - name: name
      - name: self
      - name: timezone
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Depending on your setup, connecting JIRA is a five or seven-step process:

1. [Whitelist Stitch's IP Addresses](#whitelist-stitch-ips) `*`
2. [Verify protocol support](#verify-protocol-support) `*`
3. [Retrieve the Stitch Public Key](#retrieve-stitch-public-key)
4. [Grant Stitch application access to JIRA](#grant-stitch-access-to-jira)
5. [Add JIRA as a Stitch data source](#add-stitch-data-source)
6. [Define the Historical Sync](#define-historical-sync)
7. [Define the Replication Frequency](#define-rep-frequency)

`*` These steps only need to be completed **if you're using a self-hosted (on-site) version of JIRA.**

### Prerequisites 

**You must have Adminstrator permissions in JIRA.** This is required to complete parts of the setup process.

### Whitelist Stitch's IP Addresses {#whitelist-stitch-ips}
**If your JIRA instance is both self-hosted AND behind a firewall**, you’ll need to whitelist the Stitch IP addresses to successfully connect to Stitch. Whitelist all of the following IP addresses:

{% for ip-address in ip-addresses %}
- {{ ip-address.ip }}
{% endfor %}

Be sure to do this before continuing through the rest of the setup or you may encounter errors when saving the integration.

### Verify Your Protocol Support {#verify-protocol-support}

**If your JIRA instance is self-hosted**, you'll also need to verify that your server uses `HTTPs` as the protocol. Stitch does not support `HTTP` for security reasons.

When you complete the JIRA setup in Stitch, you'll be asked to enter your JIRA base URL. If Stitch determines that the protocol is not `HTTPs`, connection errors will arise.

### Retrieve the Stitch Public Key {#retrieve-stitch-public-key}

1. {{ app.menu-paths.add-integration | flatify }}
2. Click the **JIRA** icon.
3. Locate the **Public Key** field.

Leave this page open for now - you'll need this to set up the application access in JIRA in the next step.

### Grant Stitch Application Access to JIRA {#grant-stitch-access-to-jira}

**Note that you need Administrator permissions to complete the steps in this section**. If you're not an Admin, loop in someone who can help you before continuing.

1. Sign into your JIRA account.
2. Click the **Settings (gear)** icon in the top-right corner.
3. In the drop-down menu, click **Applications**.
4. Click the **Application** link - it’s in the **Integrations** section of the menu on the left side of the page.
5. In the **Application** field, enter `stitchdata.com`.
6. Click **Create new link**.

A few ‘Configure Application URL’ messages might display after clicking the **Create new link** button. If you see these, don’t worry - everything is still on track. Click **Continue** to keep going.

#### Define the First Set of Link Application Settings

1. When the **Link Applications** window displays, enter `stitch` into the following fields:
   - Application Name
   - Service Provider Name
2. Set the **Application Type** field to **Generic Application**.
3. Enter `rjmetrics` into the following fields:
   - Consumer Key
   - Shared Secret
4. Enter `stitchdata.com` into the following fields:
   - Request Token URL
   - Token URL
   - Authorize URL
5. Check the **Create incoming link** box.
6. Click the **Continue** button and a second Link Applications window will display.

#### Define the Second Set of Link Application Settings

1. In the **Consumer Key** field, enter `rjmetrics`.
2. In the **Consumer Name** field, enter `stitch`.
3. In the **Public Key** field, paste the entire Public Key from the Stitch JIRA credentials page.
4. Click the **Continue** button.

If the link configuration was successful, you’ll see a **Success!** message on the Configure Application Links page.

{% include integrations/shared-setup/connection-setup.html %}
4. In the **Base URL** field, enter the base URL for your JIRA site. **Remember: if you're connecting a self-hosted instance**, your server must use the `HTTPs` protocol or Stitch will be unable to successfully connect. 

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}