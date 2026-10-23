# ClientReady vs. Strata — team decision brief

October 9, 2026. AI-assisted assessment for team discussion, not a recorded team vote. This supplements the interview synthesis; it does not replace the missing pre-AI Part A.

**Recommendation: prioritize a one-week ClientReady field test. Keep Strata as a conditional alternative if the team can access a real document-pipeline owner, an approved sample and a measured baseline. Neither idea has demonstrated willingness to pay.**

The recommendation concerns what the team can learn next, not which company has the larger eventual market. Existing ClientReady design work is a sunk cost, not evidence of demand. Team engineering strengths, professional customer access and available time have not been established well enough to score founder fit.

## Compare the actual concepts

The team's Homework 2.2 document defines ClientReady as a page-oriented content brief for small web studios, and Strata as quality-aware document routing for engineers responsible for processing cost. Strata is not simply a PDF reader or a generic OCR app. A review-focused extraction tool would be a revised hypothesis, not validation of the original cost-saving one.

| Decision factor | ClientReady | Strata | Implication now |
|---|---|---|---|
| Strongest interview evidence | CR02 reports inconsistent contribution depth; CR05 receives a long document and images that still need selection and page placement. | ST02 checks table values, years and units; ST03 verifies blurry scans; ST04 adds OCR after scan extraction fails. | Both address real work. The exact proposed solution remains untested. |
| Fit with original buyer | All five interviews concern student work or unpaid favors. Paid studios are not represented by these interviews. | Students and one task-level RA do not represent a production pipeline's budget owner. ST03 does not know institutional spending. | Both need better recruitment. Strata especially lacks evidence about its central cost claim. |
| Boundaries and weak fits | CR01 is mainly waiting; CR03 has little collection trouble; CR04 needs changed facts kept current. | ST01 has occasional low-intensity friction; ST05 primarily reads PDFs. | Do not call all five in either set target customers. Different tasks need different solutions. |
| Candidate payer | A recurring website builder or studio could pay for less preparation and clarification work. This is a hypothesis. | A pipeline-owning engineer or team could pay for measured net savings at acceptable quality. This is a hypothesis. | Ask decision-makers about actual work and budgets, not only students whether the idea sounds useful. |
| First test | Use an existing document and images; manually produce a section brief, page/asset mapping and unresolved-question list. | Benchmark one document type against the customer's current extraction method, including quality, cost and correction work. | ClientReady can test its main workflow before building software. Strata needs a representative dataset and evaluation definition. |
| Main technical uncertainty | Preserving facts, asking useful gap questions, assigning material sensibly and exporting something the builder accepts. | Choosing when a cheap route is adequate, detecting silent errors, evaluating tables, and integrating reliably. | A routing demo is easy to overvalue; a quality-preserving routing policy needs measurement. |
| Adoption risk | Contributors may ignore another form; a shared document or conversation may already be enough. Builder savings must not simply transfer effort to the contributor. | Integration, approval to use documents, ongoing maintenance and human review can erase model-call savings. | Measure all participants' effort and the full workflow. |
| Differentiation | Generic collection, templates, reminders, guest access and AI-generated questions overlap with Content Snare. | Native-text/OCR fallback exists in Unstructured; LlamaParse already offers page-level cost optimization. | Neither has an established moat. Test an advantage in a specific workflow, not novelty of a feature list. |
| Reach and recurrence | Builders with current client projects are a plausible recruitment route; actual access and repeat frequency remain unproven. Occasional student events may not support a subscription. | Access to recurring paid document workloads is unproven. Repeated processing could create usage revenue if net value is demonstrated. | A larger theoretical budget is not the same as an accessible buyer. |

Interview sources: [all notes and snapshots](evidence/README.md); [full interview synthesis](synthesis_comparison.md). The statements above retain the supplied notes' limits: no recorded interview dates, no isolated time measurements and no confirmed payments.

## What the Reddit research changes

The local review covers 148 distinct discovery post bodies and 20 selected saved comment threads. It adds professional website-work context, including preparation labor, scope disagreements and client participation constraints. These are self-reported public accounts, not interviews or trial commitments. See [research summary](reddit_research/reddit_research_summary.md) and [coverage](reddit_research/coverage.md).

This research was deliberately about ClientReady. Strata has no equivalent Reddit corpus here, so the extra ClientReady volume is not evidence that Strata has a smaller market. Search selection also favors problem discussions. Crossposts of the same story do not become independent validation.

One particularly relevant counterexample is a freelancer who has already tried collection tools and sees client time as the central issue: [regular client delays](https://www.reddit.com/r/freelance/comments/1o7f187/regular_client_delays_causing_project_backlog/). This reinforces CR01's warning: better organization cannot guarantee participation. A highly specific page-mapping comment in [the redesign thread](https://www.reddit.com/r/web_design/comments/1wfwk38/what_steps_should_i_take_to_professionally/) discloses that its author builds a planning tool; treat it as a competitor's perspective, not independent customer validation.

## Current alternatives checked

- **Content Snare:** its official tour describes sectioned requests, reusable templates, AI-assisted question creation, no-login client participation, reminders and approval handling. Those features cannot by themselves be ClientReady's unique claim. We have not run a usability comparison. [Official tour](https://contentsnare.com/tour/), checked October 9, 2026.
- **Unstructured:** official documentation describes automatic selection between text extraction and OCR, plus other processing strategies. Simple fallback is already available. [PDF partitioning documentation](https://docs.unstructured.io/open-source/core-functionality/partitioning#partition-pdf), checked October 9, 2026.
- **LlamaParse:** its official documentation describes Cost Optimizer routing simple pages to a cheaper tier and complex pages to a premium tier. Strata would need an advantage beyond proposing this architecture. Vendor claims are not a benchmark on the team's documents. [Parse overview](https://developers.llamaindex.ai/llamaparse/parse/), checked October 9, 2026.

These are targeted checks, not an exhaustive competitor review. They establish overlap; they do not prove a competitor completely solves either problem.

## A narrower ClientReady test

Target someone building a small client website who already has some source material but cannot use it directly. The proposed outcome is **a human-confirmed content pack organized by page**, not another storage location or a promise to make an unresponsive client act.

Use an agreed page list, the existing text/images, short questions only where information is insufficient, and a final pack containing section text, linked assets, source references and unresolved decisions. Keep editorial suggestions separate from supplied business facts. Test the brief inside the existing shared-document workflow first. A separate application needs evidence that it improves that workflow.

For the next week, aim for three qualifying builders and two active projects. These are proposed recruitment and trial targets, not completed results. Include at least one contributor in each trial; builder enthusiasm alone misses half the adoption problem.

1. Ask for the last actual content handoff: what arrived, what needed work, who did it, how many clarification exchanges occurred, and what they tried already.
2. On two small live projects, agree on what “usable” means before helping. Observe their usual process on comparable sections where feasible; record the differences when a clean comparison is impossible.
3. Deliver the first pack manually and log builder time, contributor time, the team's own preparation time, clarification rounds and factual corrections. Separate working time from calendar time spent waiting.
4. Ask the builder to use the result in the actual site and identify what still needs repair. Then offer a clearly scoped second project at a stated price. Homework 2.2's $49/project is one existing untested offer, not validated pricing. Record behavior: refusal, scheduled trial, paid commitment or actual reuse.

**Proposed continuation gate:** both builders use the pack in real work; the complete workflow shows useful time or clarification improvement without extra factual errors; and at least one makes a concrete second-project or paid-pilot commitment. These small-sample gates guide the team's next step, not a statistical market-validation claim. If a short shared template achieves the same result, retain it as a template or service until there is a reason to build a separate product. If nonresponse dominates, do not add more reminders and call the hypothesis confirmed.

## What would make Strata the better choice?

Strata becomes a stronger next experiment if a teammate can introduce a pipeline owner with recurring volume, documented current processing costs, an approved representative sample and an explicit quality requirement. That access would be more valuable than more general student opinions about PDFs.

Start with one document family and approximately 50–100 permissioned pages, chosen to include ordinary and difficult cases. This is a proposed feasibility sample, not enough to establish production reliability. Define the actual task: for example correct numeric cells with units and source pages, rather than whether extracted text “looks good.” Keep a separate holdout, compare with the customer's current pipeline and a relevant existing alternative, and report failures by document type.

Measure total extraction/compute cost, retries, latency, human correction and integration effort. A useful business calculation is: **avoided processing and review cost minus new processing, review, integration, maintenance and product fees**. Fewer paid model calls alone do not establish savings. Page citations and uncertainty indicators might help review, but the team must test whether they reduce missed errors and correction time; their presence is not a quality guarantee.

**Proposed continuation gate:** a real owner can evaluate and adopt the result; a held-out sample meets the agreed task-quality requirement; and meaningful net savings survive review and integration costs. Without this access, pause broad router development. If the team instead chooses an accuracy/review product, explicitly write and test that new hypothesis.

## Decision to record together

Decide the next experiment, who recruits the buyer, who measures the baseline, and when the evidence will be reviewed. Do not let an already-made logo decide the product. On the evidence available today, ClientReady offers the clearer short path to a real workflow test; Strata remains viable if the team brings stronger customer access and a credible benchmark.
