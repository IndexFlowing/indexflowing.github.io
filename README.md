# IndexFlowing 博客内容规范

本文用于规范 IndexFlowing 博客的文章分类、标签、文件命名和视觉资源。

以后写新文章时，按照本文规则执行即可。

------

## 一、文章分类

IndexFlowing 目前只使用以下五个一级分类：

1. Products
2. Engineering
3. Growth
4. Thoughts
5. Open Source

**原则：不要随意创建新的一级分类。**

------

## 二、五个分类分别代表什么

### 1. Products —— 产品

用于介绍、分析、使用和构建产品。

适合的内容：

- 产品介绍
- 产品功能
- 产品使用教程
- 产品设计
- 产品定位
- 产品解决的问题
- 产品开发过程中的产品决策
- 产品之间的比较
- 产品使用案例

判断标准：

> **这篇文章主要是在讲“我做了什么产品、产品解决什么问题、产品怎么使用”？**

例如：

```yaml
categories:
  - Products
```

可以使用的标签：

```yaml
tags:
  - MandarinClips
  - IndexFlow
  - 产品设计
  - AI
  - SaaS
```

------

### 2. Engineering —— 工程

用于技术实现和工程实践。

适合的内容：

- Rust
- Go
- Hugo
- MCP
- AI Coding
- 软件架构
- 数据库
- API
- Docker
- Cloudflare
- 性能优化
- 工程实践
- Bug 排查
- 技术选型
- 系统设计

判断标准：

> **这篇文章主要是在讲“这个东西是怎么实现的”？**

例如：

```yaml
categories:
  - Engineering
```

可以使用的标签：

```yaml
tags:
  - Rust
  - MCP
  - Hugo
  - Docker
  - PostgreSQL
  - 软件架构
```

------

### 3. Growth —— 增长

用于网站流量、SEO、GEO、营销、推广和用户增长。

适合的内容：

- SEO
- GEO
- Google
- 搜索引擎收录
- Sitemap
- IndexNow
- 内容营销
- X
- Hacker News
- Reddit
- 外链
- 流量增长
- 用户增长
- 独立开发推广
- 产品分发
- 增长实验

判断标准：

> **这篇文章主要是在讲“怎么让更多人发现我的产品或网站”？**

例如：

```yaml
categories:
  - Growth
```

可以使用的标签：

```yaml
tags:
  - SEO
  - GEO
  - Google
  - 搜索引擎
  - 增长
  - 营销
  - 独立开发
```

------

### 4. Thoughts —— 思考

用于个人观点、经验、反思和独立开发过程中的思考。

适合的内容：

- 为什么开始做一个产品
- 独立开发经验
- 产品思考
- 开发过程中的感悟
- 失败经验
- 做错的事情
- AI 带来的变化
- 对行业的观察
- 商业上的思考
- 技术之外的个人判断

判断标准：

> **这篇文章主要是在讲“我从这件事情中学到了什么、想到了什么”？**

例如：

```yaml
categories:
  - Thoughts
```

可以使用的标签：

```yaml
tags:
  - 独立开发
  - 产品思考
  - AI
  - 经验
  - 失败经验
```

------

### 5. Open Source —— 开源

用于开源项目、GitHub 项目、开源发布和开源经验。

适合的内容：

- 开源项目介绍
- GitHub 项目
- Release
- 开源项目架构
- 开源项目开发
- 开源项目维护
- GitHub 社区
- 开源贡献
- Rust Crate
- MCP 开源项目
- 开源项目推广
- 开源经验

判断标准：

> **这篇文章主要是在讲“我开源了什么、如何维护开源项目、开源过程中发生了什么”？**

例如：

```yaml
categories:
  - Open Source
```

可以使用的标签：

```yaml
tags:
  - Open Source
  - GitHub
  - Rust
  - MCP
  - AgentBridge
  - IndexFlow-core
```

------

# 三、Category 和 Tag 的区别

这是最重要的规则之一。

## Category 是“文章属于什么类型”

一篇文章原则上只选择一个主要 Category。

例如：

```yaml
categories:
  - Engineering
```

## Tag 是“这篇文章具体讲了什么”

一篇文章可以有多个 Tag。

例如：

```yaml
tags:
  - Rust
  - MCP
  - AI Coding
  - AgentBridge
```

------

## 错误写法

不要把所有关键词都放进 Category：

```yaml
categories:
  - Engineering
  - Rust
  - MCP
  - AI
  - Docker
```

## 正确写法

```yaml
categories:
  - Engineering

tags:
  - Rust
  - MCP
  - AI
  - Docker
```

简单理解：

> **Category 是栏目。**
>
> **Tag 是关键词。**

------

# 四、如果一篇文章同时符合多个分类怎么办？

这是很正常的。

例如一篇文章：

> 我使用 Rust + PostgreSQL 构建了一个 SEO 工具，并分享这个工具如何获得用户。

它同时涉及：

- Products
- Engineering
- Growth
- Open Source

但是不能因此创建四个 Category。

应该看：

> **这篇文章最主要想解决什么问题？**

如果重点是技术实现：

```yaml
categories:
  - Engineering
```

如果重点是产品：

```yaml
categories:
  - Products
```

如果重点是 SEO / 获客：

```yaml
categories:
  - Growth
```

如果重点是开源项目：

```yaml
categories:
  - Open Source
```

剩下的内容通过 Tag 表达。

------

# 五、最简单的五分类判断方法

以后写文章时，只需要问自己五个问题。

```text
Products
↓
我在讲什么产品？

Engineering
↓
我是怎么把它做出来的？

Growth
↓
我是怎么让别人发现它的？

Thoughts
↓
我从这件事情中想到了什么？

Open Source
↓
我开源了什么，或者从开源中学到了什么？
```

如果还是无法判断：

> **看文章标题和文章最核心的问题。**

不要根据文章里面出现了多少技术名词来决定 Category。

------

# 六、文章文件命名

文件名禁止使用空格。

正确：

```text
how-to-build-an-mcp-server.md
```

错误：

```text
how to build an mcp server.md
```

推荐使用：

```text
小写英文 + 连字符
```

例如：

```text
how-to-learn-mandarin-faster.md
seo-indexing-guide.md
building-an-mcp-server-with-rust.md
why-i-started-building-indexflow.md
```

------

# 七、Hugo 文章目录

文章使用 Hugo Page Bundle。

例如：

```text
content/
├── en/
│   └── products/
│       └── article-name/
│           └── index.md
│
└── zh/
    └── products/
        └── article-name/
            └── index.md
```

英文和中文文章尽可能保持对应关系。

------

# 八、文章视觉资源

文章不是必须有图片。

原则：

> **有必要才添加视觉资源。**

不要为了“每篇文章必须有几张图”而强行添加图片。

一篇文章可能：

```text
0 张图
```

也可能：

```text
1 张 Hero 图
```

也可能：

```text
1 张 Hero 图
+
1 张流程图
+
1 张架构图
```

具体根据文章内容决定。

------

# 九、不同视觉资源的使用方式

## 1. SVG / 技术图

SVG 适合：

- 流程图
- 架构图
- 数据流
- 学习路径
- 决策树
- 对比矩阵
- 技术流程

特点：

> **信息必须准确。**

例如：

```text
用户
 ↓
API
 ↓
Rust
 ↓
PostgreSQL
 ↓
搜索
```

这种图不应该依赖 AI 随机生成。

可以使用：

- SVG
- Mermaid
- 程序生成
- HTML/CSS
- 截图

------

## 2. WebP / 概念图片

WebP 更适合：

- Hero 图
- 概念图
- Editorial 图片
- 产品概念
- 氛围图
- 抽象视觉

例如：

> 为什么我要做 IndexFlow？

这种文章可以使用一张具有独立开发者氛围的 Hero 图。

------

## 3. Screenshot / 截图

如果文章需要展示真实产品：

> **优先使用真实截图。**

例如：

- GitHub
- Search Console
- IndexFlow
- AgentBridge
- Hugo
- Dashboard

不要用 AI 图片伪造真实产品界面。

------

# 十、不同 Category 推荐的视觉方式

## Products

优先：

- Hero
- 产品概念图
- 产品流程图
- 产品截图
- 功能对比
- 使用流程

目标：

> 让读者理解产品是什么，以及它解决什么问题。

------

## Engineering

优先：

- 架构图
- 数据流
- 技术流程
- Pipeline
- 系统结构
- API 流程

优先使用：

> SVG / Mermaid / 程序生成图

因为技术信息需要准确。

------

## Growth

优先：

- SEO 流程
- GEO 流程
- 流量漏斗
- 增长循环
- 内容分发流程
- 数据图表

目标：

> 让读者看懂增长机制。

------

## Thoughts

少使用图。

优先：

- Hero
- Editorial
- 概念视觉

重点是文章本身，而不是信息图。

------

## Open Source

优先：

- 项目架构
- Repository 结构
- Release 流程
- Contribution 流程
- 项目截图
- 开源生态图

目标：

> 让开发者快速理解项目。

------

# 十一、视觉资源的核心原则

永远遵循：

```text
有用
 ↓
相关
 ↓
美观
 ↓
数量
```

而不是：

```text
数量
 ↓
美观
 ↓
相关
 ↓
有用
```

**不要为了 SEO 或文章长度而堆图片。**

------

# 十二、最终发布检查

写完一篇文章以后检查：

### 内容

-  是否只有一个核心问题？
-  是否选择了正确的 Category？
-  Tag 是否描述具体主题？
-  Title 是否清晰？
-  Description 是否准确？
-  文件名是否没有空格？
-  中英文文章结构是否对应？

### Category

-  产品 → Products
-  技术实现 → Engineering
-  SEO / GEO / 营销 / 增长 → Growth
-  个人观点 / 经验 / 思考 → Thoughts
-  开源项目 / GitHub / 开源经验 → Open Source

### Visual

-  图片是否真的有帮助？
-  技术图是否准确？
-  概念图是否适合使用 WebP？
-  真实产品是否使用真实截图？
-  是否可以复用已有视觉资源？
-  是否因为“必须有图片”而添加了无意义图片？

------

# 十三、最重要的一条

以后写文章，不要先想：

> “这篇文章应该放哪个分类？”

而应该先想：

> **“我到底想回答读者什么问题？”**

然后根据这个问题选择分类。

```text
我在介绍一个产品
→ Products

我在解释怎么实现
→ Engineering

我在研究怎么获得流量
→ Growth

我在分享自己的思考
→ Thoughts

我在介绍或维护开源项目
→ Open Source
```

这五个分类就是 IndexFlowing 的长期内容骨架。

**不要轻易增加新的一级分类。**
