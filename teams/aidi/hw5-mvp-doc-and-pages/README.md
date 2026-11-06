# HW 5 MVP Document and Pages

## Table of Contents

- [Overview](#overview)
- [Repository Directory](#repository-directory)
- [Homepage and Landing Pages](#homepage-and-landing-pages)
- [Deployment Status](#deployment-status)
- [Results](#results)

## Overview

This folder contains Aplovia's MVP product brief and the homepage and landing-page plan developed for HW 5. Aplovia is a bilingual college-planning product for international high-school students applying for first-year admission to U.S. undergraduate programs. The pages describe the broader product vision, distinguish it from the smaller working MVP, and test three research-backed value propositions: personal fit, financial feasibility, and trustworthy college information.

## Repository Directory

| File | Description |
|---|---|
| [MVP Product Brief](./mvp_doc.md) | Defines the current MVP, later product direction, cut and Wizard of Oz work, technical stack, success measure, risks, and named team responsibilities. |

## Homepage and Landing Pages

The four public marketing routes are deployed on Render Singapore. The deployment exposes only the homepage and three value-proposition landing pages; the working MVP product routes remain unavailable in this public marketing build.

| Page | Production URL | Audience | Value proposition |
|---|---|---|---|
| Homepage | [https://aplovia-frontend.onrender.com/](https://aplovia-frontend.onrender.com/) | International high-school students applying for first-year admission to U.S. undergraduate programs, especially students who lack experienced family or counselor support and do not know where to begin | Aplovia helps students find colleges that fit their preferences, financial situation, and academic background, then build a clearer and more trustworthy path from college research to application planning. |
| College Fit Landing Page | [https://aplovia-frontend.onrender.com/fit](https://aplovia-frontend.onrender.com/fit) | International students who rely on rankings because they are unsure what kind of college suits them or how to translate their priorities into a college search | Students can choose the location, campus setting, school type, and other factors that matter to them, apply those requirements consistently, and verify the details instead of receiving another generic ranking list. |
| Affordability Landing Page | [https://aplovia-frontend.onrender.com/affordability](https://aplovia-frontend.onrender.com/affordability) | International students and families who need to understand whether a college may be financially realistic before spending time and money on an application | Students can compare their family's maximum annual contribution with an official annual cost estimate and review international financial-aid policies separately, without treating aid as guaranteed. |
| Trust Landing Page | [https://aplovia-frontend.onrender.com/trust](https://aplovia-frontend.onrender.com/trust) | International students who find college information scattered across websites and third-party sources and are uncertain whether summaries are current, complete, or trustworthy | Aplovia organizes important college information while keeping the original source, data year, link, and last-checked date visible so students can verify consequential facts themselves. |

Each page includes a waitlist call to action. The homepage collects an email address, user identity, current college-process challenge, and optional interest in testing the prototype. Each focused landing page collects an email address and optional testing interest. The waitlist does not collect grades, test scores, family budget, or product preferences.

## Deployment Status

Aplovia is deployed on Render using three Singapore resources: a React Web Service, a Django Web Service, and PostgreSQL.

The deployment was verified through the public homepage and all three landing-page routes, direct route refreshes, English and Simplified Chinese switching, Django health and database-readiness endpoints, and end-to-end waitlist submissions. Repeated submissions with the same email retained one contact, created separate page-level attribution records, and incremented the submission count for each page as designed.

## Results

The completed and deployed work translates the interview and synthesis findings into four testable demand pages. The homepage communicates Aplovia's complete product direction and the smaller feature set already implemented. The three landing pages each isolate one student problem and value proposition, use research language and current product screenshots, and invite visitors to join the waitlist or volunteer for prototype testing. The public Render deployment now provides working URLs for demand testing while keeping unfinished MVP product routes private.
