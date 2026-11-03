#!/usr/bin/env python3
"""Render publications, news, and homepage news from their JSON records.

Run from any directory with Python 3. No third-party packages required.
"""
import calendar
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'journals': 'Journal Articles',
    'conferences': 'Conference Papers',
    'preprints': 'Preprints',
    'theses': 'Theses & Project Reports',
    'presentations': 'Presentations & Activities',
    'products': 'Software, Data & StoryMaps',
}
e = lambda value: escape(str(value), quote=True)

def dated(value):
    parts = str(value).split('-')
    if len(parts) == 1:
        return parts[0]
    return f'{calendar.month_name[int(parts[1])]} {parts[0]}'

def newest(records, key):
    # Missing month/day remain unspecified in the record and display. Within a
    # year, records with only a year follow those with known months/days.
    return sorted(records, key=lambda x: (tuple(int(v) for v in (x[key].split('-') + ['0', '0'])[:3]), x['title']), reverse=True)

def link(url, text):
    return f'<a href="{e(url)}">{e(text)}</a>' if url else e(text)

def entry(p):
    authors = p.get('authors', [])
    category = p['display_category']
    abbreviated = ', '.join(authors[:3]) + ' et al.' if len(authors) > 5 and category != 'presentations' else ', '.join(authors)
    venue = p['venue']
    citation_venue = f'{p["article_type"]}, {venue}' if category == 'theses' else venue
    full = ', '.join(authors) + f' ({p["year"]}). {p["title"]}. {citation_venue}'
    if p.get('volume'):
        full += ', ' + p['volume'] + (f'({p["issue"]})' if p.get('issue') else '')
    if p.get('pages'): full += ', pp. ' + p['pages']
    if p.get('article'): full += ', article ' + p['article']
    full += '.'
    citation = e(full)
    if p.get('doi'):
        citation += ' ' + link('https://doi.org/' + p['doi'], 'doi:' + p['doi'])
    notes = ''
    if p.get('public_note'): notes += f'<p class="pub-authors">{e(p["public_note"])}</p>'
    if p.get('last_revised'): notes += f'<p class="pub-authors">Preprint revised {dated(p["last_revised"])}.</p>'
    if category in ('presentations', 'products'):
        details = notes
    else:
        details = f'<details><summary>Citation<span class="sr-only"> for {e(p["title"])}</span></summary><p class="pub-authors">{citation}</p>{notes}</details>'
    title = link(p.get('url'), p['title'])
    if p.get('title_links'):
        title = ''.join(link(part.get('url'), part['text']) for part in p['title_links'])
    search = ' '.join([p['title'], ' '.join(authors), venue, str(p['year']), p['sort_date'], CATEGORIES[p['display_category']], p.get('doi') or '']).lower()
    kind = p.get('article_type', '')
    if kind in ['Journal article', 'Preprint', 'Conference paper']: kind = ''
    meta = ' · '.join(x for x in [dated(p['sort_date']), venue, kind] if x)
    return f'''<article class="publication bib-entry" id="{e(p['id'])}" data-category="{e(p['display_category'])}" data-date="{e(p['sort_date'])}" data-search="{e(search)}">
<p class="pub-meta">{e(meta)}</p>
<h3>{title}</h3>
<p class="citation-authors">{e(abbreviated)}</p>
{details}
</article>'''

def page_shell(title, page):
    original = (ROOT / 'publications.html').read_text()
    before = original.split('<main id="main">')[0]
    before = re.sub(r'<title>.*?</title>', f'<title>{title} | FLOODWARRIOR</title>', before)
    before = re.sub(r' aria-current="page"', '', before)
    before = before.replace(f'<a href="{page}"', f'<a href="{page}" aria-current="page"')
    footer = '<footer>' + original.split('<footer>', 1)[1].split('</footer>', 1)[0] + '</footer>'
    return before, footer

def news_entry(n, compact=False):
    description = '' if compact else f'<p class="news-meta">{e(n["type"])}' + (f' · {e(n["note"])}' if n.get('note') else '') + '</p>'
    return f'<article class="news-entry" id="{e(n["id"])}"><p class="pub-meta"><time datetime="{e(n["date"])}">{dated(n["date"])}</time> · {link(n.get("source_url"), n["source"])}</p><h3>{link(n["url"], n["title"])}</h3>{description}</article>'

def main():
    pubs = json.loads((ROOT / 'data/publications.json').read_text())
    news = json.loads((ROOT / 'data/news.json').read_text())
    for records in [pubs, news]:
        ids = [p['id'] for p in records]
        if len(ids) != len(set(ids)): raise ValueError('Duplicate record IDs')
    before, footer = page_shell('Publications & Products', 'publications.html')
    options = '<option value="all">All Types</option>' + ''.join(f'<option value="{k}">{e(v)}</option>' for k,v in CATEGORIES.items())
    jumps = ''.join(f'<a href="#{k}" data-group-link="{k}">{e(v)} <span>{sum(p["display_category"]==k for p in pubs)}</span></a>' for k,v in CATEGORIES.items())
    content = '<main id="main"><section class="page-heading section"><h1>Publications &amp; Products</h1></section><section class="section bibliography-section">'
    content += f'<div class="bib-controls" hidden><label for="bib-search">Search<input id="bib-search" type="search" placeholder="Title, author, venue, or year"></label><label for="bib-category">Type<select id="bib-category">{options}</select></label><p id="bib-count" role="status" aria-live="polite">{len(pubs)} records</p></div>'
    content += f'<div class="category-links" role="navigation" aria-label="Publication categories">{jumps}</div><p class="sort-label">Newest first within each category</p>'
    for key, name in CATEGORIES.items():
        rows = newest([p for p in pubs if p['display_category']==key], 'sort_date')
        content += f'<section class="bib-group" id="{key}" aria-labelledby="heading-{key}"><h2 id="heading-{key}">{e(name)} <span class="group-count">{len(rows)}</span></h2><div class="publication-list">' + '\n'.join(entry(p) for p in rows) + '</div></section>'
    content += '<p class="bib-empty" hidden>No matching records.</p></section></main>'
    (ROOT/'publications.html').write_text(before + content + footer + '<script src="assets/site.js" defer></script><script src="assets/bibliography.js?v=20261103-catalog" defer></script></body></html>\n')
    before, footer = page_shell('News & Updates', 'news.html')
    content = '<main id="main"><section class="page-heading section"><h1>News &amp; Updates</h1></section><section class="section news-archive" aria-label="All news and updates">'
    ordered = newest(news, 'date')
    for year in sorted({n['date'][:4] for n in news}, reverse=True):
        content += f'<section class="news-year" aria-labelledby="news-{year}"><h2 id="news-{year}">{year}</h2><div class="news-list">'
        content += ''.join(news_entry(n) for n in ordered if n['date'].startswith(year)) + '</div></section>'
    content += '</section></main>'
    (ROOT/'news.html').write_text(before + content + footer + '<script src="assets/site.js" defer></script></body></html>\n')
    home = (ROOT/'index.html').read_text()
    highlights = ''.join(news_entry(n, True) for n in ordered if n.get('featured'))
    section = '<section id="news" class="section media-section section-rule"><div class="section-heading-row"><h2>Selected News</h2><a class="text-link" href="news.html">All News &amp; Updates →</a></div><div class="news-list home-news">' + highlights + '</div><div class="section-return"><a href="#top" class="back-to-top"><span aria-hidden="true">↑</span> Back to Top</a></div></section>'
    home = re.sub(r'<section id="news".*?</section>', lambda _: section, home, flags=re.S)
    (ROOT/'index.html').write_text(home)
    print(f'Rendered {len(pubs)} catalog entries and {len(news)} news items.')

if __name__ == '__main__': main()
