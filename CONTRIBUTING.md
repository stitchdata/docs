![Stitch black and white logo](https://www.stitchdata.com/docs/images/stitch-logo.png)

# Contributing

First off, we want to thank you for your interest in contributing to the Stitch Docs. Your contributions and feedback will not only help Stitch provide top-notch docs, they'll also enrich the Stitch community overall.

- [Code of Conduct](#code-of-conduct)
- [Your First Contribution](#your-first-contribution)
- [Suggesting Features and Content](#suggesting-features-and-content)
- [Jekyll](#jekyll)
   - [Install Jekyll](#install-jekyll)
   - [Preview Local Changes](#preview-local-changes)
- [Pull Requests](#pull-requests)
   - [Merge Requirements](#merge-requirements)
   - [CLA](#cla)
- [Stitch Docs Basics](#stitch-docs-basics)
   - [Front Matter](#front-matter)
   - [Content](#content)
   - [Layouts and Where Content Lives](#layouts-and-where-content-lives)
   - [Content Structure and Collections](#content-structure-and-collections)
   - [Includes](#includes)
- [Dependencies and Other Important Things](#dependencies-and-other-important-things)
   - [General](#general)
   - [Templates](#templates)
   - [Internal Links](#internal-links)
   - [The Stitch App: Page Names, Buttons, and Menu Paths](#the-stitch-app-page-names-buttons--menu-paths)
   - [Quirky Things](#quirks)
- [Questions?](#questions)
- [Resources](#resources)

---

# Code of Conduct

Here at Stitch we strive to inspire, empower, and help data-driven people take back control and ownership of their data.

We strongly believe in the concept of DTRT, or Doing The Right Thing. That means creating and maintaining a welcoming, productive, and diverse community where everyone's ideas and contributions are appreciated and respected.

Whether you're submitting your own contribution, commenting on someone else's work, or participating in a Stitch Docs discussion, everyone in the community is expected to abide by our [Code of Conduct][codeofconduct].

---

# Your First Contribution

Want to contribute to the Stitch Docs, but not sure where to start?

- If you're not familiar with git/GitHub:
   - [Check out this git and pull request tutorial](http://makeapullrequest.com/),
   - [Learn your way around the GitHub web app](https://guides.github.com/activities/hello-world/) and [how we handle pull requests](#pull-requests),
   - [Learn GitHub-flavored Markdown][github-markdown].
- **Get a feel for the Stitch Docs.** Check out the [Stitch Docs Basics](#stitch-docs-basics) for an overview of how things work.
- **Try tackling some of these [beginner issues](https://github.com/stitchdata/docs/labels/good%20for%20beginners)**. These are typically typos, small copy additions or removals, adding or fixing links, etc. and are meant to get you comfortable using GitHub and navigating the Stitch Docs.
- **Check out the Stitch Style Guide**. [Coming Soon]

---

# Suggesting Features and Content

Ever find yourself wondering _"The Stitch Docs are awesome. They'd be even _more_ awesome if [awesome idea here]."_? 

You're probably not alone. Our goal is to provide top-quality, comprehensive, useful docs that enable you to get the most out of Stitch. We can only do that if we know what's missing or isn't working.

You can:
- [Open an issue](https://github.com/stitchdata/docs/issues) and describe the feature, content, or improvement you want and why you need it. For features, please include how you expect them to work.
- Submit a [pull request](#pull-requests) with the your suggested changes.

## Please don't submit issues for Stitch support questions. Contact Stitch Support (stitchsupport@talend.com) if you need assistance.

---

# Jekyll

**Note:** If you're unfamiliar with Jekyll, don't want to install it, or are uncomfortable with coding, you can still submit changes. [You can use GitHub in your web browser instead](https://help.github.com/articles/creating-a-pull-request/).

The instructions below assume you're using a Mac, which typically comes with Ruby and RubyGems installed.

Additionally, issues with installing Jekyll dependencies can occasionally arise. If this happens, you may need to also install [Xcode Command-Line Tools from the Apple Store](https://learn.cloudcannon.com/jekyll/install-jekyll-on-os-x/).

## Install Jekyll

1. Download or clone this repo.
2. Open Terminal and navigate to the local location of the repo:

   ```
   cd /Users/folder/docs
   ```

3. Install Jekyll:

   ```
   gem install jekyll
   ```

4. If you don't already have [Bundler](http://bundler.io/) installed, install it now:

   ```
   gem install bundler
   ```

5. Run Bundler to retrieve all the required Gems:

   ```
   bundle install
   ```

6. Build the site:

   ```
   jekyll build
   ```

   If you encounter issues with `jekyll build`, try:

   ```
   bundle exec jekyll build
   ```

## Preview Local Changes

While developing, you can preview your changes by spinning up a local Jekyll server:

```
jekyll serve
```

If you encounter issues with `jekyll serve`, try:

```
bundle exec jekyll serve
```

Then in your web browser, browse to `localhost:4005/docs`

The Jekyll server will watch for changes and regenerate the local site whenever you save a file. You'll need to refresh the page to reflect your changes.

To reduce the time it takes to regenerate the site between individual changes, you can enable incremental watch:

```
bundle exec jekyll serve -iw
```

**Note: Incremental watch will only regenerate files where direct changes are made**. For example: if a new SaaS integration is added to `_saas-integrations`, you'll be able to navigate to that integration's specific page but it won't show up on the [SaaS integrations category page](https://www.stitchdata.com/docs/integrations/saas).

---

# Pull Requests

1. Create a new feature branch off of `master` to work in. If you're using GitHub's UI, [these instructions will show you how to do this](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/).
   
   **Note**: All changes must be in their own branch, no matter how small. Please do not commit directly to `master`.
2. As you work, commit changes in logical chunks. When writing commit messages, please:
   - Provide a short summary. For example: `Add new troubleshooting section to sidenav`
   - Provide additional detail that explains the change, if necessary. For example:
      
      ```
      This adds a new troubleshooting section for extraction errors to the sidenav. 
      This replaces the "error notifications" category.
      ```
3. Open a pull request with a clear title and description. **If you're working from an existing issue**, please reference it on the pull request.
5. **Optional**: If you aren't using Jekyll to work, use Netlify's deploy preview to check out your changes on a preview site. Every time a new commit is added to a pull request, Netlify will re-generate the preview site.

   Open the deploy preview by scrolling to the **Checks** section on the pull request page, clicking **Show all checks**, then **Details**:
   
   ![Opening Netlify pull request deploy preview](https://www.stitchdata.com/docs/images/guide-resources/netlify-deploy-preview.gif)
6. When finished working, apply the **Ready for Review** label to your pull request. Generally, pull requests will be evaluated within one week.
7. That's it! :tada:

## Merge Requirements

Pull requests will only be merged into `master` by Stitch if:

- They are associated with a signed CLA (see below),
- They have an approved review from a maintainer,
- There are no requested changes, and
- The branch is up-to-date with `master`

## CLA

Before your pull request can be merged, you'll need to submit a completed Contributor License Agreement (CLA) to Stitch.

Our reason for having a CLA is to define the rights of the contributors — Stitches and non-Stitches alike - and avoid potential confusion and misunderstandings. We believe in DTRT, or Doing The Right Thing. For this project, that means:

- Ensuring all contributors are equal, and
- The rights to contributions used by the community cannot be withheld or revoked

Shortly after you open a pull request, you should receive an email from Stitch containing a link to the CLA. Click the link, complete the form, read the CLA, then click **I agree**. You won't be asked to sign the CLA again unless we make a change.

Stitch will not merge a pull request made against the Stitch Docs project until it is associated with a signed CLA.

---

# Stitch Docs Basics

The only requirement to creating content for the Stitch Docs is familiarity with [Markdown][github-markdown].

That being said, there are a few things to keep in mind when perusing the content files in this repo:

1. Content files are made up of two parts: [Front Matter](#frontmatter) and [content](#content).
2. Depending on the **layout** used by the particular file you're looking at, the content itself may be either in the page's Front Matter or in the content section. More on this in a moment.

To simplify contributing, templates for each type of content have been added to the `_templates` folder. See [Templates](#templates) for more info.

## Front Matter

[Front Matter](http://jekyllrb.com/docs/frontmatter/) is the first section of any content file. In this section, you can set predefined variables or create some of your own. These variables are used in layout templates, in content across the page (or site), etc.

Front Matter is contained within two sets of triple-dashed lines at the top of the file:

```
---
title: HubSpot
permalink: /integrations/saas/hubspot
layout: singer                                // this defines the layout template the page uses
                                              // corresponding layout file is in /_layouts
---
```

Important things to note:

1. For Jekyll to 'detect' the file, the file must contain both sets of dashes. Otherwise, the file won't be generated when the site is built.
2. Variables are optional.
3. Front Matter uses a language called [YAML](http://yaml.org). YAML is extremely powerful and enables you to do some really cool things. You can create what are essentially structured data files: depending on how the data is structured, you can loop through it to generate content, apply conditional logic to "query" the data and display the results, create references, and more. [More info is here in the Jekyll documentation](http://jekyllrb.com/docs/frontmatter/).
4. While YAML is extremely powerful, it's also extremely picky. [YAML has specific rules around spacing](http://www.yaml.org/spec/1.2/spec.html#Basic) that, when not observed, will cause errors and prevent the site from generating. If you don't space your YAML correctly, you're gonna have a bad time.

## Content

Everything after the second set of dashes is the 'content' section of the file.

```
---
title: HubSpot
...
---

Page content goes here.
```

## Layouts and Where Content Lives

Some layouts require that certain pieces of page content be in defined sections of a page's Front Matter. Because Front Matter data must conform to a certain structure, it's perfect for reducing repetition, cleaning up cluttered formatting code, and ensuring consistency across similar content files. In this case, content files that all use the same layout template.

For example: Every FAQ article uses a layout template called `faq`. Instead of doing something like the following and constantly (and manually) repeating formatting code in the content section:

```
## billing-faq.md:
   ---
   title: Billing FAQ
   permalink: /account-security/billing-faq
   ---

   ## How does Stitch billing work?

   Plans are based on the volume of rows and events replicated per month.

   ## Where can I find more info about Stitch plans?

   Detailed info on each of Stitch's plan can be found on our pricing page: stitchdata.com/pricing
```

The `faq` layout can be applied, which will loop through defined variables in the page's Front Matter and apply formatting appropriately. Separating the majority of formatting from the content makes the resulting code easier to read and more [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```
## _account-security/billing-faq.md:
   ---
   title: Billing FAQ
   permalink: /account-security/billing-faq
   layout: faq                                  // the faq layout is applied

   frequently-asked-questions:
     - question "How does Stitch billing work?"
       answer: |
         Plans are based on the volume of rows and events replicated per month.

     - question: "Where can I find more info about Stitch plans?"
       answer: |
         Detailed info on each of Stitch's plan can be found on our pricing page: stitchdata.com/pricing
   ---

   Some additional content.                      // any content after the Front Matter is placed
                                                 // in the {{ content }} variable in the layout



## /_layouts/faq.html:

  {% for faq in page.frequently-asked-questions %}
    <h2>{{ faq.question }}</h2>

    {{ faq.answer | markdownify }}              // the markdownify filter ensures that any Markdown 
                                                // is processed as Markdown and not as HTML
  {% endfor %}


  {{ content }}                                // anything after the page's Front Matter section
                                               // will display here
   
   
## Output (/account-security/billing-faq.html):

<h2>How does Stitch billing work?</h2>
<p>Plans are based on the volume of rows and events replicated per month.</p>

<h2>Where can I find more info about Stitch plans?</h2>
<p>Detailed info on each of Stitch's plan can be found on our pricing page: stitchdata.com/pricing</p>

```

**Note**: Content can still live in the section after a page's Front Matter, even if the layout applied is using the above approach. You can see where the content in this section will display by referring to the corresponding [layout template](https://github.com/stitchdata/docs/tree/master/_layouts) for the page being worked on and locating the `{{ content }}` variable.

## Content Structure and Collections

This site uses [Jekyll collections](http://jekyllrb.com/docs/collections/) to structure the majority of content.

The output control and default settings for collections like layout, sidebar, and so on are maintained in `_config.yml`:

```
## _config.yml:

collections:                               // everything listed under this variable is a valid collection
  saas-integrations:                       // the name of the collection. corresponds to a folder in /docs, e.g. /docs/_saas-integrations
   output: true                            // indicates if pages for the collection should be rendered in the site output


defaults:                                  // controls the default settings for collections
  - scope:
      type: saas-integrations              // the collection
    values:
      layout: page                         // the default layout the collection uses
      sidebar: stitchnav                   // the default sidenav the collection uses
      display-summary: "false"             // indicates if the value of page.summary displays for the collection
      toc: false                           // indicates if a table of contents displays for the collection
```

## Includes

[Includes are files that can be used in other files](https://jekyllrb.com/docs/includes/). This allows content to be single-sourced, meaning that a single piece of content can be re-used anywhere but only needs to be updated in one place.

In the Stitch Docs, includes are used to control parts of the layout, re-use and adapt pieces of content for setup guides, re-use changeable pieces of formatting code, and so on.

Include files are stored in the `_includes` folder at the root of the `/docs` directory. In content files, includes are called using the `include` tag followed by the file's location within the `_includes` folder:

```
{% include note.html %}                               // file location is _includes/note.html

{% include shared/whitelist-stitch-ips.html %}       // file location is _includes/shared/whitelist-stitch-ips.html
```

For example: If you needed to include instructions for whitelisting Stitch's IP addresses in a setup guide, you could do this:

```
## _includes/shared/whitelist-stitch-ips.html:

For the connection to be successful, you'll need to configure your firewall to allow access from our IP addresses. Whitelist the following IPs before continuing onto the next step:

{% for ip-address in ip-addresses %}
- {{ ip-address.ip }}
{% endfor %}


## some-file.html:

{% include shared/whitelist-stitch-ips.html %}


## Output:

For the connection to be successful, you'll need to configure your firewall to allow access from our IP addresses. Whitelist the following IPs before continuing onto the next step:

- Stitch IP address 1
- Stitch IP address 2
...

```

If you needed to make a change to this copy, you'd need to change the include file (`_includes/shared/whitelist-stitch-ips.html`), not the file where it's referenced.

### Callout Boxes and Include Parameters

Some includes - like those for callout boxes - allow you to pass a `content` parameter to the include. This allows you to use the formatting code in the include while passing it situation-specific copy.

```
{% include note.html content="If you're not using an SSH tunnel, skip this step." %}
```

The value of `content` (`If you're not using an SSH tunnel, skip this step.`) will be inserted into the `{{ include.content }}` parameter of the include file.

If you need to include a Liquid variable (like `{{ site.stitch-support }}`) in the `content` parameter, you'll first need to `{% capture %}` the copy and then assign it to the `content` parameter. For example:

```
{% capture contact-support %}
For assistance, contact [Stitch Support](mailto: {{site.stitch-support }}).
{% endcapture %}


{% include note.html content=contact-support %}
```

---

# Dependencies and Other Important Things

## General

- The Stitch Docs site uses **Jekyll v3.6.2**. Information about the other gems used can be found in the site's [`GEMFILE`](). Versions of gems are in [`GEMFILE.lock`](https://github.com/stitchdata/docs/blob/master/Gemfile.lock).
- The Stitch Docs site uses [Kramdown][kramdown] to render Markdown.
- The layout for the Stitch Docs site is based on a Jekyll theme created by Tom Johnson. For an in-depth look at the other features this theme includes, [refer to the Jekyll Documentation Theme][documentation-theme].
- Files generated from building the site will be placed in `_site`. The files in this folder are overwritten every time a build occurs.

## Templates

A basic template for each of the site's categories (ex: SaaS integrations, destinations, etc) are in the `_templates` folder. These templates contain the necessary [Front Matter variables](#frontmatter) for that category, allowing you to get started quickly.

1. Create a copy of the template you want and save it in that category's folder. For example: if creating an **account-focused** article, save a copy of the `account-or-billing-template.md` template in the `_account-security` folder.
2. Follow the instructions for filling out the Front Matter section. Don't worry - everything you need is in the template.
3. Write your content.
4. That's it! :tada:


## Internal Links

A few important things to know about internal links:

1. All **internal** links must include `site.baseurl` or the link will not work. For example:

   ```
   [Getting Started Guide]({{ site.baseurl }}/getting-started)
   ```

2. Dynamic linking (meaning all links to a page will update if that page's location changes) isn't possible in Jekyll.

   To get around this, you can create links by using the values in `_data/urls.yaml`. Every article in the site will have its permalink value added to this file, along with a unique ID.

   For example: the code below would output a link to the Replication Frequency article:

   ```
   ## _data/urls.yaml:
   
   replication:
     rep-frequency: /replication/replication-frequency
   
   
   ## some-file.md:
   
   [Replication Frequency]({{ site.data.urls.replication.rep-frequency | prepend: site.baseurl }})
   
   
   ## Output:
   
   [Replication Frequency](/docs/replication/replication-frequency)
   ```

3. It's also possible to shorten links to make them easier to read and remember. To simplify the variables, include `misc/data-files.html` just after the page's Front Matter. This will assign `link` to `site.data.urls`, thus shortening the variable:

   ```
   ## /includes/misc/data-files.html:
   
   {% assign link = site.data.urls %}               // site.data.urls corresponds to the _data/urls.yaml file
   
   
   ## some-file.md:
   
   {% include misc/data-files.html %}
   
   [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }})
   
   
   ## Output:
   
   [Replication Frequency](/docs/replication/replication-frequency)
   ```

   **Detailed instructions for doing this are in the [`urls.yaml`](https://github.com/stitchdata/docs/blob/master/_data/urls.yaml) file.**


## The Stitch App: Page Names, Buttons, & Menu Paths

Named components of the Stitch app - the copy on buttons, for example - are stored in `_data/app.yml`. Just like `_data/urls.yaml`, the `app.yml` file contains key and value pairs for page names, buttons, and menu paths in the Stitch app.

This not only makes keeping up with UI changes easier, it also means a variable can output strings or blocks of content and speed up the writing process.

For example:

```
## _data/app.yml:

menu-paths:
  account-settings: "User menu (your icon) > Manage Account Settings"
  add-user: "In the Team Members section, click Add a Team Member.
    

## _account-security/managing-team-members.md:

  1. To add a new user, click the {{ site.data.app.menu-paths.account-settings }}.
  2. {{ site.data.app.menu-paths.add-user }}
  ...
     
     
## Output (account-security/managing-team-members.md):

  1. To add a new user, click the User menu (your icon) > Manage Account Settings.
  2. In the Team Members section, click Add a Team Member.
  ...
```

To simplify the variables, include `misc/data-files.html` just after the page's Front Matter. This will assign `app` to `site.data.app`, thus shortening the variable:

```
## /includes/misc/data-files.html:

{% assign app = site.data.app %}               // site.data.app corresponds to the _data/app.yml file


## _account-security/managing-team-members:

{% include misc/data-files.html %}

  1. To add a new user, click the {{ app.menu-paths.account-settings }}.
  2. {{ app.menu-paths.add-user }}
  ...
```

## Quirks

- You can mix Markdown and HTML in Markdown files. If you use HTML, the HTML code in its entirety must be flush left. Jekyll will otherwise literally interpret the HTML as code and generate codeblocks.
- Without the `flatify` filter, Liquid variables used inside of Front Matter will only render as a string without calling the variable value. For example:

   ```
   ## _config.yml:

   stitch-site: https://www.stitchdata.com


   ## _saas-integrations/intercom.md:
   
   ---
   title: Intercom
   summary: |
     [Stitch's]({{ site.stitch-site }}) Intercom integration.
   ---

   {{ page.summary }}

   {{ page.summary | flatify }}
   ```

  Output:

  ```
  ## Without flatify:
     [Stitch's]({{ site.stitch-site }}) Intercom integration.

  ## With flatify:
     [Stitch's](https://www.stitchdata.com) Intercom integration.
  ```

---

# Questions?

If something wasn't covered, feel free to submit a pull request with your suggestions or reach out to Erin, the Stitch Technical Documentation Manager (@erinkcochran87)

---

# Resources

- [Jekyll Documentation](http://jekyllrb.com)
- [Jekyll Talk](https://talk.jekyllrb.com/): Community forum for all-things Jekyll.
- [Jekyll Theme Documentation][documentation-theme]: Documentation for much of the site's theme, created by [Tom Johnson](http://idratherbewriting.com/).
- [Shopify Liquid Reference](https://help.shopify.com/themes/liquid)
- [Kramdown Markdown Quick Reference][kramdown]


[codeofconduct]: https://github.com/stitchdata/docs/blob/master/CODE_OF_CONDUCT.md
[documentation-theme]: http://idratherbewriting.com/documentation-theme-jekyll/
[github-markdown]: https://guides.github.com/features/mastering-markdown/
[kramdown]: https://kramdown.gettalong.org/quickref.html
