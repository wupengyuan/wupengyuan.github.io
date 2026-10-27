# Pengyuan Wu — academic homepage

English academic website built from [Academic Pages](https://github.com/academicpages/academicpages.github.io), powered by Jekyll and hosted on GitHub Pages.

**Website:** https://wupengyuan.github.io/

The homepage contains a short introduction, all public publications, and selected honors. Background details are on a separate page. The site opens in light mode; visitors can switch themes manually.

## Update content

| File | Content |
| --- | --- |
| `_config.yml` | Site address, email, GitHub, and Google Scholar links |
| `_pages/about.md` | English introduction and homepage structure |
| `_data/profile.yml` | Selected education, experience, and honors |
| `_data/papers.yml` | Publication metadata, author lists, and resource links |
| `files/*.bib` | BibTeX citations for the linked public versions |
| `images/research/` | Attributed figures from the papers |
| `_sass/_academic.scss` | Personal styles and responsive layouts |

The portrait in `images/profile-photo.jpg` was supplied by the owner. To replace it, update `avatar:` under `author:` in `_config.yml`.

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
