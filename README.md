[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/andikusumah78/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/andikusumah78/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

# Make the AI judge rich

make.fun bounty entry: [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01)

A 30-day plan for an AI agent with $100, a computer, internet access and no
human help, to end the 30 days with the most money. `main.py` (Python 3.13,
stdlib only) writes the plan to `/output/entry.txt`, the same bytes on every
run.

## The plan

> Day 1: one service - clean and enrich lead lists for small sales teams: dedupe, fix emails, add company and role. $30 per 500 leads, paid in advance, one-page site up.
>
> Days 2-7: find buyers where they already ask (r/sales, r/smallbusiness, Upwork, X): answer 20 a day, first 100 leads free as proof. Target 3 paying jobs by day 7; if none, switch to receipt cleanup for bookkeepers.
>
> Days 8-14: deliver same day with code; ask each buyer for a review; raise price to $45 after five 5-star reviews. Drop any channel with no paying buyer in 4 days.
>
> Days 15-30: keep selling; risk at most 20% of profits - never the original $100 - on small fast-resolving prediction-market positions where I can name the mispriced fact, $5 max each, stop after 3 losses in a row. Keep $40 reserve.
>
> Most likely day 30: $300-$500 from 10-15 jobs; worst case the $100 is nearly intact, since every dollar spent follows a paying buyer.

911 characters, UTF-8, deterministic across runs.

## Why this plan

- **Executable by an agent alone:** every step is browser, code and APIs — no
  human needed. The service is done with code, the buyers are found where
  they already ask for help, and payment is in advance through a link.
- **Most-likely money, not best case:** the engine is paid service work,
  not a lottery ticket. 10–15 small jobs at $30–$45 is a realistic month;
  the speculative part can only ever risk profits, never the $100.
- **Works today:** lead-list cleaning, forums, Upwork and prediction
  markets all exist now and pay an agent's work.
- **Concrete:** one named service, one named buyer, one price, one place to
  find them, and a day-one action.
- **Edge:** a thousand agents would either gamble the $100 or sell generic
  hours. This one sells a narrow, same-day service to buyers who already
  asked for it, proves itself with a free sample, kills dead channels in 4
  days, and only speculates with money it has already earned.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt
```

## Referral

https://make.fun/r/69w7r9cr
