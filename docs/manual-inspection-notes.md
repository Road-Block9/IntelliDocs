# CardioTrack CT-200 Manual Inspection Notes

## Scope and inspection method

This document records a manual structural inspection of the two uploaded CardioTrack CT-200 manuals. Every page of both PDFs was visually reviewed because version 1 contains 6 pages and version 2 contains 7 pages. Visual page renders were checked alongside embedded-text extraction so that heading hierarchy, line placement, tables, page breaks, and cross-page continuation were not inferred from plain text alone.

The labels **version 1** and **version 2** below refer to the uploaded filenames, not to revision text printed inside the PDFs. Neither PDF visibly prints a revision number or version identifier.

## 1. Files inspected

| Manual label | Exact filename | Total pages | Content type | OCR necessary? |
|---|---|---:|---|---|
| Version 1 | `ct200_manual.pdf` | 6 | Selectable embedded text with vector text and ruled tables; no scanned-page imagery was observed | No. Embedded text is selectable and extracts legibly. Visual inspection remains necessary for hierarchy, tables, rules, and page-break behavior. |
| Version 2 | `ct200_manual_v2.pdf` | 7 | Selectable embedded text with vector text and ruled tables; no scanned-page imagery was observed | No. Embedded text is selectable and extracts legibly. Visual inspection remains necessary for hierarchy, tables, rules, and page-break behavior. |

Both files use an A5 portrait page layout. No mixture of scanned and native pages was observed.

## 2. Document title and opening structure

### Version 1

- **Main title:** `CardioTrack CT-200 Home Blood Pressure Monitor — Technical & User Manual` (page 1).
- The title occupies three lines at the top of page 1 in large bold type, followed by a thin horizontal rule.
- `CT-200` is the model number embedded in the title.
- No subtitle separate from the title was observed.
- No printed revision number, publication date, document code, or version number was observed.
- There is no standalone cover page. Page 1 combines the title and the opening content.
- No table of contents is present.
- The first main section, `1. Device Overview`, begins on page 1 directly below the title area.
- No preface, legal notice, symbol key, or other content appears before Section 1.

### Version 2

- **Main title:** `CardioTrack CT-200 Home Blood Pressure Monitor — Technical & User Manual` (page 1).
- The title has the same three-line, large-bold presentation and horizontal rule as version 1.
- `CT-200` is the model number embedded in the title.
- No subtitle separate from the title was observed.
- No printed revision number, publication date, document code, or version number was observed.
- There is no standalone cover page.
- No table of contents is present.
- `1. Device Overview` begins on page 1 immediately after the title area.
- No content appears before Section 1 other than the title.

## 3. Main heading patterns

Top-level sections use an Arabic numeral, a period, one space, and a title, for example `1. Device Overview`.

### Common visual pattern

- Large bold sans-serif type.
- Left aligned with the body text.
- A thin horizontal rule immediately below the heading.
- More vertical space above and below than is used for subsection headings.
- Title case rather than all capitals.
- No indentation.

### Version 1 top-level headings

| Heading | Page | Notes |
|---|---:|---|
| `1. Device Overview` | 1 | Normal top-level style. |
| `2. Physical and Electrical Specifications` | 1 | Appears near the bottom of the page; its body begins on page 2. |
| `3. Device Operation` | 2 | Normal top-level style. |
| `4. Alarms and Safety Behavior` | 3 | Appears at the bottom of page 3; Section 4 body begins on page 4. |
| `5. Data Management` | 4 | Appears at the bottom of page 4; Section 5 body begins on page 5. |
| `6. Maintenance and Cleaning` | 5 | Normal top-level style. |
| `7. Troubleshooting` | 5 | Appears near the bottom of page 5; Section 7 body begins on page 6. |
| `8. Regulatory Information` | 6 | Normal top-level style. |

### Version 2 top-level headings

| Heading | Page | Notes |
|---|---:|---|
| `1. Device Overview` | 1 | Normal top-level style. |
| `2. Physical and Electrical Specifications` | 1 | Body begins on page 2. |
| `3. Device Operation` | 2 | Normal top-level style. |
| `4. Alarms and Safety Behavior` | 4 | Begins at the top of page 4. |
| `5. Data Management` | 5 | Begins after the continuation of Section 4.3. |
| `6. Maintenance and Cleaning` | 5 | Normal top-level style. |
| `7. Troubleshooting` | 6 | Normal top-level style. |
| `8. Regulatory Information` | 6 | Its subsection body continues onto page 7. |

No top-level heading uses a different numbering syntax. The only placement irregularity is that several headings are isolated near a page bottom while their section content starts on the following page. This affects page-boundary reconstruction but not the visual heading pattern.

## 4. Subheading patterns

Second-level headings normally use decimal numbering in the form `N.N`, followed by a space and title text. They are bold, left aligned, smaller than top-level headings, and do **not** have a horizontal rule beneath them.

Examples include:

- `1.1 Intended Use` (both versions, page 1)
- `1.2 Indications and Contraindications` (both versions, page 1)
- `2.1 General Specifications` (both versions, page 2)
- `2.2 Cuff Specifications` (both versions, page 2)
- `3.1 Powering On and Profile Selection` (both versions, page 2)
- `4.2 Error Codes` (version 1 page 4; version 2 page 4)
- `7.2 Inconsistent Readings` (version 1 page 6; version 2 page 6)

### Deeper heading

The manuals contain one visibly deeper heading:

- `2.1.1.1 Battery Life Under Typical Use` (both versions, page 2).

This heading is bold and visually similar in size to ordinary second-level headings. Its numbering skips visible intermediary headings such as `2.1.1`. No `2.1.1` or `2.1.1.x` sibling is present elsewhere. A parser must not invent the missing levels without an explicit policy.

### Irregular order

Within Section 3, the visible subsection sequence is:

1. `3.1 Powering On and Profile Selection`
2. `3.2 Cuff Inflation Sequence`
3. `3.4 Auto Shutoff`
4. `3.3 Result Display and Classification`

This out-of-order numbering occurs in both versions on pages 2-3. It is a real document irregularity. A parser must preserve source order rather than sorting nodes numerically.

### Similarity to body or list text

- Subheadings are distinctly bold, but their size is close enough to the title text of table columns and numbered-list content that font weight alone should not determine hierarchy.
- The numbered classification items under `3.3 Result Display and Classification` (both versions, page 3) begin with `1.` through `5.` and could be mistaken for top-level section headings if numbering is detected without considering indentation, font size, and surrounding context.

## 5. Unnumbered headings and labels

No standalone unnumbered section headings were observed below the document title.

No visually boxed or prefixed labels such as `NOTE`, `WARNING`, `CAUTION`, `IMPORTANT`, or `TIP` were observed in either PDF.

Safety-related statements are written as ordinary body paragraphs, including:

- contraindications under `1.2 Indications and Contraindications` (page 1),
- overpressure behavior under `4.1 Overpressure Protection` (version 1 page 4; version 2 page 4),
- the crisis recommendation in numbered item 5 under `3.3 Result Display and Classification` (both versions, page 3), and
- the instruction to discontinue use under `7.1 Error Codes` (both versions, page 6).

These should remain paragraph or list content under their actual numbered headings. They should not be promoted to independent warning sections merely because they contain safety language.

The table column labels `Parameter`, `Value`, `Code`, `Meaning`, and `Device Behavior` are table headers, not document headings.

## 6. Duplicate headings

| Exact heading text | Occurrences | Parent sections | Interpretation |
|---|---|---|---|
| `Error Codes` | Version 1: `4.2 Error Codes` page 4 and `7.1 Error Codes` page 6. Version 2: `4.2 Error Codes` page 4 and `7.1 Error Codes` page 6. | `4. Alarms and Safety Behavior`; `7. Troubleshooting` | These are separate structural nodes. Section 4.2 contains the code table, while Section 7.1 gives user action when codes persist. They must not be merged by normalized heading text. |

No repeated heading was identified as page furniture. There are no repeated running section names in headers or footers.

## 7. Paragraph structure

- The manuals use a single-column layout throughout.
- Body paragraphs are visually rendered as multi-line blocks with normal line wrapping, not one line per paragraph.
- Multiple paragraphs can belong to one heading, although many subsections contain only one paragraph.
- Body text appears directly under top-level Section 1 before subsection `1.1`: the introductory Device Overview paragraph on page 1 belongs directly to `1. Device Overview` in both versions.
- Section `3.1 Powering On and Profile Selection` spans a page boundary in both versions. Its first sentence is on page 2 and the second sentence continues on page 3 without the heading being repeated.
- Version 2 has additional paragraph continuations caused by pagination:
  - `4.3 Alarm Thresholds` begins on page 4 and continues on page 5.
  - `6.1 Cleaning Instructions` begins on page 5 and continues on page 6.
  - `8.1 Classification` begins on page 6 and continues on page 7.
- Version 1 places complete paragraphs more compactly, but several section headings are separated from their body by a page break.
- No side-by-side columns, marginal notes, or text boxes were observed.

## 8. Lists and numbered instructions

### Numbered classification list

Under `3.3 Result Display and Classification` on page 3 in both versions, there is a five-item Arabic numbered list:

1. `Normal: systolic < 120 and diastolic < 80`
2. `Elevated: systolic 120–129 and diastolic < 80`
3. `Hypertension Stage 1: systolic 130–139 or diastolic 80–89`
4. `Hypertension Stage 2: systolic ≥ 140 or diastolic ≥ 90`
5. `Hypertensive Crisis: systolic > 180 or diastolic > 120 — device recommends seeking immediate medical attention`

The fifth item wraps onto a second visual line. These are list items under Section 3.3, not subsections.

### Other list styles

- No bullet-symbol lists were observed.
- No lettered lists were observed.
- No nested lists were observed.
- No separately formatted step-by-step procedure with numbered steps was observed.
- Instructions elsewhere are prose paragraphs, such as pressing and holding the power button under `3.1` and cleaning guidance under `6.1`.

### Parser ambiguity

The `1.` through `5.` classification list on page 3 is the principal list/heading ambiguity. A parser that identifies every leading integer and period as a section heading could create five false top-level nodes.

## 9. Tables

### Version 1

| Page | Nearby heading | Visible structure | Merged cells | Continues across pages | Likely extraction reliability | Fallback representation |
|---:|---|---|---|---|---|---|
| 2 | `2.1 General Specifications` | 2 columns × 8 rows including header. Header: `Parameter` / `Value`; 7 data rows. | None visibly merged. | No. | Likely extractable as row pairs, but plain-text extraction loses explicit cell boundaries. | Markdown table preserving one parameter-value pair per row. If row association is uncertain, use a labeled list. |
| 4 | `4.2 Error Codes` | 3 columns × 6 rows including header. Header plus E1-E5 rows. | None visibly merged. Some cell text wraps to multiple lines. | No. | Moderate. Row order is clear visually, but wrapped cell text can flatten into the wrong column in plain text. | Markdown table with one row per code; if column reconstruction fails, use separate code entries with `Meaning` and `Device behavior` fields. |

### Version 2

| Page | Nearby heading | Visible structure | Merged cells | Continues across pages | Likely extraction reliability | Fallback representation |
|---:|---|---|---|---|---|---|
| 2 | `2.1 General Specifications` | 2 columns × 8 rows including header. Same visible structure as version 1. | None visibly merged. | No. | Likely extractable as row pairs, but plain text does not preserve borders. | Markdown table or labeled parameter-value list. |
| 4 | `4.2 Error Codes` | 3 columns × 7 rows including header. Header plus E1-E6 rows. | None visibly merged. Several cells wrap. | No. | Moderate. Wrapped E5 and E6 behavior text may be detached or reordered by naive extraction. | Markdown table with one row per code; otherwise structured code entries. |

No table title separate from the nearby subsection heading was observed. No table continues across a page break. No claim is made here that any automatic table parser reconstructs these correctly.

## 10. Figures, diagrams, and captions

No device diagram, screenshot, icon legend, illustration, photograph, or separately captioned figure was observed in either manual.

The only non-paragraph visual structures are ruled tables on page 2 and page 4 of each version. They contain information whose column associations can be weakened by text-only extraction, but they are tables rather than figures.

No figure captions or labels embedded inside figures were observed.

## 11. Repeating headers and footers

- No running header is visible.
- No running footer is visible.
- No printed page numbers are visible on the PDF pages.
- No repeated document title, copyright line, revision string, or section label appears in page furniture.
- Thin horizontal rules belong to the title and top-level heading styling; they are not headers or footers.

Therefore, there is no repeated header/footer text that needs removal from the document tree. Page numbers used in this inspection refer to PDF page indices, not printed page numbers.

## 12. Cross-page content

| Manual | Pages | Cross-page case | Recommended reconstruction |
|---|---|---|---|
| Version 1 | 1→2 | `2. Physical and Electrical Specifications` appears at the bottom of page 1; subsection `2.1` starts on page 2. | Keep Section 2 as the parent of page 2 content despite the page break. |
| Version 1 | 2→3 | `3.1 Powering On and Profile Selection` begins on page 2 with the first sentence; the paragraph continues at the top of page 3. | Join the two sentences into one subsection body. Do not treat the page-3 continuation as orphan text. |
| Version 1 | 3→4 | `4. Alarms and Safety Behavior` appears at the bottom of page 3; `4.1` starts on page 4. | Keep Section 4 open across the page break. |
| Version 1 | 4→5 | `5. Data Management` appears at the bottom of page 4; `5.1` starts on page 5. | Keep Section 5 open across the page break. |
| Version 1 | 5→6 | `7. Troubleshooting` appears at the bottom of page 5; `7.1` starts on page 6. | Keep Section 7 open across the page break. |
| Version 2 | 1→2 | Section 2 heading is on page 1; `2.1` starts on page 2. | Preserve the parent-child relationship across pages. |
| Version 2 | 2→3 | `3.1 Powering On and Profile Selection` heading is at the bottom of page 2; all of its body starts on page 3. | Attach the opening page-3 paragraph to `3.1`. |
| Version 2 | 4→5 | The paragraph under `4.3 Alarm Thresholds` starts on page 4 and finishes with `(overpressure), which cannot be silenced for safety reasons.` at the top of page 5. | Join the page-5 fragment to the page-4 paragraph. |
| Version 2 | 5→6 | `6.1 Cleaning Instructions` starts on page 5 and its sentence continues at the top of page 6. | Join the fragments into one paragraph. |
| Version 2 | 6→7 | `8.1 Classification` starts on page 6 and finishes on page 7. | Join the page-7 fragment to the page-6 paragraph. |

No list or table continues across pages. No heading was observed alone at the very bottom with only a tiny fragment of body text; however, several top-level or subsection headings have all body text on the next page.

## 13. Formatting changes

### Beginning, middle, and end

The same visual system is used throughout both manuals:

- large bold top-level headings with horizontal rules,
- smaller bold numbered subsection headings without rules,
- regular left-aligned body paragraphs,
- single-column layout,
- ruled tables with bold centered column headers.

No appendix-specific style or separate appendix section is present.

### Safety, troubleshooting, specifications, and instructional sections

- Safety sections do not use colored callouts, icons, boxes, or warning-label formatting. Their content is styled as ordinary headings and body paragraphs.
- Troubleshooting uses the same heading and paragraph styles as other sections.
- Specifications use a table under `2.1`, but the surrounding heading styles are unchanged.
- The `4.2 Error Codes` table uses three columns and wrapped text, creating a layout change relevant to table extraction but not heading detection.

### Version-to-version formatting

No confirmed change in fonts, heading appearance, rules, indentation, table-border style, or column layout was observed between version 1 and version 2. The major visible pagination difference is that version 2 is one page longer because added/revised text causes more cross-page continuation.

## 14. Structural differences between version 1 and version 2

### Confirmed unchanged structure/content

Most headings and much of the body text are visibly unchanged, including:

- title and Section 1 content (both page 1),
- `2.1 General Specifications` table values (both page 2),
- `2.2 Cuff Specifications` (both page 2),
- `3.1 Powering On and Profile Selection` text (version 1 pages 2-3; version 2 pages 2-3),
- `3.4 Auto Shutoff` and `3.3 Result Display and Classification` including the five classification items (both page 3),
- `4.1 Overpressure Protection` (both page 4),
- `5.1 Local Storage` and `5.2 Bluetooth Sync` (version 1 page 5; version 2 page 5),
- Sections 6, 7, and 8 wording apart from pagination (version 1 pages 5-6; version 2 pages 5-7).

### Confirmed changes

| Change type | Version 1 page | Version 2 page | Heading/location | Confirmed difference |
|---|---:|---:|---|---|
| Changed value and explanatory text | 2 | 2 | `2.1.1.1 Battery Life Under Typical Use` | Approximate battery life changes from **300 measurement cycles** to **250 measurement cycles**. Version 2 adds that this was revised downward after extended field testing. |
| Changed threshold | 2 | 2 | `2.1.1.1 Battery Life Under Typical Use` | Low-battery icon threshold changes from **below 15%** to **below 10%** remaining capacity. |
| Changed value and added rationale | 3 | 3 | `3.2 Cuff Inflation Sequence` | Inflation increment changes from **40 mmHg** to **30 mmHg**. Version 2 adds that the increment was reduced from 40 mmHg to improve pulse-detection reliability in field testing. |
| Changed timing | 4 | 4 | `4.2 Error Codes`, E3 row | E3 device behavior changes from auto-deflation within **2 seconds** to within **1.5 seconds**. |
| Added table row / added error code | 4 | 4 | `4.2 Error Codes` | Version 2 adds **E6 Bluetooth sync failure**, with behavior: display E6 on the next sync attempt and do not affect measurement. |
| Changed cross-reference range | 4 | 4-5 | `4.3 Alarm Thresholds` | Version 1 refers to audible alarms for **E1-E5**; version 2 refers to **E1-E6**. The E3 non-silence rule remains. |
| Added subsection | — | 5 | `5.3 Data Export` | Version 2 adds CSV export support starting with firmware 1.4, identifies exported columns, and requires a successful Bluetooth sync in the current session. No corresponding subsection is present in version 1. |
| Pagination/layout consequence | 3-6 | 4-7 | Sections 4-8 | Added/revised content shifts Section 4 to page 4 and causes paragraphs in `4.3`, `6.1`, and `8.1` to continue onto following pages. This is a pagination effect accompanying content changes, not evidence of renamed or moved sections. |

### Renamed, removed, or moved sections

- No renamed heading was confirmed.
- No version 1 section was confirmed as removed in version 2.
- No section was confirmed as intentionally moved to a different structural parent. Different page positions result from pagination.
- `5.3 Data Export` is the only confirmed added section.

## 15. Suspected parser risks

| Risk | Example from PDF | Page | Possible wrong parser behaviour | Recommended handling |
|---|---|---:|---|---|
| Duplicate headings merged | `4.2 Error Codes` and `7.1 Error Codes` | Both versions: 4 and 6 | Merge two distinct nodes because normalized title text is identical. | Use numbering and parent path as part of node identity. |
| Numbered list treated as headings | Five classification items under `3.3` | Both versions: 3 | Create false top-level sections `1` through `5`. | Require heading typography and structural context, not numbering alone. |
| Deep heading causes invented hierarchy | `2.1.1.1 Battery Life Under Typical Use` with no visible `2.1.1` | Both versions: 2 | Fabricate missing headings or attach the node to the wrong parent. | Preserve the literal level token; mark skipped levels explicitly or attach to nearest existing prefix according to a documented rule. |
| Source order overwritten by numeric sorting | `3.4 Auto Shutoff` appears before `3.3 Result Display and Classification` | Both versions: 3 | Reorder content to 3.3 then 3.4 and change document sequence. | Preserve visual/source order. Store numbering separately from sequence. |
| Heading stranded from body | `3.1` heading at page 2 bottom in version 2; body starts page 3 | Version 2: 2→3 | Attach the body to Section 3 or treat it as orphan text. | Carry the active heading across page boundaries. |
| Cross-page paragraph split | `4.3 Alarm Thresholds` continues with `(overpressure)...` | Version 2: 4→5 | Create a standalone fragment or new paragraph detached from `4.3`. | Merge based on sentence continuity, typography, and lack of an intervening heading. |
| Cross-page paragraph split | `6.1 Cleaning Instructions` continues onto page 6 | Version 2: 5→6 | Separate `use alcohol...` from the cleaning instruction. | Join page fragments under the active subsection. |
| Cross-page paragraph split | `8.1 Classification` continues onto page 7 | Version 2: 6→7 | Lose or orphan the final validation clause. | Continue the active paragraph onto page 7. |
| Top-level heading body assigned to prior section | `4. Alarms and Safety Behavior` at page 3 bottom in version 1 | Version 1: 3→4 | Treat page-4 subsections as part of Section 3 because Section 4 has no same-page body. | Keep heading state across page breaks. |
| Table flattened incorrectly | E1-E5/E6 error-code tables with wrapped cells | Both versions: 4 | Interleave meanings and behaviors or assign wrapped lines to the wrong row. | Use ruling lines and cell coordinates; fall back to one structured record per code. |
| Table header promoted to headings | `Parameter`, `Value`, `Code`, `Meaning`, `Device Behavior` | Both versions: 2 and 4 | Insert table labels into the section hierarchy. | Classify text inside ruled table header cells as table metadata. |
| Similar versions matched too loosely | Battery-life subsection has same heading but different values | Both versions: 2 | Mark subsection as unchanged because heading text matches. | Compare normalized body text and table/list content under matched headings. |
| Added row overlooked in version comparison | E6 row in version 2 error-code table | Version 2: 4 | Treat tables as equal due to same heading and first five codes. | Compare row keys and row counts, not only surrounding heading text. |
| Safety prose promoted to warning node | Crisis recommendation in list item 5 | Both versions: 3 | Create an unsupported `WARNING` node from semantic language. | Preserve visible formatting; represent it as list content because no warning label or callout exists. |

## 16. Expected hierarchy reference

The following reference reconstructs **version 1, pages 1-6**, which is a connected six-page range containing the title, standard headings, a skipped heading depth, out-of-order subsections, a numbered list, two tables, duplicate heading text, and cross-page boundaries.

```text
CardioTrack CT-200 Home Blood Pressure Monitor — Technical & User Manual (p. 1)
├── 1. Device Overview (p. 1)
│   ├── [introductory paragraph directly under Section 1] (p. 1)
│   ├── 1.1 Intended Use (p. 1)
│   └── 1.2 Indications and Contraindications (p. 1)
├── 2. Physical and Electrical Specifications (p. 1)
│   ├── 2.1 General Specifications (p. 2)
│   │   ├── [2-column specification table] (p. 2)
│   │   └── 2.1.1.1 Battery Life Under Typical Use (p. 2)
│   └── 2.2 Cuff Specifications (p. 2)
├── 3. Device Operation (p. 2)
│   ├── 3.1 Powering On and Profile Selection (pp. 2-3)
│   ├── 3.2 Cuff Inflation Sequence (p. 3)
│   ├── 3.4 Auto Shutoff (p. 3)
│   └── 3.3 Result Display and Classification (p. 3)
│       └── [five-item numbered classification list] (p. 3)
├── 4. Alarms and Safety Behavior (pp. 3-4)
│   ├── 4.1 Overpressure Protection (p. 4)
│   ├── 4.2 Error Codes (p. 4)
│   │   └── [3-column E1-E5 error-code table] (p. 4)
│   └── 4.3 Alarm Thresholds (p. 4)
├── 5. Data Management (pp. 4-5)
│   ├── 5.1 Local Storage (p. 5)
│   └── 5.2 Bluetooth Sync (p. 5)
├── 6. Maintenance and Cleaning (p. 5)
│   ├── 6.1 Cleaning Instructions (p. 5)
│   └── 6.2 Calibration (p. 5)
├── 7. Troubleshooting (pp. 5-6)
│   ├── 7.1 Error Codes (p. 6)
│   └── 7.2 Inconsistent Readings (p. 6)
└── 8. Regulatory Information (p. 6)
    └── 8.1 Classification (p. 6)
```

Hierarchy notes:

- The introductory Device Overview paragraph belongs directly under Section 1, before `1.1`.
- `2.1.1.1` is shown exactly as printed. Its missing intermediate levels are **uncertain — manual verification required** for the parser's chosen parent-normalization policy. Visually, it follows the table under `2.1`, so `2.1` is the nearest supported parent.
- `3.4` must remain before `3.3` because that is the visible source order.
- The five blood-pressure classifications belong as list content under `3.3`; they are not hierarchy nodes.
- Safety statements under `1.2`, `3.3`, `4.1`, `4.3`, and `7.1` remain ordinary body/list content because no warning callout styling is present.
- `4.2 Error Codes` and `7.1 Error Codes` are separate nodes despite sharing the title `Error Codes`.
- Sections 2, 4, 5, and 7 begin on one page and receive their first subsection content on the next page.

## 17. Pages manually reviewed

### Version 1 — `ct200_manual.pdf`

Pages reviewed: **1, 2, 3, 4, 5, 6**.

This includes the first five pages, all available middle pages, the final five pages, both table pages (2 and 4), the numbered-list page (3), all top-level and subsection heading placements, and all cross-page boundaries.

### Version 2 — `ct200_manual_v2.pdf`

Pages reviewed: **1, 2, 3, 4, 5, 6, 7**.

This includes the first five pages, all available middle pages, the final five pages, both table pages (2 and 4), the numbered-list page (3), the added Data Export subsection (5), and all cross-page continuations.

## Most important extraction risks

The highest-priority risks are: preserving the out-of-order `3.4`/`3.3` source sequence; preventing the page-3 classification list from becoming headings; keeping the two `Error Codes` nodes separate; handling the skipped level in `2.1.1.1`; reconstructing headings and paragraphs split across pages; and retaining row/column associations in the error-code tables. Version comparison must inspect body values and table rows, because matching heading text alone would miss the battery, inflation, E3 timing, E6, and Data Export changes.

## Items requiring manual verification

- Confirm the intended semantic parent policy for `2.1.1.1 Battery Life Under Typical Use`, because the printed hierarchy skips visible intermediate levels.
- Confirm whether the project should label the files as “version 1” and “version 2” solely from filenames; the PDFs themselves do not visibly print those version labels.
- Confirm the exact Unicode normalization desired for en dashes, em dashes, non-breaking hyphens, `±`, `≥`, and `≤` during extraction.
- Confirm table reconstruction against the rendered page if an automatic extractor assigns wrapped error-code text to ambiguous cells.
- Confirm that no hidden PDF-layer artifacts are intended as content; none are visible in the rendered pages.
