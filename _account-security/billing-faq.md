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

# -------------------------- #
#          BASICS            #
# -------------------------- #


  - topic: "Billing basics"
    anchor: "billing-basics"
    items:
      - question: "How does Stitch billing work?"
        anchor: "stitch-billing"
        answer: |
          Plans are based on the volume of rows and events replicated per month. Each plan has a monthly allotment of replicated rows.

          In addition, access to some integrations depends on the type of plan you select. To use Stitch's Paid integrations, you'll need to select a paid plan.

      - question: "What's a replicated row?"
        anchor: "what-is-a-replicated-row"
        answer: |
          {% include billing/replicated-row-definition.html %}

          For an in-depth walkthrough of how Stitch calculates your usage, check out the [Understanding & Reducing Your Row Usage guide]({{ link.billing.billing-guide | prepend: site.baseurl }}).


# -------------------------- #
#        INTEGRATIONS        #
# -------------------------- #

  - topic: "Integrations"
    anchor: "integrations"
    items:
      - question: "What integrations are available on each plan?"
        anchor: "integrations-each-plan"
        answer: |
          {{ site.data.stitch.subscription-plans.trial-description }}

          {% assign all-integrations = site.documents | where:"input", true %}

          {% assign free-integrations = all-integrations | where:"tier","Free" | sort:"title" %}
          {% assign paid-integrations = all-integrations | where:"tier","Premium" | sort:"title" %}

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

          ### Available to all plans

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

          ### Available to paid plans

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

      - question: "Can I use paid integrations if I'm on the Free plan?"
        anchor: "paid-integrations-free-plan"
        answer: |
          No. To use any of Stitch's paid integrations, you'll need to [upgrade to a paid plan]({{ site.pricing }}).

      - question: "How many integrations can I add?"
        anchor: "how-many-integrations-can-i-add"
        answer: |
          The total number of integrations refers to the number of distinct integration types each account may add, dependent upon the selected plan type.

          <table width="100%">
          <tr>
          {% for plan in site.data.stitch.subscription-plans.all-plans %}
          <td>
          <strong>{{ plan.name | flatify }}</strong>
          </td>
          {% endfor %}
          </tr>
          <tr>
          {% for plan in site.data.stitch.subscription-plans.all-plans %}
          <td>
          {{ plan.total-integrations }}
          </td>
          {% endfor %}
          </tr>
          </table>
          <br>


          For example: Accounts using the Free plan may add up to five different types of integrations. If an account has five Google Analytics integrations connected, this will only count as one towards the integration type quota. Up to four additional types of integrations may still be added.

          **Note**: The types of integrations available are also dependent on plan type. Users of the Free Plan will only have access to Free integrations, while Paid plan users will have access to free and paid integrations.

          For more info, refer to [our pricing page]({{ site.pricing }}).

# -------------------------- #
#   HISTORICAL DATA LOADS    #
# -------------------------- #

  - topic: "Historical data loads"
    anchor: "historical-data-loads"
    items:
      - question: "What is a free historical data load?"
        anchor: "free-historical-data-load"
        answer: |
          During the first seven days after a new integration begins to replicate data, replication is free. This is a free historical data load, and means that rows replicated from the new integration during this time won't count towards your quota.

          After the seven days are over, Stitch will continue to replicate data from the integration. Be sure to **pause** or **delete** the integration if you are no longer interested in replicating its data.

          Free historical data loads are only allowed once per integration namespace. For example: If an integration named `stitch_hubspot` is created and receives a free historical data load, subsequent integrations with the same name (created by deleting and creating a new integration) will not receive free historical replication.

          **Note**: While free historical loads apply to all of Stitch's integrations, you need to be on a paid plan to use our Paid integrations.

      - question: "Do free historical data loads apply to integration or table resets?"
        anchor: "free-historical-loads-resets"
        answer: |
          If the reset occurs during the free historical data load period, yes.

          If the reset occurs after the free historical data load period has ended, no.

          Free historical data loads are only applicable to new integrations for the first seven days after they begin to replicate data. [Resetting replication]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) for an integration or a table will count towards your quota.

      - question: "When do the seven days of historical data loading begin?"
        anchor: "free-historical-data-load-begin"
        answer: |
          The free historical data load period for new integrations begins after the integration first replicates data.

          For example: You create an integration on June 1 but don't fully configure it until June 2. In this case, the free historical data load will begin on June 2 and end June 9.

          **Note**: This is applicable only to integrations created on or after May 22, 2018. 


# -------------------------- #
#          ROW COUNTS        #
# -------------------------- #

  - topic: "Row counts"
    anchor: "row-usage"
    items:
      - question: "Where can I view my usage?"
        anchor: "view-billing-usage"
        answer: |
          {% include billing/view-usage.html %}

      - question: "Why do I see 'free' rows in my usage?"
        anchor: "free-row-usage"
        answer: |
          Free rows might display on your Stitch dashboard for a handful of reasons:

          - A new integration's [free historical data load](#historical-data-loads)
          - An exemption for beta testing an integration
          - Re-replicating data due to a defect

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
          Yes. Rows replicated from [free integrations](#integrations-each-plan) will count towards your usage. The "free" in "free integration" only indicates that the integration is available on non-paid plans, not that the rows replicated don't count towards your usage.

# -------------------------- #
#    CHOOSE & CHANGE PLANS   #
# -------------------------- #

  - topic: "Choose and change plans"
    anchor: "manage-plans"
    items: 
      - question: "Do I have to select a plan after my free trial ends?"
        anchor: "select-plan-after-free-trial"
        answer: |
          Yes. When your trial ends, Stitch will automatically pause your integrations. Replication will resume after you select a plan and enter a valid credit card.

          **Note**: Some integrations require a **paid** plan after the free trial ends. To continue replicating data from these sources - for example, Salesforce - you'll need to select the Starter plan or higher after your trial concludes.

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

# -------------------------- #
# PAYMENT DETAILS & INVOICES #
# -------------------------- #

  - topic: "Manage payment details and invoices"
    anchor: "payment-invoices"
    items:
      - question: "Where do I manage my payment details?"
        anchor: "manage-payment-details"
        answer: |
          {% include note.html type="single-line" content="The user who initially enters the payment info is the user who will receive your account's monthly invoice in their email." %}

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


# -------------------------- #
#     CANCEL YOUR ACCOUNT    #
# -------------------------- #

  - topic: "Cancel your account"
    anchor: "canceling-account"
    items:
      - question: "How can I cancel my account?"
        anchor: "cancel-account"
        answer: |
          {% include billing/cancel-account.html %}
---
{% include misc/data-files.html %}

{{ page.summary }}