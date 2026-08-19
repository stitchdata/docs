# Alphahelp URL Construction Reference

This reference explains how to construct alphahelp URLs for documentation branch builds. These URLs are used to preview documentation changes before they go to production.

---

## Overview

Alphahelp URLs allow reviewers to see documentation changes in a live environment. The URL structure differs between Flare (help-documentation) and DITA (docs-core, docs-components) repositories.

---

## Repository Detection

First, determine which repository the changes are in:

| Repository | Indicators |
|---|---|
| **help-documentation** | Branch starts with `branch-`(or `docs/` for the General/Other fallback), files in `Content/` folder, `.htm` files |
| **docs-core** | Branch starts with `cloud-` or `80-`, files in DITA format (`.dita` extension) |
| **docs-components** | Branch starts with `80-`, component documentation |

---

## Flare (help-documentation) URL Construction

### Base URL Pattern

```
https://alphahelp.qliktech.com/rc/en-US/{site-segment}/{file-path}
```

### Step 1: Extract Branch Components

Branch name format: `branch-{product}-{remainder}`

Examples:
- `branch-qcs-DOC-4341-mega-validator` → product: `qcs`, remainder: `DOC-4341-mega-validator`
- `branch-migration-DOC-2686-unified-tagging-tests` → product: `migration`, remainder: `DOC-2686-unified-tagging-tests`
- `branch-onboarding-DOC-4294-recipe-applied-example` → product: `onboarding`, remainder: `DOC-4294-recipe-applied-example`

### Step 2: Map Product Code to URL Segment

| Branch Prefix | URL Segment | Notes |
|---|---|---|
| `branch-qcs-` | `cloud-services` | Qlik Cloud Services |
| `branch-sense-` | `sense` | Qlik Sense (general) |
| `branch-senseDeployAdmin-` | `sense-deployAdmin` | Qlik Sense Deploy/Admin |
| `branch-qv12-` | `qlikview` | QlikView |
| `branch-nprinting-` | `nprinting` | NPrinting |
| `branch-connectors-` | `connectors` | Connectors |
| `branch-migration-` | `migration` | Migration tools |
| `branch-onboarding-` | `onboarding` | Onboarding |
| `branch-automl-` | `automl` | AutoML |
| `branch-qlikalerting-` | `qlik-alerting` | Qlik Alerting |
| `branch-qc-` | `qlik-catalog` | Qlik Catalog |
| `branch-qlikcompose-` | `qlik-compose` | Qlik Compose |
| `branch-replicate-` | `replicate` | Replicate |
| `branch-enterprisemanager-` | `enterprise-manager` | Enterprise Manager |
| `branch-geoanalytics-` | `geoanalytics` | GeoAnalytics |
| `branch-govDashboard-` | `governance-dashboard` | Governance Dashboard |
| `branch-portal-` | `help-portal` | Help Portal |
| `branch-insight-bot-` | `insight-bot` | Insight Bot |
| `branch-nodegraph-` | `nodegraph` | NodeGraph |
| `branch-upsolverclassic-` | `upsolver-classic` | Upsolver Classic |
| `branch-upsolversqlake-` | `upsolver-sqlake` | Upsolver SQLake |
| `branch-edl-` | `edl` | EDL (internal guidelines) |

**If product code doesn't match any pattern above**, use the product code as-is (lowercase with hyphens).

### Step 3: Determine Build Type Suffix

By default, branch builds are **Release Candidate (RC)** builds: `-rc`

### Step 4: Construct Site Segment

Format: `{url-segment}-{remainder}-{suffix}`

Examples:
- `cloud-services-DOC-4341-mega-validator-rc`
- `migration-DOC-2686-unified-tagging-tests-rc`
- `onboarding-DOC-4294-recipe-applied-example-rc`

### Step 5: Transform File Path

File path transformation depends on the content location:

#### Path Transformation Rules

| Source Path Pattern | Transformation | Output Path |
|---|---|---|
| `Content/Sense_Hub/**` | Insert `Subsystems/Hub/` before `Content/` | `Subsystems/Hub/Content/Sense_Hub/**` |
| `Content/Sense_DeployAdminister/**` | Insert `Subsystems/DeployAdminister/` before `Content/` | `Subsystems/DeployAdminister/Content/Sense_DeployAdminister/**` |
| `Content/QlikView/**` | Insert `Subsystems/QlikView/` before `Content/` | `Subsystems/QlikView/Content/QlikView/**` |
| Any other `Content/**` | No transformation | `Content/**` |

**Why this matters:** Qlik Sense and QlikView content is organized into subsystems during the build process. Other products don't have this structure.

### Step 6: Assemble Final URL

Format:
```
https://alphahelp.qliktech.com/rc/en-US/{site-segment}/{transformed-path}
```

### Complete Examples

#### Example 1: Migration Product
- **Branch**: `branch-migration-DOC-2686-unified-tagging-tests`
- **File**: `Content/AnalyticsMigrationTool/Qlik-Analytics-Migration-Tool-Overview.htm`
- **Product code**: `migration`
- **URL segment**: `migration` (no transformation)
- **Site segment**: `migration-DOC-2686-unified-tagging-tests-rc`
- **Path**: `Content/AnalyticsMigrationTool/...` (no transformation)
- **Final URL**:
  ```
  https://alphahelp.qliktech.com/rc/en-US/migration-DOC-2686-unified-tagging-tests-ld/Content/AnalyticsMigrationTool/Qlik-Analytics-Migration-Tool-Overview.htm
  ```

#### Example 2: Qlik Cloud Services (QCS)
- **Branch**: `branch-qcs-DOC-4341-mega-validator`
- **File**: `Content/Sense_Hub/Introduction/creating-analytics-and-visualizing-data.htm`
- **Product code**: `qcs`
- **URL segment**: `cloud-services`
- **Site segment**: `cloud-services-DOC-4341-mega-validator-rc`
- **Path**: `Content/Sense_Hub/...` → `Subsystems/Hub/Content/Sense_Hub/...`
- **Final URL**:
  ```
  https://alphahelp.qliktech.com/rc/en-US/cloud-services-DOC-4341-mega-validator-rc/Subsystems/Hub/Content/Sense_Hub/Introduction/creating-analytics-and-visualizing-data.htm
  ```

#### Example 3: Onboarding
- **Branch**: `branch-onboarding-DOC-4294-recipe-applied-example`
- **File**: `Content/Onboarding/qlik-cloud-analytics-consumer.htm`
- **Product code**: `onboarding`
- **URL segment**: `onboarding` (no transformation)
- **Site segment**: `onboarding-DOC-4294-recipe-applied-example-rc`
- **Path**: `Content/Onboarding/...` (no transformation)
- **Final URL**:
  ```
  https://alphahelp.qliktech.com/rc/en-US/onboarding-DOC-4294-recipe-applied-example-rc/Content/Onboarding/qlik-cloud-analytics-consumer.htm
  ```

---

## DITA (docs-core, docs-components) URL Construction

### Base URL Pattern

```
https://alphahelp.qliktech.com/talend/en-US/{mapid}/{branch-name}/{pageid}
```

### Step 1: Extract Branch Name

DITA branches start with:
- `cloud-` for cloud content
- `80-` for on-premises content

Example: `cloud-DOC-4764-DE-1-6-persistence-storage`

### Step 2: Extract mapid from DITAMAP

**Simple Rule:** The mapid is always the ditamap filename without the `.ditamap` extension.

Examples:
- `installation-guide.ditamap` → mapid: `installation-guide`
- `debug-jobs.ditamap` → mapid: `debug-jobs`
- `dynamic-engine-configuration-guide.ditamap` → mapid: `dynamic-engine-configuration-guide`

#### Finding Which DITAMAP References Your Topic

Ditamaps are always located in these specific directories:

| Repository | Directory | Contents |
|---|---|---|
| **docs-core** | `en/maps-guides/` | User guides, installation guides, reference guides (33 files) |
| **docs-core** | `en/maps-kb/` | Knowledge base articles and how-to guides (99 files) |
| **docs-components** | `en/maps-kb/` | Component development guides (5 files) |

**Note:** Other component maps (standard-map-publish, mediation-map-publish) work differently and will be addressed separately.

**To find which ditamap references your changed DITA file:**
```powershell
# From repository root, search the maps directories
grep -r "your-topic-filename.dita" en/maps-guides/ en/maps-kb/
```

This will show which ditamap file references your topic. Extract the mapid from that filename.

**If you cannot determine the mapid**, note it as `[MAPID-NEEDED]` in the URL and flag for manual review.

### Step 3: Extract pageid from DITA File

 The `pageid` is defined in the DITA prolog metadata as an `<othermeta>` entry with `name="pageid"`.

Example DITA file:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept
  PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept xml:lang="en" id="r2026-05_studio_new-features_c">
   <title>New features</title>
   <shortdesc/>
   <prolog>
      <metadata>
         <othermeta content="r2026-05-studio-new-features" name="pageid"/>
      </metadata>
   </prolog>
...
</concept>
```

The `pageid` is `configure-docker-registry`.

### Step 4: Assemble Final URL

Format:
```
https://alphahelp.qliktech.com/talend/en-US/{mapid}/{branch-name}/{pageid}
```

### Complete Example

#### Example 4: DITA Cloud Content
- **Branch**: `cloud-DOC-4764-DE-1-6-persistence-storage`
- **File**: `en/engines/configure-docker-registry-task.dita`
- **DITAMAP**: `dynamic-engine-configuration-guide.ditamap` (mapid: `dynamic-engine-configuration-guide`)
- **DITA file id**: `configure-docker-registry`
- **Final URL**:
  ```
  https://alphahelp.qliktech.com/talend/en-US/dynamic-engine-configuration-guide/cloud-DOC-4764-DE-1-6-persistence-storage/configure-docker-registry
  ```

---

## Edge Cases and Special Handling

### Multiple Files Changed

Generate a URL for each changed htm or dita file.

### Snippets and Shared Content

If only snippets were changed:
- Identify which topics **include** those snippets
- Generate URLs for the parent topics
- Note in the comment: "Updated via shared snippet"

### Images and Resources

Do not generate alphahelp URLs for:
- Image files (`.png`, `.jpg`, `.svg`)
- CSS/JavaScript files
- Configuration files

### Paths Without Direct URL Mapping

Some files don't have a direct alphahelp URL:
- Project files (`.flprj`, `.ditamap` metadata)
- TOC files (`.fltoc`)
- Variable definition files

For these, note in the comment: "Configuration/structure changes only—no direct preview URL"

---

## Archive and Listing Pages

### Viewing All Branches

**Flare branches archive:**
```
https://alphahelp.qliktech.com/rc/en-US/archive
```

**Talend branches listing:**
```
https://alphahelp.qliktech.com/talend/en-US/branches
```

**Talend admin list:**
```
https://alphahelp.qliktech.com/talend/admin/list
```

---

## Validation Tips

### Quick Validation Checklist

Before posting URLs, verify:
- [ ] Branch name format matches expected pattern
- [ ] Product code correctly mapped to URL segment
- [ ] File path exists in the repository
- [ ] Subsystem insertion applied correctly (for Sense/QlikView)
- [ ] Build type suffix appropriate (`-rc` for most branches)
- [ ] For DITA: mapid and pageid extracted correctly

### Testing URLs

After generating URLs:
1. Wait for the branch build to complete (check Jenkins or Slack notifications)
2. Test at least one URL to confirm the pattern is correct
3. If a URL returns 404, recheck the path transformation rules

---

## Common Mistakes to Avoid

1. **Forgetting subsystem insertion** for Sense_Hub content
2. **Including the full branch prefix** in the site segment (should remove `branch-`)
3. **Incorrect product code mapping** (e.g., using `qcs` instead of `cloud-services`)
4. **Posting URLs before build completes** (URLs won't work until Jenkins finishes)
5. **For DITA**: Confusing filename with pageid (pageid comes from `pageid` attribute, not filename)

---

## Quick Reference

### Flare URL Template
```
https://alphahelp.qliktech.com/rc/en-US/{url-segment}-{doc-ticket}-{description}-rc/{path}
```

### DITA URL Template
```
https://alphahelp.qliktech.com/talend/en-US/{mapid}/{branch-name}/{pageid}
```

### Most Common Products
- `branch-qcs-*` → `cloud-services-*-rc`
- `branch-sense-*` → `sense-*-rc` (with Subsystems/Hub/ path insertion)
- `branch-nprinting-*` → `nprinting-*-rc`
- `cloud-*` → Talend DITA cloud content
- `80-*` → Talend DITA on-prem content
