---
name: flare-feature-conditions
description: "Use when adding, editing, or linking to any MadCap Flare content in help-documentation. Enforces the rule that feature conditions must never be created or added, and determines whether existing feature-conditioned content is safe to edit or link to."
---

# Flare feature conditions skill

## Overview

Use this skill when working with existing Flare feature conditions in the `Features` condition set, for example:

- `MadCap:conditions="Features.TLV-123"`
- `MadCap:conditions="Features.DOC-123"`
- `MadCap:conditions="Features.SUPPORT-123"`
- `MadCap:conditions="Features.NotInTLV-123"`

Do not apply this skill to other non-feature conditions.

## Definitions

- Feature condition: A normal feature condition such as `TLV-123`.
- Inverse condition: The paired `NotIn` condition, such as `NotInTLV-123`.

"Link to" means creating or modifying a link whose target content is controlled by a feature condition.

## Condition definitions and feature state

`Project/ConditionTagSets/Features.flcts` defines which feature conditions exist. Do not use it to determine whether a feature is active.

Resolve the effective state from the relevant `ProductScenarioFlags*.xml` files under `config/`.

The config contains the state of the feature condition only, for example `<name state='on'>TLV-123</name>`. The inverse `NotInTLV-123` condition always represents the inverse of the same state.

## Required behavior

### Never creating or modifying feature conditions

The agent must never create, add, change, or remove a `Features.*` feature condition. This applies to both new and existing content, regardless of whether surrounding content already has feature conditions.

Specifically, the agent must **never**:

- Create a new feature condition by adding an entry to `Features.flcts` or to any `ProductScenarioFlags*.xml` file.
- Add a `Features.*` value to a `MadCap:conditions` attribute.
- Change an existing `Features.*` value in a `MadCap:conditions` attribute.
- Remove a `Features.*` value from a `MadCap:conditions` attribute.
- Add a `MadCap:conditions` attribute containing a `Features.*` value to any element it creates or modifies.

When adding content inside an existing conditioned section, place the new content inside the already-conditioned parent element. Do not add a condition attribute to the new content itself. Do not copy or reuse a feature condition from surrounding or nearby content onto any new element — the presence of a `Features.*` condition on existing content is not a reason to add it to new content.

The agent may edit the content of an element that already has a `Features.*` condition when permitted by the decision rules below. It may also read and reason about existing feature conditions to decide whether to edit or link to conditioned content. It must never modify the conditions themselves.

### Resolving a feature condition

1.  Detect whether the content or link target has a feature condition.

    Look for:

    - `Features.<ticket-id>`
    - `Features.NotIn<ticket-id>`

    Ticket IDs use Jira-style letters, a hyphen, and numbers, such as `TLV-123`, `DOC-123`, or `SUPPORT-123`.

    Check the element itself **and all its ancestor elements** up to and including the root `<html>` element. A condition on any ancestor applies to all content inside it. Apply the decision rules for every `Features.*` condition found at any level.

    If multiple `Features.*` conditions are found at different levels and any one of them resolves to a blocked or forbidden state, do not edit or link automatically. Flag all conditions found and their resolved states for the writer to decide.

    If no `Features.*` condition is found on the element or any of its ancestors, the remaining steps in this workflow do not apply. The hard bans above still apply in all cases.

2.  Extract the ticket ID from either condition form (for example, `TLV-123`).

3.  Search all `ProductScenarioFlags*.xml` files under `config/` for that ticket ID. Use a broad search pattern such as `config/**/ProductScenarioFlags*.xml` and check every result — do not stop after the first file returns no match.

4.  Resolve the feature state from the state attribute:

    - `state="on"`: the feature is on
    - `state="off"`: the feature is off

    If the same ticket ID has conflicting states across config files, do not edit or link automatically. Flag the case as a conflicting config issue.

5.  If the ticket ID is not found, or its state cannot be resolved reliably, do not edit or link automatically. Flag the case for writer review.

## Decision rules for edits and links

Apply these rules exactly:

| Existing condition | Base feature state | Decision |
|---|---|---|
| `Features.<ticket-id>` | `on` | **Allowed** |
| `Features.<ticket-id>` | `off` | **Blocked** — future content uncertainty |
| `Features.NotIn<ticket-id>` | `off` | **Blocked** — writer review required |
| `Features.NotIn<ticket-id>` | `on` | **Forbidden** — deprecated/hidden content |

### Examples

If config contains:

`<name state='on'>TLV-123</name>`

then:

- `Features.TLV-123` is the active content and may be edited or used as a link target.
- `Features.NotInTLV-123` is the hidden/deprecated content and must not be edited or used as a link target.

If config contains:

`<name state='off'>TLV-123</name>`

then:

- `Features.TLV-123` represents future content. Do not edit or link to it automatically. Flag it for writer review.
- `Features.NotInTLV-123` is the alternate content currently shown, but do not edit or link to it automatically. Flag it for writer review.

The agent must not infer permission from visibility alone. Follow the decision table above.

## Handling blocked cases

When an edit or link is blocked, report:

- The feature condition found.
- The resolved feature state.
- The reason for blocking:
   - `future content uncertainty`
   - `deprecated/hidden content`
   - `unresolved config state`
   - `conflicting config issue`
- That writer review is required.
