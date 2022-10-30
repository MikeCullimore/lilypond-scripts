# Lilypond scripts

Goal: generate sheet music for piano sight reading app.

## Setup

Download GNU Lilypond [here](https://lilypond.org/download.html).

## How to call Lilypond

To run Lilypond with an input file `test.ly`, saving to a folder `folder`, do:

```
lilypond --svg --output=folder test.ly
```

## Sumarry of relevant Lilypond notation

### Pitch

* Clef defaults to treble. For bass clef add `\clef bass`.
* For scales it is easiest to use relative pitches: `\relative`. The first note will be absolute and following notes will be relative to it (e.g. the closest D).
* To raise the first note by an octave, use `'`, to lower it by an octave use `,` e.g. middle C is `c'`.
* Specify the key signature as e.g. `\key c \major`.
* [Lilypond docs on pitch](https://lilypond.org/doc/v2.23/Documentation/notation/writing-pitches)

### Fingering

* Simply add a dash and a number after the note to add fingering direction e.g. `c-5`.
* For fingering indications below the notes: `\override Fingering.direction = #DOWN`.
* [Lilypond docs on fingering](https://lilypond.org/doc/v2.23/Documentation/learning/within_002dstaff-objects)

## todo

* Summarise notation for duration.
* Remove time signature and bar lines.
* Extend to guitar: chord diagrams and strum rhythms.
* Possible to import common config from separate file?
* Improve SVG output:
    * Remove metadata e.g. file paths.
    * Make the images compatible with React. Workaround hack: compress the SVG using [this site](https://jakearchibald.github.io/svgomg/) (default settings) as suggested in [this post](https://github.com/facebook/create-react-app/issues/11770)
    * Remove page footer then crop to content (not page of A4!).
