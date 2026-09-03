# Classical Mechanics

Course materials for Classical Mechanics at Smith College (first taught by
me; Smith's course is PHY 317). Structure mirrors my
[MathematicalPhysics](https://github.com/mglerner/MathematicalPhysics) repo:
public materials here, organized by topic as they develop, with
current-semester planning in `SyllabusAndFirstDay/<year>/`.

Non-public materials (solutions, exams, grades, other professors' files —
including the previous professor's course archive) live in `private/`, a
gitignored symlink to `~/Dropbox/__Smith/Classes/317-Classical/private/`.
Dropbox is the backup; nothing under `private/` goes to GitHub.

Textbook: Taylor, _Classical Mechanics_ (following Will Raven's Fall 2025
PHY 317). First offering: Fall 2026; planning in `SyllabusAndFirstDay/2026/`.

## Notebooks

Class notebooks are Jupyter, meant to run on posit.smith.edu (JupyterLab)
and interactive via ipywidgets. They are committed **without outputs**:
`nbstripout` is installed as a git clean filter (`.gitattributes`), so a
working copy can be run and saved with its plots intact and git still
sees only the source. On a fresh clone, run once:

    nbstripout --install --attributes .gitattributes

(the filter definition lives in `.git/config`, which is not cloned; the
`courses/` uv venv has `nbstripout`). After running a notebook locally,
`git status` may list it as modified even though `git diff` is empty;
`git add` clears that and commits nothing. To keep outputs for a specific
notebook or directory, exempt it in `.gitattributes` (`-filter -diff`) or
tag cells `keep_output`; see the comments there.
