# Pranshul & Shilpee — Wedding Invitation

A classy, ethnic, single-page Hindu wedding invitation website, designed to be
circulated to guests (mostly viewed on mobile). It carries the event schedule,
one-tap **Google Maps navigation** to every venue, and **Add to Calendar** for
each function.

**Wedding:** 25 November 2026 · Lucknow, Uttar Pradesh
**Hashtag:** #WhenPranshulMetShilpee

---

## What's inside

| Path | Description |
|------|-------------|
| `index.html` | The entire website — **fully self-contained**. All CSS, JavaScript, fonts, images and the logo are inlined (images as data URIs), so it has **no external dependencies** and works offline / on any static host. |
| `assets/source/` | Original photos supplied by the couple (the logo image and the couple portrait). Kept for future edits. |
| `assets/generated/` | Processed assets actually used in the site: the circular PS crest, the cropped couple portrait, and the hand-drawn Ganesha (SVG). These are already embedded in `index.html` — the folder is for reference/re-editing. |
| `preview/mobile-preview.html` | A phone-mockup snapshot used to review the mobile layout. Not part of the live site. |

## Deploying (GitHub Pages)

Because `index.html` is self-contained, hosting is trivial:

1. Create a new GitHub repository and push this folder (see below).
2. In the repo, go to **Settings → Pages**.
3. Set **Source** to `Deploy from a branch`, branch `main`, folder `/ (root)`.
4. Your invitation goes live at `https://<username>.github.io/<repo>/`.

Any static host works too (Netlify, Vercel, Cloudflare Pages, S3) — just serve `index.html`.

## Editing the content

Open `index.html` and look for the `WEDDING` config object near the bottom
(inside the `<script>`). All events, dates, times, venues and addresses are
defined there in one place — edit that object and the event cards, venue cards,
navigation links and calendar entries all update automatically.

- **Contact email:** search for `pranshulandshilpee@gmail.com`.
- **Countdown target:** `weddingDate` in the `WEDDING` config.
- **Couple photo:** the `<img class="hero-photo" ...>` (base64 data URI) in the hero.
- **Logo / Ganesha:** the `.emblem` CSS rule (logo) and the inline `<svg class="ganesha">` in the hero.

## Features

- Responsive, mobile-first layout with a hamburger menu on small screens
- Live countdown to the wedding day
- Per-event **Navigate** (Google Maps directions) and **Add to Calendar**
  (Google Calendar + `.ics` for Apple/Outlook)
- Venue location cards with directions
- Rotating gold mandala, hand-drawn Ganesha, and the couple's PS crest
- No phone numbers exposed — contact is via email + venue directions

## Pushing to GitHub

```bash
cd ~/pranshul-shilpee-wedding
# a git repo + first commit are already created for you
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```
