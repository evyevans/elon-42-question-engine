# Validation scope

The integrated repository was checked on 2026-10-20 with the bundled static validator, its automated regression tests, archive layout and CRC checks, and a byte-for-byte comparison of the repository and supplied package licenses. LICENSE remains unchanged, including the existing copyright notice.

Static checks cover required files, basic frontmatter fields and limits, matching skill directory name, relative Markdown links, UTF-8 text, forbidden package artifacts, and unique scenario IDs in the manual test tables. Root Git metadata is excluded so checks work in both a source package and a repository checkout. The validator uses the Python standard library; it is not the official Agent Skills reference validator and is not a full YAML parser.

The automated validator tests cover a source package, Git directory and worktree metadata, rejection of sensitive files and ZIP artifacts, and broken relative references. The 42 behavioral scenarios are manual specifications awaiting execution. No live model evaluations, native client installation tests, releases, or security certifications are claimed. Git publication is verified separately after committing; it is not established by these checks.

The existing README banner URL was fetched successfully and visually inspected on 2026-10-20. It serves a 1376 × 768 JPEG showing a glowing network question mark, a thinking figure, and the text "THE RIGHT QUESTION COMES FIRST" and "Question first. Build second." The verified GitHub attachment URL is retained with descriptive alt text. No local original binary was supplied, so no banner file or assets table entry was added. Remote availability can change; static validation does not check remote URLs.

To repeat the local checks from this directory:

```bash
python3 scripts/validate.py
python3 scripts/test_validate.py
```
