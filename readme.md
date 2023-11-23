# Lilypond scripts

Goal: generate sheet music for piano sight reading app.

See also the [Node/TypeScript alternative](https://github.com/MikeCullimore/lilypond-ts).

## Setup

Download GNU Lilypond [here](https://lilypond.org/download.html).

## Run via CLI

Use the CLI provided to get just the cropped output e.g.:

```bash
python cli.py guitar/e-minor-blues.ly --svg --png
```

(note this also generates both SVG and PNG output in one call).

## Call Lilypond directly

To run Lilypond with an input file `test.ly`, saving to a folder `folder`, do:

```bash
lilypond --svg --output=folder test.ly
```

For PNG output at e.g. 500 DPI:

```bash
lilypond --png -dresolution=500 test.ly
```

## Summary of relevant Lilypond notation

See [cheat sheet](https://lilypond.org/doc/v2.23/Documentation/notation/cheat-sheet).

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

* Switch to templates:
    * Template for each scale.
    * Script (bash?) to pass each one into the template and output right filename.
* Summarise notation for duration.
* Improve SVG output:
    * Remove metadata e.g. file paths.
    * Make the images compatible with React. Workaround hack: compress the SVG using [this site](https://jakearchibald.github.io/svgomg/) (default settings) as suggested in [this post](https://github.com/facebook/create-react-app/issues/11770). Use [SVGO](https://github.com/svg/svgo) directly?
* Understand structure of `predefined-guitar-fretboards.ly` and exploit Lilypond features as it does.
    * Read up on [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language)).
* Experiment with [Lilypond event listener](https://lilypond.org/doc/v2.21/Documentation/notation/saving-music-events-to-a-file) to write music events to file.