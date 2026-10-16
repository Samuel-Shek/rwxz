# English writing adaptation

Read this file when the output contains English. It covers English-specific issues only; purpose, audience and facts are handled in SKILL.md.

## 1. Plain, natural English

- Lead with the point. Business readers want the ask, the change or the conclusion in the first two sentences.
- Prefer verbs to nominalizations: *decide* not *make a decision*; *investigate* not *conduct an investigation*; *improve* not *bring about an improvement in*.
- Prefer active voice when the actor matters: *We will ship on 3 March* rather than *Shipment will be made on 3 March*.
- Keep sentences mostly under 25 words; vary length so the rhythm doesn't flatten.
- Use the everyday word unless the reader expects the technical one: *use* not *utilize*, *help* not *facilitate*, *start* not *commence*.
- One idea per paragraph. On screens, 1–4 sentences per paragraph is normal.

## 2. Chinglish and literal-translation patterns

These come from carrying Chinese sentence structure into English. Fix them even when the source text is the user's own draft.

| Pattern | Example | Better |
|---|---|---|
| Topic–comment opener | Regarding the quality issue of the samples, our engineers… | Our engineers found the cause of the sample defects… |
| Run-on comma splices | The mould is broken, production will stop, the new plan is… | Split into sentences, or join with *so* / *because* |
| Wrong transitivity or prepositions | discuss about; revert back; emphasize on; the price will increase 5% | discuss; reply; emphasize; the price will rise by 5% |
| Stock politeness | Please kindly be noted that… / Please do the needful. | Say the action: *Please note that…* / *Please sign and return the form by Friday.* |
| Empty effort statements | We will do our utmost to solve it. | Say what will actually happen and when |
| Missing articles or plurals | We will send you sample next week with new price list. | We'll send you a sample next week with the new price list. |
| Generic salutations | Dear Customer, / Dear Sir or Madam, | Use a name when you have one; match the relationship (*Dear [surname]*, *Hi [name]*) |
| Ritual openers in bad-news mail | Wish you have a nice day! (before announcing a problem) | Drop it, or move warmth to the close |
| *etc.* / *and so on* closing lists | We accept Visa, Mastercard, etc. | Name the full list, or say *including* |

## 3. Don't inflate

Signals of machine-sounding or brochure English. Each occurrence needs a reason to stay:

- Inflated vocabulary: delve, tapestry, leverage (as a verb), utilize, robust, seamless, cutting-edge, game-changer, unlock, elevate, empower, supercharge, navigate the landscape, realm, testament to.
- Empty frames: In today's fast-paced world; It's worth noting that; It's important to remember; When it comes to; At the end of the day.
- Formula structures: *not just X, but Y*; relentless groups of three; rhetorical-question openers; one-line paragraphs in a row for drama.
- Punctuation tics: em dashes in every paragraph; exclamation marks in professional text.
- Hedge stacks: *could potentially*, *may possibly*.

## 4. Register, variety and mechanics

- Register: contractions (*we're*, *don't*) fit conversational, marketing and most customer emails; avoid them in legal, formal or academic text.
- Regional variety: follow the user's instruction; otherwise the reader's locale. Keep it consistent throughout.
  - US: color, organize, center, license (noun and verb); dates *March 3*; 12-hour clock common; *$20/month*.
  - UK: colour, centre, licence (noun) / license (verb); *-ise* or *-ize* by house style, but consistent; dates *3 March*; 24-hour clock common in notices (*22:00*); *Ms* / *Mr* without full stops.
  - Other varieties (Australian, Indian, Singaporean English) follow their own conventions when the reader is local.
- Headlines and subheads: sentence case by default unless a house style says title case.
- Serial (Oxford) comma: either choice, applied consistently.
- Quotation marks: straight or curly, consistent; UK usually single quotes, US double.
- Numbers: spell out one to nine in prose unless house style differs; always use numerals for money, percentages, dates, measurements and model numbers.

## 5. Length

- *Words* are whitespace-separated words; hyphenated compounds count as one. Count before delivering (`scripts/text_check.py count`).
- A rewrite asked to be shorter must be shorter in words, not just in characters.

## 6. English checks

1. Is the main point or request in the first two sentences?
2. Any nominalizations that could be verbs? Any passive sentences hiding who acts?
3. Any Chinglish patterns from the table in section 2?
4. Any inflated words or empty frames from section 3?
5. Spelling, date format and punctuation consistent with one regional variety?
6. Word count checked against the limit?
