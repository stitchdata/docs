---
name: "dita-variables"
description: "Usage rules, numeric ID reference table, and mandatory verification gate for DITA variables (metadata-variables.dita conrefs) in docs-core (Talend/Qlik). Ensures AI agents use conref instead of hardcoded product and module names."
version: "1.1"
applyTo: "docs-core"
tags: ["dita", "conref", "product-names", "talend", "qlik"]
---

# DITA Variables Skill

## Scope

**DITA variables in docs-core means one thing:** `<keyword conref>` references to
numeric IDs in `../../../common/taxonomy/metadata-variables.dita`.

This skill covers that mechanism only. Ditamap keydef (`<keyword keyref>`) and
reuse topic conref (`<keyword conref="../reuse/...">`) are separate patterns and
are out of scope here.

---

## Purpose

This skill gives AI agents durable knowledge for correctly using DITA variables.
It answers:
- What is the numeric ID for a given product name, module, or resource?
- Which product names must never be hardcoded in body text?
- How does the path to `metadata-variables.dita` vary by calling topic location?
- What section of `metadata-variables.dita` contains a given term?

For the current audit state, read `profiles/`.
For the reasoning behind variable additions or renames, read `decisions/`.

**Variable source:** `../../../common/taxonomy/metadata-variables.dita`

---

## Upon request or quarterly: Variable Audit Gate

Run this gate in either case:

- The invoking prompt explicitly asks for a variable ID audit.
- The `Last Verified` date in this SKILL.md is more than 90 days old.

If neither condition is true, skip the audit.

### Gate Procedure

**Step 0: Decide whether to run**

- If the invoking prompt explicitly requests a variable ID audit, run the gate.
- Otherwise, read `Last Verified` in this SKILL.md.
- If `Last Verified` is missing or older than 90 days, run the gate.
- If `Last Verified` is 90 days old or newer, skip the entire gate procedure (Step1 to 4).

**Step 1: Read the source file**
Open common/taxonomy/metadata-variables.dita.

**Step 2: Verify the high-frequency IDs in the reference table.**
For each row, find the matching `<keyword id="NNN">value</keyword>` entry and confirm
the resolved text matches the table.

**Step 3: Compare against the reference table.**
- If all values match: gate passes. Proceed with confidence.
- If any ID does not match or is missing: go to Step 4.

**Step 4: Handle discrepancy**

1. Report:
   ```
   VARIABLE AUDIT DISCREPANCY
   ID: metadata-variables/NNN
   Skill value: "<old product name>"
   File value: "<new product name>" (metadata-variables.dita:<line>)
   ```
2. Update the reference table in this SKILL.md.
3. Update `Last Verified` to today.
4. Create a new DDR file in `decisions/`.
5. Append the audit result to `profiles/` as a new timestamped entry.
6. Proceed using the value from metadata-variables.dita.

**Step 5: Record successful audit**
If no discrepancies were found, still:

- Update `Last Verified` to today.
- Append a pass entry to `profiles/` with timestamp and scope checked.



**Gate failure mode:** If `metadata-variables.dita` cannot be read, stop.
Do not assume the frozen IDs are current.

---

## DITA Variable Format

**Use for:** Product names, module names, features, resources, and services.

**Format:**
```xml
<keyword conref="[relative-path]/common/taxonomy/metadata-variables.dita#metadata-variables/NNN"/>
```

**Rules:**
- `NNN` is the numeric `id=""` attribute of the `<keyword>` element in `metadata-variables.dita`.
- The relative path to `common/taxonomy/` is always `../../common/taxonomy/` because
  all content files live one level deep under `en/[folder]/`.
- The fragment `#metadata-variables/NNN` uses the topic ID (`metadata-variables`) and
  the element ID (the numeric value).
- The `<keyword>` element in topics is always self-closing: `<keyword conref="..."/>`.
- Cannot be placed inside `href=""` attribute values; only in body text and prolog.

**Full example (from an** `en/engines/` **topic):**
```xml
<p>Deploy your <keyword
   conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/677"/>
   using Helm values files.</p>
```

**Path by calling folder:**

| Calling topic folder | Correct path to taxonomy file |
|---|---|
| `en/engines/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/management-console/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/reuse/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/api-microgateway/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/security/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/data-services/` | `../../common/taxonomy/metadata-variables.dita` |
| `en/[any product folder]/` | `../../common/taxonomy/metadata-variables.dita` |

---

## High-Frequency ID Reference Table

Verify each of these against `metadata-variables.dita` before use.
The `Section` column identifies which `<section id="...">` in the file contains the entry.

### Products

| ID | Resolved Value | Section | Usage Context | Last Verified |
|---|---|---|---|---|
| `13` | Talend Cloud | Products_list | Generic name for the Talend Cloud SaaS platform; first choice for Talend Cloud references | 2026-06-29 |
| `183` | Talend Data Fabric | Products_list | On-premises platform product name | 2026-06-29 |
| `790` | Qlik Cloud | Products_list | Qlik Cloud platform references (post-acquisition branding) | 2026-06-29 |
| `794` | Qlik Talend Cloud | Products_list | Combined Qlik + Talend Cloud product name | 2026-06-29 |
| `785` | Qlik Talend Cloud Starter Edition | Products_list | Specific edition tier | 2026-06-29 |
| `786` | Qlik Talend Cloud Standard Edition | Products_list | Specific edition tier | 2026-06-29 |
| `787` | Qlik Talend Cloud Premium Edition | Products_list | Specific edition tier | 2026-06-29 |
| `788` | Qlik Talend Cloud Enterprise Edition | Products_list | Specific edition tier | 2026-06-29 |

### Modules (engines, apps, components)

| ID | Resolved Value | Section | Usage Context | Last Verified |
|---|---|---|---|---|
| `42` | Talend Studio | Modules_list | Studio authoring environment; use for all Studio references | 2026-06-29 |
| `50` | Talend JobServer | Modules_list | On-premises job execution server | 2026-06-29 |
| `51` | Talend Runtime | Modules_list | ESB/OSGi runtime container | 2026-06-29 |
| `52` | Talend ESB | Modules_list | Enterprise Service Bus product/module | 2026-06-29 |
| `184` | Talend Integration Cloud | Modules_list | Legacy cloud integration module | 2026-06-29 |
| `185` | Talend Remote Engine | Modules_list | Remote Engine (non-Gen2) module | 2026-06-29 |
| `194` | Talend Cloud Pipeline Designer | Modules_list | Pipeline Designer cloud module | 2026-06-29 |
| `625` | Talend Management Console | Modules_list | TMC UI module; use for all TMC references in body text | 2026-06-29 |
| `641` | Talend Pipeline Designer | Modules_list | On-premises pipeline designer | 2026-06-29 |
| `642` | Remote Engine Gen2 | Modules_list | Second-generation Remote Engine | 2026-06-29 |
| `653` | Talend Data Catalog | Modules_list | Data Catalog module | 2026-06-29 |
| `677` | Dynamic Engine | Modules_list | Kubernetes-based Dynamic Engine; use for all Dynamic Engine references | 2026-06-29 |
| `729` | Qlik Talend Cloud Migration Toolkit | Modules_list | Migration toolkit module | 2026-06-29 |

### Resources (company / brand names)

| ID | Resolved Value | Section | Usage Context | Last Verified |
|---|---|---|---|---|
| `442` | Talend | Resources_list | Standalone "Talend" brand reference; use when referring to the company/brand, not a specific product | 2026-06-29 |
| `774` | Qlik | Resources_list | Standalone "Qlik" brand reference | 2026-06-29 |

---

## Synonym Disambiguation

Some concepts have multiple IDs or could be confused with each other.

| Concept | Correct ID | Resolved Value | Avoid | Reason |
|---|---|---|---|---|
| Talend SaaS platform | `13` | Talend Cloud | Hardcoding "Talend Cloud" | ID 13 is the canonical source |
| Post-acquisition platform | `794` | Qlik Talend Cloud | Mixing with ID 13 | ID 794 is for the combined-brand name |
| Qlik's analytics cloud | `790` | Qlik Cloud | Mixing with ID 13 or 794 | Different product; 790 is Qlik-only |
| TMC module | `625` | Talend Management Console | Hardcoding "TMC" or "Management Console" | Use 625 for the full name; never abbreviate inline |
| Remote Engine (any gen) | `185` | Talend Remote Engine | Using 642 for generic references | Use 185 for non-Gen2; use 642 specifically for Gen2 |
| Dynamic Engine | `677` | Dynamic Engine | Hardcoding "Dynamic Engine" | ID 677 ensures consistent casing and brand control |
| Talend brand | `442` | Talend | Using 774 for Talend | 442 = Talend company, 774 = Qlik company |

---

## Violation Patterns

AI agents must replace these with `<keyword conref>`:

| Incorrect (hardcoded in body text) | Correct |
|---|---|
| `<p>Configure your Dynamic Engine...</p>` | `<keyword conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/677"/>` |
| `<p>Log into Talend Management Console...</p>` | `<keyword conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/625"/>` |
| `<p>...in Talend Cloud...</p>` | `<keyword conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/13"/>` |
| `<p>...a Talend Remote Engine...</p>` | `<keyword conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/185"/>` |

**Acceptable hardcoding (exceptions where conref cannot be used):**
- Inside `href=""` attributes (links and topicrefs). However, conref is allowed in the anchor text, so although only hardcoding can be used in the values of `href=""`, when the anchor text presents, variables still must be used there in the anchor text.
- Inside `<source>` prolog elements
- Inside `<filepath>` elements (actual file paths, not product names)
Generally speaking, hardcoding is allowed in attribute-only or map-title contexts.
---

## Dynamic Lookup Instructions

When a product name is needed and its ID is not in the reference table:

1. Search `common/taxonomy/metadata-variables.dita` for the term:
   ```
   grep_search(query="<product name>", includePattern="common/taxonomy/metadata-variables.dita", isRegexp=false)
   ```
2. Note the `id=""` attribute value of the matching `<keyword>` element.
3. Confirm the section (`Products_list`, `Modules_list`, etc.) to understand the scope.
4. Use the numeric ID in the conref:
   ```xml
   <keyword conref="../../common/taxonomy/metadata-variables.dita#metadata-variables/NNN"/>
   ```
5. Add the new ID to the reference table in this skill with today's date.


---

## DDR Creation Protocol

When the audit gate detects a discrepancy or a new product ID is added, create a DDR.

**File naming:** `decisions/DDR-NNN-<product-name>-<YYYY-MM>.md`
(NNN = next sequential number, zero-padded to three digits)

**Required content:**

```
# DDR-NNN: <Product Name> — <Brief Description>

**Date Detected:** YYYY-MM-DD
**Detected by:** <AI agent name> (<task context>)
**Status:** Detected

## Variable Change
| Property | Value |
|---|---|
| ID | `metadata-variables/NNN` |
| Old Value | "<old product name>" |
| New Value | "<new product name>" |
| Section | <Products_list / Modules_list / Resources_list> |
| Source Line | metadata-variables.dita:<line> |
| Last Verified in Skill | <date from reference table> |

## Root Cause
**Type:** [New product added / Rebrand / Renamed / Discontinued / Unknown]
**Context:** <What changed and why. If unknown: "Root cause unknown — requires human verification.">

## Impact Assessment
**Scope:** <Estimated number of topics affected>
**Product areas:** <Affected documentation areas, e.g., en/engines/, en/management-console/>

## Actions Taken
1. Updated SKILL.md reference table value.
2. Updated Last Verified date.
3. Appended gate result to profiles/.
4. <Follow-up task created, or "None — requires human review.">

## Human Follow-Up Required
- [ ] Confirm this change was intentional (rebrand/rename) or a data error.
- [ ] If intentional: initiate batch update across affected topics.
- [ ] If error: revert the metadata-variables.dita change and close this DDR.
- [ ] Set Status to Approved (intentional) or Closed (resolved/reverted).
```

---

## DITA vs Flare Comparison (for AI agents familiar with Flare)

| Property | Flare (help-documentation) | DITA (docs-core) |
|---|---|---|
| Variable format | `<MadCap:variable name="Set.Name" />` | `<keyword conref="...dita#metadata-variables/NNN"/>` |
| Variable source | `.flvar` files in `Project/VariableSets/` | `common/taxonomy/metadata-variables.dita` |
| Variable identifier | Human-readable name (`CloudFullName`) | Numeric ID (`13`) |
| Naming conventions | Suffix system (`_Short`, `_Expanded`) | No suffix system; numeric IDs only |
| Verification gate | Read `.flvar`, compare 15 values | Read `metadata-variables.dita`, confirm numeric IDs |