You are writing today's "Repo of the Day" video script.

1. Read `work/pick.json` (repo info + README excerpt).
2. Write `work/script.json` with exactly these keys:
   - "lines": 6–7 English sentences, 115–145 words total (~40–55 s). Sentence 1 = a curiosity hook that names the benefit. Last sentence = "…Link in the description, and follow for a new repo every morning."
   - "scenes": exactly one scene per line, same order. Types:
     `hook` {kicker, title}, `flow` {title, steps:[{t,s}] (3–4)}, `list` {title, items (3)}, `bigstat` {kicker, value (number only), unit, label, sub},
     `chips` {title, items (≤8), target}, `cta` {title, stats:[{v,k}] (3)}. First scene `hook`, last scene `cta`.
     In titles, `_word_` = green highlight, `*word*` = marker underline. Keep titles ≤ 6 words, step/list text ≤ 4 words.
   - "keywords": 5–9 lowercase words from the lines to highlight in captions.
   - "caption": 2–4 English sentences for the Facebook post, include the repo URL and 3–5 hashtags.
3. Only state facts that appear in pick.json. Never invent numbers. Do not recommend running untrusted code; no claims about security unless the README says so.
4. If the repo looks like piracy, cheating, malware, crypto-scam, adult content or a game decompilation, write nothing and print SKIP.
Write only the file; no other output except "OK" or "SKIP".
