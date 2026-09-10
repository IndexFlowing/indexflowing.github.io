---
date: 2026-09-10
draft: false
title: "Why I Built IndexFlow-core: From a Google Indexing Crisis to Open-Source Infrastructure"
description: "A real website's problems with Google crawling, indexing, and visibility led me to build IndexFlow-core, an open-source foundation for managing and verifying search engine indexing."
categories:
  - Open Source
tags:
  - IndexFlow-core
  - Open Source
  - SEO
  - Google
  - Search Indexing
  - Rust
  - Indie Development
---

![The starting point for IndexFlow-core](https://images.indexflowing.com/Gemini_Generated_Image_ggxko4ggxko4ggxk.jpg)

This project did not start with the idea that I wanted to build an SEO tool.

It started with a real website incident and a question that kept bothering me afterward: **How do I know whether a URL has actually been understood, crawled, and indexed correctly by a search engine?**

## A Website That Seemed to Be Doing Well

In mid-to-late June, I launched an AI-built resource website. It had a large number of URLs and multiple language versions, so I knew from the beginning that search traffic would be important.

At first, everything looked good. Google could crawl the pages and gradually began indexing them. By early July, Google's reported crawl budget briefly reached roughly 120,000 requests per day. For an independent project that had only recently launched, this was exciting: at least the search engine was discovering and visiting the site.

Then the problems began.

## It Started With Cloudflare Workers 500 Errors

I eventually discovered that the site was running into Cloudflare Workers' 50 ms CPU time limit. Some requests could not finish within that limit and resulted in a large number of 500 errors.

This was not just an ordinary runtime problem. Search engines were seeing error pages, and URLs that should have been reliably accessible became unstable. Crawl budget, server responses, and page availability began affecting one another.

I migrated the site to a server to solve the stability problem first. The server did remove the Workers limitation, but it introduced another problem: maintaining a separated frontend and backend was complicated. Fixing one issue often meant checking the API, rendering, deployment, and the relationship between pages in different languages at the same time.

![The migration and maintenance problems behind the project](https://images.indexflowing.com/why-i-built-indexflow-core.jpg)

During that migration and maintenance period, Google's indexing and the site's visibility fell off a cliff, eventually getting close to zero.

## I Thought Google Had Penalized the Site

When a site's crawling and visibility suddenly drop to zero, it is easy to reach for a simple explanation.

Had Google penalized it? Had it been banned? Had some content triggered a sandbox? Were AI-built websites simply not trusted?

I spent a lot of time studying SEO, Google Search Console data, crawl behavior, indexing status, and every possible cause. There was no immediate answer that made me feel better, because **a page being accessible, Google having crawled it, and the page appearing in search results are three different things.**

This was the point I kept coming back to:

> **Being crawled does not mean being indexed. Being indexed does not mean getting visibility.**

If you only look at server logs and see that Googlebot visited a URL, you may assume that the URL has completed its SEO journey. In reality, the page may have returned an error, failed a quality check, not yet been added to the index, or been indexed without earning meaningful rankings.

## What I Really Lacked Was Continuous Verification

Before this experience, I checked the site through a collection of separate tools: I checked whether the sitemap had been generated, opened pages to confirm their content, queried URLs manually in Search Console, and submitted URLs when necessary.

None of those actions was difficult on its own, but they did not form a continuous verification chain. I needed a tool that could answer questions such as:

- Which URLs are in the sitemap, and do they currently meet expectations?
- Does a URL meet basic SEO quality requirements?
- What does Google Search Console say about a URL's indexing status?
- Has a URL been submitted to Google, Bing, or IndexNow?
- When will a URL crawled by Google actually enter the index?

That was when I started building **IndexFlow-core**.

## What Is IndexFlow-core?

IndexFlow-core is an **open-source foundation for search engine indexing**.

It is not about how to write a title for one page, and it does not promise that one trick will make a website rank higher. It focuses on a more basic and often overlooked layer: continuously managing URLs, verifying their SEO status, understanding search engine feedback, and submitting pages when necessary.

Its five core capabilities currently include the following.

### 1. Sitemap and URL Management

Treating a website's URLs as objects that can be managed and checked, rather than treating the sitemap as an XML file generated as a side effect of deployment. This makes it easier to understand which URLs should be discovered and which ones need further investigation.

### 2. SEO Quality Gate

Running SEO quality checks before a URL enters the next stage of the indexing workflow. The goal is to catch problems with basic page information and indexability early, instead of sending obviously incomplete or unexpected URLs directly to search engines.

### 3. Google Search Console Indexing Checks

Using Google Search Console to query a URL's indexing status and distinguish between “I believe this page is live” and “Google's actual assessment of this URL.” This turns indexing problems from guesses into states that can be tracked over time.

### 4. URL Submission to Google, Bing, and IndexNow

Providing URL submission capabilities for different search engines, including Google, Bing, and IndexNow. Submission is not a guarantee of indexing, but it gives a site a more direct way to notify search engines when there is a meaningful update or a reason to request attention.

### 5. URL Indexing Monitor

The recently added **URL Indexing Monitor** came from a capability I realized I badly needed while continuing to use the project. It continuously monitors URL indexing status and helps determine when a page is actually indexed, rather than merely recording when it was crawled or submitted.

![tools image](https://images.indexflowing.com/why-i-built-indexflow-core-2.jpg)

## Why Add a URL Indexing Monitor?

Recently, Google's crawling gradually recovered to roughly 3,000 requests per day. At first glance, that was good news: Google was visiting the site again.

But this time I did not treat the crawl volume as a success signal. I already knew that **crawling and indexing are not the same thing**.

When Google requests a URL, that only tells us that the URL was discovered and visited. We still need to verify whether it passed quality checks, entered the index, and later gained visibility in search results. Without monitoring, it is easy to stop the investigation too early at “Googlebot came by.”

That is why I added the URL Indexing Monitor to IndexFlow-core. It is not intended to create more data for its own sake. It fills in one of the most important gaps in the indexing workflow: observing what happens between “crawled” and “actually indexed.”

## Why Open Source?

IndexFlow-core came from a real problem I had to solve. I experienced 500 errors, migration and maintenance complexity, and the uncertainty that came with indexing and visibility dropping close to zero.

I am still using it, and I am still iterating on its features based on data and problems from real websites. To me, it is not a project that is finished once and then abandoned. It is infrastructure that will continue changing as websites and search engine behavior change.

Because it first served a real workflow, I want to open it up so that people who manage large numbers of URLs and care about SEO quality and search engine indexing can use it, provide feedback, and improve it together.

I will continue iterating on IndexFlow-core around URL visibility, indexing status, and verification workflows. The project began with a Google indexing crisis, but it is ultimately trying to solve a longer-term problem: **instead of guessing whether a search engine understands a website correctly, we should be able to verify it continuously.**
