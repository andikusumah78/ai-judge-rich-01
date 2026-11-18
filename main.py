# ai-judge-rich-01: a 30-day plan for an AI agent to turn $100 into the most
# money, with no human doing the work. Python 3.13, standard library only.
# The program writes the plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
# outside the grader) as UTF-8 bytes, the same bytes on every run.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN_LINES = [
    "Day 1: one service - clean and enrich lead lists for small sales teams: dedupe, fix emails, add company and role. $30 per 500 leads, paid in advance, one-page site up.",
    "Days 2-7: find buyers where they already ask (r/sales, r/smallbusiness, Upwork, X): answer 20 a day, first 100 leads free as proof. Target 3 paying jobs by day 7; if none, switch to receipt cleanup for bookkeepers.",
    "Days 8-14: deliver same day with code; ask each buyer for a review; raise price to $45 after five 5-star reviews. Drop any channel with no paying buyer in 4 days.",
    "Days 15-30: keep selling; risk at most 20% of profits - never the original $100 - on small fast-resolving prediction-market positions where I can name the mispriced fact, $5 max each, stop after 3 losses in a row. Keep $40 reserve.",
    "Most likely day 30: $300-$500 from 10-15 jobs; worst case the $100 is nearly intact, since every dollar spent follows a paying buyer.",
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = "\n".join(PLAN_LINES)
    if not 1 <= len(text) <= 1000:
        raise ValueError("plan must be 1-1000 characters, got %d" % len(text))
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
