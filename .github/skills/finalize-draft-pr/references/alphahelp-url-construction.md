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

### Step 1: Identify the Product URL Pattern

Use the product route and build type shown in the table. The path after the route is either a feature-branch identifier, a release identifier, or omitted for a daily build.

| Product | Feature branch | Daily or release build |
|---|---|---|
| Replicate | `replicate/{branch}-rc` | `replicate/latestDev-...-rc` |
| Qlik Connectors | `connectors-{branch}-rc` | `connectors` |
| Qlik NPrinting | `nprinting/{branch}-rc` | `nprinting/{release}` |
| Qlik Alerting | `alerting/{branch}-rc` | `alerting/{release}` |
| QlikView for Developers | `qlikview-developer/{branch}-rc` | `qlikview-developer/latestDev-...-rc` |
| QlikView | `qlikview/{branch}-rc` | `qlikview/{release}` |
| Qlik Enterprise Manager | Not confirmed | `enterprise-manager/latestDev-...-rc` |
| Qlik Cloud | `cloud-services-{branch}-rc` | `cloud-services` |
| Onboarding | `onboarding-{branch}-rc` | Use the published route. |
| Qlik Sense on Windows | `sense/{release}` | `sense/{release}` |
| Qlik Sense for administrators | `sense-admin/{release}` | `sense-admin/{release}` |
| Qlik Sense for developers | `sense-developer/{release}` | `sense-developer/{release}` |
| Migration Center | Not applicable | `migration/{page}` |

For products without a confirmed pattern, do not infer the route from the branch name. Use a verified URL or flag the route for review.

### Step 2: Apply the Build Identifier

For feature branches, use the identifier after the product route and preserve the `-rc` suffix. For release builds, use the release name, such as `May2026`, `September2026`, or `NextIR`. Daily builds omit the identifier when the product examples show no identifier.

### Step 3: Transform File Path

File path transformation depends on the content location:

#### Path Transformation Rules

| Source Path Pattern | Transformation | Output Path |
|---|---|---|
| `Content/Sense_Hub/**` | Insert `Subsystems/Hub/` before `Content/` | `Subsystems/Hub/Content/Sense_Hub/**` |
| `Content/Sense_DeployAdminister/**` | Insert `Subsystems/DeployAdminister/` before `Content/` | `Subsystems/DeployAdminister/Content/Sense_DeployAdminister/**` |
| `Content/QlikView/**` | Insert `Subsystems/QlikView/` before `Content/` | `Subsystems/QlikView/Content/QlikView/**` |
| `Content/QV_QlikView/**` on Qlik Cloud | Map to the Hub subsystem | `Subsystems/Hub/Content/Sense_Hub/**` |
| Any other `Content/**` | No transformation | `Content/**` |

**Why this matters:** Qlik Sense and QlikView content is organized into subsystems during the build process. Other products don't have this structure.

### Step 4: Assemble Final URL

Format:
```
https://alphahelp.qliktech.com/rc/en-US/{product-route}/{transformed-path}
```

### Verified Examples

Feature branch:
```
https://alphahelp.qliktech.com/rc/en-US/replicate/DOC-3730-created-by-copilot-rc/Content/Replicate/Main/Introduction/Home.htm
```

Daily build:
```
https://alphahelp.qliktech.com/rc/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/analyzing-data.htm
```

Release build:
```
https://alphahelp.qliktech.com/rc/en-US/sense/May2026/Content/Sense_Helpsites/Home.htm
```

Migration Center:
```
https://alphahelp.qliktech.com/rc/en-US/migration/installing-qtcmt
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

Use the value of the map's mapid element: `<othermeta name="mapid" content="..."/>`.

Examples:
- `installation-guide.ditamap` → mapid: `installation-guide`
- `debug-jobs.ditamap` → mapid: `debug-jobs`
- `dynamic-engine-configuration-guide.ditamap` → mapid: `dynamic-engine-configuration-guide`

#### Operating-system build flavors

The build appends an operating-system flavor to these map IDs:

- `installation-guide`
- `hybrid-installation-guide`
- `remote-engine-user-guide`

A URL that uses one of these base map IDs without a flavor is invalid.

- Append `-linux` by default. The Linux build contains the most content.
- If all relevant changes are specific to Windows, append `-windows`.
- If all relevant changes are specific to macOS, append `-mac`.
- If the changes apply to multiple operating systems, provide one Linux preview link. Do not provide all flavor variants.

Determine whether a change is operating-system-specific from the changed content's profiling attributes and surrounding topic references. When this cannot be determined, use the Linux flavor and flag the assumption for review.

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

The `pageid` is `r2026-05-studio-new-features`.

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
- **DITA pageid**: `configure-docker-registry`
- **Final URL**:
  ```
  https://alphahelp.qliktech.com/talend/en-US/dynamic-engine-configuration-guide/cloud-DOC-4764-DE-1-6-persistence-storage/configure-docker-registry
  ```

---

## Edge Cases and Special Handling

### Preview link labels

Use the page title as the link label in PR descriptions and Jira comments. Do not use the file name, file path, topic ID, or page ID as the label.

- For DITA, resolve the topic's `<title>`, including referenced variables, so the label matches the rendered page title.
- For Flare, use the title displayed as the page heading.
- Preserve the title's capitalization and product names.
- If the title cannot be resolved, flag the label for manual review instead of substituting a file path.

Example:

```markdown
- [Installing and configuring MongoDB](https://alphahelp.qliktech.com/talend/en-US/installation-guide-linux/cloud-DOC-1234-example/installing-and-configuring-mongodb)
```

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
- [ ] Product route and build type match a verified product pattern
- [ ] File path exists in the repository
- [ ] Subsystem insertion applied correctly (for Sense/QlikView)
- [ ] `-rc` is present only where the product pattern requires it
- [ ] For DITA: mapid and pageid extracted correctly

### Testing URLs

After generating URLs:
1. Wait for the branch build to complete (check Jenkins or Slack notifications)
2. Test at least one URL to confirm the pattern is correct
3. If a URL returns 404, recheck the path transformation rules

---

## Common Mistakes to Avoid

1. **Forgetting subsystem insertion** for Sense_Hub content
2. **Applying one product's route pattern to another product**
3. **Guessing a route from the branch name** instead of using a verified product pattern
4. **Posting URLs before build completes** (URLs won't work until Jenkins finishes)
5. **For DITA**: Confusing filename with pageid (pageid comes from `pageid` attribute, not filename)
6. **Using `installation-guide`, `hybrid-installation-guide`, or `remote-engine-user-guide` without a build flavor** (append `-linux` by default)
7. **Using a file path or ID as the link label** (use the rendered page title)

---

## Quick Reference

### Flare URL Template
```
https://alphahelp.qliktech.com/rc/en-US/{product-route}/{transformed-path}
```

Feature-branch routes may combine the product and branch identifier or use separate path segments, depending on the product:
```
https://alphahelp.qliktech.com/rc/en-US/{product-route}/{branch}-rc/{transformed-path}
```

### DITA URL Template
```
https://alphahelp.qliktech.com/talend/en-US/{mapid}/{branch-name}/{pageid}
```

### Most Common Products
- Qlik Cloud feature branch → `cloud-services-{branch}-rc`
- Qlik Cloud daily → `cloud-services`
- Replicate feature branch → `replicate/{branch}-rc`
- Qlik Connectors feature branch → `connectors-{branch}-rc`
- Qlik Sense release → `sense/{release}` (with subsystem path insertion where applicable)
- `cloud-*` → Talend DITA cloud content
- `80-*` → Talend DITA on-prem content
