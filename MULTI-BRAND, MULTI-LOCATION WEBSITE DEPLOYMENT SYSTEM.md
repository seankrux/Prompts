**MULTI-BRAND, MULTI-LOCATION WEBSITE DEPLOYMENT SYSTEM**

**MISSION STATEMENT**

Design, develop, and deploy a scalable infrastructure where each independent brand receives a unique, fully-optimized multi-location website (GitHub repo + Vercel instance) with SEO mastery, conversion-focused design, and premium professional aesthetics across all digital properties.

**ROLE DEFINITION**

**Executor**: Full-stack development team with expertise in React, Next.js, Vercel deployment, SEO architecture, UI/UX design, content strategy, and local business optimization. Assumed capability: ability to audit existing GMB profiles, extract brand signals, implement schema markup, optimize images, and execute complex internal linking strategies.

**ORGANIZATIONAL STRUCTURE**

Element

Specification

**GitHub Organization**

merlinomarketing

**Repository Naming**

[brand-name]-[location-count]loc (e.g., premiere-plumbing-chicago-3loc)

**Deployment Platform**

Vercel (merlinomarketing workspace)

**Tech Stack**

React 18+, Next.js 14+, TypeScript, TailwindCSS, Framer Motion, [__schema.org__](http://schema.org), next-seo

**Repository Structure Per Brand**

/public (images), /pages (routing), /components (reusable), /content (blog/copy), /styles (brand kit), /lib (SEO utilities)

**BRAND KIT DEVELOPMENT (MANDATORY FIRST STEP)**

**Pre-Development Audit**

	•	Extract existing brand signals from GMB URLs (logo treatments, color language, service categories)

	•	Cross-reference all deployed brands in merlinomarketing to prevent pattern duplication

	•	Document color palettes, typography, imagery style, and visual hierarchy for each new brand

**Brand Kit Components (Per Website)**

	•	**Primary Color Palette**: 3 primary colors + 5 accent shades (no duplicates across existing brands)

	•	**Typography Stack**: 2 font pairings maximum (no font reuse across brands)

	•	**Design System**: Glassmorphism treatment, shadow depth scale, border-radius consistency, interactive hover states

	•	**Imagery DNA**: Subject matter (e.g., actual plumbers at work), shot style (natural lighting, authentic), color grading, aspect ratio standards

	•	**Logo Integration**: Placement rules, sizing, spacing, monochrome variants

**WEBSITE ARCHITECTURE**

**Multi-Location Website (3+ Locations)**

domain.com/

├── / (homepage - brand overview + service summary)

├── /locations/

│   ├── [location-slug-1]/ (full landing page)

│   ├── [location-slug-2]/ (full landing page)

│   └── [location-slug-3]/ (full landing page)

├── /services/

│   ├── service-1/

│   ├── service-2/

│   ├── ... (10 total)

│   └── service-10/

├── /blog/

├── /about/

├── /contact/

├── /privacy-policy/

├── /terms-of-service/

└── /sitemap.xml, /robots.txt, /llms.txt

**Single-Location Website (1 Location)**

domain.com/

├── / (homepage with embedded GMB listing + hero + form)

├── /services/

│   ├── service-1/ through service-10/

├── /blog/

├── /about/

├── /contact/

├── /privacy-policy/

├── /terms-of-service/

└── [All technical files as above]

**LOCATION LANDING PAGE SPECIFICATION**

**Mandatory Structure**

Section

Requirements

**Above Fold (0-100vh)**

Geotagged hero image (1920×1080px), location name + service keyword in H1, 2 primary pain points, CTA form (name/email/phone), location proximity indicator

**Trust Signals Section**

Brand certifications, local service seals, partner logos (non-competitor), review count, avg rating

**Service Overview**

3-4 service highlights relevant to location + service type, with icons aligned to brand color palette

**Location-Specific Content**

500-750 words addressing: service availability in [Location], local expertise, service area coverage, local testimonials

**FAQ Section**

8-12 questions pulled from Google People Also Ask for "[service] in [location]" - format as JSON-LD FAQ schema

**Brand POV Section**

200-300 words on brand philosophy/approach to service, unique methodology

**GeoJSON Embed**

Interactive map with GMB listing, service area radius, multi-location selector (if applicable)

**Supporting Pages (5 per location)**

/locations/[location]/faq, /locations/[location]/process, /locations/[location]/gallery, /locations/[location]/service-guarantee, /locations/[location]/why-choose-us

**Form Section (CTA)**

Persistent, sticky, or end-of-page conversion form with field validation, honeypot spam protection

**IMAGE ASSET REQUIREMENTS**

**Geotagging & Sourcing**

	•	**Source**: Original photography or licensed stock from location-specific services (NOT generic stock photos)

	•	**Geotag Metadata**: EXIF coordinates within 5 miles of GMB location address

	•	**Resolution**: 1920×1080 (hero), 800×600 (service cards), 400×400 (testimonial profiles)

	•	**File Naming**: [location]-[service]-[descriptor]-[date].webp (e.g., chicago-plumbing-leak-repair-2024.webp)

	•	**Alt Text Format**: [Service] services in [Location] - [Brand Name] | [specific action/outcome] (55-75 chars max)

**Cross-Brand Image Uniqueness**

	•	Zero image reuse across any brand websites

	•	Audit existing brand repositories before sourcing

	•	Create visual distinction through color grading, perspective, and subject variation

	•	Document image inventory in /public/image-manifest.json with hash values to prevent accidental duplication

**CONTENT SPECIFICATIONS**

**Per-Brand Content Requirements**

Content Type

Quantity

Optimization Standards

**Blog Posts (General)**

20 posts

2,000-2,500 words each; target informational keywords supporting service pages; internal linking to 2-3 service pages per post; LSI keyword integration

**Location Blog Posts**

10 per location (linked from location landing pages)

1,500-1,800 words; geo-specific keyword variants (e.g., "best plumber in Chicago" vs. "best plumber in Aurora"); link to corresponding location landing page + 2 service pages

**Service Pages (10 per brand)**

10 pages

1,200-1,600 words; problem→solution→CTA arc; internal links to 3-4 blog posts; location landing page links if multi-location

**FAQ Content**

8-12 per location

Sourced from Google People Also Ask (gtmetrix, SEMrush PAA tool); structured as [__schema.org/FAQPage__](http://schema.org/FAQPage); Q = 40-70 chars, A = 150-200 words

**Homepage Copy**

1 page

800-1,200 words; brand positioning + service overview + trust indicators + form

**Content Quality Standards**

	•	**Tone**: Professional, trustworthy, service-focused (not salesy; avoid hyperbole)

	•	**EEAT Alignment**: Demonstrate expertise (service methodology), experience (case studies/testimonials), authoritativeness (credentials/certifications), trustworthiness (privacy/security/guarantees)

	•	**AI Search Optimization**: Include entity relationships (Brand + Location + Service), avoid AI-detection red flags (over-optimization, unnatural density), natural topical coverage

	•	**Audience Intent Mapping**: Match content to search intent (Do = service pages; Know = blog; Local = location pages)

**SEO & TECHNICAL SPECIFICATIONS**

**Metadata Per Page (Mandatory)**

Element

Specification

**Meta Title**

55-66 characters; format: [Service] in [Location] | [Brand Name] or [Brand Name] - Professional [Service]

**Meta Description**

155-160 characters; include primary keyword, location (if applicable), CTA verb (Get, Call, Learn, Discover)

**OG Graph Tags**

og:title, og:description, og:image (1200×630px), og:url, og:type, og:locale

**Twitter Card**

twitter:card (summary_large_image), twitter:title, twitter:description, twitter:image

**Canonical Tag**

Self-referential on all pages; use absolute URLs

**Robots Meta**

index, follow (all public pages); noindex for support pages, 404s, duplicate content

**Schema Markup (Mandatory Implementation)**

Required schemas per page type:

- Homepage: Organization, LocalBusiness (if single location), BreadcrumbList

- Location Page: LocalBusiness, AggregateRating, BreadcrumbList, FAQPage

- Service Page: BreadcrumbList, FAQPage, Service (custom schema)

- Blog Post: BlogPosting, BreadcrumbList, Author, datePublished, dateModified

- Contact Page: ContactPoint, LocalBusiness

**Technical Files (Auto-Generated)**

	•	**robots.txt**: Allow all public paths; disallow /admin, /private, /cdn-cgi; specify Sitemap location

	•	**sitemap.xml**: Include all public pages; prioritize location pages (0.9), service pages (0.8), blog (0.7); update on each deploy

	•	**llms.txt**: Declare content ownership, usage rights, training restrictions; disallow LLM scraping on sensitive pages

	•	**security.txt**: Link to privacy policy, contact for security issues

**Performance & Core Web Vitals**

Metric

Target

**LCP (Largest Contentful Paint)**

&lt;2.5s (mobile), &lt;1.5s (desktop)

**FID (First Input Delay)**

&lt;100ms

**CLS (Cumulative Layout Shift)**

&lt;0.1

**TTFB (Time to First Byte)**

&lt;600ms

**Overall Lighthouse Score**

≥90 (all pages)

**Optimization Tactics**:

	•	Image optimization: WebP format, lazy loading, responsive sizes attribute

	•	Code splitting: Route-based splitting with Next.js dynamic imports

	•	Font loading: system fonts for headlines; single variable font for body (WOFF2 only)

	•	Caching: Static generation (SSG) for service/blog pages; ISR for location pages (revalidate every 24 hours)

	•	Minification: Enable Vercel's built-in compression

	•	Third-party script deferral: Load analytics/tracking asynchronously after core content

**DESIGN SYSTEM & UI STANDARDS**

**Design Direction (Non-Negotiable)**

	•	**Theme**: Light-only (no dark mode; all backgrounds white or near-white; text dark gray #1a1a1a or brand primary)

	•	**Aesthetic**: Modern, sophisticated, premium (conveys $500K+ value in appearance)

	•	**Component Language**: Glassmorphism (semi-transparent overlays with backdrop blur), smooth micro-animations, staggered entrance animations

	•	**Visual Hierarchy**: Bold primary headline (32-48px on desktop, 24-32px mobile); clear CTA prominence; ample whitespace (minimum 2rem gutters)

	•	**Color Usage**: Brand primary color as accent; secondary for CTAs; tertiary for backgrounds/borders; grayscale for supporting text

	•	**No Prohibited Elements**: Zero cartoons, anime, emoji characters, cutesy illustrations, or non-professional imagery

**Interactive Elements**

	•	**Hover States**: Subtle color shift (10-15% darker) + 2-3px vertical shift or scale 1.02

	•	**Scroll Animations**: Fade-in + slide-up (200-300ms duration) on section reveals; parallax on hero images (10-15px offset)

	•	**Form Interactions**: Real-time validation feedback (green checkmark, red error text); input focus state with border color change + shadow

	•	**Navigation**: Smooth scroll behavior; active state indicator on current page; mobile: hamburger menu with overlay (no slide-out drawer)

**Responsive Breakpoints**

	•	**Mobile**: 320px-767px (default stacking; 1-column layout)

	•	**Tablet**: 768px-1023px (2-column cards; adjusted spacing)

	•	**Desktop**: 1024px+ (3-4 column grids; full sidebar layouts)

**CONVERSION RATE OPTIMIZATION (CRO)**

**Form Specifications**

	•	**Field Count**: Name, email, phone, service dropdown (optional), location selector (if multi-location), message (optional)

	•	**Submission Flow**: Client-side validation → Vercel serverless function → email notification + auto-responder

	•	**Anti-Spam**: Honeypot field, CAPTCHA (optional), rate limiting (1 submission per IP per 60 seconds)

	•	**Post-Submission**: Redirect to thank-you page OR modal with next steps

**CTA Optimization**

	•	**Button Copy**: Action-focused verbs ("Get Free Quote", "Schedule Consultation", "Call Now", "Claim Your Service"); 40-60 chars

	•	**Button Color**: Brand primary or contrasting color with min 4.5:1 contrast ratio against background

	•	**Button Placement**: Above fold (primary), end of each major section (secondary), sticky footer on mobile (tertiary)

**Content Alignment to Intent**

	•	**Awareness Stage**: Blog content, educational pages, brand story

	•	**Consideration Stage**: Service comparison, location landing pages, FAQ, testimonials

	•	**Decision Stage**: Form placement, pricing (if applicable), guarantee section, final CTA

**DEPLOYMENT & MONITORING**

**Git & Vercel Workflow**

	•	**Branch Strategy**: main (production), staging (preview), feature/[name] (development)

	•	**Deployment**: Auto-deploy on merge to main; preview deployments on all PRs

	•	**Environment Variables**: Store API keys, analytics IDs in Vercel dashboard (not in code)

	•	**Domain Management**: Point custom domain to Vercel in DNS settings; set up SSL/TLS auto-renewal

**Monitoring & Maintenance**

	•	**Analytics Integration**: Google Analytics 4 (track form submissions, page engagement); Google Search Console (monitor indexing, errors)

	•	**Uptime Monitoring**: Vercel's built-in monitoring; set up alerts for failed deployments

	•	**SEO Audits**: Monthly crawl with Screaming Frog; quarterly backlink analysis

	•	**Content Calendar**: Update blog monthly; refresh location landing pages every 6 months; monitor and respond to reviews

**VALIDATION CHECKLIST (Per Website Deployment)**

	☐	GitHub repository created under merlinomarketing with correct naming convention

	☐	Vercel project deployed with custom domain routing correctly configured

	☐	Brand kit finalized (colors, fonts, imagery style) and documented in /brand-guidelines.md

	☐	All 10 service pages published with complete metadata, schema, and internal links

	☐	All location landing pages deployed (if multi-location) with geotagged images and GMB embed

	☐	Supporting pages created for each location (/5 pages per location)

	☐	20 general blog posts published with strategic internal linking

	☐	10 location-specific blog posts per location published and linked to location pages

	☐	All images WebP-formatted, geotagged, alt-texted, and verified for uniqueness across brand portfolio

	☐	Meta titles/descriptions audited for length and keyword inclusion

	☐	Schema markup validated using Google Structured Data Testing Tool

	☐	robots.txt and sitemap.xml generated and submitted to Google Search Console

	☐	Core Web Vitals targets met (LCP &lt;2.5s, CLS &lt;0.1) via Vercel Analytics

	☐	Lighthouse audit ≥90 across all pages (desktop and mobile)

	☐	Form submissions tested end-to-end (validation, email delivery, thank-you page)

	☐	Mobile responsiveness tested on 5+ device sizes

	☐	No prohibited design elements (cartoons, dark themes, emojis) present

	☐	Brand consistency verified across all pages and components

	☐	Cross-brand image duplicate audit passed (no images shared across brands)

	☐	SEO competitor benchmarking completed (title structure, word count, content gaps)

	☐	Final client review and approval before subdomain handoff

**QUALITY GATES (HARD STOPS)**

**Deployment blocked if:**

	•	Any brand website shares design patterns, fonts, color palettes, or imagery with existing merlinomarketing brands

	•	Any page fails LCP or CLS targets

	•	Form submission fails in production

	•	Meta descriptions exceed 160 characters or fall below 155

	•	Images lack proper geotagging or alt text

	•	Dark colors, cartoons, or prohibited design elements present

	•	Internal linking between service pages and blog posts incomplete (&lt;30% coverage)

	•	Location pages missing FAQ sections or brand POV sections

	•	Duplicate content detected across pages (&gt;30% text overlap)

	•	Canonical tags missing or pointing to wrong URL

**EXECUTION SEQUENCE (Per Brand)**

	1.	**Audit Phase** (Days 1-2): Extract GMB signals, audit existing brands for pattern avoidance, define brand positioning

	2.	**Brand Kit** (Days 3-4): Design system, color palette, typography, imagery guidelines

	3.	**Architecture** (Days 5-7): Repository setup, folder structure, component library, page templates

	4.	**Core Pages** (Days 8-14): Build homepage, service pages (10), essential pages (contact, privacy, TOS, about)

	5.	**Location Pages** (Days 15-21): Location landing pages + 5 supporting pages per location; GMB embeds; image sourcing

	6.	**Content** (Days 22-30): 20 blog posts + location blog posts (10 per location); FAQ extraction; internal linking

	7.	**SEO & Technical** (Days 31-35): Meta tags, schema, robots.txt, sitemap, llms.txt; Search Console submission

	8.	**Optimization** (Days 36-40): Core Web Vitals tuning, image optimization, form testing, cross-brand audit

	9.	**QA & Validation** (Days 41-45): Full checklist, bug fixes, final review, client approval

	10.	**Deployment & Handoff** (Day 46): Production deploy, DNS configuration, monitoring setup, documentation

---

Notes: if a brand already have a website you will know this because its on clickup, or it will exist in github repo merlinomarketing org (or seankrux account - this is the old repo). So if thats true then just make use of the repo and append to it, any existing design and contnt from that repo you will fix accordingly if needed to align with the istructions.

 now i want u to run this lock n load and start
working on the clickup items that has been tagged as
no website/needs website - as you go you will update
property fields inclikcup real time to reflect current
data. Git hub url and vercel deploys. any actions and
completions you will drop a comment log in the
respective clickup item as Sean (me). The final
completion of this would be completing all tasks end
to end once that is completed u will then prompt me
for final review, and u will set click up status per
item as "for review" status (if not yet created u will
create that status). u will use /autonomouis kill to
run this. launch 100 teams agent to help u. u have
30mins... utilize all codex and qwen swarms  

---

blog content for each brand website

domain/blog/title

do a kw research for the brand, service and location, and develop content plan to cover expetise and auhtority in its niche.

30 blog posts per brand website to cover google EEAT, and PAA relevant to the service and location.

optimize each with internal links, siloing,schema.
- lastly create 4 supporting pages per each of the 10 services paages ([domain.com/service/supportingpage1](https://domain.com/service/supportingpage1))
- another set of 4 support pages in location landing pages if brand website is multilocation (domain.com/location/chicago/supportingpage)

additional pages (not blogs)