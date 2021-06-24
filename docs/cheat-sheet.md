# Cursorless: Cheat sheet
See also the [full docs](index.md) for more information.

## Table of contents
- [Cursorless: Cheat sheet](#cursorless-cheat-sheet)
  - [Table of contents](#table-of-contents)
  - [Targets](#targets)
    - [Primitive targets](#primitive-targets)
      - [Marks](#marks)
        - [Decorated symbol](#decorated-symbol)
          - [Colors](#colors)
        - [Last mark](#last-mark)
        - [Cursor](#cursor)
      - [Transformations](#transformations)
        - [Syntactic scopes](#syntactic-scopes)
        - [Scopes with siblings](#scopes-with-siblings)
        - [Subword](#subword)
        - [Lines](#lines)
        - [File](#file)
    - [Compound targets](#compound-targets)
      - [Range targets](#range-targets)
      - [List targets](#list-targets)
  - [Actions](#actions)
    - [Move cursor](#move-cursor)
    - [Selection](#selection)
    - [Delete](#delete)
    - [Cut / Copy](#cut--copy)
    - [Swap](#swap)
    - [Insert empty lines](#insert-empty-lines)
    - [Rename](#rename)
    - [Insert/Use/Repeat](#insertuserepeat)
    - [Wrap](#wrap)
    - [Show definition/reference/quick fix](#show-definitionreferencequick-fix)
    - [Fold/unfold](#foldunfold)
    - [Extract](#extract)

## Targets
### Primitive targets
#### Marks
##### Decorated symbol
* take air
* take blue air

###### Colors
* gray: default (optional: eg "take gray air" can be shortened to "take air")
* blue: blue
* green: green
* rose: red
* squash: yellow
* plum: mauve

##### Last mark
* take that
* post that

##### Cursor
Note that these all work with multiple cursors

* chuck this
* chuck this funk
* chuck funk ("this" is implied as the mark when omitted)
* pre funk

#### Transformations
##### Syntactic scopes
* take arg [blue] air
* take arrow [blue] air
* take call [blue] air
* take class [blue] air
* take comment [blue] air
* take element [blue] air
* take funk [blue] air
* take if [blue] air
* take key [blue] air
* take lambda [blue] air
* take list [blue] air
* take map [blue] air
* take pair [blue] air
* take state [blue] air
* take string [blue] air
* take value [blue] air

##### Scopes with siblings
* take every key [blue] air
* take every funk [blue] air
* etc

##### Subword
* take second word [blue] air
* take second through fourth word [blue] air
* take last word [blue] air

##### Lines
* take line [blue] air
* take line [blue] air past [blue] bat (second "line" is implied)
* take lines in funk [blue] air

##### File
* copy file
* pre file
* copy file [blue] air (if [blue] air is in another split)

### Compound targets
#### Range targets
* take [blue] air past [green] bat
* take past [blue] air
* take past before [blue] air
* take after [blue] air past before [blue] bat
* take past end of line
* take past start of line

#### List targets
* take [blue] air and [green] bat
* take funk [blue] air and [green] bat (note second target inherits "funk")
* take funk [blue] air and token [green] bat

## Actions

### Move cursor
* pre [blue] air
* post [blue] air

### Selection
* take [blue] air

### Delete
* chuck [blue] air
* clear [blue] air

### Cut / Copy
* carve [blue] air
* copy [blue] air

### Swap
* swap with [blue] air
* swap [blue] air with [green] bat
* swap funk [blue] air with [green] bat ("funk" is implied for second target)
* swap funk [blue] air with token [green] bat

### Insert empty lines
* drink [blue] air
* pour [blue] air

### Rename
* rename [blue] air

### Insert/Use/Repeat
* bring [blue] air
* bring [blue] air to [green] bat

### Wrap
* square wrap [blue] air
* round wrap [blue] air
* curly wrap [blue] air
* (diamond | angle) wrap [blue] air
* quad wrap [blue] air
* twin wrap [blue] air
* escaped quad wrap [blue] air
* escaped twin wrap [blue] air
* puff [blue] air
* wrap [blue] air with funk FUNCTION_NAME

### Show definition/reference/quick fix
* def show [blue] air
* ref show [blue] air
* hover show [blue] air
* quick fix [blue] air

### Fold/unfold
* fold [blue] air
* unfold [blue] air

### Extract
* extract [blue] air
* extract [blue] air as my variable