---
title: Billing FAQ
permalink: /account-security/billing-faq
keywords: billing, bill info, payment history, tier, plan, charge, overage, invoice, payments, invoices
tags: [account, getting_started]

summary: "Learn how to manage and change your Stitch subscription plan, enter payment details, view invoices, and cancel your account."

toc: true
layout: faq

type: "billing"
weight: 2

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

          In addition, access to some integrations depends on the type of plan you select. To use Stitch's Standard integrations, you'll need to select a Standard plan.

          Refer to the [pricing page]({{ site.pricing }}){:target="new"} for more info.

      - question: "What's a replicated row?"
        anchor: "what-is-a-replicated-row"
        answer: |
          {% include billing/replicated-row-definition.html %}

          For an in-depth walkthrough of how Stitch calculates your usage, check out the [Understanding and Reducing Your Row Usage guide]({{ link.getting-started.row-usage | prepend: site.baseurl }}).


# -------------------------- #
#        INTEGRATIONS        #
# -------------------------- #

  - topic: "Integrations"
    anchor: "integrations"
    items:
      - question: "What integrations are available on the Free Plan?"
        anchor: "integrations-free-plan"
        answer: |
          {{ site.data.stitch.subscription-plans.enterprise.trial-description }}

          {% assign all-integrations = site.documents | where:"input", true %}

          {% assign free-integrations = all-integrations | where:"tier","Free" | sort:"title" %}

          After the Free Trial has ended, the integrations in the table below will be available to any plan.

          <table class="attribute-list">
          {% for integration in free-integrations %}

          {% assign index = forloop.index | modulo: 2 %}

          {% if index == 1 %}
          <tr>
          {% endif %}
            <td width="33%; fixed">
              <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.title | remove: "(v1)" | remove: "(v2)" | remove: "(v1.0)" | remove: "(v2.0)" }}</a>
            </td>
          {% case index %}
            {% when 0 %}
              </tr>
            {% else %}
              {% if forloop.last == true %}
                {% case index %}
                  {% when 1 %}
                    <td>
                    </td>
                    </tr>
                {% endcase %}
              {% endif %}
            {% endcase %}
          {% endfor %}
          </table>

      - question: "What integrations are available on a Standard Plan?"
        anchor: "integrations-paid-plan"
        answer: |
          {% assign standard-integrations = all-integrations | where:"tier","Standard" | sort:"title" %}

          After the Free Trial has ended, the integrations in the table below will only be available to Standard and Enterprise Plans. Refer to the [pricing page]({{ site.pricing }}){:target="new"} for a list of current Stitch plans.

          <table class="attribute-list">
          {% for integration in standard-integrations %}

          {% assign index = forloop.index | modulo: 2 %}

          {% if index == 1 %}
          <tr>
          {% endif %}
            <td width="33%; fixed">
              <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.title | remove: "(v1)" | remove: "(v2)" | remove: "(v1.0)" | remove: "(v2.0)" }}</a>
            </td>
          {% case index %}
            {% when 0 %}
              </tr>
            {% else %}
              {% if forloop.last == true %}
                {% case index %}
                  {% when 1 %}
                    <td>
                    </td>
                    </tr>
                {% endcase %}
              {% endif %}
            {% endcase %}
          {% endfor %}
          </table>

      - question: "What integrations are available on an Enterprise Plan?"
        anchor: "integrations-enterprise-plan"
        answer: |
          {% assign enterprise-integrations = all-integrations | where:"tier","Enterprise" | sort:"title" %}

          The integrations in the table below are available only to Enterprise Plans. [Reach out to sales]({{ site.sales }}){:target="new"} for more info.

          <table class="attribute-list">
          {% for integration in enterprise-integrations %}

          {% assign index = forloop.index | modulo: 2 %}

          {% if index == 1 %}
          <tr>
          {% endif %}
            <td width="33%; fixed">
              <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.title | remove: "(v1)" | remove: "(v2)" | remove: "(v1.0)" | remove: "(v2.0)" }}</a>
            </td>
          {% case index %}
            {% when 0 %}
              </tr>
            {% else %}
              {% if forloop.last == true %}
                {% case index %}
                  {% when 1 %}
                    <td>
                    </td>
                    </tr>
                {% endcase %}
              {% endif %}
            {% endcase %}
          {% endfor %}
          </table>

      - question: "Can I use Standard Plan integrations if I'm on the Free plan?"
        anchor: "paid-integrations-free-plan"
        answer: |
          No. To use any of Stitch's Standard Plan integrations, you'll need to [upgrade to a Standard plan]({{ site.pricing }}){:target="new"}.

      - question: "How many integrations can I add?"
        anchor: "how-many-integrations-can-i-add"
        answer: |
          {% include misc/icons.html %}
          The total number of integrations refers to the number of distinct integration types each account may add, dependent upon the selected plan type.

          For example: Accounts using the Free Plan may add up to five different types of integrations. If an account has five Google Analytics integrations connected, this will only count as one towards the integration type quota. Up to four additional types of integrations may still be added.

          <table class="attribute-list">
          <tr>
          <td class="attribute-name">
          <strong>Plan name</strong>
          </td>
          <td>
          <strong>Number of sources</strong>
          </td>
          </tr>
          {% for plan in site.data.stitch.subscription-plans.all-plans %}
          {% if plan.key %}
          {% assign this-plan = site.data.stitch.subscription-plans[plan.key] %}
          {% else %}
          {% assign this-plan = site.data.stitch.subscription-plans[plan.name] %}
          {% endif %}
          <tr>
          <td class="attribute-name">
          <strong>{{ plan.name | capitalize | replace:"-", " " }}</strong>

          {% if this-plan.legacy == true %}
          {{ info-icon | replace:"TOOLTIP","This is a legacy plan and has been replaced by the Standard plan." }}
          {% endif %}
          </td>
          <td>
          {{ this-plan.total-integrations }}
          </td>
          </tr>
          {% endfor %}
          </table>
          <br>

          **Note**: The types of integrations available are also dependent on plan type. Users of the Free Plan will only have access to Free integrations, while Standard Plan users will have access to Free and Standard Plan integrations.

          For more info, refer to the [pricing page]({{ site.pricing }}){:target="new"}.

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

          **Note**: While free historical loads apply to all of Stitch's integrations, you need to be on a Standard plan to use our Standard integrations.

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

      - question: "How can I reduce my row usage?"
        anchor: "reduce-row-usage"
        answer: |
          We recommend [following the simple tips in this guide]({{ link.getting-started.row-usage | prepend: site.baseurl | append: "#reducing-your-usage" }}) to reduce your row usage.

      - question: "Do rows from Free Plan integrations count towards my usage?"
        anchor: "free-integrations-usage"
        answer: |
          Yes. Rows replicated from [free integrations](#integrations-each-plan) will count towards your usage. The "free" in "free plan integration" only indicates that the integration is available on any plan, not that the rows replicated don't count towards your usage.

      - question: "What happens if I use more than the rows allotted in my plan?"
        anchor: "exceed-row-allotment"
        answer: |
          We never want you to lose access to fresh data. So instead of shutting down your data pipeline once you hit your monthly row limit, we will let you know as you approach your limit and you’ll be able to reduce frequency of updates, pause integrations, or upgrade your plan. Plan upgrades happen immediately and you will be charged only for the time remaining in your billing cycle.


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

          **Note**: Some integrations require a Standard Plan after the free trial ends. To continue replicating data from these sources - for example, Salesforce - you'll need to select a Standard Plan after your trial concludes.

      - question: "How can I change my plan?"
        anchor: "change-plan"
        answer: |
          You can change your plan in the **Plan Details** section of the {{ app.page-names.billing }} page, accessed by clicking {{ app.menu-paths.billing }}.

          Click the **Change Your Plan** button and select the plan you want from the window that displays.

      - question: "What happens if I change my plan mid-billing cycle?"
        anchor: "change-plan-mid-cycle"
        answer: |
          This depends on the billing cycle type for the plan.
          
          **For monthly plans**:

          If you're upgrading or downgrading a monthly plan, meaning the new plan has a greater or lower row limit than the current plan, the change will be effective immediately and you will be charged or refunded the difference between the current plan and the new plan.

          In addition, if you're upgrading from the Free Plan to any Standard Plan, you will also have immediate access to Standard integrations.
             
          **For annual plans**:

          - **If you're upgrading**, meaning the new plan has a greater row limit than the current plan, the change will be effective immediately and you will be charged the difference between the current plan and the new plan.

          - **If you're downgrading**, meaning the new plan has a lower row limit than the current plan, the change will take effect at the end of the billing cycle. This ensures that you can take full advantage of the higher row allotment and access to Standard integrations for the remainder of the billing cycle.

# -------------------------- #
# PAYMENT DETAILS & INVOICES #
# -------------------------- #

  - topic: "Manage payment details and invoices"
    anchor: "payment-invoices"
    items:
      - question: "Where do I manage my payment details?"
        anchor: "manage-payment-details"
        answer: |
          {% include note.html type="single-line" content="**Note**: The user who initially enters the payment info is the user who will receive your account's monthly invoice in their email." %}

          You can enter and manage your credit card details in the {{ app.page-names.billing }} page, accessed by clicking {{ app.menu-paths.billing }}.

          When you enter the cardholder's name, **make sure that a valid last name is entered**. Though Stitch does validate these fields, we've seen replication issues arise when the Last Name field is blank.

      - question: "What types of payment does Stitch accept?"
        anchor: "accepted-payment-types"
        answer: |
          Stitch accepts all major credit cards. Additional options are available for Enterprise customers.

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
