# Cursorless - Instructions

## Marks

### Simple marks
[color] (letter | symbol | number)

* `air`
* `blue air`
* `blue dash`
* `blue five`

#### eg:
`take blue air`  
Selects the token containing letter 'a' with a blue hat.

### Colors
Gray is optional `gray air` and `air` is equal

|Command|Visible color|
---|---
|gray|default|
|blue|blue|
|green|green|
|rose|red|
|squash|yellow|
|plum|mauve|

### Ranged marks
* past [blue] air
* [blue] air past [green] bat
* past before [blue] air
* past end of line
* past start of line

#### eg:
`take blue air past green bat`  
Selects the range from the token containing letter 'a' with a blue hat past the token containing letter 'b' with a green hat.

### Multiple marks
* [blue] air and [green] bat
* every key [blue] air

#### eg:
`take blue air and green bat`  
Selects both the token containing letter 'a' with a blue hat AND the token containing 'b' with a green hat.

### Last mark
* that

#### eg:
`take that`  
Select the token containing the last mentioned marker.

### Subword
Narrow marker to subword in a camelCase/kebab-case/snake_case.

* second word
* second through fourth word
* last word

#### eg:
`take second through fourth word blue air`  
Selects the second, third and fourth subword in the token containing letter 'a' with a blue hat.


## Transformations
Expand the marker to the containing scope.

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

#### eg:
`take function blue air`  
Selects the function including the token containing letter 'a' with a blue hat. 

## Actions
Perform actions on the token containing the marker.

### Move cursor
* pre
* post

#### eg:
`pre blue air`  
Moves the cursor to before the token containing letter 'a' with a blue hat.

### Selection
* take

#### eg:
`take blue air`  
Selects the token containing letter 'a' with a blue hat.

### Delete
* chuck
* clear

#### eg:
`chuck blue air`  
Deletes the token containing letter 'a' with a blue hat.

### Cut / copy
* carve - cut
* copy

#### eg:
`copy blue air`  
Copies the token containing letter 'a' with a blue hat.

### Swap
* swap with {MARKER}
* swap {MARKER1} with {MARKER2}
#### eg:
`swap blue air with green bat`  
Swaps places on the tokens.

### Insert empty lines
* drink - Insert above
* pour - Insert below

#### eg:
`pour blue air`  
Insert empty line below the token containing letter 'a' with a blue hat.

### Rename
* rename

#### eg:
`rename blue air`  
Rename the token containing letter 'a' with a blue hat.

### Insert/Use/Repeat
* bring {MARKER}
* bring {MARKER1} to {MARKER2}

#### eg:
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

#### eg:
`square wrap blue air`  
Wraps the token containing letter 'a' with a blue hat in square brackets.

### Show definition/reference/quick fix
* def show
* ref show
* hover show
* quick fix

#### eg:
`def show blue air`  
Shows definition for the token containing letter 'a' with a blue hat.

### Fold/unfold
* fold
* unfold

#### eg:
`fold blue air`  
Fold line for the token containing letter 'a' with a blue hat.

### Extract
* extract {TOKEN}
* extract {TOKEN} as my variable

#### eg:
`extract blue air`  
Extracts the token containing letter 'a' with a blue hat as its own statement.