# Pengyuan Wu — academic homepage

English academic website built from [Academic Pages](https://github.com/academicpages/academicpages.github.io), powered by Jekyll and hosted on GitHub Pages.

**Website:** https://wupengyuan.github.io/

The site contains About, Publications, and CV pages, a responsive layout, light and dark themes, and downloadable BibTeX citations. Only publicly released papers are included.

## Update content

| File | Content |
| --- | --- |
| `_config.yml` | Site address, email, GitHub, and Google Scholar links |
| `_pages/about.md` | English introduction and homepage structure |
| `_data/profile.yml` | Education, experience, awards, and research interests |
| `_data/papers.yml` | Publication metadata, author lists, and resource links |
| `files/*.bib` | BibTeX citations for the linked public versions |
| `images/research/` | Attributed figures from the papers |
| `_sass/_academic.scss` | Personal styles and responsive layouts |

To add a portrait, put the image in `images/` and add `avatar: /images/your-photo.jpg` under `author:` in `_config.yml`. Until then, the site uses an initials monogram.

## Run locally

Use Ruby 3.3 and Bundler:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://127.0.0.1:4000/.

To build and check links:

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check-site.py
```

## Deployment

GitHub Pages must use **GitHub Actions** as its build source. Every push to `master` or `main` runs `.github/workflows/jekyll.yml`, builds the site, checks internal links, and deploys it. No API token belongs in this repository.

Content provenance is recorded in [SOURCE_NOTES.md](SOURCE_NOTES.md). The original private CV is not published. The Academic Pages / Minimal Mistakes license is retained in [LICENSE](LICENSE).
