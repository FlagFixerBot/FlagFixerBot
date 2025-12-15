import pywikibot

site = pywikibot.Site('commons', 'commons')  # Connect to Commons

file_title = 'File:DeletedFlag.svg'
file_page = pywikibot.FilePage(site, file_title)

if not file_page.exists():
    placeholder = f"[[File:Copyrighted flag.svg|100px|link=w:{file_title}]]"
    comment = "<!-- Placeholder image; non-free file linked only -->"

    for page in file_page.embeddedin(namespaces=[0]):  # iterate over pages using file
        old_text = page.text
        new_text = old_text.replace(file_title, placeholder + "\n" + comment)
        # Dry-run: don't save, just print/log
        print(f"Would update page '{page.title()}':")
        print(new_text[:200], "...")  # preview first 200 characters
