# Cursorless - Instructions
See also the [cheat sheet](cheat-sheet.md) for a terse reference once you understand the concepts.

## Table of contents
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
[color] (letter | symbol | number)

* `air`
* `blue air`
* `blue dash`
* `blue five`

eg:  
`take blue air`  
Selects the token containing letter 'a' with a blue hat.

###### Colors
Gray is optional: `gray air` and `air` are equivalent

|Command|Visible color|
---|---
|`gray`|default|
|`blue`|blue|
|`bgreen`|green|
|`rose`|red|
|`squash`|yellow|
|`plum`|mauve|

##### Last mark
* that

eg:  
`take that`  
Select the token containing the last mentioned marker.

##### Cursor
Is no mark is given the current cursor/cursors is used as the taget

* `chuck this`
* `take this funk`
* `pre funk`
* `chuck line`

#### Transformations
Expand the marker to the containing scope.

##### Syntactic scopes
* arg
* arrow
* call
* class
* comment
* element
* funk
* if
* key
* lambda
* list
* map
* pair
* state
* string
* value

eg:  
`take function blue air`  
Selects the function including the token containing letter 'a' with a blue hat. 

##### Scopes with siblings
* every

eg:  
`take every key [blue] air`  
Selects every key in the map/object/dict including the token containing letter 'a' with a blue hat. 

##### Subword
Narrow marker to subword in a camelCase/kebab-case/snake_case.

* second word
* second through fourth word
* last word

eg:  
`take second through fourth word blue air`  
Selects the second, third and fourth subword in the token containing letter 'a' with a blue hat.

##### Lines
* line

eg:  
`take line [blue] air`  
Selects the line including the token containing letter 'a' with a blue hat. 

##### File
* file

eg:  
`take file [blue] air`  
Selects the file including the token containing letter 'a' with a blue hat. 

### Compound targets
#### Range targets
* past [blue] air
* [blue] air past [green] bat
* past before [blue] air
* past end of line
* past start of line

eg:  
`take blue air past green bat`  
Selects the range from the token containing letter 'a' with a blue hat past the token containing letter 'b' with a green hat.

#### List targets
* [blue] air and [green] bat

eg:  
`take blue air and green bat`  
Selects both the token containing letter 'a' with a blue hat AND the token containing 'b' with a green hat.

## Actions
Perform actions on the token containing the marker.

### Move cursor
* pre
* post

eg:  
`pre blue air`  
Moves the cursor to before the token containing letter 'a' with a blue hat.

### Selection
* take

eg:  
`take blue air`  
Selects the token containing letter 'a' with a blue hat.

### Delete
* chuck
* clear

eg:  
`chuck blue air`  
Deletes the token containing letter 'a' with a blue hat.

### Cut / copy
* carve - cut
* copy

eg:  
`copy blue air`  
Copies the token containing letter 'a' with a blue hat.

### Swap
* swap with {MARKER}
* swap {MARKER1} with {MARKER2}

eg:  
`swap blue air with green bat`  
Swaps places on the tokens.

### Insert empty lines
* drink - Insert above
* pour - Insert below

eg:  
`pour blue air`  
Insert empty line below the token containing letter 'a' with a blue hat.

### Rename
* rename

eg:  
`rename blue air`  
Rename the token containing letter 'a' with a blue hat.

### Insert/Use/Repeat
* bring {MARKER}
* bring {MARKER1} to {MARKER2}

eg:  
`bring blue air to green bat`  
Replaces the token containing letter 'b' with a green hat using the token containing letter 'a' with a blue hat.

### Wrap
* square wrap - [ ]
* round wrap - ( )
* curly wrap - { }
* (diamond | angle) wrap - < >
* quad wrap - " "
* twin wrap - ' '
* escaped quad wrap - \" \"
* escaped twin wrap - \' \'
* puff - \n \n
* wrap {MARKER} with funk {FUNCTION_NAME} - FUNCTION_NAME( )

eg:  
`square wrap blue air`  
Wraps the token containing letter 'a' with a blue hat in square brackets.

### Show definition/reference/quick fix
* def show
* ref show
* hover show
* quick fix

eg:  
`def show blue air`  
Shows definition for the token containing letter 'a' with a blue hat.

### Fold/unfold
* fold
* unfold

eg:  
`fold blue air`  
Fold line for the token containing letter 'a' with a blue hat.

### Extract
* extract {TOKEN}
* extract {TOKEN} as my variable

eg:  
`extract blue air`  
Extracts the token containing letter 'a' with a blue hat as its own statement.