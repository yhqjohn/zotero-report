import numpy, pandas as pd


df = pd.read_csv('./data.csv')
summary = ''
with open('zotero_report_template.md', encoding='utf-8') as f:
    template = f.read()
    
for _, items in df.iterrows():
    items = dict(items)
    items = [items[key] for key in [
        'Title',
        'Author',
        'Publication Title',
        'Date', 'DOI', 'Url',
        'Abstract Note',
    ]]
    title, author, publication_title, date, doi, url, abstract = items 
    content = template.format(title=title, author=author, publication_title=publication_title,
                              date=date, doi=doi, url=url, abstract=abstract)
    summary+=content

with open('summary.md', 'w', encoding='utf-8') as f:
    f.write(summary)
