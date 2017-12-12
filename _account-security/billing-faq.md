---
title: Billing FAQ
permalink: /account-security/billing-faq
keywords: billing, bill info, payment history, tier, plan, charge, overage, invoice, payments, invoices
tags: [account, getting_started]

summary: "Learn how to manage and change your Stitch subscription plan, enter payment details, view invoices, and cancel your account."
type: "billing"
toc: true
layout: faq
weight: 1

frequently-asked-questions:
  - topic: "Billing Basics"
    anchor: "billing-basics"
    items:
      - question: "How does Stitch billing work?"
        anchor: "stitch-billing"
        answer: |
          Plans are based on the volume of rows and events synced per month. Each plan has a monthly allotment of replicated rows.

          In addition, access to some integrations depends on the type of plan you select. To use Stitch's Paid integrations, you'll need to select a paid plan.

      - question: "What's a replicated row?"
        anchor: "what-is-a-replicated-row"
        answer: |
          {% include billing/replicated-row-definition.html %}

          For an in-depth walkthrough of how Stitch calculates your usage, check out the [Understanding & Reducing Your Row Usage guide]({{ link.billing.billing-guide | prepend: site.baseurl }}).

      - question: "What integrations are available on each plan?"
        anchor: "integrations-each-plan"
        answer: |
          {{ site.data.stitch.subscription-plans.trial-description }}

          {% assign free-integrations = site.documents | where:"tier","Free" | sort:"title" %}
          {% assign paid-integrations = site.documents | where:"tier","Premium" | sort:"title" %}

          {% capture paid-plans %}

          {% for plan in site.data.stitch.subscription-plans.all-plans %}

          {% unless plan.paid == false %}

          {% if forloop.last == true %}
          {{ plan.name | prepend: "and " }}
          {% else %}
          {{ plan.name | append: ", " }}
          {% endif %}

          {% endunless %}

          {% endfor %}
          {% endcapture %}

          ### Available to All Plans

          After the Free Trial has ended, the integrations in the table below will be available to all plans, regardless whether it's a free or paid plan.

          <table width="100%; fixed">
          {% for integration in free-integrations %}
          {% cycle 'free-before': '<tr>', '', '', '' %}
          <td width="25%">
          <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.title }}</a>
          </td>
          {% if forloop.last == true %}
          <td width="25%">
          </td>
          </tr>
          {% endif %}
          {% cycle 'free-after': '', '', '', '</tr>' %}
          {% endfor %}
          </table>

          <hr>

          ### Available to Paid Plans

          After the Free Trial has ended, the integrations in the table below will only be available to paid plans. As of {{ 'now' | date: "%B %d, %Y" }}, this includes the {{ paid-plans | strip_newlines }} plans.

          <table width="100%; fixed">
          {% for integration in paid-integrations %}
          {% cycle 'paid-before': '<tr>', '', '', '' %}
          <td width="25%" markdown="span">
          [{{ integration.title }}]({{ integration.url | prepend: site.baseurl }})
          </td>
          {% if forloop.last == true %}
          <td width="25%">
          </td>
          </tr>
          {% endif %}
          {% cycle 'paid-after': '', '', '', '</tr>' %}
          {% endfor %}
          </table>

  - topic: "Row Counts"
    anchor: "row-usage"
    items:
      - question: "Where can I view my usage?"
        anchor: "view-billing-usage"
        answer: |
          {% include billing/view-usage.html %}

      - question: "When will my row count will reset?"
        anchor: "when-will-row-count-reset"
        answer: |
          You can find your Reset Date in the **Plan Details** section of the {{ app.page-names.billing }} page, accessed by clicking the {{ app.menu-paths.billing }}.

      - question: "What happens if I exceed my row limit?"
        anchor: "exceed-row-limit"
        answer: |
          {% include billing/overages.html %}

      - question: "How can I prevent overages?"
        anchor: "prevent-overages"
        answer: |
          We recommend [following the simple tips in this guide]({{ link.billing.billing-guide | prepend: site.baseurl | append: "#reducing-your-usage" }}) to reduce your usage and help prevent overages.

      - question: "Do rows from free integrations count towards my usage?"
        anchor: "free-integrations-usage"
        answer: |
          Yes. Rows replicated from [free integrations](#integrations-each-plan) will count towards your usage. The "free" in "free integration" only indicates that the integration is available on non-paid plans, not that the rows replicated don't factor into your row usage.

  - topic: "Choose & Change Plans"
    anchor: "manage-plans"
    items: 
      - question: "Do I have to select a plan after my free trial ends?"
        anchor: "select-plan-after-free-trial"
        answer: |
          Yes. When your trial ends, Stitch will automatically pause your integrations. Replication will resume after you select a plan and enter a valid credit card.

          Note that some integrations require a **paid** plan after the free trial ends. To continue replicating data from these sources - for example, Salesforce - you'll need to select the Starter plan or higher after your trial concludes.

      - question: "How can I change my plan?"
        anchor: "change-plan"
        answer: |
          You can change your plan in the **Plan Details** section of the {{ app.page-names.billing }} page, accessed by clicking {{ app.menu-paths.billing }}.

          Click the **Change Your Plan** button and select the plan you want from the window that displays.

      - question: "What happens if I change my plan mid-billing cycle?"
        anchor: "change-plan-mid-cycle"
        answer: |
          This depends on whether you're upgrading or downgrading your plan:

          - **If you're upgrading**, meaning the new plan has a greater row limit than the current plan, the change will be effective immediately and you will only be billed for the difference between the current plan and the new plan.

             In addition, if you're upgrading from the Free plan to any Paid plan, you will also have immediate access to Paid integrations.

          - **If you're downgrading**, meaning the new plan has a lower row limit than the current plan, the change will take effect at the end of the billing cycle. This will ensure you can take full advantage of the higher row allotment and access to Paid integrations.

  - topic: "Manage Payment Details & Invoices"
    anchor: "payment-invoices"
    items:
      - question: "Where do I manage my payment details?"
        anchor: "manage-payment-details"
        answer: |
          {% include note.html content="The user who initially enters the payment info is the user who will receive your account's monthly invoice in their email." %}

          You can enter and manage your credit card details in the {{ app.page-names.billing }} page, accessed by clicking {{ app.menu-paths.billing }}.

          When you enter the cardholder's name, **make sure that a valid last name is entered**. Though Stitch does validate these fields, we've seen replication issues arise when the Last Name field is blank.

      - question: "What types of payment does Stitch accept?"
        anchor: "accepted-payment-types"
        answer: |
          Stitch accepts all major credit cards. We don't currently accept wire transfers or ACH payments.

      - question: "Where can I see my past payments?"
        anchor: "view-past-payments"
        answer: |
          You can view your past payments, including the payment amount and associated invoice number, in the **Past Payments** section of the {{ app.page-names.billing }} page.

      - question: "Who receives a copy of the monthly invoice?"
        anchor: "copy-monthly-invoice"
        answer: |
          The user who initially adds the payment information to the account will receive a copy of the monthly invoice in their email.

          Additionally, everyone can also view the Past Payments details in the {{ app.page-names.billing }} page.

  - topic: "Cancel Your Account"
    anchor: "canceling-account"
    items:
      - question: "How can I cancel my account?"
        anchor: "cancel-account"
        answer: |
          {% include billing/cancel-account.html %}
---
{% include misc/data-files.html %}

{{ page.summary }}