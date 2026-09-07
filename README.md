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

Class notebooks are Jupyter, meant to run on jupyterhub.smith.edu (JupyterLab)
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

## Notebook conventions (both courses, settled 2026-09-07)

Every notebook students touch reads **in order of use**, top to bottom:

1. Title + a few lines of physics context (the equations it uses).
2. **"1. Predict first (before you run anything)"**: two or three concrete
   questions, then an EMPTY markdown cell reading `*(your prediction
   here)*` with the instruction "double-click, type, Shift-Enter".
   Predictions at the end never get written.
3. Numbered sections in order of use ("2. Setup", "3. ...").
4. A "What you found" section at the end with its own empty answer
   cell(s); homework notebooks get one empty cell per question.

Code style, for students who may be seeing Python for the first time:
first code cell starts with `%matplotlib inline` (the hub defaults to
ipympl, which stacks figures inside `interact`); short named functions
rather than lambdas; time in seconds on every axis (no normalized units
such as t/T0); one or two sliders, not five; one idea per cell; no
try/except scaffolding. Every cell has an `id` (nbformat >= 4.5).
Commit without outputs (nbstripout filter). Moodle never gets an
uploaded copy: link the GitHub page of the notebook
(`https://github.com/mglerner/ClassicalMechanics/blob/main/...`), which
is always the clean, current version; students use its download button
and upload to jupyterhub.
