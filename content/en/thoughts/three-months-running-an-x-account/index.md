---
date: 2026-09-10T12:00:00+08:00
draft: false
title: After Three Months of Running an X Account, I Studied the Recommendation Algorithm Again
description: After three months of observing, publishing, and reviewing results, I have a more practical understanding of X recommendations, content distribution, and account growth.
categories:
  - Thoughts
tags:
  - X
  - Content Strategy
  - Recommendation Algorithms
  - Indie Development
---

![](https://images.indexflowing.com/Gemini_Generated_Image_qtdofrqtdofrqtdo.jpg)

I have been seriously running an X account for about three months.

Throughout those three months, I kept coming back to one question:

**Why do some accounts with relatively few followers get extremely high impressions on a single post, while accounts with many followers struggle to get their content recommended?**

At first, like many people, I focused on the visible numbers: likes, reposts, and follower count.

But recently, after studying X's public recommendation algorithm again and observing two completely different accounts, I realized that things may not be so simple.

So this is not an “X growth tutorial.”

It is my current understanding after putting together **three months of firsthand observation, X's public recommendation algorithm, and a comparison of two real accounts**.

Let me start with the conclusion.

## 1. First: Let X Know Who You Are

This is what I currently consider the most important point.

X first published part of its recommendation algorithm's source code in 2023. In 2026, it published an updated **X For You Feed Algorithm**, the core code that directly powers recommendations in the For You feed today.

After actually reading through it, I noticed something important:

**X does not simply look at how many likes a post has and then decide how much exposure to give it.**

It first needs to understand:

> **Who is this user? What does this user usually care about? What kind of content will this user interact with? Who might this post be suitable for?**

In the recommendation code now available publicly, Phoenix reads a user's recent behavioral history and predicts what the user might do after seeing a particular post.

Those actions include:

- Liking
- Replying
- Reposting
- Quoting
- Clicking the post
- Visiting the profile
- Expanding an image
- Watching a video
- Time spent
- Following the author
- Negative actions such as marking content as not interested, blocking, or reporting it

The system then combines these predictions to rank posts.

This made me rethink a basic question:

**What an account is is not decided by what you say it is. X infers it from your ongoing behavior.**

What you post.

Who you interact with.

Which posts you reply to.

Who you follow.

Whether other people interact with you.

Over time, all of this helps the system understand your interests and the territory your content belongs to.

So if you want to build a long-term account, I am no longer particularly concerned about whether I should add [#buildinpublic](https://x.com/search?q=%23buildinpublic&src=hashtag_click) to every post.

What I care more about is:

**Do my most recent few dozen original posts consistently tell X what kind of person I am?**

For example, what I am doing now is:

> Indie development + open source + AI tools + building in public

My content should stay within this general territory over time.

That does not mean every post must stay perfectly on topic.

But if more than 70% of the content stays in this direction, the remaining 30% can be personal thoughts, daily life, or complaints, and the account will still be fairly clear.

I increasingly believe that:

**Account positioning is not the sentence in your bio. It is the content you consistently publish and the interactions you consistently create.**

## 2. Second: Interaction Quality Matters Much More Than Likes Alone

This is where my thinking changed the most after studying the algorithm.

I used to naturally assume:

> More likes -> a more popular post -> X keeps recommending it.

But the public recommendation mechanism is not that simple.

X's publicly documented Phoenix recommendation model predicts the probability of many different actions a user may take on a post, rather than looking only at a single “like count.”

So as someone running an account, I now pay more attention to this:

**After users see my post, do they actually do anything?**

Likes certainly have value.

But replies, quotes, clicks, image expansions, video views, time spent, and later visits to your profile or follows may all be more meaningful user signals.

That is why, when I run my account now, I spend more of my time on:

**My own replies section > the replies sections of unfamiliar people in the same niche > meaningless likes**

When someone leaves a thoughtful reply under one of my posts, I try to respond thoughtfully as well.

Because this is not just about being polite.

It means a post changes from:

> I published something

into:

> I published something -> someone became interested -> they left a reply -> I responded -> a real conversation formed

That is a completely different interaction structure from a few dozen people simply tapping Like.

So the principle I use is simple:

**Replying to the right people matters more than replying to more people.**

## 3. Comparing Two Accounts

Studying the algorithm is one thing.

What really confirmed these ideas for me was observing two completely different accounts.

One is [@xupaopaogm](https://x.com/@xupaopaogm).

The other is [@cgnot996](https://x.com/@cgnot996).

Their content styles, audience structures, and account positioning are very different.

### Xu Paopao

Xu Paopao has one especially obvious characteristic:

**His content makes it easy for people to stop scrolling.**

Much of it does not require users to understand a complicated technical background first. It can immediately create curiosity, controversy, or discussion.

So users will:

> See it -> stop -> comment -> argue -> quote -> keep reading the replies -> watch the author respond

From the perspective of the recommendation algorithm, this is fascinating.

The public model is predicting these very behaviors.

So I no longer explain it simply as:

> “His posts get lots of likes, so X promotes him.”

A more accurate explanation would be:

> **His content is very good at triggering a sequence of connected user actions.**

That is what I think is really worth studying.

As an aside, Xu Paopao recently did not pass a creator earnings review on the first attempt.

But I do not think that event proves anything about a long-term pattern.

The result of the next review could be completely different.

So what I care about is not whether “this account can monetize,” but:

**Why can his content consistently generate so much user activity?**

### Tiezhu AGI

Tiezhu AGI represents a completely different model.

The account is not especially large, with a few thousand followers, but its content is highly focused:

**Grok, AI, Codex, developer tools, open-source projects, and product practice.**

Many of its original posts are not designed to create controversy. They directly show:

- Products
- Features
- Screenshots
- User experience
- Technical information
- Price comparisons
- Practical use of AI tools

Yet some of these original, product-focused posts still achieve extremely high impressions.

This made me notice an important distinction:

**Follower count does not directly determine how much recommendation an account's content can receive.**

A small account with a few thousand followers can still repeatedly receive recommendations beyond its own followers if its content is highly relevant to a clearly defined group of people.

And X's public algorithm does have mechanisms for this:

For You does not only find posts from people you follow. Through mechanisms such as Phoenix and SimClusters, it also looks for potentially relevant content from accounts you do not follow.

Looking at these two accounts together made X's recommendation logic easier for me to understand.

One account can earn recommendations through **strong user behavior**.

Another can earn recommendations through **a very clear match between content and audience**.

Their formats are completely different.

But underneath, both point to the same question:

**What kind of content are you providing to X, and can X find people who may be interested in it?**

## 4. So My Understanding of Account Positioning Has Changed

I used to think account positioning meant:

> Make it clear in your bio who you are.

Now I think that is far from enough.

True positioning should be:

> **Let X continually determine who you are through your content and interactions.**

So if I were starting an X account again today, I would not begin by chasing a large number of followers.

I would start with one thing:

**Make the account clear enough.**

For example:

- Main direction: indie development
- Secondary directions: open source / AI tools / building in public

Then I would keep publishing.

The benefit is that when a post performs well, I want X to find:

**People who are genuinely interested in indie development, AI, and open source.**

Not a random group of people just to inflate the numbers.

## 5. Mutual Follows Are Fine, but I Will Not Treat Them as a Growth Model

My attitude toward mutual follows has changed too.

When starting from zero, I think it is fine to find 20 to 50 genuinely active people whose content direction matches yours.

You need to build an initial network of relationships.

And if those people are genuinely interested in your content, their replies, quotes, and reposts are normal user behavior in their own right.

But if it becomes:

> Follow 500 people today
> 
> Wait for 500 people to follow back tomorrow
> 
> Then like one another's posts

I think the value is very limited.

What you really need to build is not a “mutual-follow list.”

It is:

**A relationship network that is highly relevant to the direction of your content.**

So my current understanding is:

> **Mutual follows are a cold-start tool, not a growth model.**

## 6. Communities Can Help, but Do Not Turn Them into Engagement Farms

I may use communities for this too, but very cautiously.

If the people in a community already use X and genuinely care about AI, indie development, open source, and products, it can help a new account get its first batch of real interactions.

But if the rules become:

> Whenever anyone posts, everyone must like, comment, and repost.

Then it is something completely different.

I would rather think of a community as:

**A place to accelerate the first wave of real interactions.**

Not:

**A place to manufacture fake metrics.**

The content itself is still the most important thing.

# Finally, Here Is What I Will Do Next

After studying the algorithm and observing these two accounts, I have set myself a very simple operating plan.

**First, keep the positioning clear.**

Indie development + open source + AI + building in public.

**Second, publish fewer original posts, but make them more thoughtful.**

I would rather publish one to three pieces of content with real substance each day than a dozen worthless posts.

**Third, replies carry a lot of weight.**

After studying X's recommendation mechanism, I realized that replies are not merely “engagement data.” They are important signals of user behavior.

So instead of chasing likes alone, I will value real replies and conversations more:

> **My own replies section > the replies sections of unfamiliar people in the same niche > meaningless likes**

**Replying to the right people matters more than replying to more people.**

**Fourth, do not put external links in original posts.**

In X's algorithm, **external links in an original post can affect its recommendations, so if my goal is to gain followers, I will put the link in a reply instead.**

I will first keep users on X to read and interact. When a link is necessary, I will put it in the replies.

**Fifth, do not expect every post to go viral.**

What I really want is for X to become increasingly clear about:

> Who is Zhang Sanfeng?
>
> What does he mainly do?
>
> What kind of people will like his content?

If these answers become clearer and clearer, I believe long-term account growth will start to become more predictable.

That is the most important conclusion I have reached after studying X's recommendation algorithm for three months:

**Running an X account is not just about finding ways to get more exposure for one post.**

**It is about continuously telling X who you are, what you are doing, and what kind of people should see your content.**

I am [@indexflowing](https://x.com/@indexflowing), an indie developer.

I currently focus on indie development, AI, open source, and building in public.

I have open-sourced two projects: AgentBridge and IndexFlow-core.

This article marks the beginning of my systematic approach to running X.

Next, I will continue practicing this approach and publicly recording the results.
