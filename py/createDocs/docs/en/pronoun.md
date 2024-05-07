{page_header}

## List of pronouns

Pronouns are listed in the following table.

||English|SFGPL|
|:-:|:-:|:-:|
|First Person Pronoun|I|{pronoun_I}|
|Second Person Pronoun|you|{pronoun_you}|
|Third Person Pronoun|he/she/it|{pronoun_he}|
|Proximate Pronoun|this|{pronoun_proximal}|
|Distant Pronoun|that|{pronoun_distal}|
|Interrogative Pronoun|what|{pronoun_interrogative}|
|Indefinite Pronoun|something|{pronoun_indefinite}|

## Pronoun applications

As a rule, SFGPL pronouns do not distinguish between people, organisms, objects, concepts, places, times, reasons, methods, etc.
There is no distinction based on gender or number.
These distinctions can be made by using [noun determiner]({docs_DeterminerN}).

### Interrogative word

The following table shows the use of noun determiners for interrogatives.

|English|SFGPL|
|:-:|:-:|
|what|{pronoun_what}|
|who|{pronoun_who}|
|when|{pronoun_when}|
|where|{pronoun_where}|
|why|{pronoun_why}|
|how|{pronoun_how}|

### Plural pronouns

To indicate plurals, use ```{determinerN_plural}```.
For example, ```{pronoun_we}``` is used to denote "We".

#### Clusivity of person pronoun

In particular, the plural of first-person pronouns may be distinguished based on whether they include the speaker or the addressee.
The SFGPL cannot directly distinguish between these, but it can do so by doing the following.

||Include the addressee|Exclude the addressee|
|:-:|:-:|:-:|
|Include the Speaker|```{clusivity_II}```|```{clusivity_IE}```|
|Exclude the Speaker|```{clusivity_EI}```|```{clusivity_EE}```|

### Examples of conjugation of third person pronouns

Gender distinctions do not exist in the SFGPL.
Nor is there a distinction between persons and things.
For example, to make explicit the third person pronouns masculine, feminine and thing, one can do the following.

||English|SFGPL|
|:-:|:-:|:-:|
|male|he|{pronoun_he_male}|
|female|she|{pronoun_he_female}|
|thing|it|{pronoun_he_thing}|

### Possessive and Recursive pronouns

In addition, you can create possessive and reflexive pronouns using ```{determinerN_possessive}``` and ```{determinerN_reflexive}```.
The following table shows the possessive and reflexive pronouns for first person pronouns.

||English|SFGPL|
|:-:|:-:|:-:|
|Possessive Pronoun|mine|{mine}|
|Reflexive Pronoun|myself|{myself}|
