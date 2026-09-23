# THE BLOON POWER GRAPH™ — Pre-Publish QA

## Status

**Seed dataset / prototype.** The current files run, but the dataset should not yet be presented as a fully source-verified research dataset.

## Smoke test

The current Python program runs successfully with:

- Nodes: 30
- Edges loaded by `bloon_computational_model.py`: 23
- Temporal edges present in `temporal_edges.csv`: 7

The current script printed structural-centrality output and exited normally.

## What is good

- Node and edge references are internally consistent.
- No orphan node references were found.
- Evidence scores are within 0–1.
- Temporal start/end dates are logically ordered.
- The program includes an explicit warning that centrality is not conspiracy/causality.
- The article explicitly frames the model as heuristic rather than an empirical law.

## Blocking issues before calling this a verified model

### 1. `temporal_edges.csv` is not used by the current program

The script only loads `nodes.csv` and `edges.csv`.

So the article's temporal-network discussion is ahead of the implementation.

### 2. Information and Capital factors are currently category-based mocks

The script assigns Information/Capital factors from node category. This is not a data-driven measurement.

Do not describe the resulting `Power_Score` as an empirical power index.

### 3. `evidence_score` is used directly as NetworkX path weight

For path-based algorithms, a larger weight normally behaves like a larger distance/cost. If higher `evidence_score` means stronger evidence, it should be separated from path distance or transformed explicitly.

### 4. `DiGraph` will overwrite parallel relationships

The present sample has no duplicate source-target pairs, but future data may contain multiple edges between the same pair.

A `MultiDiGraph` or explicit unique edge IDs would be safer.

### 5. Source provenance is too thin

`source_doc` contains labels such as `Mueller_Report_Vol1`, `FEC_Filings`, etc., but the dataset does not currently include a source ledger with URLs, titles, publication dates, and access dates.

Before publication, add `sources.csv` and make every edge traceable.

### 6. A few relationships are coded more strongly than the current evidence schema warrants

Examples to review:

- Peter Thiel → Palantir is coded as `INVESTMENT` with date `2003-05-01`; the public SEC record establishes Thiel as a Palantir co-founder, but the current edge label/date/source combination should be redesigned rather than treating the founding relationship as an SEC-documented 2003 investment.
- Mueller → Donald Trump is coded as `INVESTIGATION`; this should be checked against the actual scope of the Special Counsel's investigation and may be better represented as an institutional investigation/scope relation.
- Palantir → Department of Defense is represented as one continuous temporal contract from 2019 to 2026. The underlying government-contract history should be modeled as specific awards/periods rather than assumed continuous coverage.
- J.D. Vance → Donald Trump is represented as one continuous political-support edge from 2021 through 2026; split into dated documented events if that is what the sources support.

## Article wording to fix

The article currently says that Graph B *proves* Institutional Access is the largest multiplier. That is a model assumption, not a demonstrated empirical result.

Use language such as:

> "In this heuristic model, Institutional Access is implemented as a multiplier; its numerical influence is a modeling choice, not an empirical finding."

Likewise, avoid turning a graph structure into a claim of intent, command, control, or conspiracy.

## Verified external context used in QA

Official DOJ materials confirm:

- Robert Mueller was appointed Special Counsel on May 17, 2017. 
- DOJ's 2018 indictment attributed the DNC/DCCC/Clinton campaign hacking activity to 12 GRU officers and described the use of DCLeaks and Guccifer 2.0.
- Mueller's report documents GRU-operated personas transferring stolen documents to WikiLeaks and communications around the July 2016 DNC release.
- Mueller's report documents the June 9, 2016 Trump Tower meeting involving Donald Trump Jr., Jared Kushner, Paul Manafort, and Natalia Veselnitskaya.
- Palantir SEC filings identify Peter Thiel as a co-founder and chairman; they also identify his Founders Fund relationship.

These sources support the general existence of several relationships in the seed dataset, but they do **not** automatically validate every field, date, relation label, or score in the current CSVs.

## Recommended publish framing

Use:

> **This repository contains a BLOON-style computational toy model and a provisional seed dataset for network analysis. It is not a factual ranking of political power and does not establish conspiracy, intent, or causality.**

## Current conclusion

**Good for GitHub as `v0.1-seed` / prototype.**

**Not good yet as `v1.0 verified dataset`.**

The strongest next step is to add a source ledger, repair temporal handling, replace category-based mock factors, and re-code the few ambiguous relationships above.
