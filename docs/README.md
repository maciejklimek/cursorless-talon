# Cursorless - Instructions
You may find it helpful to start with the [tutorial video](https://www.youtube.com/watch?v=JxcNW0hnfTk).

See also the [cheat sheet](cheat-sheet.md) for a more compact reference once you understand the concepts.

## Table of contents
- [Table of contents](#table-of-contents)
- [Overview](#overview)
- [Targets](#targets)
  - [Primitive targets](#primitive-targets)
    - [Marks](#marks)
      - [Decorated symbol](#decorated-symbol)
        - [Colors](#colors)
      - [`"this"`](#this)
      - [`"that"`](#that)
    - [Transformations](#transformations)
      - [Syntactic scopes](#syntactic-scopes)
      - [Syntactic scopes with siblings](#syntactic-scopes-with-siblings)
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
  - [Cut / copy](#cut--copy)
  - [Swap](#swap)
  - [Insert empty lines](#insert-empty-lines)
  - [Rename](#rename)
  - [Insert/Use/Repeat](#insertuserepeat)
  - [Wrap](#wrap)
  - [Show definition/reference/quick fix](#show-definitionreferencequick-fix)
  - [Fold/unfold](#foldunfold)
  - [Extract](#extract)
  

## Overview
Every cursorless command consists of an action performed on a target. For example, the command `"chuck blue air"` deletes the token with a blue hat over the `"a"`. In this command, the action is `"chuck"` (delete), and the target is `"blue air"`.

## Targets
There are two types of targets: primitive targets and compound targets. Compound targets are constructed from primitive targets, so let's begin with primitive targets.

### Primitive targets
A primitive target consists of a mark and an optional transformation. The simplest primitive targets just consist of a mark, so let's begin with those

#### Marks
There are several types of marks:

##### Decorated symbol
This is the first type of mark you'll notice when you start using cursorless. We can refer to any token on the screen by the hat that is over a particular character within that token:

* `"air"` (if the color is gray)
* `"blue bat"`
* `"blue dash"`
* `"blue five"`

The general form of this type of mark is:

`"[<color>] (<letter> | <symbol> | <number>)"`

Combining this with an action, we might say `"take blue air"` to select the token containing letter `'a'` with a blue hat over it.

###### Colors
The following colors are supported. As mentioned above, note that gray is optional: `"gray air"` and `"air"` are equivalent

|Command|Visible color|
---|---
|`"gray"`|default|
|`"blue"`|blue|
|`"green"`|green|
|`"rose"`|red|
|`"squash"`|yellow|
|`"plum"`|mauve|


##### `"this"`
The word `"this"` can be used as a mark to refer to the current cursor(s) or selection(s). Note that when combined with a transformation, the `"this"` mark can be omitted, and it will be implied.

* `chuck this`
* `take this funk`
* `pre funk`
* `chuck line`

##### `"that"`
The word that can be used as a mark to refer to the target of the previous cursorless command.

* `"pre that"`
* `"round wrap that"`

#### Transformations
Transformations can be applied to any mark to modify its extent. This is commonly used to refer to larger syntactic elements within a source code document. 

Note that if the mark is `"this"`, you have multiple cursors, the transformation will be applied to each cursor individually.

##### Syntactic scopes
|Term|Syntactic element|
---|---
 `"arg"` | function parameter or function call argument
 `"arrow"` | anonymous lambda function
 `"call"` | function call, eg `foo(1, 2)`
 `"class"` | class definition
 `"comment"` | comment
 `"element"` | list element
 `"funk"` | function definition
 `"if"` | if statement
 `"key"` | key in a map / object
 `"lambda"` | equivalent to `"arrow"`
 `"list"` | list
 `"map"` | map / object
 `"pair"` | an entry in a map / object
 `"state"` | a statement, eg `let foo;`
 `"string"` | string
 `"value"` | a value in a map / object

For example, `"take funk blue air"` selects the function containing the token with a blue hat over the letter `'a'`. 

##### Syntactic scopes with siblings
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