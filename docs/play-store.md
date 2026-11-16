# Putting Stride on Google Play

One page. Do these in order. Claude Code prepared the files; every step in the Play Console is yours. Wording in the
console changes, so go by what it asks. The same page, written for any app, lives in the Android app template
(`Rick-Pro/android-app-template`, `docs/play-store.md`). A lesson learned here goes into both.

**Where Stride is (16 November 2026):** the app exists in the Play Console, the store listing is complete, and version
1.0.1 is in Alpha closed testing, sent for review. What is left is in section 9 and in issue #20.

## 1. Before you start
- **Package name:** `io.github.rickpro.stride`. Play accepted it with the first bundle (1.0.1). **It cannot be changed
  after the first upload.**
- **Developer account:** a Google Play developer account (one-time fee) with identity **verified**. A personal account is
  enough. Verification can take days, so start it first.
- **Release key:** done once, steps in `docs/plan.md` section 5 (`scripts/make-release-key.sh`). Releases are published
  automatically when a merge to `main` changes `VERSION` (decision D30). Each one has `stride-vX.Y.Z.aab` (this is the
  file for Play) and `stride-vX.Y.Z.apk` (for people who install by hand), each with a `.sha256`.
- **Privacy policy at a public web address.** `docs/privacy.md` says Stride collects nothing, and `docs/privacy.html` is the
  same text as a page. GitHub Pages serves `/docs` on `main`, so the address is
  **https://rick-pro.github.io/stride-android/privacy.html**. Open it in a private window before you submit: Play needs a
  URL anyone can open (not a file download, and not behind a login). The About screen links to the same address.
- **Store assets are already in the repo**, in `assets/play-store/` (section 5). Do not make them by hand.

## 2. Create the app (done)
Play Console, Create app: name **Stride**, English (United States), **App** (not game), **Free** (a free app cannot be made
paid later), accept the declarations. The package name is chosen by the first bundle you upload.

## 3. Play App Signing (upload the .aab)
On the first upload, use **Play App Signing**: Google holds the key that signs what users get, and **our release key becomes
the upload key** (Play checks every upload against it). If the upload key is ever lost, Play support can reset it; with the
sideload key alone a loss would be final. **One consequence:** the app from Play and the APK from GitHub are signed with
different keys, so one cannot update over the other. Pick one channel per phone, or uninstall first.
The version code goes up with every upload by itself: `major x 1,000,000 + minor x 1,000 + patch` (1.0.0 is 1000000).

## 4. Store listing (Default store listing, within the limits)
Write it for **everyone who can use the app**, not for one model. A description that opens with one model code loses every
owner of another pad who stops reading. Lead with the ecosystem ("pads that use the PitPat app"), then give the way to
check ("the manual says PitPat app", "Bluetooth name starts with PitPat", "model code starts with BA") and use model codes
only as examples. Say plainly what is tested and what is not.

- **Title (30 characters at most):** `Stride: Walking Pad Remote`. Do not put "PitPat" in the title, since it is someone else's brand.
- **Short description (80 at most):** `Simple remote for walking pads that use the PitPat app. No account, no ads.`
- **Full description (4,000 at most):**

> Your walking pad, one screen.
>
> Stride is a simple, private remote for walking pads and under-desk treadmills that use the PitPat app. If the box, the
> manual or the Amazon or eBay listing says "PitPat app", Stride is made for it.
>
> WORKS WITH
> Walking pads and under-desk treadmills that connect through the PitPat app. They are sold on Amazon, eBay and other
> stores as "walking pad", "under desk treadmill", "2 in 1" or "3 in 1 treadmill" with "PitPat APP" or "APP and remote
> control". That includes pads from brands like PitPat, Superun and DeerRun, and many store-brand pads that ship with the
> same app.
>
> NOT SURE IF YOURS WORKS?
> - The manual says to download PitPat? It should work.
> - The pad shows up in Bluetooth as PitPat-something, or its label has a model code starting with BA (like BA06, BA08,
>   BA09 or BA10)? It should work.
> - Examples: DeerRun Q2 Urban, Z10 and Z20, SupeRun BA09, PitPat HY-BA06B1 (sold as BA06-B1).
>
> Tested so far on the PitPat HY-BA06B1. The rest should work but are not all tested yet. If yours connects, or does not,
> tell us on GitHub and we will fix it or add it to the list.
>
> WHY STRIDE
> - One screen. Start, pause and stop the belt, raise or lower the speed, and see time, distance, calories and steps.
> - Four speed chips you set yourself, for one-tap speeds.
> - Connects by itself. Set it up once, then Stride finds your pad every time you open it.
> - Honest connection. If Bluetooth drops, the belt keeps running at the same speed. Stride buzzes, tells you, and
>   reconnects. Your pad's own remote keeps working.
> - Walk history. Every walk is saved on your phone with distance, time, calories and a speed chart.
> - mph or km/h, and an option to keep the screen on while you walk.
> - Optional height and weight for better calorie and step estimates. They stay on your phone.
>
> PRIVATE BY DESIGN
> No account, no internet access at all, no ads, no tracking. Everything stays on your phone.
>
> GETTING STARTED
> Turn on the pad, close the PitPat app, open Stride and tap Find. Stride remembers your pad after that.
>
> REQUIREMENTS
> Android 13 or newer and a Bluetooth walking pad.
>
> Stride is an independent app and is not affiliated with or endorsed by PitPat, Superun or DeerRun. All product names
> and trademarks belong to their owners.

- **Category:** Health & Fitness. **Contact:** your email and https://ricardouzcategui.com. **Privacy policy:** https://rick-pro.github.io/stride-android/privacy.html (from section 1).

## 5. Store assets (in `assets/play-store/`)
An agent makes these, in the PR that builds the app, from the repo's own art and screenshots it already has from running the
app. Nobody should make them by hand.

| Asset | Size | In the repo |
|---|---|---|
| App icon | 512 x 512 PNG, up to 1 MB | `icon-512.png` |
| Feature graphic (banner) | 1024 x 500 | `feature-graphic-1024x500.png` |
| Phone screenshots | 3 or more, 9:16 or 16:9, 1152 x 2048 here | `screenshots/01-control.png`, `02-history.png`, `03-setup.png` |
| 7-inch and 10-inch tablet | the same three screenshots | reuse the phone files |

- `make_assets.py` renders the icon and the feature graphic from `ic_launcher_foreground` on the `#0F1419` background. Run it
  again if the icon changes.
- Screenshot rules: real captures from the running app, never mock-ups. Each side 320 to 3840 px (10-inch tablet: 1080 to
  7680 px), and the long side at most twice the short side. Play wants at least 2 phone screenshots, and at least 4 at
  1080 px or larger to be eligible for promotion.
- A raw Pixel screenshot (1008 x 2244, about 2.2:1) is **rejected**. Crop out the status and navigation bars, then paste it
  centered on a canvas in the app's background color at 1152 x 2048.
- Uploading several files at once can land them in reverse order. Check the order after the upload and drag to fix it.
- The 7-inch and 10-inch slots are asked for even by a phone-only app. Reuse the phone screenshots.
- The listing also asks whether the assets are AI-generated. Answer it truthfully.

## 6. App content forms
- **Data safety:** *Does the app collect or share any of the required user data types?* **No.** Nothing is sent off the
  device (the profile, walks and settings stay in private storage). If the form asks about encryption in transit or data
  deletion, say there is no data collected, so neither applies.
- **App access:** everything works without a login. **Ads:** none. **News, government, financial features:** none.
- **Target audience:** 18 and over (not a children's app). **Health:** if the console shows a health apps declaration, say
  Stride is a fitness utility, not a medical app, and does not use Health Connect.
- **Content rating:** complete the questionnaire (no violence, no user content, no data sharing). Expect "Everyone".
- **Permissions:** Nearby devices (Bluetooth scan with `neverForLocation`, and connect) and Vibrate. Reason: find and control the treadmill.
- **Target API:** Stride targets API 37, which is fine.
- **Donation link:** the About screen has a Support Stride row that opens Buy Me a Coffee in the browser. Google Play's payments
  policy limits apps that ask for money outside Google Play Billing, and a tip link may be read that way. Read the current policy
  text in the Play Console help before the closed test. If it is a problem, tell Claude Code and the Play build ships without the
  row (the GitHub build can keep it).
- **Trader status (EU):** a legal declaration for the account owner. The console shows a banner with a deadline. It does not block
  the review, but do it before the deadline.

## 7. Closed testing and sending the app for review
The Publishing overview's **Send app for review** stays locked until a release exists on a track, even when every dashboard task
is done. Make the release first:

1. Testing, Closed testing, the **Alpha** track, Create new release. Upload `stride-vX.Y.Z.aab` from the GitHub release, check the
   release notes, Next.
2. The track page has four steps: Select countries (all of them), Select testers, Preview and confirm, Send for review. Set
   the countries first: Preview and confirm shows an error until at least one country is selected.
3. Testers: Create email list (the list is shared by every app in the account, so give it a general name), add the emails, tick the
   list, Save. One email is enough to send the release for review.
4. Preview and confirm: read the errors and warnings (section 9), Save, Go to overview.
5. Publishing overview, **Send N changes for review**. The console first runs its own checks (up to about 15 minutes) and sends
   the changes as soon as they pass. Google says reviews usually take up to 7 days.

For production, a personal developer account created after November 2023 must run a **closed test with at least 12 testers opted
in for 14 days in a row**, then apply for production access. As of this writing; check the console for the current numbers.
Fix what testers report with a new version: bump `VERSION` in the fix PR, the merge publishes the release, upload its new `.aab`.
The 14 days run on the track, not on a version.

## 8. Production
After Google grants access: Production, create a release, upload the `.aab`, write release notes from the README What's new
row, review, and roll out. Keep the README in step with the store listing. Stride is open source under the MIT license
(`LICENSE`), so the listing may say so and link the repo; keep out "free of charge forever", "popular" and "reviewed" claims
that the app does not earn. When the app is live, update the README Install section, which still says Stride is not on Google Play.

## 9. Warnings to clear on the next upload
Play showed these for 1.0.1. Issue #20 tracks the fix; this page changes when it lands.
- **No native debug symbols.** The bundle has native code (arm64-v8a, armeabi-v7a, x86, x86_64) and no debug symbols.
- **DEX code optimization: Low.** Obfuscation is 0% because of `-dontobfuscate` in `app/proguard-rules.pro`.
- **16 KB page size.** Play says "Supports 16 KB" and warns it cannot see everything. Verify the native libs are aligned.

## 10. Things that bite
- **The package name** cannot change after the first upload.
- **Send app for review is locked** until a release exists on a track. Create the closed test release first.
- **A closed test release shows an error** ("No countries or regions have been selected for this track") until countries are set.
- **Screenshots:** wrong aspect ratio is rejected, and multi-file uploads can reverse. See section 5.
- **A description built around one model** loses most of the people the app is for. See section 4.
- **The app from Play and the APK from GitHub** have different signatures. Pick one channel per phone.
- **Every lesson goes in two places:** this page (and the template's), and a CI check where a machine can check it.
