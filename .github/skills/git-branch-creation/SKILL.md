---
name: git-branch-creation
description: "Create feature branches for documentation changes across Qlik (help-documentation Flare) and Talend (docs-core and docs-components DITA) repositories. Auto-detects repository, applies content-specific naming rules, and handles Studio monthly release integration branches. Use when: starting draft work tied to a Jira ticket in any supported repository, creating a branch after planning completes."
---

# Git branch creation for documentation repositories

## Supported repositories

| Repository | URL | Markup format | Content path | Base branch |
|---|---|---|---|---|
| help-documentation | https://github.com/qlik-trial/help-documentation | Flare (HTML) | `Content/` | `daily` |
| docs-core | https://github.com/Talend/docs-core | DITA (XML) | `en/` | `cloud-main` or `80-main` or an integration branch (see Step 4) |
| docs-components | https://github.com/Talend/docs-components | DITA (XML) | `en/` | `80-main` |

---

## Procedure

### Step 1 — Gather required context

#### Fetch the Jira issue and collect documentation plan details:

**From Jira** use `getJiraIssue` tool to fetch:
"fields": ["summary", "fixVersions", "customfield_10300", "components", "description", "issuelinks"]

 Verify your API response includes fixVersions before proceeding. If missing, re-run with the fields parameter above.

#### **From documentation plan:**
- **Affected file paths**: all paths to update/create (e.g., `help-documentation/Content/...`, `docs-core/en/...`, `docs-components/en/...`)

### Step 2 — Detect the repository

Examine affected file paths to determine which repository you are working with:

| File path marker | Repository |
|---|---|
| Contains `help-documentation` or `Content/` | **help-documentation** (Flare) |
| Contains `docs-components` | **docs-components** (DITA) |
| Contains `docs-core` or primarily in `en/` (no docs-components marker) | **docs-core** (DITA) |

Proceed to the repository-specific subsection in Step 3 below.

---

### Step 3 — Repository-specific branch naming

#### **help-documentation (Flare)**

Detect the product by examining file paths in the documentation plan. Each product site has a corresponding branch prefix that enables the right site to build automatically.

##### Product detection by file path

Examine the affected file paths to determine the product. The path patterns follow the folder structure under `Content/`:

| Priority | File path pattern | Product | Branch prefix |
|---|---|---|---|
| 1 | `Content/Connectors_*/` | Connectors | `branch-connectors-` |
| 1 | `Content/EDL/` | EDL | `branch-edl-` |
| 1 | `Content/EnterpriseManager/` | Enterprise Manager | `branch-enterprisemanager-` |
| 1 | `Content/Qlik_GeoAnalytics/` | GeoAnalytics | `branch-geoanalytics-` |
| 1 | `Content/Governance*/` | Governance Dashboard | `branch-govDashboard-` |
| 1 | `Content/Qlik_HelpPortal/` or `Content/Help*/` | Help Portal | `branch-portal-` |
| 1 | `Content/*InsightBot*/` or `Content/*Insight-Bot*/` | Insight Bot | `branch-insight-bot-` |
| 1 | `Content/NodeGraph/` | NodeGraph | `branch-nodegraph-` |
| 1 | `Content/NPrinting/` | NPrinting | `branch-nprinting-` |
| 1 | `Content/*Migration*/` | Migration | `branch-migration-` |
| 1 | `Content/Onboarding/` | Onboarding | `branch-onboarding-` |
| 1 | `Content/QlikAlerting/` or `Content/*Alerting*/` | Qlik Alerting | `branch-qlikalerting-` |
| 1 | `Content/*AutoML*/` | Qlik AutoML | `branch-automl-` |
| 1 | `Content/Qlik_Catalog/` or `Content/Catalog/` | Qlik Catalog | `branch-qc-` |
| 1 | `Content/Compose*/` | Qlik Compose | `branch-qlikcompose-` |
| 1 | `Content/QlikView/` | QlikView | `branch-qv12-` |
| 1 | `Content/Replicate/` | Replicate | `branch-replicate-` |
| 1 | `Content/Sense_Hub/` | Qlik Cloud Services | `branch-qcs-` |
| 2 | `Content/Sense_DeployAdminister/` | Sense Deploy Administer | `branch-senseDeployAdmin-` |
| 2 | `Content/Sense_*/` | Sense | `branch-sense-` |
| 2 | `Content/Upsolver*Classic*/` | Upsolver Classic | `branch-upsolverclassic-` |
| 2 | `Content/Upsolver*Sqlake*/` or `Content/Upsolver*SQLake*/` | Upsolver Sqlake | `branch-upsolversqlake-` |
| 3 | None of the above | General/Other | `docs/` |

**Branch name format:**
```
<prefix><DOC-ticket-id>-created-by-copilot
```

**Examples:**
- `branch-connectors-DOC-12345-created-by-copilot`
- `branch-senseDeployAdmin-DOC-12345-created-by-copilot`
- `branch-qcs-DOC-12345-created-by-copilot`
- `docs/DOC-12345-created-by-copilot` (fallback for unmatched products)

---

#### **docs-core (DITA)**

##### Step 1: Detect cloud vs on-premises content

Use this priority to determine content type:

1. **Product field check**: If Jira **Product** contains "TMC" or "Talend Management Cloud" → **cloud** content.
2. **Components field check**: If Jira **Components** contains "Talend Cloud" or "Talend Cloud Migration Platform" → **cloud** content.
3. **Keyword search** in description and file paths:
   - **Cloud keywords**: "cloud", "SaaS", "Talend Cloud", "TMC", "Qlik Cloud"
   - **On-prem keywords**: "on-premises", "on-prem", "self-hosted", "installation", "client-managed"
4. **If still ambiguous**: Ask the user: *"Are you updating cloud or on-premises content?"*

##### Step 2: Form the branch name (docs-core)

Apply the naming pattern based on content type and Studio release status:

| Content type | Branch name pattern | Example |
|---|---|---|
| **Cloud** |`cloud-DOC-XXXX-<keywords>-created-by-copilot` | `cloud-DOC-1234-new-feature-created-by-copilot` |
| **On-prem** |`80-DOC-XXXX-<keywords>-created-by-copilot` | `80-DOC-1234-new-feature-created-by-copilot` |

**Note on keywords:** Include relevant keywords from the Jira summary to make the branch self-documenting.

---

#### **docs-components (DITA)**

**Branch name format:**
```
80-<DOC-ticket-id>-<keywords>-created-by-copilot
```

Include relevant keywords from the Jira summary to make the branch self-documenting.

**Examples:**
- `80-DOC-1234-Java-21-support-created-by-copilot`
- `80-DOC-5678-Databricks-connector-created-by-copilot`

---

### Step 4 — Determine the base branch

#### If the docs-core or docs-components repository was detected and a fixVersions value was found, check for a Studio monthly release:

Identify if the **fixVersions** field matches the pattern: `8.0.1-RYYYY-MM` (for example, `8.0.1-R2026-04`)

**If yes:** Extract the release code `rYYYYMM` (for example, `r202604` from `8.0.1-R2026-04`)

#### Then determine the base branch using the following rules:

| Repository | Condition | Base branch |
|---|---|---|
| **help-documentation** | — | `daily` |
| **docs-core** | Cloud content| `cloud-main` |
| **docs-core** | On-prem content, Studio release detected | `80-r<YYYYMM>-studio-integration-and-rn` (the integration branch) |
| **docs-core** | On-prem content, no Studio release | `80-main` |
| **docs-components** | Studio monthly release detected | `80-r<YYYYMM>-integration` (the integration branch) |
| **docs-components** | Standard work | `80-main` |

### Step 4a — Ensure integration branch exists (Studio monthly releases only)

If a Studio monthly release integration branch was identified in Step 4, verify it exists on the remote before proceeding:

1. **Fetch latest remote refs:** `git fetch origin`
2. **Check if the integration branch exists:** `git branch -r | grep <integration-branch-name>`
   - **If it exists**: Proceed to Step 5.
   - **If it does not exist**: Proceed to Creating a new integration branch below.

#### Creating a new integration branch

If the integration branch does not exist (common for newly-announced monthly releases):

1. Checkout the `80-main` branch locally:
   ```
   git checkout 80-main
   git pull origin 80-main
   ```
2. Create the new integration branch from `80-main`:
   ```
   git checkout -b <integration-branch-name>
   ```
   (e.g., `git checkout -b 80-r202604-studio-integration-and-rn` for docs-core or `80-r202604-integration` for docs-components)
3. Push the new branch to remote:
   ```
   git push origin <integration-branch-name>
   ```
4. Confirm the branch was created and pushed: `git branch -r | grep <integration-branch-name>`

After the integration branch is created and pushed, proceed to Step 5 to create your feature branch.

### Step 5 — Create and switch to the feature branch

Execute the following commands in your terminal (in the repository root):

1. Ensure working directory is clean: `git status`
2. Checkout the base branch: `git checkout <base-branch>`
3. Pull latest changes: `git pull origin <base-branch>`
4. Create and switch to the new branch — guarding against an already-existing local branch:
   ```powershell
   git branch --list <branch-name>
   ```
   - If the command returns the branch name, the branch already exists locally — run `git checkout <branch-name>` to switch to it.
   - If the command returns nothing, the branch is new — run `git checkout -b <branch-name>` to create and switch to it.
5. Confirm the branch was created: `git branch --show-current`

### Step 6 — Return the branch name

Store and return the branch name for use in subsequent workflow steps (commits, PR creation).

---

## Troubleshooting

### Ambiguous repository detection

**If you cannot determine which repository from file paths alone:**
1. Check the Jira ticket description and linked PRs for repo context.
2. Verify the project key: `DOC-` tickets typically span multiple repos. Look for explicit repo mentions.
3. Ask the user: *"Are you updating help-documentation (Flare), docs-core (DITA), or docs-components (DITA)?"*

### Cloud vs on-premises ambiguity (docs-core only)

**If Product, Components, and keywords don't clarify:**
1. Review linked PRs (via issuelinks) to see which branch was used in related changes.
2. Check file paths: `cloud/` vs `on-prem/` subfolder naming.
3. Ask the user directly.

### Base branch not found

**If the detected base branch does not exist:**
1. Verify the branch name spelling (check `git branch -r` for remote branches).
2. For integration branches: confirm the Studio release version is correct.
3. Pull latest remote refs: `git fetch origin`
4. If still missing, confirm with the team which base branch to use.
