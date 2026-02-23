# Data Modelling

In this workshop you will...

- Compare Auction House data models with a peer
- Construct new conceptual and logical models using a different scenario.

## Learning Objectives

- Compare and contrast data models
- Construct conceptual models that can be understood by stakeholders and used to build logical models
- Construct logical models that generate further questions about the conceptual model

## Part 1: Comparing Models

In this first part, we'll look back at the Auction House exercise as a cohort.

## Part 2: Building new Models

In this second part, you'll again work in pairs, this time to build some new models.

### The Scenario

You're working as a data engineer for a company who is building a system to be used by conveyancing solicitors.

#### Jaspreet Ruiz-Wickham

You ask Jaspreet, a solicitor at Connie's Conveyancing Co., to describe her work and she says...

"I’m the hub that moves a property from offer to ownership while keeping risk down and everyone aligned. A typical file starts when I receive the memorandum of sale: I verify the client’s ID and source of funds, open a matter, and review the seller’s contract pack (title, plan, protocol forms, fixtures list, lease/management info if leasehold). I order searches—local authority, water & drainage, environmental, sometimes mining/chancel—and compare everything with the title to spot gaps or red flags. I raise enquiries with the seller’s solicitor, track replies, and keep the client and any broker or agent updated in plain English. In parallel I check the mortgage offer and special conditions, then produce a report on title that explains what the client is buying and what to watch for. On exchange I agree dates, handle deposit funds, and sort signatures; before completion I prepare statements, apportion ground rent/service charge or council tax, give undertakings to redeem the seller’s mortgage, and coordinate the money movements. Completion day is calls and confirmations until keys are released; afterwards I file the SDLT return, register the new owner and any charge at HM Land Registry, and close the matter. A typical day mixes reviewing search results, drafting reports, chasing replies, reconciling client accounts, and answering client questions."

<br>
<details>
<summary>Glossary of Conveyancing Terms</summary>
<p>
<ul>
<li><strong>Memorandum of Sale</strong> — One-page summary from the agent confirming buyer, seller, price, and solicitors.</li>
<li><strong>Matter</strong> — The internal case file for a client/instruction.</li>
<li><strong>Contract Pack</strong> — Seller's documents sent to buyer's solicitor: title register/plan, property forms, draft contract.</li>
<li><strong>Title (Register/Plan)</strong> — HM Land Registry record showing ownership, rights, restrictions, and a mapped boundary.</li>
<li><strong>Protocol Forms (TA6/TA10/TA7)</strong> — Seller questionnaires on the property, fixtures & fittings, and (if relevant) leasehold details.</li>
<li><strong>Fixtures & Fittings List (TA10)</strong> — What items are included or excluded from the sale.</li>
<li><strong>Leasehold / Management Pack</strong> — Extra docs for flats/leases: ground rent, service charges, building rules, planned works.</li>
<li><strong>ID & Source of Funds (KYC/AML)</strong> — Checks to confirm the client's identity and where purchase money comes from.</li>
<li><strong>Searches</strong> — Third-party checks (local authority, water & drainage, environmental; sometimes mining/chancel) for legal or environmental risks.</li>
<li><strong>Enquiries</strong> — Written questions to the seller's solicitor to clarify issues revealed by papers or searches.</li>
<li><strong>Mortgage Offer & Conditions</strong> — Lender's loan terms; special conditions must be satisfied before exchange/completion.</li>
<li><strong>Report on Title</strong> — Plain-English summary to the buyer explaining what is being purchased and any risks/obligations.</li>
<li><strong>Exchange of Contracts</strong> — Point when the deal becomes binding and a completion date is fixed; deposit usually paid.</li>
<li><strong>Completion</strong> — Money transfers settle the purchase; seller's mortgage is redeemed and keys are released.</li>
<li><strong>Undertaking</strong> — A solicitor's binding promise (e.g., to repay the seller's lender from completion funds).</li>
<li><strong>Redemption</strong> — Paying off the seller's existing mortgage to remove the lender's charge from the title.</li>
<li><strong>Apportionments</strong> — Splitting ground rent, service charge, or council tax between parties based on the completion date.</li>
<li><strong>Completion Statement</strong> — Final bill showing price, fees, searches, SDLT, apportionments, and funds required.</li>
<li><strong>Stamp Duty Land Tax (SDLT) Return</strong> — Tax form and payment submitted after completion (England & N. Ireland).</li>
<li><strong>Registration</strong> — Post-completion application to HM Land Registry to record the new owner and any lender's charge.</li>
</ul>
</p>
</details>
<br>

### Your Tasks

1. Read through Jaspreet's reply without worrying about bits you're not familiar with, for now – you can (imagine that you will) ask her to clarify later.
2. Carve out a bit of Jaspreet's workflow and make a conceptual model of it.
3. Use your conceptual map to make a logical model.

### Sharing

Be ready to share your work with the cohort!

