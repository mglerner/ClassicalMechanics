# What was actually looked at for the handout's references

Checked 2026-11-06. "Listing" means the publisher's or Crossref's bibliographic record
(title, authors, journal, volume, pages, year), saved here as `texts/crossref-<DOI>.json`.
"Full text" means the paper itself, saved here with a `pdftotext` extraction beside it.

| Reference (handout number) | Wikipedia article that cites it | What was seen | File here |
|---|---|---|---|
| Taylor (course text) | -- | the book | -- |
| Murray and Dermott 1999 | Jacobi integral; Lagrange point | table of contents only (CUP page, the book's QMUL companion site) | -- |
| Goldstein, Poole and Safko 2002 | -- | table of contents only (Section 3.12 title and page) | -- |
| Peebles 1980 | -- | table of contents only (UPenn catalog record) | -- |
| Bruns 1887, Acta Math. 11 | Heinrich Bruns, under its Leipzig printing only | listing only | `texts/crossref-10.1007_BF02612319.json` |
| Poincare 1890, Acta Math. 13 | Chaos theory | listing only | `texts/crossref-10.1007_BF02392506.json` |
| Sundman 1912, Acta Math. 36 | n-body problem; Karl F. Sundman | listing only (Crossref dates the volume 1913) | `texts/crossref-10.1007_BF02422379.json` |
| Belorizky 1930, Bull. Astron. 6 | Three-body problem (which also quotes the 10^8,000,000 figure) | listing and the Persee preview of p. 417 only; the 10^8,000,000 figure is Wikipedia's and Diacu's, not read in the 1930 text | `texts/crossref-10.3406_bastr.1930.14038.json` |
| Diacu 1996, Math. Intelligencer 18 | Three-body problem; n-body problem | listing only | `texts/crossref-10.1007_BF03024313.json` |
| Barrow-Green 2010, Historia Math. 37 | Three-body problem; Karl F. Sundman | listing only | `texts/crossref-10.1016_j.hm.2009.12.004.json` |
| Gascheau 1843, C. R. 16 | Point de Lagrange (French), with pp. 393-394 | listing only (the French article's entry and Sicardy's reference list) | -- |
| Sicardy 2010, Celest. Mech. Dyn. Astron. 107 | Point de Lagrange (French) | full text (author's copy, lesia.obspm.fr) | `texts/Sicardy-2010-CMDA-107-145.pdf`, `.txt` |
| Deprit and Deprit-Bartholome 1967, Astron. J. 72 | -- | listing only; the two resonant mass ratios as quoted by Sicardy (p. 2 of his paper) | `texts/crossref-10.1086_110213.json` |
| Greenberg and Davis 1978, Am. J. Phys. 46 | -- | abstract only (AIP page, not saved) | `texts/crossref-10.1119_1.11492.json` |
| Edlund 2024, Am. J. Phys. 92 | -- | full text (author's copy, facultyweb.cortland.edu) | `texts/Edlund-2024-AJP-92-414.pdf`, `.txt` |
| Thomson and Tait 1879, Treatise, Part I | -- | Sec. 345 (pp. 387-393) read in the archive.org OCR of the 1912 reprint; the no-stability-with-dissipation sentence is Sec. 345 vi, p. 391 | `texts/Thomson-Tait-1879-section-345-extract.txt`, full OCR `texts/Thomson-Tait-1879-Treatise-Part-I-1912-reprint-archive.org-OCR.txt` |
| Kirillov and Verhulst 2010, ZAMM 90 | -- | full text (arXiv 0906.1650 version) | `texts/Kirillov-Verhulst-2010-ZAMM-90-462-arXiv-0906.1650.pdf`, `.txt` |
| Wikipedia articles | -- | wikitext as of 2026-11-06 | `wikipedia/*.wikitext` |

Sources of the copies: Sicardy from <https://www.lesia.obspm.fr/perso/bruno-sicardy/biblio/biblio/Sicardy_Gascheau_CelMec10.pdf>;
Edlund from <https://facultyweb.cortland.edu/eric.edlund/portfolio/research/publications/Edlund-AJP2024.pdf>;
Kirillov and Verhulst from <https://arxiv.org/pdf/0906.1650>; Thomson and Tait from
<https://archive.org/details/treatiseonnatura01kelvuoft> (the 1912 reprint of the 1879 edition);
Wikipedia from each article's `action=raw` URL.
