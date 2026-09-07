---
name: repository-classifier
description: "Classify Jira tickets to the correct documentation repository based on Product field value. Uses direct mapping for most products and AI inference for ambiguous cases. Returns repository labels, automation skip flag, and optional notes. Use when: assessing documentation impact, routing tickets, or determining target repository for documentation changes."
---

# Repository Classifier Skill

## Purpose

Determine which documentation repository (or repositories) should handle a given Jira ticket based on the Product field value. For ambiguous product values, use AI inference from Jira context to make the classification.

## Input

Provide the following from the Jira ticket:
- **Product field** (`fields.customfield_10178`)
- **Description** (`fields.description`)
- **Summary** (`fields.summary`)
- **What's New content** (`fields.customfield_10478`) - optional

## Output Format

Return a JSON structure with two fields:

```json
{
  "labels": ["repository-label"],
  "note": ""
}
```

- **`labels`** (array): Repository label(s) to apply to the Jira ticket
- **`note`** (string): Explanation when AI inference was used

## Classification Logic

### Tier 1: Direct Mappings

Most products map directly to a repository without AI inference needed:

| Product Field Value | Repository Label | Notes |
|---|---|---|
| All products | `help-documentation` | |
| Compose | `help-documentation` | |
| Data Product Catalog | `help-documentation` | |
| Insight bot | `help-documentation` | |
| Inventory Heritage | `docs-core-cloud` | |
| Nprinting | `help-documentation` | |
| Pipeline Designer Heritage | `docs-core-cloud` | |
| Qlik Alerting | `help-documentation` | |
| Qlik Analytics Connector | `help-documentation` | |
| Qlik Answers | `help-documentation` | |
| Qlik Automation | `help-documentation` | |
| Qlik Data Gateway - Data Movement | `help-documentation` | |
| Qlik Data Gateway - Direct Access | `help-documentation` | |
| Qlik Insight Advisor | `help-documentation` | |
| Qlik Predict | `help-documentation` | |
| Qlik Proactive | `help-documentation` | |
| Qlik Sense | `help-documentation` | |
| Qlik Web Connectors (standalone) | `help-documentation` | |
| Qlikview | `help-documentation` | |
| QTC Data Movement | `help-documentation` | |
| QTC Pipelines | `help-documentation` | |
| QTC Stewardship | `help-documentation` | |
| Replicate | `help-documentation` | |
| RnD Operations | `help-documentation` | |
| Stewardship Heritage | `docs-core-80` | Assuming no more cloud changes |
| Stitch Heritage | `stitch-docs` | |
| TAC | `docs-core-80` | |
| Talend Data Preparation Heritage | `docs-core-80` | Assuming no more cloud changes |
| TMC | `docs-core-cloud` | |

**For Tier 1 products:**
```json
{
  "labels": ["<repository-label>"],
  "note": ""
}
```

---

### Tier 2: Conditional Mappings (AI Inference Required)

These products require examining Jira context to determine the correct repository:

#### Data Processing

**Possible repositories:** `help-documentation` OR `docs-core-cloud`

**Decision criteria:**
- **help-documentation signals:** "Qlik", "Qlik Cloud"
- **docs-core-cloud signals:** "Talend"
- **Default if ambiguous:** `help-documentation`

**Output when help-documentation:**
```json
{
  "labels": ["help-documentation"],
  "note": "AI inference: Qlik Cloud signals detected - [list key signals]"
}
```

**Output when docs-core-cloud:**
```json
{
  "labels": ["docs-core-cloud"],
  "note": "AI inference: Talend signals detected - [list key signals]"
}
```

#### APP-API Integration

**Possible repositories:** `help-documentation` OR `docs-core-cloud`

**Decision criteria:**
- **help-documentation signals:** Qlik
- **docs-core-cloud signals:** Talend
- **Default if ambiguous:** `help-documentation`

**Output format:** Same structure as Data Processing above

#### Studio

**Possible repositories:** `docs-core-80` OR `docs-components`

**Decision criteria:**
- **docs-core-80 signals:** Studio UI, Studio perspectives, editors, workspace features, Studio preferences, Studio-specific functionality, general Studio documentation
- **docs-components signals:** Individual components or connectors (tMap, tLogRow, tMysqlInput, etc.), component parameters, component library, Hadoop components, reusable component definitions
- **Default if ambiguous:** `docs-core-80`

**Output when docs-core-80:**
```json
{
  "labels": ["docs-core-80"],
  "note": "AI inference: Studio core functionality detected - [list key signals]"
}
```

**Output when docs-components:**
```json
{
  "labels": ["docs-components"],
  "note": "AI inference: Component-related keywords detected - [list key signals]"
}
```

---

## Implementation Guidelines

### Step 1: Extract Product Field

Get the product value from `fields.customfield_10178`. If empty or null, check description for inline product mentions.

### Step 2: Apply Classification Logic

1. Check Tier 2 (conditional mappings) - if match found, run AI inference
2. Check Tier 1 (direct mappings)
3. If no match found: return empty labels and note the issue

### Step 3: Run AI Inference (Tier 2 only)

For conditional mappings:
1. Extract relevant keywords from description, summary, and What's New content
2. Score signals for each possible repository
3. Select repository with strongest signals
4. If tied or no clear signals: use default
5. Record detected signals in the `note` field for transparency

### Step 4: Return Structured Output

Always return the two-field JSON structure as specified above.

---

## Error Handling

**If product field is empty:**
- Check description for product mentions
- If still not found: return `{"labels": [], "note": "Product field is empty and no product mentioned in description"}`

**If product value doesn't match any tier:**
- Return `{"labels": [], "note": "Unknown product value: [product value]. Manual classification required."}`

---

## Examples

### Example 1: Direct Mapping

**Input:**
- Product: "Qlik Sense"

**Output:**
```json
{
  "labels": ["help-documentation"],
  "note": ""
}
```

### Example 2: AI Inference (Data Processing → Talend)

**Input:**
- Product: "Data Processing"
- Description: "Add new scheduling feature in Talend Remote engine for SaaS users..."

**Output:**
```json
{
  "labels": ["docs-core-cloud"],
  "note": "AI inference: Talend signals detected - 'Talend'"
}
```

### Example 3: AI Inference (Studio → Components)

**Input:**
- Product: "Studio"
- Description: "Update tMysqlInput component to support new authentication method. Add parameter for connection pooling to tMap component."

**Output:**
```json
{
  "labels": ["docs-components"],
  "note": "AI inference: Component-related keywords detected - 'tMysqlInput', 'tMap', 'component parameters'"
}
```

---

## Integration Notes

This skill is designed to be invoked by:
- **Assess-doc-impact agent** - to apply repository labels during impact assessment

The skill performs classification only - it does not apply labels or modify Jira tickets. The calling agent is responsible for using the output appropriately.
