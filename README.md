# FLOODWARRIOR website

Website source for https://github.com/ryanxunhuan/floodwarrior and GitHub Pages
hosting.

## Preview

Run `python3 -m http.server 4173 --bind 127.0.0.1` from this directory and open
http://127.0.0.1:4173. Pages also open directly in a browser. No build or
installation step is needed. Fonts load from Google Fonts with local fallbacks.
Internal paths support the `/floodwarrior/` project URL.

## Content and editing

- `index.html`: project name, Detroit Arsenal collaboration, two StoryMaps,
  six research teams in Physical/Human/Decision pairs, publication highlights,
  leadership, and media coverage. Publication highlights represent Vinh/Valeriy,
  Kevin/Francina, and John/Sarah; the latter two are public preprints.
- `research/`: one page per team with research descriptions and figures.
  Physical Sciences pairs Atmospheric Science and Flood Science; Human Sciences
  pairs Anthropology and Decision Support & Visualization; Decision Sciences
  pairs Uncertainty Quantification and Decision Science.
- `team.html`: 30 members, combining the March 30, 2026 meeting roster
  with the project PI’s additions and alumni corrections. Xun Huan and
  Valeriy Ivanov are PIs; the other four faculty are co-PIs. Each investigator
  has a public university email link. Each team uses one continuous grid, ordered by position category and surname,
  with current members before alumni. Alumni retain their project role with an
  “(Alumni)” label and a subsequent position where verified or supplied by the PI.
- `publications.html`: 22 public records, with search and status filters.
  The bibliography has 13 published records, 6 preprints, and 3 other outputs, including Whitaker et al. (2026) in Human Organization.
  Manuscripts without confirmed public citations remain for a later update.
- `credits.html`: the website’s public attribution page, linked from every footer,
  with sources for the photographs, logos, portraits, and figures. The separate
  illustrated source-and-permissions review stays outside this website.
- `assets/styles.css`: typography and responsive page layouts.
- `assets/site.js`: Research dropdown dismissal. The menu works without it.
- `assets/bibliography.js`: optional bibliography search and status filters.
- `data/`: public metadata corresponding to the displayed content.

Text can be edited directly in the HTML files through GitHub's browser editor.
Use a branch and pull request when suggesting changes for review. The JSON files
are reference metadata; changes there do not automatically regenerate the HTML.
Keep repeated navigation and footer wording consistent across the ten pages.

The site uses larger type, short introductory copy, original research figures,
and full-resolution figure links. Claims preserve the scope of synthetic
studies, numerical experiments, proposed models, and early prototypes.

## Funding acknowledgment

This work is supported by the Department of the Navy under awards
N000142312735 (MURI) and N000142512411, issued by the Office of Naval Research.
The award details were supplied by the project PI. Add any required agency
notice before public release.

## Collaboration

Use branches and pull requests for proposed changes. GitHub Pages serves the
published site from the repository's configured Pages source.

## Source handling

All supplied Dropbox originals remain untouched. Raw proposals, reports,
meeting decks, extracted text, and internal verification notes stay outside
this repository and its history. The draft contains only the selected web
assets and content requested by the user.

The March 2026 meeting materials supply five team figures and 14 team portraits.
The UQ figure is the unaltered left panel of Figure 8 from Cheng et al.,
arXiv:2608.21182v1, downloaded from its public HTML source. Its version-specific
credit links to the full figure; arXiv hosting is not a general open reuse license.
Public institutional profiles supply five faculty portraits and the Brian Jewett, Kevin Gray, Deffi Putri, Caleb
Dahlke, Tsedeniya Amare, Ishika Joshi, and Remi Masterson photographs. Xun Huan
supplied his portrait. Portraits use consistent frames with individual
positioning; original image files are retained. Initials stand in for the
three portraits still awaiting verification or a source image. Logos identify the
participating institutions. Image sources and applicable figure licenses appear
on the credits page; no general open license is inferred for supplied images.
The WRF and stormwater highlights use credited project meeting illustrations;
these are distinguished from figures taken from a paper. The hero uses the
unaltered 5760×3240 NASA Landsat original, using a wider Detroit-centered view
framed with page styles.
The roster incorporates PI corrections supplied in October 2026. Project
title for Shormila Sarker awaits confirmation. Weichen Huang is a PhD Student. Duc Hai
Nguyen’s candidate photograph awaits identity confirmation. Subsequent
positions for Chen Cheng and Remi Masterson remain unverified. Caleb Dahlke is
now a Postdoctoral Fellow at the University of Michigan C-PRIME Center, as
supplied by the PI and corroborated by the center’s team page.
The membership details should be checked before release. Public citation metadata was checked in October 2026.

## Publication

Publish only after explicit approval. Remove draft markers, complete the final
content review, push the approved files, and configure Pages to serve the
approved branch's root directory. Intended public URL:
https://ryanxunhuan.github.io/floodwarrior/.
